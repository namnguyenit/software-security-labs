# HƯỚNG DẪN TÁI HIỆN LAB 7 (ĐƠN GIẢN & NHANH CHÓNG)

Thư mục này chứa toàn bộ mã nguồn kiểm thử độ phủ mã động (Code Coverage với gcov), bộ sinh test case tổ hợp tự động từ lớp tương đương với Oracle độc lập, các tập dữ liệu test và bộ kiểm thử tự động của bài thực hành Lab 7 (Module Order Processing - Xử lý đơn hàng).

---

## 1. CÁCH CHẠY NHANH TRONG 3 BƯỚC

Mở terminal tại thư mục `lab7/code` và chạy các lệnh sau:

### Bước 1: Chạy đo độ phủ mã (Code Coverage Runner)
Thực hiện biên dịch chương trình C với cờ `--coverage`, chạy bộ test và phân tích kết quả gcov:
```bash
python python/coverage_runner.py
```
*Kết quả kỳ vọng:*
- Bộ test **partial** (2 test case): `Coverage: 79.69% (51/64 dòng)`, 2/2 PASS.
  *Minh chứng:* Tỷ lệ test PASS 100% không đồng nghĩa với độ phủ mã cao!
- Bộ test **full** (9 test case): `Coverage: 92.19% (59/64 dòng)`, 9/9 PASS.
  *Minh chứng:* Bổ sung các giá trị biên giúp tăng độ phủ vượt bậc (+12.5%).
- 5 dòng chưa phủ (7.81%) thuộc về nhánh xử lý ngoại lệ CLI (`argc < 2`, `fopen` thất bại) và `default: return UNKNOWN`, không thuộc luồng nghiệp vụ thông thường.

### Bước 2: Chạy sinh test case tổ hợp tự động (Combinatorial Testing)
Sinh test tự động từ tích Descartes các lớp tương đương kèm Oracle độc lập:
```bash
python python/test_case_generator.py
```
*Kết quả kỳ vọng:*
- Tự động sinh **56 test case tổ hợp** (7 lớp quantity $\times$ 4 lớp price $\times$ 2 lớp member), bao gồm cả giá trị biên mới `qty = 9` (ngay dưới ngưỡng thành viên 10).
- Tập dữ liệu lưu tại `dataset/order_test_inputs_combinatorial.csv`.

### Bước 3: Chạy bộ kiểm thử tự động toàn diện (Test Suite)
Chạy 1 lệnh duy nhất để kiểm tra toàn bộ 4 test case:
```bash
python tests/test_coverage.py
```
*Kết quả kỳ vọng:* `4/4 test da PASS`.

---

## 2. CẤU TRÚC THƯ MỤC CODE

* `c/order_processor.c`: Module C xử lý đơn hàng `process_order()` với nhiều nhánh lồng nhau và giao diện CLI đọc file CSV.
* `python/coverage_runner.py`: Script tự động biên dịch C với gcov, chạy test suite từ CSV và trích xuất tỷ lệ coverage cùng danh sách các dòng chưa phủ.
* `python/test_case_generator.py`: Bộ sinh test case tổ hợp dựa trên phân hoạch lớp tương đương và hàm Oracle độc lập `expected_status()`.
* `dataset/`:
  - `order_test_inputs_partial.csv`: Bộ test không đầy đủ (2 ca kiểm thử).
  - `order_test_inputs_full.csv`: Bộ test đầy đủ bao quát các nhánh biên (9 ca kiểm thử).
  - `order_test_inputs_combinatorial.csv`: Bộ test tổ hợp tự sinh (56 ca kiểm thử).
  - `coverage_comparison_results.json`: Kết quả đối chiếu chi tiết độ phủ giữa các bộ test.
* `tests/test_coverage.py`: Bộ kiểm thử tự động 4 test case xác nhận tỷ lệ PASS và cải thiện độ phủ.
* `patch_diff.diff`: Bản ghi chép khác biệt bổ sung lớp tương đương biên `qty = 9` vào bộ sinh test.
