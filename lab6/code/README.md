# HƯỚNG DẪN TÁI HIỆN LAB 6 (ĐƠN GIẢN & NHANH CHÓNG)

Thư mục này chứa toàn bộ mã nguồn của động cơ Bounded Model Checking (BMC) tự viết bằng Z3, chương trình C truy cập mảng đối chiếu runtime với AddressSanitizer, tập dữ liệu 5 chương trình kiểm chứng (bao gồm BMC-05 tự thêm) và bộ kiểm thử tự động của bài thực hành Lab 6 (Module Inventory - Catalog sách).

---

## 1. CÁCH CHẠY NHANH TRONG 3 BƯỚC

Mở terminal tại thư mục `lab6/code` và chạy các lệnh sau:

### Bước 1: Chạy động cơ Bounded Model Checking (Python / Z3)
Thực hiện mở cuộn (unwind) vòng lặp, mã hóa ràng buộc đường đi và kiểm chứng an toàn truy cập mảng bằng Z3 solver:
```bash
python python/bmc_engine.py
```
*Kết quả kỳ vọng:*
- Kiểm chứng thành công toàn bộ 5 chương trình trong dataset:
  + `BMC-01-SAFE-FULL-SCAN`: **SAFE** (an toàn trong 10 bước unwind).
  + `BMC-02-UNSAFE-OFFBYONE`: **UNSAFE** (bắt lỗi off-by-one tại bước $i=10$, truy cập index 10).
  + `BMC-03-UNSAFE-SYMBOLIC-OFFSET`: **UNSAFE** (nhân chứng: `base_index = 9`, vi phạm tại bước $i=1$, truy cập index 10).
  + `BMC-04-SAFE-SYMBOLIC-OFFSET-BOUNDED`: **SAFE** (tiền điều kiện `base_index <= 5` bảo vệ mảng an toàn trong 5 bước unwind).
  + `BMC-05-UNSAFE-REVERSE-SCAN`: **UNSAFE** (duyệt ngược `catalog[array_size - i]`, vi phạm ngay bước đầu tiên $i=0$, truy cập index 10).
- Kết quả chi tiết tự động lưu tại `dataset/bmc_results.json`.

### Bước 2: Chạy đối chiếu Runtime thực tế trên C (với AddressSanitizer)
Biên dịch và chạy chương trình C tương ứng để đối chiếu nhân chứng tìm được từ BMC:
```bash
# Biên dịch chương trình:
gcc -g -fsanitize=address -Wall -Wextra -o c/array_access.exe c/array_access.c

# 1. Chạy bản an toàn toàn diện:
./c/array_access.exe safe_full_scan

# 2. Chạy bản lỗi off-by-one:
./c/array_access.exe offbyone

# 3. Chạy với tham số nhân chứng từ BMC-03 (base_index=9) -> Bắt lỗi tràn bộ đệm:
./c/array_access.exe symbolic_unsafe 9

# 4. Chạy bản an toàn với tiền điều kiện (từ chối tham số xấu base_index=9):
./c/array_access.exe symbolic_safe 9

# 5. Chạy bản duyệt ngược lỗi BMC-05 -> Bắt lỗi tràn bộ đệm tại bước đầu tiên:
./c/array_access.exe reverse_scan
```

### Bước 3: Chạy bộ kiểm thử tự động toàn diện (Test Suite)
Chạy 1 lệnh duy nhất để kiểm tra toàn bộ 7 test case:
```bash
python tests/test_bmc.py
```
*Kết quả kỳ vọng:* `7/7 test da PASS`.

---

## 2. CẤU TRÚC THƯ MỤC CODE

* `python/bmc_engine.py`: Động cơ Bounded Model Checking tự cài đặt bằng thư viện Z3, thực hiện mở cuộn vòng lặp tối đa $k$ bước, mã hóa biểu thức chỉ số và giải bài toán tồn tại vi phạm.
* `c/array_access.c`: Mã nguồn C mô phỏng các kịch bản truy cập mảng catalog sách, hỗ trợ AddressSanitizer để kiểm chứng động tại runtime.
* `dataset/`:
  - `bmc_programs.json`: Đặc tả 5 chương trình kiểm chứng (kích thước mảng, số bước unwind, biến tượng trưng symbolic base, tiền điều kiện).
  - `bmc_results.json`: Kết quả phân tích chi tiết của động cơ BMC kèm nhân chứng (witness) cụ thể.
* `tests/test_bmc.py`: Bộ kiểm thử tự động xác nhận tính đúng đắn của BMC và sự khớp nối hoàn hảo giữa nhân chứng tĩnh và lỗi runtime.
* `patch_diff.diff`: Bản ghi chép khác biệt bổ sung chương trình duyệt ngược BMC-05 vào hệ thống.
