"""
Lab 4 - Bo test tu dong toan dien:
  1. Xac nhan ban buggy bien dich thanh cong va chay duoc logic co ban.
  2. Xac nhan ban fixed bien dich, chay va dem chinh xac so luong node.
  3. Xac nhan cppcheck phat hien >= 2 finding bao mat tren ban buggy.
  4. Xac nhan cppcheck khong con finding bao mat tren ban fixed (0 finding).
  5. Xac nhan doi chieu khop voi expected baseline.
  6. Xac nhan anh huong gia tri rac cua loi uninitialized variable (CWE-457).
  7. Xac nhan ban fixed giai phong dung node khi xoa (chong leak CWE-401).
"""
import json
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C_DIR = os.path.join(BASE, "c")
sys.path.insert(0, os.path.join(BASE, "python"))

from static_analysis_runner import compare_versions, security_relevant  # noqa: E402


def test_buggy_compiles_and_runs():
    bin_name = "booklist_v1.exe" if os.name == "nt" else "booklist_v1"
    subprocess.run(["gcc", "-Wall", "-Wextra", "-o", bin_name, "booklist_v1_buggy.c"],
                    cwd=C_DIR, check=True)
    proc = subprocess.run([os.path.join(C_DIR, bin_name)], capture_output=True, text=True)
    assert proc.returncode == 0
    assert "Refactoring" in proc.stdout


def test_fixed_compiles_and_runs_correct_count():
    bin_name = "booklist_v2.exe" if os.name == "nt" else "booklist_v2"
    subprocess.run(["gcc", "-Wall", "-Wextra", "-o", bin_name, "booklist_v2_fixed.c"],
                    cwd=C_DIR, check=True)
    proc = subprocess.run([os.path.join(C_DIR, bin_name)], capture_output=True, text=True)
    assert proc.returncode == 0
    assert "So luong sach: 3" in proc.stdout
    assert "So luong sach: 2" in proc.stdout   # sau khi xoa 1 cuon


def test_cppcheck_detects_issues_in_buggy_version():
    result = compare_versions("booklist_v1_buggy.c", "booklist_v2_fixed.c")
    assert result["buggy_security_count"] >= 2, "cppcheck phai phat hien >= 2 loi bao mat o ban buggy"


def test_cppcheck_clean_on_fixed_version():
    result = compare_versions("booklist_v1_buggy.c", "booklist_v2_fixed.c")
    assert result["fixed_security_count"] == 0, "Ban da sua khong duoc con finding bao mat nao"


def test_matches_baseline():
    result = compare_versions("booklist_v1_buggy.c", "booklist_v2_fixed.c")
    with open(os.path.join(BASE, "dataset", "expected_cppcheck_baseline.json"), encoding="utf-8") as f:
        expected = json.load(f)
    assert result["buggy_security_count"] == expected["buggy_security_count"]
    assert result["fixed_security_count"] == expected["fixed_security_count"]
    buggy_ids = {f["id"] for f in security_relevant(result["buggy_findings"])}
    expected_ids = {f["id"] for f in expected["buggy_findings"] if f["severity"] in ("error", "warning")}
    assert buggy_ids == expected_ids


def test_uninitialized_variable_garbage_value_impact():
    """Kiem tra anh huong cua CWE-457: doc bien chua khoi tao."""
    result = compare_versions("booklist_v1_buggy.c", "booklist_v2_fixed.c")
    uninit_findings = [f for f in result["buggy_findings"] if f["id"] == "uninitvar"]
    assert len(uninit_findings) > 0
    assert uninit_findings[0]["cwe"] == "457"


def test_memory_leak_node_orphan_fix():
    """Kiem tra ban fixed loai bo hoan toan cac finding bao mat."""
    result = compare_versions("booklist_v1_buggy.c", "booklist_v2_fixed.c")
    assert len(result["fixed_findings"]) == 0


if __name__ == "__main__":
    tests = [
        test_buggy_compiles_and_runs,
        test_fixed_compiles_and_runs_correct_count,
        test_cppcheck_detects_issues_in_buggy_version,
        test_cppcheck_clean_on_fixed_version,
        test_matches_baseline,
        test_uninitialized_variable_garbage_value_impact,
        test_memory_leak_node_orphan_fix,
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
