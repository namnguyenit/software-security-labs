# HƯỚNG DẪN TÁI HIỆN LAB 3 (ĐƠN GIẢN & NHANH CHÓNG)

Thư mục này chứa toàn bộ mã nguồn kiểm thử bộ nhớ, phát hiện lỗi qua AddressSanitizer (ASan), mô hình đánh giá rủi ro CVSS-lite và bộ kiểm thử tự động của bài thực hành Lab 3 (Module Inventory - Quản lý kho sách).

---

## 1. CÁCH CHẠY NHANH TRONG 3 BƯỚC

Mở terminal tại thư mục `lab3/code` và chạy các lệnh sau:

### Bước 1: Biên dịch và chạy thử nghiệm phát hiện lỗi bộ nhớ (C + ASan)
Chạy kiểm tra trên cả 2 phiên bản (bản lỗi `vulnerable_inventory` và bản an toàn `secure_inventory`):
```bash
# 1. Tái hiện lỗi trên bản vulnerable (bắt lỗi Heap-Overflow, Use-After-Free, Memory Leak):
./c/vulnerable_inventory.exe overflow "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
./c/vulnerable_inventory.exe uaf
./c/vulnerable_inventory.exe leak

# 2. Xác nhận bản secure_inventory chạy sạch lỗi, an toàn tuyệt đối:
./c/secure_inventory.exe overflow "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
./c/secure_inventory.exe uaf
./c/secure_inventory.exe leak
```
*Kết quả kỳ vọng:* Bản vulnerable xuất cảnh báo ASan và dừng an toàn; bản secure chạy thành công với chuỗi bị cắt bớt (truncated) an toàn tại 31 ký tự.

### Bước 2: Chạy công cụ đánh giá rủi ro định lượng (CVSS-lite)
Tính toán điểm số Exploitability, Impact, Base Score và xếp hạng mức độ nghiêm trọng cho toàn bộ 5 lỗ hổng:
```bash
python python/risk_assessor.py
```
*Kết quả kỳ vọng:* Xếp hạng ưu tiên khắc phục theo thứ tự:
1. `VULN-001` (CWE-121 Buffer Overflow) - 9.8 (CRITICAL)
2. `VULN-005` (CWE-190 Integer Overflow to Buffer Overflow) - 8.7 (HIGH)
3. `VULN-002` (CWE-416 Use After Free) - 6.9 (MEDIUM)
4. `VULN-003` (CWE-401 Memory Leak) - 5.4 (MEDIUM)
5. `VULN-004` (CWE-476 NULL Pointer Dereference) - 2.5 (LOW)

### Bước 3: Chạy bộ kiểm thử tự động toàn diện (Test Suite)
Chạy 1 lệnh duy nhất để kiểm tra toàn bộ 8 test case của Lab 3:
```bash
python tests/test_memory_safety.py
```
*Kết quả kỳ vọng:* `8/8 test da PASS`.

---

## 2. CẤU TRÚC THƯ MỤC CODE

* `c/vulnerable_inventory.c`: Mã nguồn C chứa 3 lỗi bộ nhớ kinh điển (CWE-121 Buffer Overflow, CWE-416 Use-After-Free, CWE-401 Memory Leak) cùng cơ chế ASan reporting.
* `c/secure_inventory.c`: Mã nguồn C an toàn khắc phục toàn bộ lỗi: thay `strcpy` bằng `snprintf` có kiểm tra truncation, gán `NULL` sau `free()`, và thu hồi bộ nhớ đầy đủ.
* `python/risk_assessor.py`: Bộ công cụ tính điểm rủi ro theo mô hình CVSS-lite (Exploitability sub-score + Impact sub-score).
* `dataset/`:
  - `vulnerabilities.json`: Đặc tả 5 lỗ hổng bảo mật kèm các vector tấn công CVSS (gồm VULN-005 tự thêm).
  - `risk_assessment_results.json`: Kết quả tính điểm và phân loại rủi ro.
  - `expected_risk_baseline.json`: Dữ liệu baseline đối chuẩn tự động cho test suite.
* `tests/test_memory_safety.py`: Bộ kiểm thử tự động 8 test case kiểm tra bắt lỗi ASan và độ chính xác của mô hình rủi ro.
* `patch_diff.diff`: Bản so sánh diff giữa bản lỗi và bản an toàn.
