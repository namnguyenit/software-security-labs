# HƯỚNG DẪN TÁI HIỆN LAB 5 (ĐƠN GIẢN & NHANH CHÓNG)

Thư mục này chứa toàn bộ mã nguồn kiểm chứng hình thức bằng SAT/SMT Solving (Z3), đối chiếu vét cạn bằng C, tập dữ liệu 7 cặp điều kiện logic và bộ kiểm thử tự động của bài thực hành Lab 5 (Module Auth + Access Control).

---

## 1. CÁCH CHẠY NHANH TRONG 3 BƯỚC

Mở terminal tại thư mục `lab5/code` và chạy các lệnh sau:

### Bước 1: Chạy kiểm chứng hình thức bằng SMT Solver (Z3)
Kiểm tra tính tương đương logic giữa các cặp điều kiện nguyên bản (original) và điều kiện viết lại (optimized):
```bash
python python/smt_equivalence_checker.py
```
*Kết quả kỳ vọng:* 
- Kiểm chứng thành công cả 7 cặp điều kiện:
  + COND-01 (Mở khóa cửa De Morgan): TƯƠNG ĐƯƠNG (UNSAT).
  + COND-02 (Ngưỡng khóa tài khoản): KHÔNG TƯƠNG ĐƯƠNG (SAT) -> Bắt lỗi Off-by-one tại `failed_attempts = 3`.
  + COND-03 (PIN hợp lệ): TƯƠNG ĐƯƠNG (UNSAT).
  + COND-04 (Cảnh báo tamper -> alarm): TƯƠNG ĐƯƠNG (UNSAT).
  + COND-05 (Bypass xác thực): KHÔNG TƯƠNG ĐƯƠNG (SAT) -> Bắt lỗi Backdoor CWE-288 với phản ví dụ `{authenticated: False, is_admin: True, bypass_flag: True}`.
  + COND-06 (Giới hạn mượn sách): TƯƠNG ĐƯƠNG (UNSAT).
  + COND-07 (Mã giảm giá VIP): KHÔNG TƯƠNG ĐƯƠNG (SAT) -> Bắt lỗi gian lận nghiệp vụ với phản ví dụ `{is_vip: False, has_coupon: True, order_total: 999}`.
- Kết quả chi tiết tự động lưu tại `dataset/smt_verification_results.json`.

### Bước 2: Chạy đối chiếu chéo bằng Liệt kê Vét cạn (C Brute-force)
Liệt kê toàn bộ $2^n$ tổ hợp giá trị boolean trong C và đối chiếu với Z3:
```bash
# Biên dịch (nếu cần) và chạy:
gcc -Wall -Wextra -std=c11 -o c/brute_force_checker.exe c/brute_force_checker.c
./c/brute_force_checker.exe
```
*Kết quả kỳ vọng:* Kết quả hoàn toàn nhất quán 100% với Z3 trên toàn bộ các điều kiện boolean thuần túy.

### Bước 3: Chạy bộ kiểm thử tự động toàn diện (Test Suite)
Chạy 1 lệnh duy nhất để kiểm tra toàn bộ 6 test case của Lab 5:
```bash
python tests/test_smt_verification.py
```
*Kết quả kỳ vọng:* `6/6 test da PASS`.

---

## 2. CẤU TRÚC THƯ MỤC CODE

* `python/smt_equivalence_checker.py`: Bộ kiểm chứng tương đương logic SMT sử dụng thư viện Z3, giải công thức `P XOR Q` và trích xuất phản ví dụ (counterexample).
* `c/brute_force_checker.c`: Chương trình C duyệt vét cạn toàn bộ $2^n$ tổ hợp chân trị để kiểm chứng chéo với SMT solver.
* `dataset/`:
  - `condition_pairs.json`: Tập dữ liệu 7 cặp điều kiện logic trích từ các module của hệ thống SecureSys (bao gồm COND-07 tự thêm).
  - `smt_verification_results.json`: Kết quả chi tiết kiểm chứng SMT và phản ví dụ.
* `tests/test_smt_verification.py`: Bộ kiểm thử tự động 6 test case kiểm tra đối chuẩn kỳ vọng, tính hợp lệ của phản ví dụ và đối chiếu C/Z3.
* `patch_diff.diff`: Bản so sánh diff bổ sung cặp điều kiện COND-07 vào bộ dữ liệu.
