"""
Lab 2 - Bo test tu dong toan dien:
  1. Kiem tra bo test hop den PASS 100% (18/18).
  2. Kiem tra do phu ma dat nguong toi thieu (>= 90%).
  3. Kiem tra bien khoa tai khoan (BVA: 2, 3, 4 lan sai).
  4. Kiem tra bo sung test case hop trang nang do phu len >= 98%.
  5. Kiem tra chinh sach ma PIN yeu (tuan tu tang/giam vs khong tuan tu).
  6. Kiem tra an toan phong thu voi con tro NULL va chuoi rong.
  7. Kiem chung an toan thu tu kiem tra failed_attempts truoc do dai PIN.
"""
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "python"))

from black_box_tester import run_black_box_suite, load_lib  # noqa: E402
from white_box_coverage import (  # noqa: E402
    build_instrumented_cli, compute_branch_coverage, clean_coverage_artifacts,
    run_cli_with_dataset, run_additional_coverage_tests,
)

MIN_COVERAGE_PCT = 90.0
BOOSTED_COVERAGE_PCT = 98.0


def test_black_box_suite_all_pass():
    passed, total, detail = run_black_box_suite()
    failed = [d for d in detail if not d["pass"]]
    assert not failed, f"Cac test hop den bi FAIL: {failed}"
    assert passed == total == 18


def test_white_box_coverage_meets_threshold():
    clean_coverage_artifacts()
    build_instrumented_cli()
    csv_path = os.path.join(BASE, "dataset", "pin_test_cases.csv")
    assert os.path.exists(csv_path), "Chay white_box_coverage.py truoc de sinh dataset CSV"
    run_cli_with_dataset(csv_path)
    cov = compute_branch_coverage()
    assert cov["coverage_percent"] >= MIN_COVERAGE_PCT, (
        f"Do phu ma {cov['coverage_percent']}% thap hon nguong yeu cau {MIN_COVERAGE_PCT}%"
    )


def test_account_lockout_boundary():
    """Kiem tra rieng bien 3 lan sai = khoa tai khoan (BVA)."""
    lib = load_lib()
    assert lib.validate_pin(b"482913", 2) == 0        # OK
    assert lib.validate_pin(b"482913", 3) == 4        # ACCOUNT_LOCKED
    assert lib.validate_pin(b"482913", 4) == 4        # ACCOUNT_LOCKED


def test_cli_negative_cases_boost_coverage():
    """Kiem tra bo sung test case hop trang nang coverage len >= 98%."""
    run_additional_coverage_tests()
    cov = compute_branch_coverage()
    assert cov["coverage_percent"] >= BOOSTED_COVERAGE_PCT, (
        f"Do phu ma sau khi bo sung {cov['coverage_percent']}% chua dat nguong {BOOSTED_COVERAGE_PCT}%"
    )


def test_sequential_weak_pin_rules():
    """Kiem tra quy tac nghiep vu: tu choi PIN yeu tang/giam lien tiep."""
    lib = load_lib()
    assert lib.validate_pin(b"123456", 0) == 3        # SEQUENTIAL_WEAK (tang)
    assert lib.validate_pin(b"654321", 0) == 3        # SEQUENTIAL_WEAK (giam)
    assert lib.validate_pin(b"112233", 0) == 0        # OK (khong tuan tu lien tiep)


def test_defensive_null_and_empty_handling():
    """Kiem tra lap trinh phong thu: khong crash voi NULL va chuoi rong."""
    lib = load_lib()
    assert lib.validate_pin(None, 0) == 5              # NULL_INPUT
    assert lib.validate_pin(b"", 0) == 1               # WRONG_LENGTH


def test_failed_attempts_order_security_vulnerability():
    """Chung minh tinh an toan cua thu tu kiem tra: failed_attempts phai duoc
    kiem tra TRUOC do dai PIN de tranh ro ri thong tin va tan cong tu choi dich vu."""
    lib = load_lib()
    # Khi tai khoan da bi khoa (failed_attempts = 5), du nhap PIN sai do dai ("123"),
    # he thong van phai tra ve ngay ACCOUNT_LOCKED (4), khong duoc tra ve WRONG_LENGTH (1).
    res = lib.validate_pin(b"123", 5)
    assert res == 4, f"Loi bao mat: tai khoan da khoa nhung tra ve ma {res} thay vi ACCOUNT_LOCKED (4)"


if __name__ == "__main__":
    tests = [
        test_black_box_suite_all_pass,
        test_white_box_coverage_meets_threshold,
        test_account_lockout_boundary,
        test_cli_negative_cases_boost_coverage,
        test_sequential_weak_pin_rules,
        test_defensive_null_and_empty_handling,
        test_failed_attempts_order_security_vulnerability,
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
