# Chương 5. Phân tích và hướng dẫn hiểu 8 bài lab

## 5.1 Quan hệ giữa các bài thực hành

| Lab | Bài toán | Kiến thức trọng tâm | Bằng chứng mong muốn |
| --- | --- | --- | --- |
| 1 | Khóa cửa/access control | Kripke, BFS, safety, reachability | PASS/FAIL và trace |
| 2 | PIN validator | EP/BVA, oracle, coverage | Expected/actual và code chưa phủ |
| 3 | Inventory có lỗi bộ nhớ | Overflow, UAF, leak, chấm rủi ro | ASan/log và ưu tiên sửa |
| 4 | Danh sách sách | Ownership, uninitialized data, static analysis | Warning trước/sau |
| 5 | Điều kiện bảo mật | SAT/SMT và tương đương logic | XOR SAT/UNSAT, phản ví dụ |
| 6 | Truy cập catalog | BMC và bounds index | Bound, index, witness |
| 7 | Xử lý đơn hàng | Coverage và test tổ hợp | Bộ test nhỏ/đầy đủ/tổ hợp |
| 8 | Parser lệnh | Fuzzing, dictionary, feedback | Crash input và coverage mới |

Mỗi lab có PDF, README, Makefile, code, test; phần lớn có dataset/kết quả mẫu. File lưu sẵn là bằng chứng của nguồn ban đầu. Bảng dưới phân biệt phần đã chạy lại trong lần tổng hợp với phần mới chỉ đối chiếu tĩnh.

## 5.2 Lab 1 - Kripke cho access control

**Nguồn:** `lab1_kripke_access_model/lab1_kripke_access_model/`.

JSON khai báo state bằng object có `id,name,labels`; transition có `from,event,to`; initial dùng `initial_states`; thuộc tính nằm trong `properties_to_check`. CSV là biểu diễn cho simulator C. Đây **không phải** cùng schema với JSON `verification`, vốn dùng `states` là danh sách tên và `labeling` riêng.

`python/kripke_model.py`:

- `from_json`: chuyển dataset thành adjacency list và mapping label.
- `reachable_states`: BFS từ initial.
- `_find_path`: BFS lưu đường đi tới predicate.
- `_eval_formula`: ngôn ngữ nhỏ gồm atom, NOT, AND và implication; không phải parser CTL tổng quát.
- `check_AG_not`: tìm state reachable thỏa điều kiện xấu.
- `check_AG_implies`: tìm state thỏa vế trái nhưng không thỏa vế phải.
- `check_EF`: tìm witness tới label/công thức mục tiêu.
- `run_verification`: tạo kết quả có cấu trúc và chuyển trace state thành event.

Kết quả **đã chạy lại**:

| Thuộc tính | SAFE | BUGGY | Diễn giải |
| --- | --- | --- | --- |
| P1: không mở khi chưa xác thực | Đúng | Sai | Trace BUGGY `S0 → S1 → S5`, events `insert_card, timeout_glitch` |
| P2: tamper kéo theo alarm | Đúng | Đúng | Cần kiểm tra vacuity ở bản BUGGY |
| P3: có thể tới unlocked | Đúng | Đúng | Witness `S0 → S1 → S2` |

Trong BUGGY, transition `tamper_sensor` từ S0 quay về S0; state S4 mang tamper không đạt được. P2 đúng vì tiền đề tamper không xảy ra ở state reachable. **Bài học:** invariant dựa trên label chưa bao phủ yêu cầu “sự kiện tamper_sensor phải được xử lý”; cần thêm reachability hoặc thuộc tính transition/event phù hợp.

Simulator C đọc CSV và đi theo sự kiện cụ thể; warning runtime đối chiếu một trace không thay thế kiểm tra mọi state của Python. Test có sẵn gồm 3 test mô hình và 2 test simulator C; lần tổng hợp chạy lại 3 test Python và đều đạt.

**Tự làm:** thêm thuộc tính không đồng thời unlocked/alarm; thêm `EF(tamper)` để lộ vacuity; sửa cạnh timeout_glitch và tamper_sensor; kiểm tra lại toàn bộ thuộc tính. Chỉ sửa graph không tự sửa implementation thiết bị.

## 5.3 Lab 2 - Black-box và white-box cho PIN

`validate_pin(pin,failed_attempts)` kiểm tra theo thứ tự: NULL → account locked nếu attempts≥3 → length đúng 6 → tất cả là chữ số → không phải dãy tăng/giảm liên tiếp → OK. Thứ tự kiểm tra chính là ưu tiên mã lỗi khi input có nhiều vấn đề.

| Input | Attempts | Kết quả theo code |
| --- | ---: | --- |
| `482913` | 0 | OK |
| `48291` / `4829137` | 0 | WRONG_LENGTH |
| `48a913` | 0 | NON_DIGIT |
| `123456` / `654321` | 0 | SEQUENTIAL_WEAK |
| `112233` | 0 | OK theo quy tắc hiện tại |
| `482913` | 2 / 3 | OK / ACCOUNT_LOCKED |
| NULL | 0 | NULL_INPUT |

`black_box_tester.py` tạo 18 cases EP/BVA/business rule rồi dùng ctypes gọi C library. Việc cùng một PIN xuất hiện ở nhiều test có ý nghĩa khác nhau về kỹ thuật và attempts.

`white_box_coverage.py` build C CLI với coverage, đọc CSV và parse gcov. Hàm `compute_branch_coverage` **thực tế đếm dòng**, không đọc branch records. Test ngưỡng 90% là ngưỡng line metric hiện tại của file/driver, không chứng minh 90% quyết định được bao phủ.

**Điểm cần review:** failed_attempts âm; embedded NUL; xác thực “ký tự chữ số” chỉ ASCII; `strnlen` không bảo đảm pointer đầu vào trỏ tới ít nhất vùng hợp lệ cần đọc. CLI dùng atoi và tokenization đơn giản, nên chỉ phù hợp dataset mẫu. Nếu làm API sản phẩm, định nghĩa rõ miền attempts và hợp đồng buffer.

**Tự làm:** test `(NULL,3)` để xác minh ưu tiên mã lỗi; bổ sung attempts -1; tách phạm vi coverage hàm validator khỏi driver; dùng oracle độc lập kiểm tra rule yếu PIN mà đặc tả mong muốn.

## 5.4 Lab 3 - An toàn bộ nhớ và rủi ro

Bản vulnerable có:

1. `add_book_title_UNSAFE`: strcpy vào field `title[32]`.
2. `add_book_title_UNSAFE_HEAP`: malloc 32 byte rồi strcpy.
3. `demo_use_after_free`: free Book rồi đọc year.
4. `demo_memory_leak`: allocation nhiều Book nhưng không free.

Bản secure dùng snprintf, copy year trước free, đặt pointer NULL và cleanup các allocation. Payload 39 ký tự A cần 40 byte khi thêm NUL; allocation heap 32 byte không đủ. Lỗi minh họa heap overflow nên phân loại cụ thể là **CWE-122**, trong khi một số label nguồn vẫn ghi CWE-121.

Nếu tràn từ title sang field author nhưng chưa vượt allocation Book, ASan có thể không nhận thấy lỗi theo object boundary. Input sạch/không có ASan finding ở một trường hợp không cho phép suy ra mọi field đều an toàn.

`risk_assessor.py` đọc `vulnerabilities.json`, tính exploitability/impact, gắn severity và sort. Kết quả **đã chạy lại bằng công thức của chương trình**:

| ID | Điểm theo lab | Severity theo lab |
| --- | ---: | --- |
| VULN-001 | 9,8 | CRITICAL |
| VULN-002 | 6,9 | MEDIUM |
| VULN-003 | 5,4 | MEDIUM |
| VULN-004 | 2,5 | LOW |

Đây là công thức CVSS-like minh họa, chưa phải implementation CVSS đầy đủ: không có xử lý Scope hoàn chỉnh và dùng round gần nhất thay cho Roundup của CVSS 3.1. Không đem các điểm này ghi là điểm CVSS chuẩn mà không tính lại.

Test ASan trong nguồn kiểm tra overflow/UAF/leak trước sửa và sạch trên input mẫu sau sửa; chưa được chạy lại trong lần này. Cần xét khả năng hỗ trợ LeakSanitizer theo platform. **Tự làm:** thêm lỗi allocation failure và NULL source vào hợp đồng API; thêm bounds/truncation test; ghi rõ sự khác nhau giữa lỗi bộ nhớ và mức nghiêm trọng triển khai.

## 5.5 Lab 4 - Linked list và cppcheck

`booklist_v1_buggy.c` có allocation chưa kiểm tra NULL, count chưa khởi tạo và node bị unlink không free. `booklist_v2_fixed.c` kiểm tra allocation, khởi tạo count=0 và free node bị xóa; `list_free_all` giữ next trước free.

`static_analysis_runner.py` gọi cppcheck, đọc XML từ stderr, bỏ ID thông tin include, rồi đếm warning/error như security-relevant. Cần hiểu đây là **quy tắc lọc của lab**; không phải mọi warning có cùng mức nghiêm trọng và không phải style finding luôn vô nghĩa với bảo mật.

Baseline nguồn có 2 warning/error ở buggy (`uninitvar`, `uninitdata`), 0 ở fixed; có thêm style `unassignedVariable`. Tool không nhất thiết báo mọi lỗi nhìn thấy bằng review, đặc biệt leak trên control flow phức tạp. `expected_cppcheck_baseline.json` và `cppcheck_comparison_results.json` giống hệt nhau về byte: đó là baseline lưu sẵn, không là hai thực nghiệm độc lập.

Test “buggy compiles and runs” vẫn có thể đạt dù code có UB; chạy ra danh sách không chứng minh count đúng. **Tự làm:** test remove đầu/giữa/cuối/node duy nhất/không tồn tại; inject allocation failure; kết hợp analyzer và leak checker; xét thay đổi version làm ID hoặc line finding khác.

## 5.6 Lab 5 - SMT kiểm tra tương đương

Dataset có 6 cặp điều kiện. Kết quả **đã chạy lại**:

| Cặp | Tương đương? | Giải thích/phản ví dụ |
| --- | --- | --- |
| COND-01 | Có | De Morgan của điều kiện mở khóa |
| COND-02 | Không | `failed_attempts=3` phân biệt `>=3` với `>3` |
| COND-03 | Có | AND giao hoán/kết hợp với các atom Boolean thuần túy |
| COND-04 | Có | `tamper -> alarm` bằng `!tamper || (alarm && tamper)` |
| COND-05 | Không | authenticated=false, is_admin=true, bypass_flag=true |
| COND-06 | Có | `borrowed_count<=max_limit` bằng `!(borrowed_count>max_limit)` trên Int |

`make_vars` tạo Bool/Int; `eval_expr` lấy biểu thức dataset; `check_equivalence` đưa XOR vào solver và thu model; `run_all` đối chiếu expected. Hai test Python kiểm tra kết quả và tính hợp lệ của phản ví dụ đều đạt trong lần tổng hợp.

Brute-force C duyệt đầy đủ 8 tổ hợp cho điều kiện 3 Boolean, 4 tổ hợp cho 2 Boolean; đây là kiểm tra exhaustive được trong miền rất nhỏ. Không mở rộng kết luận này sang hàm có input 32-bit mà chưa mã hóa.

**Tự làm:** thêm constraint miền attempts≥0; bỏ eval nhận biểu thức không tin cậy; xử lý UNKNOWN như trạng thái riêng; phân biệt equivalence logic và thay đổi code có side effect.

## 5.7 Lab 6 - BMC cho truy cập mảng

Catalog có 10 phần tử. Engine nhận `array_size,unwind_bound,symbolic_base,fixed_base,precondition_max_base`, rồi tìm `base+i` ngoài `[0,10)` ở từng i.

| Trường hợp | Kết quả chạy lại | Bằng chứng |
| --- | --- | --- |
| BMC-01 full scan | SAFE trong bound 10 | i=0..9 hợp lệ |
| BMC-02 off-by-one | UNSAFE | i=10, index=10 |
| BMC-03 offset symbolic | UNSAFE | base=9, i=1, index=10 |
| BMC-04 có precondition | SAFE trong bound 5 | 0≤base≤5, i=0..4 |

Để quét 5 phần tử từ base trong mảng 10 phần tử, cần `0<=base<=5`. Kiểm tra chỉ `base<10` chưa đủ vì còn offset bên trong loop.

`array_access.c` có scan đúng `< ARRAY_SIZE`, scan lỗi `<=`, symbolic_unsafe và symbolic_safe. Đối chiếu witness với ASan là bước quan trọng trong test nguồn nhưng chưa được chạy lại ở đây. Test Python so 4 nhãn kỳ vọng đã đạt.

**Tự làm:** giảm bound của off-by-one xuống 10 và xem bug chưa xuất hiện; tăng lại 11; thêm input âm; xem miền Z3 hiện đã giả sử base≥0 nên chưa tìm phản ví dụ âm của C; mở rộng ngữ nghĩa overflow của `base+i` nếu cần.

## 5.8 Lab 7 - Coverage cho xử lý đơn hàng

Hàm `process_order` từ chối quantity ngoài 1..100, giá≤0 và pointer output NULL. Member được giảm 15% nếu qty≥10, ngược lại 5%; non-member được giảm 10% nếu qty≥20; tổng sau giảm >10.000.000 cần approval.

| Member | Quantity | Discount |
| --- | --- | ---: |
| Có | <10 | 5% |
| Có | ≥10 | 15% |
| Không | <20 | 0% |
| Không | ≥20 | 10% |

Có ba bộ test: partial 2 case, full 9 case và combinatorial 6×4×2=48 case. Các lớp quantity/price/member được chọn đại diện; 48 case là toàn bộ tích **các đại diện đó**, không phải mọi input khả dĩ.

Kết quả gcov **lưu sẵn trong dataset**, chưa đo lại:

- Partial: 51/64 dòng, 79,69%.
- Full: 59/64 dòng, 92,19%.
- Cải thiện: 12,50 **điểm phần trăm**.

Driver lỗi mở file, thiếu argv và default enum vẫn chưa phủ. Không gọi bộ “full” là 100% coverage. Oracle Python sao chép gần như cùng logic với C, nên có nguy cơ hai bên cùng mắc một lỗi đặc tả.

**Tự làm:** thêm quantity 9/10/11,19/20/21,100/101; thêm total bằng và sát ngưỡng approval; kiểm tra `NaN`, infinity của giá nếu API cho phép double bất kỳ. So sánh `price<=0` không tự từ chối NaN. Kiểm tra cả discount/total, không chỉ status.

## 5.9 Lab 8 - Fuzzing parser lệnh

`process_input` phân nhánh theo prefix `ADMIN:`/`ORDER:`. Trong nhánh ADMIN, nếu payload bắt đầu X thì strcpy vào `cmd[16]`; nhánh khác dùng snprintf. Điều kiện vào lỗi gồm prefix đúng, ký tự X và payload dài hơn capacity chuỗi cho phép.

Input regression mẫu trong test nguồn:

```text
ADMIN:XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

Đây là minh họa lỗi trong chương trình học tập. Không cần bất kỳ hệ thống bên ngoài nào để hiểu cơ chế.

`blackbox_fuzzer.py` mutate seed với insert/delete/replace/token; không đọc coverage và thêm candidate ngẫu nhiên 5%. `whitebox_fuzzer.py` đọc tập dòng chạy bằng gcov, giữ input tạo coverage mới, có thêm append_block và trọng số mutation khác. Nó không giải path bằng SMT.

Dataset **lưu sẵn** ghi black-box 1.000 lần: 0 crash, corpus 49; coverage-guided 500 lần: 3 crash, 17 dòng, crash đầu ở iteration 402. Những con số phụ thuộc seed, toolchain, oracle và các khác biệt mutation. Chúng không chứng minh “black-box không tìm được lỗi” hoặc hệ số tăng tốc tổng quát.

Test `blackbox_fuzzer_fails_within_same_budget` thực tế budget 1.000, khác 500 của coverage fuzzer. Assertion bắt buộc 0 crash rất dễ lệ thuộc kết quả ngẫu nhiên/phiên bản; báo cáo khoa học nên ghi phân bố qua nhiều seed và budget công bằng.

**Tự làm:** giữ cùng mutation/corpus/budget/seed policy, chỉ thay feedback; so unique root causes, exec/s và time-to-first-crash; lưu timeout riêng; minimize input; sửa strcpy rồi replay corpus.

## 5.10 Chạy lại và lập báo cáo thực hành

Cấu trúc thư mục có hai lớp tên lặp lại, ví dụ `lab5_sat_smt_verification/lab5_sat_smt_verification`. Chạy từ root bên trong chứa README/Makefile để relative paths đúng. Các README/Makefile phần lớn giả định công cụ kiểu POSIX (`python3`, `.so`, tên executable không `.exe`); Windows cần xét compiler, runtime, sanitizer và cách tìm binary. Không lấy lỗi môi trường làm bằng chứng rằng thuật toán sai.

Mẫu bằng chứng cho mỗi lab:

| Mục | Nội dung cần ghi |
| --- | --- |
| Mục tiêu | Thuộc tính/bug muốn kiểm tra |
| Phiên bản | Source, dataset, Python/compiler/tool version |
| Cấu hình | Command, flags, bound, seed, budget |
| Kết quả | Expected, actual, warning/trace/crash |
| Giải thích | Vì sao có kết quả đó, liên hệ lý thuyết |
| Sửa lỗi | Thay đổi invariant và input regression |
| Giới hạn | Đường chưa phủ, giả thiết, công cụ chưa chạy hoặc UNKNOWN |

Lab PDF có các yêu cầu nộp và câu hỏi thảo luận riêng. Các phần trên hệ thống hóa kiến thức để làm bài; vẫn nên xem PDF/README gốc khi cần đúng yêu cầu nộp của một lab cụ thể.
