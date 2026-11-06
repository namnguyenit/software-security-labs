# HƯỚNG DẪN TÁI HIỆN LAB 8 (ĐƠN GIẢN & NHANH CHÓNG)

Thư mục này chứa toàn bộ mã nguồn kiểm thử mờ (Fuzzing) hộp đen (Black-box) và hộp trắng dẫn dắt bởi độ phủ (Coverage-guided White-box), mục tiêu kiểm thử `fuzz_target.c`, các tệp crash thu được và bộ kiểm thử tự động của bài thực hành Lab 8 (Kênh lệnh quản trị ẩn ADMIN debug channel).

---

## 1. CÁCH CHẠY NHANH TRONG 3 BƯỚC

Mở terminal tại thư mục `lab8/code` và chạy các lệnh sau:

### Bước 1: Xác nhận lỗi thủ công bằng Payload kích hoạt trực tiếp
Biên dịch mục tiêu và truyền trực tiếp chuỗi đầu vào kích hoạt lỗ hổng tràn bộ đệm:
```bash
# Biên dịch chương trình:
gcc -g -Wall -Wextra --coverage -o c/fuzz_target.exe c/fuzz_target.c

# Chạy với payload gây lỗi (ADMIN:X + chuỗi dài > 15 byte):
./c/fuzz_target.exe "ADMIN:XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
```
*Kết quả kỳ vọng:* AddressSanitizer phát hiện lỗi `stack-buffer-overflow` tại hàm `process_input` (lệnh `strcpy` vào bộ đệm 16 byte), chương trình bị dừng ngay lập tức.

### Bước 2: Chạy đối chiếu giữa Fuzzer Hộp đen và Fuzzer Hộp trắng
Chạy cả hai chiến lược để quan sát sự khác biệt vượt trội về hiệu năng tìm lỗi:
```bash
# 1. Chạy Fuzzer Hộp đen (ngân sách 1000 lần thử):
python python/blackbox_fuzzer.py

# 2. Chạy Fuzzer Hộp trắng Coverage-guided (ngân sách 500 lần thử):
python python/whitebox_fuzzer.py
```
*Kết quả kỳ vọng:*
- Fuzzer Hộp đen (1000 lần thử): **0 crash** (xác suất mò ngẫu nhiên đúng chuỗi tiền tố 6 ký tự `ADMIN:` và ký tự `X` là cực kỳ thấp).
- Fuzzer Hộp trắng (500 lần thử): **3 crash** (lần đầu tìm thấy tại lần thử thứ 402; nhờ vòng phản hồi coverage của `gcov`, fuzzer từng bước khám phá nhánh `ADMIN:`, sau đó tới nhánh `ADMIN:X`, và cuối cùng đột biến chuỗi dài gây tràn bộ đệm).
- Các tệp đầu vào gây crash được tự động lưu trong thư mục `crashes/`.

### Bước 3: Chạy bộ kiểm thử tự động toàn diện (Test Suite)
Chạy 1 lệnh duy nhất để kiểm tra toàn bộ 4 test case:
```bash
python tests/test_fuzzing.py
```
*Kết quả kỳ vọng:* `4/4 test da PASS`.

---

## 2. CẤU TRÚC THƯ MỤC CODE

* `c/fuzz_target.c`: Mã nguồn chương trình mục tiêu chứa kênh debug bí mật (`ADMIN:X`) và lỗ hổng tràn bộ đệm CWE-121.
* `python/blackbox_fuzzer.py`: Fuzzer hộp đen đột biến ngẫu nhiên không có phản hồi độ phủ.
* `python/whitebox_fuzzer.py`: Fuzzer hộp trắng dẫn dắt bởi độ phủ (Coverage-guided) sử dụng phản hồi dòng lệnh từ `gcov` và hàng đợi ưu tiên LIFO.
* `seed_corpus/`: Tập dữ liệu hạt giống ban đầu (`seed_01.txt`, `seed_02.txt`).
* `crashes/`: Thư mục lưu trữ các tệp đầu vào kích hoạt crash (`whitebox_crash_*.txt`).
* `dataset/fuzzing_comparison_results.json`: Bảng dữ liệu định lượng so sánh kết quả giữa hai fuzzer.
* `tests/test_fuzzing.py`: Bộ kiểm thử tự động 4 test case xác nhận tính đúng đắn và ưu thế vượt trội của coverage-guided fuzzing.
* `patch_diff.diff`: Bản vá mã nguồn an toàn thay thế `strcpy()` bằng `snprintf()`.
