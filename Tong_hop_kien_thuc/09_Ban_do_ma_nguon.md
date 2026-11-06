# Chương 9. Bản đồ toàn bộ mã nguồn và dữ liệu liên quan

Có **84 file source**:53 Python, 30 C, 1 header. Bản đồ này liệt kê từng file, API và vai trò; phần giải thích nguyên lý ở Chương 1-4, walkthrough lab ở Chương 5, đặc tả ở Chương 6. Dòng API là vị trí trong file gốc, không phải số dòng của tài liệu tổng hợp.

## 9.1 Luồng gọi và tổ chức thư mục

| Nhóm | Chuỗi xử lý | Điểm vào cần đọc |
| --- | --- | --- |
| atpm | Test → module Python → mô hình/Z3/công cụ C → report | tests và API tương ứng từng chương |
| lab 1 | JSON/CSV → Kripke hoặc simulator C → property/witness | run_verification / main |
| lab 2 | Case PIN → ctypes/CLI → validate_pin → result/gcov | run_black_box_suite / compute_branch_coverage |
| lab 3-4 | C buggy/fixed → sanitizer/cppcheck → so sánh + risk | test_memory_safety / compare_versions |
| lab 5-6 | JSON điều kiện/chỉ số → Z3 → counterexample | run_all trong checker/engine |
| lab 7 | CSV → process_order → expected status + gcov | evaluate_suite |
| lab 8 | Seed → mutation → target → crash/coverage → corpus | fuzz trong hai fuzzer |
| toolkit | Ví dụ nhỏ độc lập, một số có main/demo | Từng file theo ch1/ch2/ch3/ch4 |

Không mặc nhiên dùng chung class Kripke của ba nhóm: định dạng input, tập toán tử và quy ước nhiều trạng thái đầu khác nhau. Các script Python gọi executable C cũng không tự kiểm tra toàn bộ contract C.

## 9.2 Nhóm atpm_project

Gói ví dụ tích hợp bốn chương: mô hình Kripke, bộ nhớ C, wrapper cppcheck, SMT/CBMC và fuzzing theo coverage. Python gọi công cụ ngoài qua subprocess; vì vậy kết quả phụ thuộc compiler, parser đầu ra và flags.

### atpm_project/atpm_project/c/ch2_memory/fixed.c

[Mở file nguồn](../atpm_project/atpm_project/c/ch2_memory/fixed.c) · 95 dòng · SHA-256 `075ac1c85b1d0073…`

Bản sửa các lỗi mục tiêu của vulnerable.c; kiểm tra allocation, copy và cleanup theo đường đi.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 11 | `void fixed_buffer_overflow(const char *user_input)` |  |
| 18 | `void fixed_format_string(const char *user_input)` |  |
| 23 | `int *fixed_integer_overflow_alloc(size_t count)` |  |
| 31 | `void fixed_use_after_free(void)` |  |
| 41 | `void fixed_double_free(void)` |  |
| 52 | `void fixed_memory_leak(void)` |  |
| 62 | `void fixed_null_deref(void)` |  |
| 78 | `void fixed_padding_leak(char *out_buffer)` |  |
| 86 | `int main(void)` |  |

### atpm_project/atpm_project/c/ch2_memory/safe_string.c

[Mở file nguồn](../atpm_project/atpm_project/c/ch2_memory/safe_string.c) · 47 dòng · SHA-256 `05daa12b123083d3…`

Cài đặt ss_copy/ss_concat theo capacity và ss_alloc_checked chống tràn kích thước. Return value giúp phát hiện truncation; source vẫn phải hợp lệ và tuân thủ contract overlap.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 7 | `size_t ss_copy(char *dst, size_t dst_size, const char *src)` |  |
| 19 | `size_t ss_concat(char *dst, size_t dst_size, const char *src)` |  |
| 36 | `void *ss_alloc_checked(size_t count, size_t elem_size)` |  |

### atpm_project/atpm_project/c/ch2_memory/safe_string.h

[Mở file nguồn](../atpm_project/atpm_project/c/ch2_memory/safe_string.h) · 23 dòng · SHA-256 `b7d15ab5250629ca…`

Giao diện helper chuỗi/cấp phát. Đọc contract về capacity, giá trị trả về và con trỏ cùng implementation.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 13 | `size_t ss_copy(char *dst, size_t dst_size, const char *src)` |  |
| 17 | `size_t ss_concat(char *dst, size_t dst_size, const char *src)` |  |
| 21 | `void *ss_alloc_checked(size_t count, size_t elem_size)` |  |

### atpm_project/atpm_project/c/ch2_memory/test_safe_string.c

[Mở file nguồn](../atpm_project/atpm_project/c/ch2_memory/test_safe_string.c) · 90 dòng · SHA-256 `6ab5f27f411cab02…`

Test helper copy/concat và cấp phát có kiểm tra tràn. Cần phân biệt test các ca đã viết với bằng chứng mọi input.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 18 | `void test_ss_copy_normal(void)` |  |
| 25 | `void test_ss_copy_truncate(void)` |  |
| 33 | `void test_ss_copy_empty_src(void)` |  |
| 40 | `void test_ss_copy_null_src(void)` |  |
| 47 | `void test_ss_copy_zero_size(void)` |  |
| 53 | `void test_ss_concat_normal(void)` |  |
| 59 | `void test_ss_concat_truncate(void)` |  |
| 66 | `void test_ss_alloc_checked_normal(void)` |  |
| 72 | `void test_ss_alloc_checked_overflow(void)` |  |
| 77 | `int main(void)` |  |

### atpm_project/atpm_project/c/ch2_memory/vulnerable.c

[Mở file nguồn](../atpm_project/atpm_project/c/ch2_memory/vulnerable.c) · 83 dòng · SHA-256 `0c78c5c332b769b9…`

Ví dụ lỗi overflow, UAF và leak để đối chiếu sanitizer/phân tích tĩnh.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 14 | `void bug_buffer_overflow(const char *user_input)` |  |
| 21 | `void bug_format_string(const char *user_input)` |  |
| 26 | `int *bug_integer_overflow_alloc(unsigned int count)` |  |
| 33 | `void bug_use_after_free(void)` |  |
| 42 | `void bug_double_free(void)` |  |
| 49 | `void bug_memory_leak(void)` |  |
| 56 | `void bug_null_deref(void)` |  |
| 71 | `void bug_padding_leak(char *out_buffer)` |  |
| 79 | `int main(void)` |  |

### atpm_project/atpm_project/c/ch3_static/bmc_demo.c

[Mở file nguồn](../atpm_project/atpm_project/c/ch3_static/bmc_demo.c) · 74 dòng · SHA-256 `131b2dc2eed9a5a0…`

Các hàm cộng/mảng/chia và bản sửa cho CBMC; harness, assumptions và unwind quyết định phạm vi kiểm tra.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 9 | `int sum_array(int *arr, int n)` |  |
| 17 | `void check_sum(void)` |  |
| 24 | `void write_n(int *buffer, int n)` |  |
| 30 | `void check_overflow(void)` |  |
| 36 | `void write_n_fixed(int *buffer, int n)` |  |
| 42 | `void check_overflow_fixed(void)` |  |
| 48 | `int safe_divide(int a, int b)` |  |
| 52 | `int nondet_int(void)` |  |
| 54 | `void check_divide(void)` |  |
| 60 | `void check_divide_guarded(void)` |  |
| 68 | `void check_heap(void)` |  |

### atpm_project/atpm_project/c/ch4_dynamic/fuzz_target.c

[Mở file nguồn](../atpm_project/atpm_project/c/ch4_dynamic/fuzz_target.c) · 28 dòng · SHA-256 `a48050d1adfee4e0…`

Target magic FUZZ theo từng byte để coverage có tiến triển; input đủ prefix đi vào đường gây lỗi. Hai bản file ở C và Python trùng hash.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 11 | `void check_magic(const char *buf, int len)` |  |
| 20 | `int main(int argc, char **argv)` |  |

### atpm_project/atpm_project/python/atpm/__init__.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/__init__.py) · 0 dòng · SHA-256 `e3b0c44298fc1c14…`

Đánh dấu package Python; file rỗng trong bộ nguồn này, không chứa thuật toán.

Không có hàm/lớp riêng; xem biến, import, khai báo hoặc nội dung file.

### atpm_project/atpm_project/python/atpm/ch1_concepts/__init__.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch1_concepts/__init__.py) · 0 dòng · SHA-256 `e3b0c44298fc1c14…`

Đánh dấu package Python; file rỗng trong bộ nguồn này, không chứa thuật toán.

Không có hàm/lớp riêng; xem biến, import, khai báo hoặc nội dung file.

### atpm_project/atpm_project/python/atpm/ch1_concepts/kripke.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch1_concepts/kripke.py) · 171 dòng · SHA-256 `b177e7d37a4803c5…`

KripkeStructure với validate_total, reachable BFS, invariant/reachability, phản ví dụ và DOT; build_login_example có biến thể bypass.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 22 | `class KripkeStructureError` | Loi cau truc: vi pham tinh 'total' cua quan he chuyen trang thai, |
| 28 | `class KripkeStructure` |  |
| 34 | `KripkeStructure.add_state(self, s: str, labels: Iterable[str]=())` |  |
| 40 | `KripkeStructure.set_initial(self, *states: str)` |  |
| 46 | `KripkeStructure.add_transition(self, src: str, dst: str)` |  |
| 51 | `KripkeStructure.validate_total(self)` | Theo dinh nghia hinh thuc, R phai la 'total': moi trang thai |
| 62 | `KripkeStructure.labels_of(self, s: str)` |  |
| 67 | `KripkeStructure.reachable_from(self, start_states: Optional[Iterable[str]]=None)` | BFS: tap trang thai co the toi duoc tu tap trang thai khoi dau. |
| 79 | `KripkeStructure.check_invariant(self, unsafe_label: str)` | Kiem tra thuoc tinh AG(not unsafe_label): 'tren moi duong thi hanh, |
| 110 | `KripkeStructure._rebuild_path(parent: Dict[str, Optional[str]], target: str)` |  |
| 117 | `KripkeStructure.check_reachability(self, goal_label: str)` | Kiem tra thuoc tinh EF(goal_label): 'ton tai it nhat mot duong |
| 125 | `KripkeStructure.to_dot(self)` | Xuat sang dinh dang Graphviz DOT de truc quan hoa (dung trong slide). |
| 139 | `build_login_example()` | Vi du kinh dien dung trong bai giang: mo hinh hoa mot he thong dang |

### atpm_project/atpm_project/python/atpm/ch2_secure_c/__init__.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch2_secure_c/__init__.py) · 0 dòng · SHA-256 `e3b0c44298fc1c14…`

Đánh dấu package Python; file rỗng trong bộ nguồn này, không chứa thuật toán.

Không có hàm/lớp riêng; xem biến, import, khai báo hoặc nội dung file.

### atpm_project/atpm_project/python/atpm/ch2_secure_c/static_check.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch2_secure_c/static_check.py) · 125 dòng · SHA-256 `3f12ddba019b8611…`

Wrapper cppcheck: chạy công cụ, parse XML thành finding/report, lọc mức độ và quét thư mục. Parse lỗi thành report rỗng là giới hạn cần nhớ.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 20 | `class CppcheckFinding` |  |
| 30 | `class CppcheckReport` |  |
| 33 | `CppcheckReport.by_severity(self)` |  |
| 36 | `CppcheckReport.errors_and_warnings(self)` |  |
| 39 | `CppcheckReport.summary(self)` |  |
| 47 | `class CppcheckNotFoundError` | Cppcheck khong duoc cai dat hoac khong tim thay trong PATH. |
| 51 | `run_cppcheck(paths: List[str] \| str, std: str='c11', enable: str='all')` | Chay cppcheck tren danh sach file/thu muc va tra ve CppcheckReport. |
| 83 | `_parse_cppcheck_xml(xml_text: str)` |  |
| 110 | `scan_directory(directory: str, pattern: str='*.c')` | Chay cppcheck tren toan bo file khop pattern trong mot thu muc. |

### atpm_project/atpm_project/python/atpm/ch3_static_analysis/__init__.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch3_static_analysis/__init__.py) · 0 dòng · SHA-256 `e3b0c44298fc1c14…`

Đánh dấu package Python; file rỗng trong bộ nguồn này, không chứa thuật toán.

Không có hàm/lớp riêng; xem biến, import, khai báo hoặc nội dung file.

### atpm_project/atpm_project/python/atpm/ch3_static_analysis/smt_checks.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch3_static_analysis/smt_checks.py) · 136 dòng · SHA-256 `fe0db1022eaf2478…`

Z3 kiểm tra chỉ số, multiplication overflow, chia0; wrapper CBMC cho code C. So sánh signed/unsigned và sat/unsat/unknown phải đúng mục tiêu.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 20 | `class SmtCheckResult` |  |
| 25 | `check_index_bounds(index_min: int, index_max_exclusive: int, assume_checked: bool=False)` | Tuong ung slide 'kiem tra Buffer Overflow bang Z3'. |
| 46 | `check_integer_overflow_multiply(bits: int=32, elem_size: int=4)` | Tuong ung slide 'Integer Overflow -- ma hoa bang Bitvector'. |
| 62 | `check_division_safety(assume_nonzero: bool=False)` | Tuong ung bai tap tong hop 3.7: kiem tra 'chia cho 0' bang Z3 |
| 81 | `class CbmcResult` |  |
| 87 | `class CbmcNotFoundError` |  |
| 91 | `run_cbmc(c_file: str, function: str, extra_flags: Optional[list[str]]=None, unwind: int=10, timeout: int=60)` | Chay CBMC tren mot file C, tra ve CbmcResult da phan tich. |

### atpm_project/atpm_project/python/atpm/ch4_dynamic_analysis/__init__.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch4_dynamic_analysis/__init__.py) · 0 dòng · SHA-256 `e3b0c44298fc1c14…`

Đánh dấu package Python; file rỗng trong bộ nguồn này, không chứa thuật toán.

Không có hàm/lớp riêng; xem biến, import, khai báo hoặc nội dung file.

### atpm_project/atpm_project/python/atpm/ch4_dynamic_analysis/fuzz_target.c

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch4_dynamic_analysis/fuzz_target.c) · 28 dòng · SHA-256 `a48050d1adfee4e0…`

Target magic FUZZ theo từng byte để coverage có tiến triển; input đủ prefix đi vào đường gây lỗi. Hai bản file ở C và Python trùng hash.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 11 | `void check_magic(const char *buf, int len)` |  |
| 20 | `int main(int argc, char **argv)` |  |

### atpm_project/atpm_project/python/atpm/ch4_dynamic_analysis/fuzzing.py

[Mở file nguồn](../atpm_project/atpm_project/python/atpm/ch4_dynamic_analysis/fuzzing.py) · 154 dòng · SHA-256 `57e6b70aecc59b8a…`

Biên dịch target, đo gcov, chạy random/coverage-guided fuzzing. Crash/hang và cách tính coverage còn giản lược.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 25 | `class FuzzResult` |  |
| 32 | `compile_with_coverage(source: str, output_binary: str)` | Bien dich file C voi flag --coverage (sinh .gcno, dung cho gcov). |
| 57 | `_reset_coverage_counters(work_dir: str)` |  |
| 62 | `measure_coverage_percent(source_basename: str, work_dir: str)` | Chay gcov va tra ve % dong lenh da duoc thuc thi (cumulative). |
| 72 | `_run_target(binary_path: str, input_bytes: bytes, work_dir: str)` | Chay target voi input (ghi ra file tam), tra ve returncode. |
| 86 | `black_box_fuzz(binary_path: str, max_iterations: int=5000, input_len: int=4, seed: int=1)` | Fuzzing hop den THUAN TUY: sinh byte NGAU NHIEN, KHONG dung feedback |
| 101 | `coverage_guided_fuzz(binary_path: str, source_basename: str, max_iterations: int=5000, input_len_max: int=8, seed: int=1)` | Fuzzing huong dan boi code coverage (don gian hoa nguyen ly cua |

### atpm_project/atpm_project/python/tests/__init__.py

[Mở file nguồn](../atpm_project/atpm_project/python/tests/__init__.py) · 0 dòng · SHA-256 `e3b0c44298fc1c14…`

Đánh dấu package Python; file rỗng trong bộ nguồn này, không chứa thuật toán.

Không có hàm/lớp riêng; xem biến, import, khai báo hoặc nội dung file.

### atpm_project/atpm_project/python/tests/test_ch1_kripke.py

[Mở file nguồn](../atpm_project/atpm_project/python/tests/test_ch1_kripke.py) · 48 dòng · SHA-256 `e9125bf3628a5c2a…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 7 | `test_login_example_finds_vulnerability()` |  |
| 15 | `test_reachability_admin()` |  |
| 23 | `test_total_transition_relation_enforced()` |  |
| 37 | `test_safe_variant_without_bypass()` |  |

### atpm_project/atpm_project/python/tests/test_ch2_static_check.py

[Mở file nguồn](../atpm_project/atpm_project/python/tests/test_ch2_static_check.py) · 51 dòng · SHA-256 `04d6f9eae1931502…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 12 | `_cppcheck_available()` |  |
| 18 | `test_scan_vulnerable_c_finds_known_bugs()` |  |
| 28 | `test_fixed_c_has_no_error_severity_findings()` |  |
| 34 | `test_empty_xml_returns_empty_report()` |  |
| 41 | `test_report_summary_counts_by_severity()` |  |

### atpm_project/atpm_project/python/tests/test_ch3_smt_checks.py

[Mở file nguồn](../atpm_project/atpm_project/python/tests/test_ch3_smt_checks.py) · 79 dòng · SHA-256 `6cf91dfd3a6887c8…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 13 | `_cbmc_available()` |  |
| 19 | `test_index_bounds_finds_violation_without_check()` |  |
| 25 | `test_index_bounds_safe_with_check()` |  |
| 31 | `test_integer_overflow_multiply_detected()` |  |
| 36 | `test_division_safety_without_guard()` |  |
| 41 | `test_division_safety_with_guard()` |  |
| 49 | `test_cbmc_check_sum_succeeds_with_enough_unwind()` |  |
| 55 | `test_cbmc_detects_off_by_one_overflow()` |  |
| 63 | `test_cbmc_fixed_version_passes()` |  |
| 70 | `test_cbmc_detects_division_by_zero()` |  |
| 77 | `test_cbmc_guarded_division_passes()` |  |

### atpm_project/atpm_project/python/tests/test_ch4_fuzzing.py

[Mở file nguồn](../atpm_project/atpm_project/python/tests/test_ch4_fuzzing.py) · 53 dòng · SHA-256 `84fd33631d10d983…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 14 | `_gcc_available()` |  |
| 19 | `compiled_binary()` |  |
| 29 | `test_coverage_increases_with_partial_magic_match(compiled_binary)` |  |
| 41 | `test_black_box_fuzz_fails_within_small_budget(compiled_binary)` |  |
| 48 | `test_coverage_guided_fuzz_finds_crash(compiled_binary)` |  |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.3 Nhóm lab 1_kripke_access_model

Mô hình access control từ JSON và CSV, duyệt reachable, tìm witness và mô phỏng C. Hai bộ SAFE/BUGGY là dữ liệu đối chiếu.

### lab1_kripke_access_model/lab1_kripke_access_model/c/access_simulator.c

[Mở file nguồn](../lab1_kripke_access_model/lab1_kripke_access_model/c/access_simulator.c) · 236 dòng · SHA-256 `db43ce8d8788bd39…`

Đọc CSV trạng thái/chuyển tiếp, chạy chuỗi sự kiện và cảnh báo trạng thái không an toàn; parser CSV/atoi là bản nhỏ cho bài học.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 60 | `static int safe_read_line(FILE *fp, char *buf, size_t bufsize)` |  |
| 73 | `static int split_csv(char *line, char *fields[], int max_fields)` |  |
| 83 | `static int load_states(const char *path)` |  |
| 109 | `static int load_transitions(const char *path)` |  |
| 135 | `static const State *find_state(const char *id)` |  |
| 142 | `static int has_label(const State *s, const char *label)` |  |
| 158 | `static const char *next_state(const char *cur, const char *event)` |  |
| 168 | `int main(int argc, char *argv[])` |  |

### lab1_kripke_access_model/lab1_kripke_access_model/python/kripke_model.py

[Mở file nguồn](../lab1_kripke_access_model/lab1_kripke_access_model/python/kripke_model.py) · 218 dòng · SHA-256 `baf12103d5d45495…`

Nạp JSON, BFS và kiểm tra các dạng AG/EF hạn chế của bài access-control; chuyển witness trạng thái thành sự kiện.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 38 | `class KripkeStructure` |  |
| 46 | `KripkeStructure.from_json(cls, path: str)` |  |
| 65 | `KripkeStructure.reachable_states(self)` | Tra ve tap tat ca trang thai co the den duoc tu cac trang thai khoi tao. |
| 78 | `KripkeStructure._find_path(self, target_predicate)` | BFS tim duong di ngan nhat tu init den mot trang thai thoa target_predicate. |
| 98 | `KripkeStructure._eval_formula(self, state_id: str, formula: str)` |  |
| 116 | `KripkeStructure._eval_and(expr: str, atom_fn)` |  |
| 123 | `KripkeStructure.check_AG_not(self, formula: str)` | AG !formula : khong trang thai nao dat duoc thoa 'formula'. |
| 132 | `KripkeStructure.check_AG_implies(self, formula: str)` | AG (p -> q): tren MOI trang thai reachable, neu p dung thi q phai dung. |
| 144 | `KripkeStructure.check_EF(self, formula: str)` | EF formula: ton tai duong di den mot trang thai thoa 'formula'. |
| 149 | `KripkeStructure.check_property(self, prop: dict)` |  |
| 160 | `KripkeStructure.path_to_events(self, path: List[str])` |  |
| 167 | `load_full_spec(path: str)` |  |
| 172 | `run_verification(model_path: str, verbose: bool=True)` | Chay toan bo kiem chung cho mot mo hinh, tra ve dict ket qua co cau truc |

### lab1_kripke_access_model/lab1_kripke_access_model/tests/test_kripke.py

[Mở file nguồn](../lab1_kripke_access_model/lab1_kripke_access_model/tests/test_kripke.py) · 101 dòng · SHA-256 `36f17ae9b6b2027c…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 27 | `test_safe_model_all_properties_hold()` |  |
| 33 | `test_buggy_model_violates_p1()` |  |
| 43 | `test_buggy_model_reachability_still_holds()` |  |
| 49 | `_ensure_c_binary_built()` |  |
| 58 | `test_c_simulator_detects_runtime_violation()` |  |
| 72 | `test_c_simulator_safe_sequence_no_warning()` |  |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.4 Nhóm lab 2_testing_verification

Hàm kiểm tra PIN C được gọi từ ctypes và CLI; test black-box theo partition/boundary, đo dòng gcov qua white-box runner.

### lab2_testing_verification/lab2_testing_verification/c/pin_validator.c

[Mở file nguồn](../lab2_testing_verification/lab2_testing_verification/c/pin_validator.c) · 144 dòng · SHA-256 `2e87e09407e583ce…`

Validation PIN6 chữ số, NULL/length/non-digit, lockout>=3 và chuỗi tăng/giảm dễ đoán; có CLI đọc dataset.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 42 | `static int is_sequential(const char *pin)` |  |
| 54 | `PinResult validate_pin(const char *pin, int failed_attempts)` |  |
| 76 | `const char *pin_result_to_string(PinResult r)` |  |
| 91 | `int main(int argc, char *argv[])` |  |

### lab2_testing_verification/lab2_testing_verification/python/black_box_tester.py

[Mở file nguồn](../lab2_testing_verification/lab2_testing_verification/python/black_box_tester.py) · 124 dòng · SHA-256 `53bd81d60f1aa76d…`

Build shared library, nạp ctypes, sinh18 case và lưu kết quả. Đường dẫn .so giả định môi trường kiểu POSIX.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 33 | `build_shared_lib()` |  |
| 40 | `load_lib()` |  |
| 49 | `generate_black_box_cases()` | Sinh test case theo Equivalence Partitioning + Boundary Value Analysis. |
| 93 | `run_black_box_suite(save_csv: str \| None=None)` |  |

### lab2_testing_verification/lab2_testing_verification/python/white_box_coverage.py

[Mở file nguồn](../lab2_testing_verification/lab2_testing_verification/python/white_box_coverage.py) · 110 dòng · SHA-256 `2f39dc034959c51e…`

Build target có counter, chạy dataset, đọc gcov. Hàm tên compute_branch_coverage thực tế đếm dòng.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 20 | `build_instrumented_cli()` | Bien dich pin_validator voi co --coverage (sinh file .gcno) va driver |
| 37 | `run_cli_with_dataset(csv_path: str)` |  |
| 45 | `compute_branch_coverage()` | Chay gcov, phan tich phan tram branch coverage cho pin_validator.c. |
| 74 | `clean_coverage_artifacts()` |  |

### lab2_testing_verification/lab2_testing_verification/tests/test_pin_validator.py

[Mở file nguồn](../lab2_testing_verification/lab2_testing_verification/tests/test_pin_validator.py) · 60 dòng · SHA-256 `9fb44f00409290f7…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 20 | `test_black_box_suite_all_pass()` |  |
| 27 | `test_white_box_coverage_meets_threshold()` |  |
| 39 | `test_account_lockout_boundary()` | Kiem tra rieng bien 3 lan sai = khoa tai khoan (BVA). |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.5 Nhóm lab 3_secure_memory

Inventory C bản lỗi và bản sửa, test sanitizer và công thức chấm rủi ro CVSS-like.

### lab3_secure_memory/lab3_secure_memory/c/secure_inventory.c

[Mở file nguồn](../lab3_secure_memory/lab3_secure_memory/c/secure_inventory.c) · 117 dòng · SHA-256 `2605c2cfb48ae67a…`

Sửa lỗi bộ nhớ của inventory theo bài; tiếp tục xem NULL input, count và đường failure nếu dùng như API tổng quát.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 35 | `char *add_book_title_SAFE_HEAP(const char *title)` |  |
| 42 | `int add_book_title_SAFE(Book *b, const char *title)` |  |
| 55 | `void demo_use_after_free_FIXED(void)` |  |
| 70 | `void demo_memory_leak_FIXED(int count)` |  |
| 88 | `int main(int argc, char *argv[])` |  |

### lab3_secure_memory/lab3_secure_memory/c/vulnerable_inventory.c

[Mở file nguồn](../lab3_secure_memory/lab3_secure_memory/c/vulnerable_inventory.c) · 106 dòng · SHA-256 `bea8ca49d13d5aae…`

Đối tượng sách và chuỗi cấp phát heap chứa overflow/UAF/leak; input chọn từng lỗi giúp tái hiện riêng.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 34 | `void add_book_title_UNSAFE(Book *b, const char *title)` |  |
| 46 | `char *add_book_title_UNSAFE_HEAP(const char *title)` |  |
| 55 | `void demo_use_after_free(void)` |  |
| 66 | `void demo_memory_leak(int count)` |  |
| 75 | `int main(int argc, char *argv[])` |  |

### lab3_secure_memory/lab3_secure_memory/python/risk_assessor.py

[Mở file nguồn](../lab3_secure_memory/lab3_secure_memory/python/risk_assessor.py) · 113 dòng · SHA-256 `b2f2dce30c8051ab…`

Trọng số AV/AC/PR/UI và C/I/A, tính subscore/base/severity, xuất report. Đây là CVSS-like, không đầy đủ CVSS3.1.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 38 | `exploitability_subscore(v: dict)` |  |
| 47 | `impact_subscore(v: dict)` |  |
| 55 | `base_score(v: dict)` |  |
| 64 | `severity_label(score: float)` |  |
| 76 | `assess_all(dataset_path: str)` |  |
| 95 | `print_report(results: list[dict])` |  |

### lab3_secure_memory/lab3_secure_memory/tests/test_memory_safety.py

[Mở file nguồn](../lab3_secure_memory/lab3_secure_memory/tests/test_memory_safety.py) · 117 dòng · SHA-256 `425a3183b0b587ed…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 21 | `_build(src_name: str, bin_name: str)` |  |
| 28 | `_run(bin_name: str, args: list[str])` |  |
| 35 | `setup_module(_module=None)` |  |
| 40 | `test_vulnerable_overflow_detected()` |  |
| 46 | `test_vulnerable_uaf_detected()` |  |
| 52 | `test_vulnerable_leak_detected()` |  |
| 61 | `test_secure_overflow_clean()` |  |
| 67 | `test_secure_uaf_clean()` |  |
| 73 | `test_secure_leak_clean()` |  |
| 83 | `test_risk_assessment_matches_baseline()` |  |
| 94 | `test_critical_vuln_is_the_buffer_overflow()` |  |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.6 Nhóm lab 4_data_structures_static_analysis

Linked list trước/sau sửa; chạy cppcheck, lọc finding và đối chiếu baseline.

### lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/c/booklist_v1_buggy.c

[Mở file nguồn](../lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/c/booklist_v1_buggy.c) · 113 dòng · SHA-256 `abaa8f784a5011f8…`

Danh sách sách với count chưa khởi tạo, malloc thiếu guard và unlink chưa free.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 30 | `BookNode *list_insert_front(BookNode *head, const char *title, int year)` |  |
| 41 | `BookNode *list_remove_by_title(BookNode *head, const char *title)` |  |
| 64 | `int list_count_UNSAFE(BookNode *head)` |  |
| 78 | `void list_print(BookNode *head)` |  |
| 84 | `void list_free_all(BookNode *head)` |  |
| 94 | `int main(void)` |  |

### lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/c/booklist_v2_fixed.c

[Mở file nguồn](../lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/c/booklist_v2_fixed.c) · 91 dòng · SHA-256 `489d8ada2a69676a…`

Khởi tạo count, xử lý allocation failure và free node xóa; đối chiếu invariants của list.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 19 | `BookNode *list_insert_front(BookNode *head, const char *title, int year)` |  |
| 31 | `BookNode *list_remove_by_title(BookNode *head, const char *title)` |  |
| 49 | `int list_count_SAFE(BookNode *head)` |  |
| 57 | `void list_print(BookNode *head)` |  |
| 63 | `void list_free_all(BookNode *head)` |  |
| 73 | `int main(void)` |  |

### lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/python/static_analysis_runner.py

[Mở file nguồn](../lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/python/static_analysis_runner.py) · 106 dòng · SHA-256 `034994e897d93e0f…`

Thu XML cppcheck từ stderr, lọc error/warning và so sánh hai phiên bản với baseline.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 33 | `run_cppcheck(c_file: str)` | Chay cppcheck tren 1 file C, tra ve danh sach finding da duoc loc. |
| 57 | `security_relevant(findings: list[dict])` | Chi giu lai cac finding co muc do error/warning (loai bo style/info |
| 63 | `compare_versions(buggy_file: str, fixed_file: str)` |  |
| 76 | `print_report(result: dict)` |  |

### lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/tests/test_static_analysis.py

[Mở file nguồn](../lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/tests/test_static_analysis.py) · 73 dòng · SHA-256 `1aac3380a079c10c…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 21 | `test_buggy_compiles_and_runs()` |  |
| 29 | `test_fixed_compiles_and_runs_correct_count()` |  |
| 38 | `test_cppcheck_detects_issues_in_buggy_version()` |  |
| 43 | `test_cppcheck_clean_on_fixed_version()` |  |
| 48 | `test_matches_baseline()` |  |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.7 Nhóm lab 5_sat_smt_verification

Sáu cặp điều kiện, kiểm tra XOR bằng Z3 và brute-force C cho một miền nhỏ.

### lab5_sat_smt_verification/lab5_sat_smt_verification/c/brute_force_checker.c

[Mở file nguồn](../lab5_sat_smt_verification/lab5_sat_smt_verification/c/brute_force_checker.c) · 131 dòng · SHA-256 `aa88c4096aa77ae9…`

Liệt kê miền giá trị nhỏ và tìm cặp điều kiện khác kết quả; minh họa đối chứng SMT.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 27 | `static bool cond01_original(bool authenticated, bool unlocked_requested, bool alarm_active)` |  |
| 30 | `static bool cond01_optimized(bool authenticated, bool unlocked_requested, bool alarm_active)` |  |
| 35 | `static bool cond03_original(bool len_ok, bool all_digits, bool not_sequential)` |  |
| 38 | `static bool cond03_optimized(bool len_ok, bool all_digits, bool not_sequential)` |  |
| 43 | `static bool cond04_original(bool tamper, bool alarm)` |  |
| 46 | `static bool cond04_optimized(bool tamper, bool alarm)` |  |
| 51 | `static bool cond05_original(bool authenticated, bool is_admin, bool bypass_flag)` |  |
| 55 | `static bool cond05_optimized(bool authenticated, bool is_admin, bool bypass_flag)` |  |
| 61 | `static int enumerate3(const char *name, bool (*orig)(bool, bool, bool), bool (*opt)(bool, bool, bool))` |  |
| 89 | `static int enumerate2(const char *name, bool (*orig)(bool, bool), bool (*opt)(bool, bool))` |  |
| 110 | `int main(void)` |  |

### lab5_sat_smt_verification/lab5_sat_smt_verification/python/smt_equivalence_checker.py

[Mở file nguồn](../lab5_sat_smt_verification/lab5_sat_smt_verification/python/smt_equivalence_checker.py) · 110 dòng · SHA-256 `e774df12d12e7c68…`

Dựng biến/biểu thức Z3 từ dataset rồi giải XOR để tìm counterexample. eval chỉ dành dữ liệu tin cậy.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 32 | `make_vars(var_types: dict)` | Tao cac bien Z3 tuong ung khai bao kieu trong dataset. |
| 45 | `eval_expr(expr_str: str, env: dict)` | Danh gia mot chuoi bieu thuc Z3 (vi du 'And(a, Not(b))') trong ngu |
| 53 | `check_equivalence(pair: dict)` |  |
| 81 | `run_all(dataset_path: str)` |  |
| 87 | `print_report(results: list[dict])` |  |

### lab5_sat_smt_verification/lab5_sat_smt_verification/tests/test_smt_verification.py

[Mở file nguồn](../lab5_sat_smt_verification/lab5_sat_smt_verification/tests/test_smt_verification.py) · 83 dòng · SHA-256 `930219017979e09a…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 23 | `test_all_pairs_match_expectation()` |  |
| 30 | `test_counterexample_is_valid_for_non_equivalent_pairs()` |  |
| 56 | `test_c_brute_force_matches_z3()` |  |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.8 Nhóm lab 6_bounded_model_checking

Mã C truy cập mảng và engine Python mã hóa chỉ số theo cấu hình JSON; không phải compiler C tổng quát.

### lab6_bounded_model_checking/lab6_bounded_model_checking/c/array_access.c

[Mở file nguồn](../lab6_bounded_model_checking/lab6_bounded_model_checking/c/array_access.c) · 87 dòng · SHA-256 `ce6adf3bd3827d6f…`

Quét mảng 10 phần tử với <, <= và offset; có bản guard offset0..5.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 21 | `static void fill_catalog(CatalogEntry catalog[ARRAY_SIZE])` |  |
| 29 | `static void safe_full_scan(CatalogEntry catalog[ARRAY_SIZE])` |  |
| 36 | `static void offbyone_scan(CatalogEntry catalog[ARRAY_SIZE])` |  |
| 43 | `static void symbolic_unsafe(CatalogEntry catalog[ARRAY_SIZE], int base_index)` |  |
| 51 | `static void symbolic_safe(CatalogEntry catalog[ARRAY_SIZE], int base_index)` |  |
| 63 | `int main(int argc, char *argv[])` |  |

### lab6_bounded_model_checking/lab6_bounded_model_checking/python/bmc_engine.py

[Mở file nguồn](../lab6_bounded_model_checking/lab6_bounded_model_checking/python/bmc_engine.py) · 124 dòng · SHA-256 `fe725cbf23a8424b…`

Unroll chỉ số và tìm vi phạm biên theo từng bước từ JSON; báo SAFE-UP-TO-BOUND và witness.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 35 | `run_bmc(program: dict)` |  |
| 90 | `run_all(dataset_path: str)` |  |
| 103 | `print_report(results: list[dict])` |  |

### lab6_bounded_model_checking/lab6_bounded_model_checking/tests/test_bmc.py

[Mở file nguồn](../lab6_bounded_model_checking/lab6_bounded_model_checking/tests/test_bmc.py) · 87 dòng · SHA-256 `4d55a76d44c451d4…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 25 | `test_bmc_results_match_expectation()` |  |
| 32 | `test_bmc03_witness_matches_c_runtime_bug()` | Nhan chung cua BMC-03 (base_index=9) phai la gia tri THUC SU gay loi |
| 50 | `test_c_safe_full_scan_no_crash()` |  |
| 59 | `test_c_symbolic_safe_with_precondition_rejects_bad_input()` |  |
| 66 | `test_c_symbolic_safe_with_valid_input_runs_clean()` |  |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.9 Nhóm lab 7_dynamic_coverage

Xử lý đơn hàng, bộ test partial/full/combinatorial, harness CSV và đo line coverage gcov.

### lab7_dynamic_coverage/lab7_dynamic_coverage/c/order_processor.c

[Mở file nguồn](../lab7_dynamic_coverage/lab7_dynamic_coverage/c/order_processor.c) · 147 dòng · SHA-256 `0e1afc9398d9a95b…`

Validate số lượng/giá, phân mức giảm giá theo member/quantity và ngưỡng phê duyệt; CLI CSV có cả đường lỗi parser.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 48 | `OrderStatus process_order(int quantity, double unit_price, int is_member, OrderResult *out)` |  |
| 86 | `const char *order_status_to_string(OrderStatus s)` |  |
| 99 | `int main(int argc, char *argv[])` |  |

### lab7_dynamic_coverage/lab7_dynamic_coverage/python/coverage_runner.py

[Mở file nguồn](../lab7_dynamic_coverage/lab7_dynamic_coverage/python/coverage_runner.py) · 115 dòng · SHA-256 `9852cafd3e3c33f6…`

Dọn counter, build gcov, chạy input suite, so kết quả và tính dòng phủ.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 27 | `clean_coverage_artifacts()` |  |
| 33 | `build_instrumented()` |  |
| 45 | `run_test_suite(csv_path: str)` |  |
| 53 | `compute_coverage()` |  |
| 77 | `evaluate_suite(csv_name: str)` |  |

### lab7_dynamic_coverage/lab7_dynamic_coverage/python/test_case_generator.py

[Mở file nguồn](../lab7_dynamic_coverage/lab7_dynamic_coverage/python/test_case_generator.py) · 82 dòng · SHA-256 `e920044b57df8442…`

Sinh48 ca từ6 quantity×4 price×2 membership và tính expected_status. Reference gần code C nên cần oracle độc lập.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 36 | `expected_status(qty: int, price: float, is_member: int)` | Mo phong lai dac ta cua process_order() (oracle doc lap voi C code, |
| 53 | `generate_combinatorial_cases()` |  |
| 67 | `save_csv(cases: list[dict], path: str)` |  |

### lab7_dynamic_coverage/lab7_dynamic_coverage/tests/test_coverage.py

[Mở file nguồn](../lab7_dynamic_coverage/lab7_dynamic_coverage/tests/test_coverage.py) · 69 dòng · SHA-256 `96d073d32c0bf079…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 20 | `test_partial_suite_all_pass()` |  |
| 25 | `test_full_suite_all_pass()` |  |
| 30 | `test_full_suite_covers_significantly_more_than_partial()` |  |
| 40 | `test_combinatorial_suite_all_pass_and_matches_or_exceeds_full_coverage()` |  |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.10 Nhóm lab 8_fuzzing

Parser ADMIN/ORDER, seed corpus, random mutation và fuzzer có feedback tập dòng; sanitizer là oracle lỗi bộ nhớ.

### lab8_fuzzing/lab8_fuzzing/c/fuzz_target.c

[Mở file nguồn](../lab8_fuzzing/lab8_fuzzing/c/fuzz_target.c) · 55 dòng · SHA-256 `cfbe6debb3d59d08…`

Parser ADMIN/ORDER: ADMIN payload bắt đầu X đi vào strcpy cmd[16]; input ADMIN:X kèm nhiều A là regression overflow.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 26 | `void process_input(const char *line)` |  |
| 48 | `int main(int argc, char *argv[])` |  |

### lab8_fuzzing/lab8_fuzzing/python/blackbox_fuzzer.py

[Mở file nguồn](../lab8_fuzzing/lab8_fuzzing/python/blackbox_fuzzer.py) · 105 dòng · SHA-256 `1fd3067788f4e5b5…`

Đọc seed, mutation byte/token, chạy target và gom input crash; thêm corpus có yếu tố ngẫu nhiên.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 31 | `load_seeds()` |  |
| 39 | `mutate(s: str, rng: random.Random)` |  |
| 58 | `run_target(input_str: str)` |  |
| 65 | `build_target()` |  |
| 73 | `fuzz(iterations: int=2000, seed: int=42)` |  |

### lab8_fuzzing/lab8_fuzzing/python/whitebox_fuzzer.py

[Mở file nguồn](../lab8_fuzzing/lab8_fuzzing/python/whitebox_fuzzer.py) · 172 dòng · SHA-256 `93c105be33a3963f…`

Mutation và queue input theo tập dòng mới đo bằng gcov; có thêm operator/token nên khác black-box ở nhiều yếu tố.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 36 | `load_seeds()` |  |
| 44 | `mutate(s: str, rng: random.Random)` |  |
| 72 | `build_target()` |  |
| 83 | `run_and_get_coverage(input_str: str)` | Chay 1 lan (co lap coverage - xoa .gcda truoc do), tra ve |
| 114 | `fuzz(iterations: int=500, seed: int=7)` |  |

### lab8_fuzzing/lab8_fuzzing/tests/test_fuzzing.py

[Mở file nguồn](../lab8_fuzzing/lab8_fuzzing/tests/test_fuzzing.py) · 76 dòng · SHA-256 `68d69731078f2ae2…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 23 | `_build()` |  |
| 31 | `test_normal_inputs_do_not_crash()` |  |
| 39 | `test_known_crash_input_triggers_asan()` |  |
| 48 | `test_whitebox_fuzzer_finds_crash_within_budget()` |  |
| 55 | `test_blackbox_fuzzer_fails_within_same_budget()` |  |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.11 Nhóm softsec-toolkit

Các ví dụ nhỏ theo từng chủ đề, thường chạy độc lập. Có ví dụ mô phỏng khái niệm và ví dụ cần Z3/CBMC/sanitizer; không coi mọi script là công cụ công nghiệp.

### softsec-toolkit/softsec-toolkit/ch1_models/__init__.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch1_models/__init__.py) · 8 dòng · SHA-256 `f20983ef123f567d…`

Đánh dấu package Python; file rỗng trong bộ nguồn này, không chứa thuật toán.

Không có hàm/lớp riêng; xem biến, import, khai báo hoặc nội dung file.

### softsec-toolkit/softsec-toolkit/ch1_models/kripke.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch1_models/kripke.py) · 241 dòng · SHA-256 `f7d0092d2e162648…`

Kripke với reachability/path, EF và AG-EF; model counter/traffic/vending/ATM. Chú ý nhiều initial và việc xét unreachable trong AG-EF.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 22 | `class KripkeStructure` | Kripke structure M = (S, S0, R, L). |
| 31 | `KripkeStructure.__init__(self)` |  |
| 38 | `KripkeStructure.add_state(self, s: str, labels: Optional[Iterable[str]]=None, initial: bool=False)` |  |
| 45 | `KripkeStructure.add_transition(self, src: str, dst: str)` |  |
| 51 | `KripkeStructure.reachable_states(self)` | BFS/DFS tu tap trang thai khoi tao, tra ve tat ca trang thai dat toi. |
| 65 | `KripkeStructure.is_reachable(self, target: str)` |  |
| 68 | `KripkeStructure.find_path(self, target: str)` | Tim mot duong di (counterexample-style) tu mot trang thai khoi tao |
| 77 | `KripkeStructure._bfs_path(self, start: str, target: str)` |  |
| 93 | `KripkeStructure.states_with_label(self, prop: str)` |  |
| 97 | `KripkeStructure.satisfies_EF(self, prop: str, frm: Optional[str]=None)` | EF p tai `frm`: ton tai duong di tu `frm` toi mot trang thai co |
| 109 | `KripkeStructure.satisfies_AG_EF(self, prop: str)` | AG EF p: tu MOI trang thai s trong S, EF p dung tai s. |
| 119 | `KripkeStructure._reachable_from(self, s: str)` |  |
| 140 | `build_counter_model(max_value: int=3)` |  |
| 157 | `build_traffic_light_model()` |  |
| 173 | `build_vending_machine_model()` |  |
| 191 | `build_atm_model(insecure: bool=False)` |  |

### softsec-toolkit/softsec-toolkit/ch1_models/testing.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch1_models/testing.py) · 197 dòng · SHA-256 `b9d6f1bd664a318d…`

Equivalence classes, boundary, cyclomatic complexity, coverage của f_reference và decision table insurance; số liệu minh họa cần mẫu số rõ.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 28 | `class EquivalenceClass` |  |
| 35 | `build_range_classes(low: int, high: int)` | Sinh 3 lop tuong duong chuan cho mot khoang [low, high] dong: |
| 47 | `boundary_value_test_cases(low: int, high: int)` | Sinh 4 gia tri bien chuan: low-1, low, high, high+1 kem nhan (expected) |
| 62 | `is_valid_age(age: int)` | Ham vi du slide 87/100 (0 <= age <= 120). |
| 67 | `is_valid_password_length(pwd: str)` | Bai tap Equivalence Partitioning / BVA cho mat khau (slide 88-91): |
| 90 | `cyclomatic_complexity(edges: int, nodes: int, connected_components: int=1)` | V(G) = E - N + 2 P (P = so thanh phan lien thong, thuong = 1). |
| 95 | `f_reference(a: int, b: int)` | Cai dat lai ham f(a, b) trong bai tap de co the do coverage thuc te. |
| 105 | `branch_coverage(test_cases: List[Tuple[int, int]])` | Bai tap: Statement vs Branch Coverage (slide 393 vung Chuong1_Phan2). |
| 143 | `suggested_extra_test_cases()` | De xuat test case bo sung de dat 100% branch coverage (cau 3, slide 393). |
| 154 | `insurance_decision(overdue: bool, fraud_detected: bool)` | 4 to hop dieu kien -> quyet dinh 'Tu choi' / 'Chap nhan', |
| 162 | `full_decision_table()` |  |

### softsec-toolkit/softsec-toolkit/ch1_models/tests/test_testing.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch1_models/tests/test_testing.py) · 35 dòng · SHA-256 `5a1940a002c88e2e…`

Các test có sẵn của nhóm tương ứng; đọc assert, skip và điều kiện môi trường để biết chính xác điều được kiểm tra. Một số test gọi compiler/công cụ ngoài.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 15 | `test_age_lower_boundary()` |  |
| 20 | `test_age_upper_boundary()` |  |
| 25 | `test_password_boundary_values()` |  |
| 32 | `test_password_equivalence_classes()` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/01_linked_list_uaf.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/01_linked_list_uaf.c) · 51 dòng · SHA-256 `d5f702d554e46f8a…`

Ví dụ lỗi node sử dụng sau free trong linked list; minh họa lưu next trước free và tránh alias dangling.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 14 | `Node *make_node(int v, Node *next)` |  |
| 22 | `void remove_first_buggy(Node **head)` |  |
| 30 | `void remove_first_fixed(Node **head)` |  |
| 38 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/02_memory_leak.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/02_memory_leak.c) · 40 dòng · SHA-256 `dea7f9826a29dc81…`

Cấp phát không được giải phóng trên đường đã chọn; dùng leak report và ownership để tìm nguyên nhân.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 13 | `char *duplicate_string(const char *s)` |  |
| 20 | `void process_leaky(void)` |  |
| 27 | `void process_fixed(void)` |  |
| 33 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/03_ub_signed_overflow.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/03_ub_signed_overflow.c) · 36 dòng · SHA-256 `762680fbabf4f4fb…`

Kiểm tra sau phép cộng có thể bị UB/optimizer làm mất ý nghĩa; sửa bằng guard trước cộng hoặc kiểu rộng phù hợp.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 12 | `int compute_ub(int a, int b)` |  |
| 18 | `bool safe_add(int a, int b, int *out)` |  |
| 26 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/04_unsafe_fixes.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/04_unsafe_fixes.c) · 89 dòng · SHA-256 `3c82256f49dcff6f…`

Những cách sửa chuỗi/bộ nhớ tưởng an toàn nhưng còn vấn đề, đối chiếu NUL, truncation và miền đầu vào.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 15 | `void greet_unsafe(char *name)` |  |
| 22 | `void greet_safe(const char *name)` |  |
| 29 | `int *make_array_unsafe(int n)` |  |
| 37 | `int *make_array_safe(int n)` |  |
| 48 | `char *read_line_unsafe(FILE *f)` |  |
| 56 | `char *read_line_safe(FILE *f)` |  |
| 66 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/05_recursion_depth.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/05_recursion_depth.c) · 38 dòng · SHA-256 `f7cc1ca0d4d1d14d…`

Recursion sâu và stack exhaustion; điều kiện dừng chưa tự đảm bảo tài nguyên cho input lớn.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 15 | `int parse_expr(const char *s, int depth)` |  |
| 26 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/06_struct_alignment.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/06_struct_alignment.c) · 83 dòng · SHA-256 `a4f07453c07715ea…`

In sizeof/offsetof và so sánh thứ tự field để học padding/alignment phụ thuộc ABI.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 58 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/07_cppcheck_demo.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/07_cppcheck_demo.c) · 44 dòng · SHA-256 `c4ae2133ead9cf76…`

Mẫu lỗi để đọc warning static analyzer; phải đối chiếu đường thực thi và không đồng nhất warning với exploit.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 11 | `char *duplicate_string(const char *s)` |  |
| 17 | `void leaky_caller(void)` |  |
| 23 | `void greet(char *name)` |  |
| 30 | `int *make_array(int n)` |  |
| 38 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/08_student_module.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/08_student_module.c) · 107 dòng · SHA-256 `e51c8a269c7e547e…`

List sinh viên: thêm/xóa/ghi file và free_all. StudentRecord bỏ pointer nhưng raw fwrite còn padding/ABI và thiếu kiểm tra ghi đủ.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 29 | `Student *add_student(Student *head, int id, const char *name, double gpa)` |  |
| 46 | `Student *remove_student(Student *head, int id)` |  |
| 67 | `void write_students_binary(Student *head, const char *path)` |  |
| 79 | `void free_all(Student *head)` |  |
| 87 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/09_product_list_extended.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/09_product_list_extended.c) · 84 dòng · SHA-256 `bedb71f0b309e90c…`

List sản phẩm: thêm/xóa/tìm, test list rỗng/ID không tồn tại; comment size cần tính thêm pointer next.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 23 | `Product *add_product(Product *head, int id, const char *name, double price)` |  |
| 34 | `Product *remove_product(Product *head, int id)` |  |
| 49 | `Product *find_product(Product *head, int id)` |  |
| 55 | `void free_all(Product *head)` |  |
| 63 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch2_memsafe/pattern_scanner.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch2_memsafe/pattern_scanner.py) · 76 dòng · SHA-256 `057b17f3c8526bf5…`

Quét pattern nguy hiểm thành Finding với dòng; không theo dõi ngữ nghĩa, lifetime hoặc reachability.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 24 | `class Finding` |  |
| 45 | `scan_source(path: str)` |  |
| 58 | `report(findings: List[Finding])` |  |

### softsec-toolkit/softsec-toolkit/ch3_verify/01_sat_manual.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch3_verify/01_sat_manual.py) · 65 dòng · SHA-256 `24d14520b1ba1ce7…`

Đánh giá phi, brute-force phép gán và đối chiếu Z3; không cài DPLL/CDCL đầy đủ.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 23 | `phi(a: bool, b: bool, c: bool)` | phi = (a v ~b) ^ (b v c) ^ (~a v ~c) |
| 28 | `brute_force_sat()` | Vet can toan bo 2^3 = 8 to hop (a,b,c) -> tim phep gan thoa man. |
| 37 | `z3_sat()` |  |

### softsec-toolkit/softsec-toolkit/ch3_verify/02_smt_examples.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch3_verify/02_smt_examples.py) · 86 dòng · SHA-256 `f3d854d09593f918…`

Bài age/license, CNF, bit-vector overflow và dịch điều kiện source sang SMT.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 19 | `exercise_1_age_license()` | Bai tap: Viet rang buoc SMT (slide 1159). |
| 30 | `exercise_2_cnf()` | Bai tap: Phan tich cong thuc CNF (slide 1350): (a ^ b) v c |
| 45 | `exercise_3_bitvector_overflow()` | Bai tap: Mo hinh hoa bang Bit-vector (slide 1375): |
| 53 | `exercise_4_source_to_smt()` | Bai tap tong hop: Tu ma nguon toi SMT (slide 1471): |

### softsec-toolkit/softsec-toolkit/ch3_verify/03_bmc_manual.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch3_verify/03_bmc_manual.py) · 48 dòng · SHA-256 `9cfdabaa4df63178…`

Quan hệ R và trạng thái bad nhỏ, mã hóa BMC k=1 bằng Z3 để hiểu công thức.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 18 | `R(x: int, y: int)` | Quan he chuyen tiep: R(0,1) va R(1,1) (self-loop tai 1). |
| 23 | `bad(s: int)` | Thuoc tinh xau: dat trang thai 1. |
| 28 | `bmc_k1_with_z3()` |  |

### softsec-toolkit/softsec-toolkit/ch3_verify/04_cbmc_unwind_demo.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch3_verify/04_cbmc_unwind_demo.c) · 33 dòng · SHA-256 `edb185e2d1ec715e…`

Loop ghi arr[10] theo n<=15; kiểm tra unwind và lỗi index10. Harness đặc thù CBMC không phải C chạy thường.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 21 | `void process(int n)` |  |
| 28 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch3_verify/05_bmc_loop_demo.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch3_verify/05_bmc_loop_demo.c) · 35 dòng · SHA-256 `265379dc0b4f3212…`

Các loop minh họa bound và off-by-one; phải xem entry function, assumptions và unwinding assertions.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 19 | `int sum_array(int *arr, int n)` |  |
| 27 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch3_verify/06_memory_model_doublefree.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch3_verify/06_memory_model_doublefree.py) · 68 dòng · SHA-256 `849d8a0ad313c469…`

Mô hình live/free của object bằng trạng thái Boolean để phát hiện free lần hai.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 17 | `model_double_free_scenario(second_free_checks_validity: bool)` | Mo phong: malloc(p) -> free(p) -> free(p) lan 2. |

### softsec-toolkit/softsec-toolkit/ch3_verify/07_alignment_z3.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch3_verify/07_alignment_z3.py) · 60 dòng · SHA-256 `0d4591c5b0e1e019…`

Ràng buộc modulo alignment, allocator sai và mảng với stride hợp lệ.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 18 | `exercise_1_custom_allocator_violation()` | addr la boi so cua 4 (addr % 4 == 0). Hoi: co the addr % 8 != 0 |
| 30 | `exercise_2_array_alignment_proof()` | Chung minh: neu base % 4 == 0 va sizeof(S) == 8, thi voi moi i, |

### softsec-toolkit/softsec-toolkit/ch3_verify/08_cbmc_packet_parser.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch3_verify/08_cbmc_packet_parser.c) · 51 dòng · SHA-256 `2f1c9459bf9d8d75…`

Parser buggy/fixed với buffer 256 và header_len0..300; bản fixed clamp độ dài nhưng vẫn cần contract source/output capacity.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 18 | `void parse_packet_buggy(const uint8_t *network_data, int header_len, uint8_t *out_buf)` |  |
| 25 | `void parse_packet_fixed(const uint8_t *network_data, int header_len, uint8_t *out_buf)` |  |
| 34 | `int main(void)` |  |
| 43 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/01_malicious_input.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/01_malicious_input.py) · 55 dòng · SHA-256 `3811b08f1f490a34…`

Mô phỏng xử lý tên/strncpy để thấy input dài và NUL; Python model không tái hiện mọi UB của C.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 19 | `process_name_model(name: str, max_len: int, buffer_size: int=64)` | Mo phong lai strncpy(buffer, name, max_len) vao buffer 64 byte de |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/01b_malicious_input_harness.c

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/01b_malicious_input_harness.c) · 15 dòng · SHA-256 `7c0e6b6175fb4691…`

Harness C cho input bất thường của xử lý chuỗi; quan sát khác biệt giữa model Python và target C.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 5 | `void process_name(char *name, int max_len)` |  |
| 11 | `int main(void)` |  |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/02_seed_corpus.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/02_seed_corpus.py) · 40 dòng · SHA-256 `a727262d1debafd2…`

Tạo seed JSON đa dạng về trường và giá trị; seed tốt cần mở được các cấu trúc target.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 15 | `build_seed_corpus()` |  |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/03_edge_coverage.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/03_edge_coverage.py) · 62 dòng · SHA-256 `a2b9d608c04b23f4…`

Gán nhãn đường/nhánh minh họa và đếm tập đã thấy; không phải bitmap cạnh cơ bản đầy đủ.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 20 | `f_instrumented(a: int, b: int)` | Cai dat lai f(a,b), tra ve nhan cua nhanh duoc thuc thi (A/B/C/D) |
| 36 | `edge_coverage(test_cases: List[Tuple[int, int]])` |  |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/04_concolic_execution.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/04_concolic_execution.py) · 86 dòng · SHA-256 `3e20b12552bf9941…`

Chạy classify cụ thể, dựng path condition và phủ định để giải input cho nhánh mới.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 25 | `classify_concrete(x: int, y: int)` | Thuc thi CU THE (concrete) -- dong thoi ghi lai path condition. |
| 34 | `classify_path_condition(x_sym, y_sym, x_concrete, y_concrete)` | Sinh path condition (danh sach dieu kien symbolic) theo DUNG duong |
| 49 | `explore_new_branch(path_conditions, negate_index)` | Phu dinh dieu kien tai vi tri `negate_index` trong path condition, |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/05_dfs_vs_coverage_guided.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/05_dfs_vs_coverage_guided.py) · 68 dòng · SHA-256 `6ceb334a350e00d7…`

Mô phỏng hai chiến lược search để thấy tác động lựa chọn trạng thái; số liệu phụ thuộc mô hình toy.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 20 | `dfs_strategy(n: int, budget: int)` | DFS thuan tuy: uu tien di sau theo 1 nhanh co dinh (vd luon chon |
| 37 | `coverage_guided_strategy(n: int, budget: int, seed: int=42)` | Coverage-guided (mo phong don gian AFL-style): moi lan thu uu tien |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/06_white_box_fuzzing.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/06_white_box_fuzzing.py) · 62 dòng · SHA-256 `471c7e8a012bb98d…`

Giải magic4919 bằng SMT rồi so random attempt; ví dụ white-box dùng constraints.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 19 | `check(code: int)` |  |
| 23 | `white_box_solve()` | White-box: dung SMT solver de GIAI NGUOC dieu kien code == 0 x1337. |
| 33 | `black_box_attempt(max_tries: int=2000000, seed: int=1)` | Black-box: thu ngau nhien trong pham vi int 32-bit -- xac suat trung |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/07_infeasible_path.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/07_infeasible_path.py) · 35 dòng · SHA-256 `54f2adbd99e12867…`

Kiểm tra ràng buộc unsigned bằng UGT/ULT để chứng minh một đường bất khả thi.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 18 | `check_feasibility()` |  |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/08_mutation_strategy.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/08_mutation_strategy.py) · 63 dòng · SHA-256 `6f47e6555f7c202c…`

Seed gồm magic SFTP, length little-endian32 bit và payload; giữ magic, mutate length/bit payload.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 17 | `make_seed(payload: bytes)` |  |
| 21 | `mutate(data: bytes, seed: int=0)` | Ap dung chien luoc dot bien da de xuat trong dap an slide: |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/09_dictionary_probability.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/09_dictionary_probability.py) · 59 dòng · SHA-256 `a1b947098fd67042…`

So random5 byte với chọn token dictionary20 từ; hàm xác suất đúng, chuỗi giải thích kỳ vọng sai10 lần.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 15 | `probability_without_dictionary(keyword: str)` | Xac suat 5 byte ngau nhien (dong deu trong 256 gia tri) VUA VAN |
| 21 | `simulate_random_mutation(keyword: str, trials: int=2000000, seed: int=7)` | Mo phong thuc te: random.choice tren 256 gia tri byte, dem so lan |
| 34 | `probability_with_dictionary()` | Voi dictionary-based mutation: fuzzer CHON tu dictionary (gia su co |

### softsec-toolkit/softsec-toolkit/ch4_dynafuzz/10_symbolic_cost.py

[Mở file nguồn](../softsec-toolkit/softsec-toolkit/ch4_dynafuzz/10_symbolic_cost.py) · 45 dòng · SHA-256 `04704375f520ba8a…`

Hai công thức giả định chi phí; cần sửa diễn giải independent/nested theo CFG và mục tiêu branch/path.

| Dòng | Hàm/lớp/API | Gợi ý từ docstring gốc |
| ---: | --- | --- |
| 13 | `independent_branches_cost(n_branches: int)` | 20 nhanh doc lap: moi nhanh chi can 1 lan goi solver de kiem tra |
| 19 | `nested_branches_cost(depth: int)` | n tang long nhau: so duong thi hanh phan biet la 2^n (moi tang co |

**Build và phụ thuộc:** Makefile/README/SETUP/requirements của nhóm được liệt kê đầy đủ trong Chương 10. Các recipe `.so`, `/tmp`, sanitizer và tiện ích POSIX cần môi trường phù hợp; không coi chúng mặc nhiên chạy được nguyên trạng trên Windows.

## 9.12 Dữ liệu JSON/CSV/seed và truy vết

35 JSON và 9 CSV đã được đọc. JSON/CSV bao gồm mô hình, case input, expected/baseline và kết quả lịch sử. Không gán mọi JSON cho cùng một schema.

| File | Cấu trúc/khối lượng | Vai trò |
| --- | --- | --- |
| [atpm_project/atpm_project/python/requirements.txt](../atpm_project/atpm_project/python/requirements.txt) | 7 dòng | Tên phụ thuộc Python; cài tương ứng môi trường/phiên bản. |
| [lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_buggy_init.txt](../lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_buggy_init.txt) | 1 dòng | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_buggy_states.csv](../lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_buggy_states.csv) | 13 dòng dữ liệu; cột: id, name, labels | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_buggy_transitions.csv](../lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_buggy_transitions.csv) | 19 dòng dữ liệu; cột: from, event, to | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_safe_init.txt](../lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_safe_init.txt) | 1 dòng | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_safe_states.csv](../lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_safe_states.csv) | 11 dòng dữ liệu; cột: id, name, labels | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_safe_transitions.csv](../lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_safe_transitions.csv) | 17 dòng dữ liệu; cột: from, event, to | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_system_model.json](../lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_system_model.json) | object: system_name, description, atomic_propositions, states, initial_states, transitions, properties_to_check | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_system_model_BUGGY.json](../lab1_kripke_access_model/lab1_kripke_access_model/dataset/access_system_model_BUGGY.json) | object: system_name, description, atomic_propositions, states, initial_states, transitions, properties_to_check | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab2_testing_verification/lab2_testing_verification/dataset/black_box_test_results.csv](../lab2_testing_verification/lab2_testing_verification/dataset/black_box_test_results.csv) | 37 dòng dữ liệu; cột: pin, failed_attempts, expected, technique, rationale, actual, pass | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab2_testing_verification/lab2_testing_verification/dataset/pin_test_cases.csv](../lab2_testing_verification/lab2_testing_verification/dataset/pin_test_cases.csv) | 37 dòng dữ liệu; cột: pin, failed_attempts, expected | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab3_secure_memory/lab3_secure_memory/dataset/expected_risk_baseline.json](../lab3_secure_memory/lab3_secure_memory/dataset/expected_risk_baseline.json) | array: 4 phần tử | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab3_secure_memory/lab3_secure_memory/dataset/risk_assessment_results.json](../lab3_secure_memory/lab3_secure_memory/dataset/risk_assessment_results.json) | array: 4 phần tử | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab3_secure_memory/lab3_secure_memory/dataset/vulnerabilities.json](../lab3_secure_memory/lab3_secure_memory/dataset/vulnerabilities.json) | object: module, vulnerabilities | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/dataset/cppcheck_comparison_results.json](../lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/dataset/cppcheck_comparison_results.json) | object: buggy_file, fixed_file, buggy_findings, fixed_findings, buggy_security_count, fixed_security_count | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/dataset/expected_cppcheck_baseline.json](../lab4_data_structures_static_analysis/lab4_data_structures_static_analysis/dataset/expected_cppcheck_baseline.json) | object: buggy_file, fixed_file, buggy_findings, fixed_findings, buggy_security_count, fixed_security_count | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab5_sat_smt_verification/lab5_sat_smt_verification/dataset/condition_pairs.json](../lab5_sat_smt_verification/lab5_sat_smt_verification/dataset/condition_pairs.json) | object: description, variables, condition_pairs | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab5_sat_smt_verification/lab5_sat_smt_verification/dataset/smt_verification_results.json](../lab5_sat_smt_verification/lab5_sat_smt_verification/dataset/smt_verification_results.json) | array: 6 phần tử | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab6_bounded_model_checking/lab6_bounded_model_checking/dataset/bmc_programs.json](../lab6_bounded_model_checking/lab6_bounded_model_checking/dataset/bmc_programs.json) | object: description, programs | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab6_bounded_model_checking/lab6_bounded_model_checking/dataset/bmc_results.json](../lab6_bounded_model_checking/lab6_bounded_model_checking/dataset/bmc_results.json) | array: 4 phần tử | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab7_dynamic_coverage/lab7_dynamic_coverage/dataset/coverage_comparison_results.json](../lab7_dynamic_coverage/lab7_dynamic_coverage/dataset/coverage_comparison_results.json) | object: partial, full | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab7_dynamic_coverage/lab7_dynamic_coverage/dataset/order_test_inputs_combinatorial.csv](../lab7_dynamic_coverage/lab7_dynamic_coverage/dataset/order_test_inputs_combinatorial.csv) | 97 dòng dữ liệu; cột: quantity, unit_price, is_member, expected_status | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab7_dynamic_coverage/lab7_dynamic_coverage/dataset/order_test_inputs_full.csv](../lab7_dynamic_coverage/lab7_dynamic_coverage/dataset/order_test_inputs_full.csv) | 9 dòng dữ liệu; cột: quantity, unit_price, is_member, expected_status | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab7_dynamic_coverage/lab7_dynamic_coverage/dataset/order_test_inputs_partial.csv](../lab7_dynamic_coverage/lab7_dynamic_coverage/dataset/order_test_inputs_partial.csv) | 2 dòng dữ liệu; cột: quantity, unit_price, is_member, expected_status | Input cấu hình/case/mô hình của bài lab; xem Chương 5. |
| [lab8_fuzzing/lab8_fuzzing/dataset/fuzzing_comparison_results.json](../lab8_fuzzing/lab8_fuzzing/dataset/fuzzing_comparison_results.json) | object: blackbox_1000_iters, whitebox_500_iters | Kết quả/baseline lưu sẵn; phân biệt với kết quả chạy mới. |
| [lab8_fuzzing/lab8_fuzzing/seed_corpus/seed1.txt](../lab8_fuzzing/lab8_fuzzing/seed_corpus/seed1.txt) | 1 dòng | Seed văn bản cho fuzzing ADMIN/ORDER. |
| [lab8_fuzzing/lab8_fuzzing/seed_corpus/seed2.txt](../lab8_fuzzing/lab8_fuzzing/seed_corpus/seed2.txt) | 1 dòng | Seed văn bản cho fuzzing ADMIN/ORDER. |
| [lab8_fuzzing/lab8_fuzzing/seed_corpus/seed3.txt](../lab8_fuzzing/lab8_fuzzing/seed_corpus/seed3.txt) | 1 dòng | Seed văn bản cho fuzzing ADMIN/ORDER. |
| [softsec-toolkit/softsec-toolkit/requirements.txt](../softsec-toolkit/softsec-toolkit/requirements.txt) | 2 dòng | Tên phụ thuộc Python; cài tương ứng môi trường/phiên bản. |
| [specs/specs/auth_rate_limit_spec.json](../specs/specs/auth_rate_limit_spec.json) | object: name, description, requirements, state_machine, additional_flows, safety_properties, mutual_exclusion, functions, arithmetic_checks, test_cases | Đặc tả yêu cầu, mô hình và bài toán sinh mã/số học; Chương 6. |
| [specs/specs/elevator_control_spec.json](../specs/specs/elevator_control_spec.json) | object: name, description, requirements, state_machine, additional_flows, safety_properties, mutual_exclusion, functions, arithmetic_checks, test_cases | Đặc tả yêu cầu, mô hình và bài toán sinh mã/số học; Chương 6. |
| [specs/specs/file_upload_auth_spec.json](../specs/specs/file_upload_auth_spec.json) | object: name, description, requirements, state_machine, additional_flows, safety_properties, mutual_exclusion, functions, arithmetic_checks, test_cases | Đặc tả yêu cầu, mô hình và bài toán sinh mã/số học; Chương 6. |
| [specs/specs/iot_gateway_spec.json](../specs/specs/iot_gateway_spec.json) | object: name, description, requirements, state_machine, additional_flows, safety_properties, mutual_exclusion, functions, arithmetic_checks | Đặc tả yêu cầu, mô hình và bài toán sinh mã/số học; Chương 6. |
| [specs/specs/resource_pool_spec.json](../specs/specs/resource_pool_spec.json) | object: name, description, requirements, state_machine, safety_properties, mutual_exclusion, functions, arithmetic_checks | Đặc tả yêu cầu, mô hình và bài toán sinh mã/số học; Chương 6. |
| [specs/specs/session_manager_fixed_spec.json](../specs/specs/session_manager_fixed_spec.json) | object: name, description, requirements, state_machine, safety_properties, mutual_exclusion, functions, arithmetic_checks | Đặc tả yêu cầu, mô hình và bài toán sinh mã/số học; Chương 6. |
| [specs/specs/session_manager_spec.json](../specs/specs/session_manager_spec.json) | object: name, description, requirements, state_machine, additional_flows, safety_properties, mutual_exclusion, functions, arithmetic_checks | Đặc tả yêu cầu, mô hình và bài toán sinh mã/số học; Chương 6. |
| [verification/verification/dining_philosophers_deadlock.json](../verification/verification/dining_philosophers_deadlock.json) | object: description, states, initial, labeling, transitions, flows, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/elevator_system.json](../verification/verification/elevator_system.json) | object: description, states, initial, labeling, transitions, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/linear_terminating_chain.json](../verification/verification/linear_terminating_chain.json) | object: title, description, states, initial, labeling, transitions, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/multi_initial_boot_modes.json](../verification/verification/multi_initial_boot_modes.json) | object: title, description, states, initial, labeling, transitions, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/mutex_fixed.json](../verification/verification/mutex_fixed.json) | object: description, states, initial, labeling, transitions, flows, suggested_ctl_formulas, suggested_mutex_atoms | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/mutex_two_process.json](../verification/verification/mutex_two_process.json) | object: description, states, initial, labeling, transitions, flows, suggested_ctl_formulas, suggested_mutex_atoms | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/nondeterministic_branch.json](../verification/verification/nondeterministic_branch.json) | object: title, description, states, initial, labeling, transitions, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/producer_consumer.json](../verification/verification/producer_consumer.json) | object: description, title, flows, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/readers_writers.json](../verification/verification/readers_writers.json) | object: description, title, flows, suggested_ctl_formulas, suggested_mutex_atoms | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/self_loop_retry_livelock.json](../verification/verification/self_loop_retry_livelock.json) | object: title, description, states, initial, labeling, transitions, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/session_login_lifecycle.json](../verification/verification/session_login_lifecycle.json) | object: description, states, initial, labeling, transitions, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/ticket_lock_mutex.json](../verification/verification/ticket_lock_mutex.json) | object: description, states, initial, labeling, transitions, flows, suggested_ctl_formulas, suggested_mutex_atoms | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/traffic_light.json](../verification/verification/traffic_light.json) | object: description, states, initial, labeling, transitions, flows, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/unreachable_legacy_state.json](../verification/verification/unreachable_legacy_state.json) | object: title, description, states, initial, labeling, transitions, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |
| [verification/verification/vending_machine.json](../verification/verification/vending_machine.json) | object: description, states, initial, labeling, transitions, suggested_ctl_formulas | Mô hình đồ thị phục vụ học CTL, reachable, deadlock, fairness; Chương 6. |

## 9.13 Đối chiếu cấu trúc các đồ thị chính

Các con số dưới đây lấy từ dữ liệu và phép duyệt reachable. Vi phạm mutex là **đồng thời mang hai nhãn**; cột này không phải tập mọi trạng thái có thể dẫn tới vi phạm. Không có mô hình chính được ghi riêng, không thay bằng đồ thị0 trạng thái.

| File | Trạng thái | Cạnh | Reachable | Unreachable | Deadlock gốc | Vi phạm mutex trực tiếp |
| --- | ---: | ---: | ---: | --- | --- | --- |
| [specs/specs/auth_rate_limit_spec.json](../specs/specs/auth_rate_limit_spec.json) | 4 | 6 | 4 | — | — | — |
| [specs/specs/elevator_control_spec.json](../specs/specs/elevator_control_spec.json) | 4 | 4 | 4 | — | — | — |
| [specs/specs/file_upload_auth_spec.json](../specs/specs/file_upload_auth_spec.json) | 7 | 10 | 7 | — | — | — |
| [specs/specs/iot_gateway_spec.json](../specs/specs/iot_gateway_spec.json) | 4 | 6 | 4 | — | — | conflict |
| [specs/specs/resource_pool_spec.json](../specs/specs/resource_pool_spec.json) | 0 | 0 | 0 | — | — | — |
| [specs/specs/session_manager_fixed_spec.json](../specs/specs/session_manager_fixed_spec.json) | 3 | 4 | 3 | — | — | — |
| [specs/specs/session_manager_spec.json](../specs/specs/session_manager_spec.json) | 4 | 6 | 4 | — | — | crit1_crit2 |
| [verification/verification/dining_philosophers_deadlock.json](../verification/verification/dining_philosophers_deadlock.json) | 6 | 8 | 6 | — | hasleft_hasleft | — |
| [verification/verification/elevator_system.json](../verification/verification/elevator_system.json) | 4 | 4 | 4 | — | — | — |
| [verification/verification/linear_terminating_chain.json](../verification/verification/linear_terminating_chain.json) | 5 | 5 | 5 | — | — | — |
| [verification/verification/multi_initial_boot_modes.json](../verification/verification/multi_initial_boot_modes.json) | 4 | 4 | 4 | — | — | — |
| [verification/verification/mutex_fixed.json](../verification/verification/mutex_fixed.json) | 3 | 4 | 3 | — | — | — |
| [verification/verification/mutex_two_process.json](../verification/verification/mutex_two_process.json) | 4 | 6 | 4 | — | — | crit1_crit2 |
| [verification/verification/nondeterministic_branch.json](../verification/verification/nondeterministic_branch.json) | 3 | 4 | 3 | — | — | — |
| [verification/verification/producer_consumer.json](../verification/verification/producer_consumer.json) | 0 | 0 | 0 | — | — | — |
| [verification/verification/readers_writers.json](../verification/verification/readers_writers.json) | 0 | 0 | 0 | — | — | — |
| [verification/verification/self_loop_retry_livelock.json](../verification/verification/self_loop_retry_livelock.json) | 3 | 5 | 3 | — | — | — |
| [verification/verification/session_login_lifecycle.json](../verification/verification/session_login_lifecycle.json) | 5 | 8 | 5 | — | — | — |
| [verification/verification/ticket_lock_mutex.json](../verification/verification/ticket_lock_mutex.json) | 7 | 10 | 7 | — | — | — |
| [verification/verification/traffic_light.json](../verification/verification/traffic_light.json) | 3 | 3 | 3 | — | — | — |
| [verification/verification/unreachable_legacy_state.json](../verification/verification/unreachable_legacy_state.json) | 4 | 4 | 3 | legacy_debug_mode | — | — |
| [verification/verification/vending_machine.json](../verification/verification/vending_machine.json) | 4 | 5 | 4 | — | — | — |

## 9.14 Đồ thị riêng lẻ và kết hợp trong flows

| File | Flow | Trạng thái | Cạnh | Reachable | Deadlock |
| --- | --- | ---: | ---: | ---: | --- |
| [specs/specs/auth_rate_limit_spec.json](../specs/specs/auth_rate_limit_spec.json) | Chỉ riêng vòng lặp xác thực (bỏ qua khóa) | 3 | 4 | 3 | — |
| [specs/specs/auth_rate_limit_spec.json](../specs/specs/auth_rate_limit_spec.json) | Chỉ riêng cơ chế khóa (lockout) | 3 | 3 | 3 | — |
| [specs/specs/file_upload_auth_spec.json](../specs/specs/file_upload_auth_spec.json) | Worker 1 - rieng le | 3 | 3 | 3 | — |
| [specs/specs/file_upload_auth_spec.json](../specs/specs/file_upload_auth_spec.json) | Worker 2 - rieng le | 3 | 3 | 3 | — |
| [specs/specs/iot_gateway_spec.json](../specs/specs/iot_gateway_spec.json) | Worker chính (riêng lẻ, trước khi kết hợp) | 2 | 2 | 2 | — |
| [specs/specs/iot_gateway_spec.json](../specs/specs/iot_gateway_spec.json) | Worker ghi log (riêng lẻ, trước khi kết hợp) | 2 | 2 | 2 | — |
| [specs/specs/session_manager_spec.json](../specs/specs/session_manager_spec.json) | Tiến trình 1 (riêng lẻ, trước khi kết hợp) | 2 | 2 | 2 | — |
| [specs/specs/session_manager_spec.json](../specs/specs/session_manager_spec.json) | Tiến trình 2 (riêng lẻ, trước khi kết hợp) | 2 | 2 | 2 | — |
| [verification/verification/dining_philosophers_deadlock.json](../verification/verification/dining_philosophers_deadlock.json) | Triết gia 1 (P1) - riêng lẻ | 3 | 3 | 3 | — |
| [verification/verification/dining_philosophers_deadlock.json](../verification/verification/dining_philosophers_deadlock.json) | Triết gia 2 (P2) - riêng lẻ | 3 | 3 | 3 | — |
| [verification/verification/dining_philosophers_deadlock.json](../verification/verification/dining_philosophers_deadlock.json) | Hệ thống kết hợp (2 triết gia, 2 chiếc đũa - CÓ DEADLOCK) | 6 | 8 | 6 | hasleft_hasleft |
| [verification/verification/mutex_fixed.json](../verification/verification/mutex_fixed.json) | Tiến trình 1 (P1) - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/mutex_fixed.json](../verification/verification/mutex_fixed.json) | Tiến trình 2 (P2) - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/mutex_fixed.json](../verification/verification/mutex_fixed.json) | Hệ thống kết hợp (Product Automaton - ĐÃ SỬA LỖI, AN TOÀN) | 3 | 4 | 3 | — |
| [verification/verification/mutex_two_process.json](../verification/verification/mutex_two_process.json) | Tiến trình 1 (P1) - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/mutex_two_process.json](../verification/verification/mutex_two_process.json) | Tiến trình 2 (P2) - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/mutex_two_process.json](../verification/verification/mutex_two_process.json) | Hệ thống kết hợp (Product Automaton - CÓ LỖI THIẾT KẾ) | 4 | 6 | 4 | — |
| [verification/verification/producer_consumer.json](../verification/verification/producer_consumer.json) | Producer - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/producer_consumer.json](../verification/verification/producer_consumer.json) | Consumer - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/producer_consumer.json](../verification/verification/producer_consumer.json) | Hệ thống kết hợp (Bounded Buffer, kích thước=1) | 2 | 2 | 2 | — |
| [verification/verification/readers_writers.json](../verification/verification/readers_writers.json) | Reader - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/readers_writers.json](../verification/verification/readers_writers.json) | Writer - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/readers_writers.json](../verification/verification/readers_writers.json) | Hệ thống kết hợp (Coordinator - đếm số đọc giả) | 4 | 6 | 4 | — |
| [verification/verification/ticket_lock_mutex.json](../verification/verification/ticket_lock_mutex.json) | Tiến trình 1 (P1) - riêng lẻ | 3 | 3 | 3 | — |
| [verification/verification/ticket_lock_mutex.json](../verification/verification/ticket_lock_mutex.json) | Tiến trình 2 (P2) - riêng lẻ | 3 | 3 | 3 | — |
| [verification/verification/ticket_lock_mutex.json](../verification/verification/ticket_lock_mutex.json) | Hệ thống kết hợp (Ticket Lock - AN TOÀN) | 7 | 10 | 7 | — |
| [verification/verification/traffic_light.json](../verification/verification/traffic_light.json) | Đèn xe (Vehicle light) - riêng lẻ | 3 | 3 | 3 | — |
| [verification/verification/traffic_light.json](../verification/verification/traffic_light.json) | Đèn người đi bộ (Pedestrian light) - riêng lẻ | 2 | 2 | 2 | — |
| [verification/verification/traffic_light.json](../verification/verification/traffic_light.json) | Hệ thống kết hợp (Vehicle x Pedestrian) | 4 | 5 | 4 | — |

## 9.15 Cách đọc một ví dụ code hiệu quả

Đọc dataset/đặc tả trước, rồi entry function, các guard, thao tác dữ liệu/bộ nhớ, đường trả về, oracle và test. Ghi lại miền input, giả thiết, kiểu số, lifetime và trạng thái. Nếu chương trình tạo báo cáo, kiểm tra cả cách parse lỗi công cụ để tránh một report rỗng bị hiểu là đã đạt.

Các API tự động trích xuất từ AST Python và khai báo/định nghĩa hàm C. Bảng C không thay thế parser/compiler đầy đủ; macros, cấu hình `#ifdef` và contract con trỏ vẫn cần đọc trực tiếp. Không có lỗi parse AST Python trong lượt lập bản đồ.
