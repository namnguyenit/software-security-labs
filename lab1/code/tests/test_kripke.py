"""
Lab 1 - Bo test tu dong
=======================
Kiem tra rang:
  1) Mo hinh SAFE thoa man ca 3 thuoc tinh an toan.
  2) Mo hinh BUGGY phat hien VI PHAM thuoc tinh P1 (unlock khong xac thuc),
     va tao ra duong di phan chung (counterexample) chinh xac.
  3) Chuong trinh C mo phong (compiled binary) tao canh bao runtime tuong ung.

Chay: python3 -m pytest tests/test_kripke.py -v
      hoac: python3 tests/test_kripke.py
"""
import json
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "python"))

from kripke_model import run_verification  # noqa: E402

DATASET = os.path.join(BASE, "dataset")
C_BIN = os.path.join(BASE, "c", "access_simulator")


def test_safe_model_all_properties_hold():
    result = run_verification(os.path.join(DATASET, "access_system_model.json"), verbose=False)
    for prop in result["properties"]:
        assert prop["holds"] is True, f"Thuoc tinh {prop['id']} phai THOA MAN tren mo hinh SAFE"


def test_buggy_model_violates_p1():
    result = run_verification(os.path.join(DATASET, "access_system_model_BUGGY.json"), verbose=False)
    props = {p["id"]: p for p in result["properties"]}
    assert props["P1_SAFETY_NO_UNLOCK_WITHOUT_AUTH"]["holds"] is False, \
        "Mo hinh BUGGY phai VI PHAM thuoc tinh P1"
    witness = props["P1_SAFETY_NO_UNLOCK_WITHOUT_AUTH"]["witness_states"]
    assert witness[0] == "S0" and witness[-1] == "S5", \
        f"Duong di phan chung khong dung: {witness}"


def test_buggy_model_reachability_still_holds():
    result = run_verification(os.path.join(DATASET, "access_system_model_BUGGY.json"), verbose=False)
    props = {p["id"]: p for p in result["properties"]}
    assert props["P3_REACHABILITY_UNLOCK"]["holds"] is True


def _ensure_c_binary_built():
    bin_path = C_BIN if os.path.exists(C_BIN) else C_BIN + ".exe"
    if not os.path.exists(bin_path):
        subprocess.run(
            ["gcc", "-Wall", "-Wextra", "-std=c11", "-o", "access_simulator", "access_simulator.c"],
            cwd=os.path.join(BASE, "c"),
            check=True,
        )


def _get_c_bin():
    _ensure_c_binary_built()
    return C_BIN if os.path.exists(C_BIN) else C_BIN + ".exe"


def test_c_simulator_detects_runtime_violation():
    bin_exe = _get_c_bin()
    proc = subprocess.run(
        [bin_exe,
         os.path.join(DATASET, "access_buggy_states.csv"),
         os.path.join(DATASET, "access_buggy_transitions.csv"),
         os.path.join(DATASET, "access_buggy_init.txt"),
         "insert_card", "timeout_glitch"],
        capture_output=True, text=True, check=True,
    )
    assert "CANH BAO AN TOAN" in proc.stdout
    assert "vi pham thuoc tinh P1" in proc.stdout


def test_c_simulator_safe_sequence_no_warning():
    bin_exe = _get_c_bin()
    proc = subprocess.run(
        [bin_exe,
         os.path.join(DATASET, "access_safe_states.csv"),
         os.path.join(DATASET, "access_safe_transitions.csv"),
         os.path.join(DATASET, "access_safe_init.txt"),
         "insert_card", "auth_success", "door_closed_timeout"],
        capture_output=True, text=True, check=True,
    )
    assert "CANH BAO AN TOAN" not in proc.stdout


def test_fixed_model_all_properties_hold():
    fixed_path = os.path.join(DATASET, "access_system_model_FIXED.json")
    assert os.path.exists(fixed_path), "File access_system_model_FIXED.json phai ton tai"
    result = run_verification(fixed_path, verbose=False)
    for prop in result["properties"]:
        assert prop["holds"] is True, f"Thuoc tinh {prop['id']} phai THOA MAN tren mo hinh FIXED"
        assert not prop.get("is_vacuous", False), f"Thuoc tinh {prop['id']} khong duoc vacuous tren FIXED"


def test_vacuous_pass_detected_on_buggy():
    result = run_verification(os.path.join(DATASET, "access_system_model_BUGGY.json"), verbose=False)
    props = {p["id"]: p for p in result["properties"]}
    assert props["P2_SAFETY_ALARM_ON_TAMPER"]["holds"] is True
    assert props["P2_SAFETY_ALARM_ON_TAMPER"].get("is_vacuous", False) is True, \
        "Thuoc tinh P2 tren mo hinh BUGGY phai duoc canh bao la VACUOUS PASS"


def test_c_simulator_fixed_sequence():
    bin_exe = _get_c_bin()
    proc = subprocess.run(
        [bin_exe,
         os.path.join(DATASET, "access_fixed_states.csv"),
         os.path.join(DATASET, "access_fixed_transitions.csv"),
         os.path.join(DATASET, "access_fixed_init.txt"),
         "insert_card", "auth_success", "door_closed_timeout", "tamper_sensor", "operator_reset"],
        capture_output=True, text=True, check=True,
    )
    assert "CANH BAO AN TOAN" not in proc.stdout
    assert "So su kien bi tu choi (khong hop le): 0" in proc.stdout


if __name__ == "__main__":
    tests = [
        test_safe_model_all_properties_hold,
        test_buggy_model_violates_p1,
        test_buggy_model_reachability_still_holds,
        test_c_simulator_detects_runtime_violation,
        test_c_simulator_safe_sequence_no_warning,
        test_fixed_model_all_properties_hold,
        test_vacuous_pass_detected_on_buggy,
        test_c_simulator_fixed_sequence,
    ]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"[PASS] {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"[FAIL] {t.__name__}: {e}")
    print(f"\n{passed}/{len(tests)} test da PASS")
