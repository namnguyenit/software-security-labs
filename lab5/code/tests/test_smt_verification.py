"""
Lab 5 - Bo test tu dong toan dien:
  1. Xac nhan ket qua Z3 khop ky vong tren toan bo 7 cap dieu kien (bao gom COND-07).
  2. Xac nhan phan vi du (counterexample) cho cac cap KHONG tuong duong la chinh xac.
  3. Xac nhan chuong trinh C brute-force cho ket qua NHAT QUAN tuyet doi voi Z3.
  4. Kiem tra rieng biet loi Off-by-one tai COND-02.
  5. Kiem tra rieng biet lo hong backdoor bypass xac thuc CWE-288 tai COND-05.
  6. Kiem tra rieng biet lo hong bypass nghiep vu giam gia tai COND-07.
"""
import json
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "python"))

from smt_equivalence_checker import run_all, eval_expr, make_vars  # noqa: E402
from z3 import sat, Solver, Xor, BoolRef  # noqa: E402

DATASET = os.path.join(BASE, "dataset", "condition_pairs.json")


def test_all_pairs_match_expectation():
    results = run_all(DATASET)
    mismatches = [r for r in results if not r["matches_expectation"]]
    assert not mismatches, f"Cac cap sai lech ky vong: {[m['id'] for m in mismatches]}"
    assert len(results) == 7, f"Ky vong 7 cap dieu kien nhung nhan duoc {len(results)}"


def test_counterexample_is_valid_for_non_equivalent_pairs():
    with open(DATASET, encoding="utf-8") as f:
        data = json.load(f)
    results = run_all(DATASET)
    by_id = {r["id"]: r for r in results}
    for pair in data["condition_pairs"]:
        if pair["expected_equivalent"]:
            continue
        r = by_id[pair["id"]]
        assert r["counterexample"] is not None
        # Xac nhan phan vi du thuc su lam P va Q khac nhau
        env = make_vars(pair["var_types"])
        P = eval_expr(pair["original"], env)
        Q = eval_expr(pair["optimized"], env)
        s = Solver()
        for name, val in r["counterexample"].items():
            var = env[name]
            if isinstance(var, BoolRef) or str(var.sort()) == "Bool":
                s.add(var == (val == "True"))
            else:
                s.add(var == int(val))
        s.add(Xor(P, Q))
        assert s.check() == sat, f"Phan vi du cua {pair['id']} khong hop le"


def test_c_brute_force_matches_z3():
    bin_name = "brute_force_checker.exe" if os.name == "nt" else "brute_force_checker"
    bin_path = os.path.join(BASE, "c", bin_name)
    subprocess.run(
        ["gcc", "-Wall", "-Wextra", "-std=c11", "-o", bin_path, "brute_force_checker.c"],
        cwd=os.path.join(BASE, "c"), check=True,
    )
    proc = subprocess.run([bin_path], capture_output=True, text=True, check=True)
    out = proc.stdout
    assert "[COND-01] TUONG DUONG" in out
    assert "[COND-03] TUONG DUONG" in out
    assert "[COND-04] TUONG DUONG" in out
    assert "[COND-05] KHONG TUONG DUONG" in out


def test_cond02_off_by_one_detection():
    """Kiem tra phat hien loi off-by-one tai failed_attempts == 3."""
    results = {r["id"]: r for r in run_all(DATASET)}
    r2 = results["COND-02"]
    assert not r2["is_equivalent"]
    assert r2["counterexample"]["failed_attempts"] == "3"


def test_cond05_backdoor_authentication_bypass():
    """Kiem tra phat hien backdoor CWE-288: authenticated=False, is_admin=True, bypass_flag=True."""
    results = {r["id"]: r for r in run_all(DATASET)}
    r5 = results["COND-05"]
    assert not r5["is_equivalent"]
    cx = r5["counterexample"]
    assert cx["authenticated"] == "False"
    assert cx["is_admin"] == "True"
    assert cx["bypass_flag"] == "True"


def test_cond07_business_logic_bypass():
    """Kiem tra phat hien gian lan ma giam gia VIP tai COND-07."""
    results = {r["id"]: r for r in run_all(DATASET)}
    r7 = results["COND-07"]
    assert not r7["is_equivalent"]
    cx = r7["counterexample"]
    assert cx["is_vip"] == "False"
    assert cx["has_coupon"] == "True"
    assert int(cx["order_total"]) < 1000


if __name__ == "__main__":
    tests = [
        test_all_pairs_match_expectation,
        test_counterexample_is_valid_for_non_equivalent_pairs,
        test_c_brute_force_matches_z3,
        test_cond02_off_by_one_detection,
        test_cond05_backdoor_authentication_bypass,
        test_cond07_business_logic_bypass,
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
