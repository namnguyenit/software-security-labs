# HƯỚNG DẪN TÁI HIỆN LAB 2 (ĐƠN GIẢN & NHANH CHÓNG)

Thư mục này chứa toàn bộ mã nguồn kiểm thử hộp đen, hộp trắng, dữ liệu thực nghiệm và bộ kiểm thử tự động của bài thực hành Lab 2 (Module Auth - Xác thực mã PIN).

---

## 1. CÁCH CHẠY NHANH TRONG 3 BƯỚC

Mở terminal tại thư mục `lab2/code` và chạy các lệnh sau:

### Bước 1: Chạy kiểm thử hộp đen (Black-box Testing)
Sinh và chạy toàn bộ 18 test case thiết kế theo Equivalence Partitioning (EP) và Boundary Value Analysis (BVA):
```bash
python python/black_box_tester.py
```
*Kết quả kỳ vọng:* Toàn bộ `18/18 test PASS`, kết quả chi tiết tự động lưu tại `dataset/black_box_test_results.csv`.

### Bước 2: Đo độ phủ mã hộp trắng (White-box Coverage qua gcov)
Biên dịch driver CLI với cờ `--coverage` và đo độ phủ câu lệnh thực thi (Statement Coverage) bằng `gcov`:
```bash
python python/white_box_coverage.py
```
*Kết quả kỳ vọng:* 
- Bộ test hộp đen ban đầu đạt độ phủ: **92.42%** (61/66 dòng).
- Sau khi kích hoạt bổ sung các ca kiểm thử hộp trắng (CLI negative cases), độ phủ tăng lên: **98.48%** (65/66 dòng).

### Bước 3: Chạy bộ kiểm thử tự động toàn diện (Test Suite)
Chạy 1 lệnh duy nhất để kiểm tra toàn bộ 7 test case của Lab 2:
```bash
python tests/test_pin_validator.py
```
*Kết quả kỳ vọng:* `7/7 test da PASS`.

---

## 2. CẤU TRÚC THƯ MỤC CODE

* `c/pin_validator.c`: Mã nguồn C của hàm `validate_pin()`, kiểm tra độ dài 6 ký tự số, chính sách PIN yếu (dãy tăng/giảm liên tục) và khóa tài khoản sau 3 lần sai.
* `c/pin_validator_cli.exe`: Trình thực thi CLI đọc file CSV và tự động chấm điểm test case (hỗ trợ cờ đo coverage gcov).
* `c/pin_runner.exe`: Trình bao thực thi độc lập hỗ trợ Python gọi an toàn trên môi trường Windows đa kiến trúc.
* `python/black_box_tester.py`: Bộ sinh test case tự động theo kỹ thuật EP, BVA và kiểm thử phòng thủ.
* `python/white_box_coverage.py`: Trình biên dịch có cờ coverage, chạy gcov và phân tích các dòng chưa được kiểm thử.
* `dataset/`:
  - `pin_test_cases.csv`: Tập dữ liệu 18 test case đầu vào phục vụ cho CLI C.
  - `black_box_test_results.csv`: Kết quả chi tiết thực thi của từng test case.
* `tests/test_pin_validator.py`: Bộ 7 bài test tự động bao quát kiểm thử hộp đen, hộp trắng, biên lockout và chứng minh an toàn thứ tự kiểm tra.
* `patch_diff.diff`: Tệp so sánh diff bản vá bổ sung các ca kiểm thử hộp trắng tăng độ phủ mã.
