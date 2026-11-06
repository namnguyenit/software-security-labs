# HƯỚNG DẪN TÁI HIỆN LAB 4 (ĐƠN GIẢN & NHANH CHÓNG)

Thư mục này chứa toàn bộ mã nguồn cấu trúc dữ liệu linked list, công cụ phân tích tĩnh cppcheck, dữ liệu so sánh và bộ kiểm thử tự động của bài thực hành Lab 4 (Module Inventory - Catalog sách).

---

## 1. CÁCH CHẠY NHANH TRONG 3 BƯỚC

Mở terminal tại thư mục `lab4/code` và chạy các lệnh sau:

### Bước 1: Biên dịch và chạy thử nghiệm cấu trúc linked list
Chạy cả 2 phiên bản (bản lỗi `booklist_v1` và bản đã sửa `booklist_v2`):
```bash
# 1. Chạy bản có lỗi:
./c/booklist_v1.exe

# 2. Chạy bản đã sửa an toàn:
./c/booklist_v2.exe
```
*Kết quả kỳ vọng:* Bản buggy hiển thị số lượng sách không chính xác do biến `count` chưa khởi tạo; bản fixed hiển thị chính xác 3 cuốn ban đầu và 2 cuốn sau khi xóa.

### Bước 2: Chạy công cụ phân tích tĩnh (Static Analysis Runner)
Phân tích AST/CFG của mã nguồn mà không cần thực thi chương trình:
```bash
python python/static_analysis_runner.py
```
*Kết quả kỳ vọng:* 
- Bản `booklist_v1_buggy.c`: Phát hiện 2 lỗi bảo mật (`[WARNING] Uninitialized variable: count` và `[ERROR] Memory is allocated but not initialized: node`).
- Bản `booklist_v2_fixed.c`: Đạt chuẩn sạch **0 finding bảo mật**.
- Giảm 2 finding bảo mật sau khi sửa lỗi. Kết quả tự động lưu tại `dataset/cppcheck_comparison_results.json`.

### Bước 3: Chạy bộ kiểm thử tự động toàn diện (Test Suite)
Chạy 1 lệnh duy nhất để kiểm tra toàn bộ 7 test case của Lab 4:
```bash
python tests/test_static_analysis.py
```
*Kết quả kỳ vọng:* `7/7 test da PASS`.

---

## 2. CẤU TRÚC THƯ MỤC CODE

* `c/booklist_v1_buggy.c`: Mã nguồn linked list chứa 3 lỗi bảo mật tinh vi (CWE-476 NULL dereference, CWE-401 memory leak khi xóa node, CWE-457 biến count chưa khởi tạo).
* `c/booklist_v2_fixed.c`: Mã nguồn linked list đã sửa toàn diện toàn bộ 3 lỗi.
* `python/static_analysis_runner.py`: Trình phân tích tĩnh tự động quét mã nguồn qua cppcheck, trích xuất mã CWE và so sánh mức độ cải thiện an toàn.
* `dataset/`:
  - `expected_cppcheck_baseline.json`: Dữ liệu baseline đối chuẩn kết quả phân tích tĩnh.
  - `cppcheck_comparison_results.json`: Kết quả chi tiết sau khi chạy phân tích.
* `tests/test_static_analysis.py`: Bộ 7 bài test tự động bao quát cả biên dịch, phân tích tĩnh và đối chuẩn baseline.
* `patch_diff.diff`: Bản so sánh diff ghi nhận các đoạn mã đã được sửa an toàn trong linked list.
