# Software Security & Formal Verification Laboratory Suite (CSE703093)

Trọn bộ hệ thống bài giảng, mã nguồn thực hành và phòng thí nghiệm môn **An toàn phần mềm (Mã học phần: CSE703093)** — Khoa Hệ thống Thông tin & CNTT, Trường Đại học Phenikaa.

---

## 📌 Tổng quan Chương trình Phòng thí nghiệm

Dự án cung cấp môi trường thực nghiệm toàn diện từ các mô hình lý thuyết kiểm chứng hình thức (Formal Verification) đến các kỹ thuật phân tích tĩnh (Static Analysis), an toàn bộ nhớ ở mức hệ thống (Memory Safety) và kiểm thử fuzzing tự động (Automated Fuzz Testing):

| Bài Lab | Chuyên đề | Kỹ thuật / Công cụ chính | Nội dung cốt lõi |
| :---: | :--- | :--- | :--- |
| **Lab 1** | **Mô hình Hóa Kripke (Access Control)** | Kripke Structure, Transition Systems | Mô hình hóa máy trạng thái, đặc tả ma trận chuyển trạng thái truy cập và kiểm chứng thuộc tính an toàn (Safety Properties). |
| **Lab 2** | **Nền tảng Kiểm thử & Kiểm chứng** | Testing & Verification Specs | Xây dựng bộ test cases định nghĩa theo đặc tả toán học hình thức. |
| **Lab 3** | **An toàn Bộ nhớ Hệ thống** | C/C++, Memory Allocator, ASLR, Stack Canaries | Phân tích và phòng chống tràn bộ đệm (Buffer Overflow), Use-After-Free, Double Free và rò rỉ bộ nhớ. |
| **Lab 4** | **Phân tích Mã nguồn Tĩnh (AST)** | Abstract Syntax Tree (AST), Clang/LLVM | Phân tích luồng điều khiển (CFG), phát hiện các anti-patterns bảo mật trực tiếp trên cây cú pháp. |
| **Lab 5** | **Kiểm chứng Hình thức SMT Solver** | **Z3 Theorem Prover (Microsoft Research)** | Chuyển đổi bài toán logic xác minh an toàn mã nguồn sang công thức SAT/SMT và chứng minh tự động. |
| **Lab 6** | **Bounded Model Checking (BMC)** | BMC, Unrolling Loops, SMT | Mở vòng lặp hữu hạn (Loop unrolling) để tìm kiếm vi phạm bất biến an toàn (Invariant Violations). |
| **Lab 7** | **Phân tích Độ bao phủ Động** | Instrumentation, Branch Coverage | Đo lường độ phủ nhánh thực thi của chương trình dưới các đầu vào ngẫu nhiên và biên. |
| **Lab 8** | **Kiểm thử Fuzzing Tự động** | Coverage-Guided Fuzzing, Mutation Engine | Sinh đột biến đầu vào (Input Mutations) để tìm kiếm crash, assertion failure và lỗi phân đoạn (SIGSEGV). |

---

## 📂 Cấu trúc Thư mục

```text
software-security-labs/
├── lab1_kripke_access_model/             # Thực nghiệm mô hình trạng thái Kripke
├── lab2_testing_verification/            # Đặc tả kiểm chứng hình thức
├── lab3_secure_memory/                   # Mã nguồn C thực hành an toàn bộ nhớ
├── lab4_data_structures_static_analysis/ # Phân tích tĩnh cấu trúc dữ liệu & AST
├── lab5_sat_smt_verification/            # Bộ kiểm chứng logic với Z3 SMT Solver
├── lab6_bounded_model_checking/          # Bounded model checker thực nghiệm
├── lab7_dynamic_coverage/                # Đo độ bao phủ thực thi động
├── lab8_fuzzing/                         # Fuzzing engine và generator testcase
├── softsec-toolkit/                      # Bộ công cụ tiện ích hỗ trợ phân tích an toàn
├── specs/                                # Các file đặc tả kỹ thuật hệ thống
└── verification/                         # Báo cáo và ma trận chứng minh logic
```

---

## 🚀 Hướng dẫn Cài đặt & Sử dụng

### 1. Yêu cầu Môi trường
- **Python**: `>= 3.10`
- **Bộ giải SMT Z3**: `pip install z3-solver`
- **Compiler C/C++**: `GCC/Clang` hỗ trợ cờ bảo vệ `-fstack-protector-all`, `-D_FORTIFY_SOURCE=2`

### 2. Chạy bài thực nghiệm Z3 SMT (Lab 5)
```bash
cd lab5_sat_smt_verification
python -m unittest discover -s . -p "*.py"
```

### 3. Thực hiện Fuzzing kiểm thử an toàn (Lab 8)
```bash
cd lab8_fuzzing
python run_fuzzer.py --target=atpm_project --max-iterations=10000
```

---

## 👤 Tác giả & Thông tin Học thuật
- **Sinh viên**: Cao Đức Trung (MSSV: `23010018`)
- **Khoá học**: K17 CNTT — Đại học Phenikaa
- **Giảng viên hướng dẫn**: ThS. Vũ Quang Dũng
- **Giấy phép**: MIT License
