# HƯỚNG DẪN TÁI HIỆN LAB 1 (ĐƠN GIẢN & NHANH CHÓNG)

Thư mục này chứa toàn bộ mã nguồn, dữ liệu thực nghiệm và bộ kiểm thử tự động của bài thực hành Lab 1.

---

## 1. CÁCH CHẠY NHANH TRONG 3 BƯỚC

Mở terminal tại thư mục `lab1/code` và chạy các lệnh sau:

### Bước 1: Chạy kiểm chứng mô hình Kripke (Python)
Kiểm tra mô hình chuẩn (SAFE), mô hình lỗi (BUGGY), và mô hình đã vá (FIXED):
```bash
# 1. Chạy trên mô hình chuẩn (SAFE) -> Cả 3 thuộc tính P1, P2, P3 đều PASS
python python/kripke_model.py dataset/access_system_model.json

# 2. Chạy trên mô hình lỗi (BUGGY) -> Bắt lỗi P1 FAIL (trace: S0 -> S1 -> S5) và cảnh báo P2 Vacuous Pass
python python/kripke_model.py dataset/access_system_model_BUGGY.json

# 3. Chạy trên mô hình đã vá (FIXED) -> Cả 5 thuộc tính P1..P5 đều PASS (không còn vacuous pass)
python python/kripke_model.py dataset/access_system_model_FIXED.json
```

### Bước 2: Chạy bộ mô phỏng thực thi (C)
Biên dịch (nếu cần) và chạy mô phỏng runtime:
```bash
# Biên dịch mã nguồn C (đã có sẵn file access_simulator.exe):
gcc -Wall -Wextra -std=c11 -o c/access_simulator.exe c/access_simulator.c

# Chạy kịch bản bình thường:
./c/access_simulator.exe dataset/access_safe_states.csv dataset/access_safe_transitions.csv dataset/access_safe_init.txt insert_card auth_success door_closed_timeout

# Chạy kịch bản kích hoạt lỗi (xuất cảnh báo an toàn vi phạm P1 tại S5):
./c/access_simulator.exe dataset/access_buggy_states.csv dataset/access_buggy_transitions.csv dataset/access_buggy_init.txt insert_card timeout_glitch

# Chạy kịch bản sự kiện không hợp lệ (kiểm tra nguyên tắc bảo vệ Fail-Closed):
./c/access_simulator.exe dataset/access_safe_states.csv dataset/access_safe_transitions.csv dataset/access_safe_init.txt insert_card operator_reset
```

### Bước 3: Chạy bộ kiểm thử tự động (Test Suite)
Chạy 1 lệnh duy nhất để kiểm tra toàn bộ 8 test case:
```bash
python tests/test_kripke.py
```
*Kết quả kỳ vọng:* `8/8 test da PASS`.

---

## 2. CẤU TRÚC THƯ MỤC CODE

* `python/kripke_model.py`: Trình kiểm chứng mô hình hình thức Kripke (hỗ trợ BFS, kiểm tra CTL AG !p, AG (p -> q), EF p, và tự động bắt lỗi Vacuous Truth).
* `c/access_simulator.c`: Chương trình C mô phỏng runtime của khóa cửa (an toàn bộ nhớ, fail-closed).
* `dataset/`:
  - `access_system_model.json`: Mô hình chuẩn SAFE (5 trạng thái, 8 chuyển tiếp).
  - `access_system_model_BUGGY.json`: Mô hình lỗi BUGGY (chứa race condition S1 -> S5 và cắt đứt cảm biến tamper).
  - `access_system_model_FIXED.json`: Mô hình đã sửa toàn diện (loại bỏ S5, trỏ tamper về S4, thêm thuộc tính an toàn P4 và P5).
  - Các tệp `.csv` và `.txt` tương ứng cho simulator C.
* `tests/test_kripke.py`: Bộ 8 bài test tự động bao quát cả Python và C.
* `patch_diff.diff`: Tệp so sánh diff bản vá giữa BUGGY và FIXED.
