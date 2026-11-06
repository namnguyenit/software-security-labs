"""
Lab 6 - Bo test tu dong toan dien
==================================
1. Xac nhan dong co BMC (Python/Z3) cho ket qua khop ky vong tren toan bo 5 chuong trinh.
2. Xac nhan cai dat C thuc te (ASan) khop voi ket qua kiem chung tinh:
   - safe_full_scan  : chay sach, khong loi.
   - offbyone        : ASan bao loi tai index 10.
   - symbolic_unsafe (base=9) : ASan bao loi (khop nhan chung BMC: base_index=9).
   - symbolic_safe (base=9)   : bi TU CHOI o tien dieu kien (khong crash).
   - symbolic_safe (base=3)   : chay sach.
   - reverse_scan    : ASan bao loi tai buoc dau tien (index 10).
"""
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C_DIR = os.path.join(BASE, "c")
sys.path.insert(0, os.path.join(BASE, "python"))

from bmc_engine import run_all  # noqa: E402

DATASET = os.path.join(BASE, "dataset", "bmc_programs.json")


def _build():
    bin_name = "array_access.exe" if os.name == "nt" else "array_access"
    bin_path = os.path.join(C_DIR, bin_name)
    try:
        subprocess.run(
            ["gcc", "-g", "-fsanitize=address", "-Wall", "-Wextra", "-o", bin_name, "array_access.c"],
            cwd=C_DIR, check=True, capture_output=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        subprocess.run(
            ["gcc", "-g", "-Wall", "-Wextra", "-o", bin_name, "array_access.c"],
            cwd=C_DIR, check=True,
        )
    return bin_path


def _run(args: list[str]):
    bin_path = _build()
    return subprocess.run([bin_path] + args, cwd=C_DIR, capture_output=True, text=True)


def test_bmc_results_match_expectation():
    results = run_all(DATASET)
    mismatches = [r for r in results if not r["matches_expectation"]]
    assert not mismatches, f"BMC sai lech ky vong: {[m['id'] for m in mismatches]}"
    assert len(results) == 5, f"Ky vong 5 chuong trinh nhung nhan duoc {len(results)}"


def test_bmc03_witness_matches_c_runtime_bug():
    """Nhan chung cua BMC-03 (base_index=9) phai la gia tri THUC SU gay loi
    khi chay chuong trinh C tuong ung - day la buoc 'doi chieu' quan trong
    giua ket qua kiem chung tinh va hanh vi runtime."""
    results = {r["id"]: r for r in run_all(DATASET)}
    witness = results["BMC-03-UNSAFE-SYMBOLIC-OFFSET"]["witness"]
    base_index = witness["base_index"]

    proc = _run(["symbolic_unsafe", str(base_index)])
    assert proc.returncode != 0, "Chuong trinh C phai crash voi base_index tu nhan chung BMC"
    assert "AddressSanitizer" in proc.stderr


def test_c_safe_full_scan_no_crash():
    proc = _run(["safe_full_scan"])
    assert proc.returncode == 0
    assert "AddressSanitizer" not in proc.stderr


def test_c_symbolic_safe_with_precondition_rejects_bad_input():
    proc = _run(["symbolic_safe", "9"])
    assert proc.returncode == 0
    assert "TU CHOI" in proc.stderr


def test_c_symbolic_safe_with_valid_input_runs_clean():
    proc = _run(["symbolic_safe", "3"])
    assert proc.returncode == 0
    assert "AddressSanitizer" not in proc.stderr


def test_c_offbyone_detected():
    proc = _run(["offbyone"])
    assert proc.returncode != 0
    assert "AddressSanitizer" in proc.stderr


def test_c_reverse_scan_detected():
    proc = _run(["reverse_scan"])
    assert proc.returncode != 0
    assert "AddressSanitizer" in proc.stderr


if __name__ == "__main__":
    _build()
    tests = [
        test_bmc_results_match_expectation,
        test_bmc03_witness_matches_c_runtime_bug,
        test_c_safe_full_scan_no_crash,
        test_c_symbolic_safe_with_precondition_rejects_bad_input,
        test_c_symbolic_safe_with_valid_input_runs_clean,
        test_c_offbyone_detected,
        test_c_reverse_scan_detected,
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
