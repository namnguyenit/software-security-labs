# Chương 8. Đính chính, khác biệt giữa nguồn và giới hạn kết luận

## 8.1 Cách sử dụng chương này

Tài liệu học tập gồm nhiều phiên bản slide, giáo trình, chương trình minh họa và đáp án. Một số mô tả là cách đơn giản hóa để giảng dạy; một số là lỗi số học hoặc chưa khớp code. Chương này ghi nhận cụ thể để tránh học sai. **Đính chính không sửa các file nguồn:** dữ liệu gốc được giữ, phần tổng hợp nêu cách hiểu chính xác hơn.

Bốn mức bằng chứng được dùng:

1. **Đọc nguồn:** kết luận từ văn bản, công thức hoặc code đã đọc.
2. **Đối chiếu cấu trúc:** kiểm tra tên file, schema, hash, đồ thị và sự trùng lặp.
3. **Chạy có chọn lọc:** kết quả Python/test được chạy lại trong bản sao tạm.
4. **Kết quả nguồn:** số liệu lưu sẵn trong JSON/CSV/PDF, chưa chạy lại toàn bộ công cụ tạo ra chúng.

Một test pass chỉ chứng minh điều kiện mà test thật sự kiểm tra. Một công thức UNSAT chỉ có ý nghĩa với miền biến, giả thiết và encoding đã đưa vào solver.

## 8.2 Những điểm cần sửa khi học lý thuyết

| Điểm trong nguồn | Cách hiểu/đính chính | Căn cứ |
| --- | --- | --- |
| Ví dụ `(5,3)` được tính statement coverage 3/4 trong slide Chương 1 phần 2, trang24 | Bộ đếm toolkit gồm hai điểm kiểm tra điều kiện và ba return: mẫu số 5, phủ 3/5=60%; branch2/4=50%. Định nghĩa câu lệnh/dòng theo công cụ khác phải ghi rõ | Đối chiếu bộ đếm và chạy `softsec-toolkit/ch1_models/testing.py` |
| Docstring của ví dụ coverage có chỗ mô tả test đơn đạt100% | Implementation tính60% statement và 50% branch; bộ ba input mới phủ đủ ví dụ | Kết quả chạy và code |
| Coverage-guided fuzzing được gọi toàn bộ là white-box; AFL có chỗ được xếp black-box | Phân loại phổ biến: black không feedback nội bộ; grey dùng feedback nhẹ như coverage; white phân tích semantics/ràng buộc. Việc có source chưa đủ phân loại | Phân tích thuật toán cụ thể trong thư mục; không chỉ theo tên file |
| “100% coverage” được diễn giải thành hết lỗi | Coverage không bao phủ mọi giá trị, trạng thái, oracle hoặc tương tác | Phản ví dụ chia0, overflow, NaN và logic nghiệp vụ |
| Mô tả mọi nhánh độc lập là O(n), mọi if lồng nhau là 2 ⁿ | Phải phân biệt phủ branch với liệt kê full path. n binary if nối tiếp có thể2 ⁿ đường; chuỗi if/else-if có thể n+1 lá; một chuỗi chỉ tiếp tục ở nhánh true cũng có n+1 lối thoát | Đồ thị điều khiển; `10_symbolic_cost.py` chỉ trả công thức giả định |
| Chuỗi 5 byte có xác suất in trong đoạn giải thích là 9,09×10⁻¹² | Đúng là 256⁻⁵≈9,094947×10⁻¹³; hai triệu lần có kỳ vọng≈1,818989×10⁻⁶ | Hàm `probability_without_dictionary` đúng; chuỗi `print` sai hệ số 10 |
| Unsat core được mô tả mặc nhiên là tối thiểu | Unsat core là tập con ràng buộc không thỏa; không tự đảm bảo tối thiểu theo bao hàm hoặc nhỏ nhất theo số lượng | Ngữ nghĩa thuật ngữ; muốn tối thiểu cần bước giảm riêng |
| `unsat`/`SAFE` được hiểu là chứng minh mọi code an toàn | Chỉ kết luận về thuộc tính, giả thiết, miền và bound đã mã hóa; phải xét `unknown` và completeness | Chương 3 và engine lab 6 |
| Sound/complete được dùng mà không nêu “kết luận” là tìm lỗi hay chứng minh an toàn | Nêu quy ước trước. Over-approximation có thể hữu ích để chứng minh không lỗi nhưng tạo cảnh báo giả; under-approximation có thể tìm lỗi thật nhưng bỏ sót | Chương 3, tập hành vi thật và tập xấp xỉ |
| `EX/AX` hoặc `AG/AF` được áp dụng vào đồ thị kết thúc mà không nói semantics | CTL thường dùng quan hệ total và đường vô hạn; terminal có thể được thêm self-loop, phải giữ thông tin deadlock gốc | Các mô hình linear chain/deadlock |

## 8.3 CWE, CVE và chấm điểm rủi ro

### Buffer over-read khác buffer overflow

Heartbleed, CVE-2014-0160, là đọc quá giới hạn do kiểm tra chiều dài heartbeat không đúng; không nên dùng như ví dụ ghi tràn buffer. Hai lớp lỗi có thể cùng bắt nguồn từ kiểm tra biên nhưng ảnh hưởng và thao tác sai khác nhau. Đối chiếu [bản ghi CVE-2014-0160 của MITRE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2014-0160).

Dirty COW, CVE-2016-5195, là lỗi race liên quan cơ chế copy-on-write, không phải ví dụ integer overflow. [NVD ghi CWE-362](https://nvd.nist.gov/vuln/detail/cve-2016-5195). Nếu slide/đáp án dùng CVE này dưới phép cộng tràn, giữ riêng khái niệm overflow và thay case study cho đúng.

`vulnerabilities.json` lab 3 dùng `CWE-121` cùng tên “Stack/Heap-based Buffer Overflow”, nhưng đối tượng lỗi được mô tả là cấp phát heap. CWE-121 chỉ stack-based; heap-based là CWE-122. Nên định danh theo vị trí object thực tế thay vì gộp hai lớp dưới một mã.

### Điểm lab 3 là CVSS-like

`risk_assessor.py` tính điểm giống CVSS nhưng giản lược Scope, dùng làm tròn Python và không thể hiện đầy đủ mọi quy tắc CVSS3.1. Kết quả chạy là 9,8;6,9;5,4;2,5. Có thể dùng để học mức ưu tiên **trong bài lab**, không gọi mọi giá trị là điểm CVSS chính thức.

CVSS3.1 dùng quy tắc Roundup trong bước tính Base; việc thay bằng `round(...,1)` có thể khác, chẳng hạn giá trị thô lớn hơn6,9 nhưng nhỏ hơn7,0. Scope cũng ảnh hưởng công thức. Đối chiếu [đặc tả CVSS3.1 của FIRST](https://www.first.org/cvss/v3-1/specification-document).

Mức rủi ro tổ chức còn phụ thuộc exposure và tác động thực tế. Điểm CVSS, số warning và số crash không thể dùng thay thế nhau. Không tự gán CVE cho code học tập hoặc suy một CWE từ mọi crash.

## 8.4 Những giới hạn trong code cần ghi rõ

| Thành phần | Quan sát từ code | Hệ quả và hướng xử lý |
| --- | --- | --- |
| `atpm/.../static_check.py` | Parse XML thất bại có thể trả report rỗng | Report rỗng có thể bị hiểu nhầm là sạch; phân biệt lỗi công cụ/parse với 0 finding |
| `atpm/.../smt_checks.py` và checker lab 5 | Một số nhánh dùng “khác sat” như không tìm thấy phản ví dụ | `unknown` phải là chưa kết luận; chỉ `unsat` mới xác nhận theo encoding |
| Lab5 `smt_equivalence_checker.py` | Dùng `eval` cho biểu thức dataset | Chỉ phù hợp dữ liệu tin cậy của bài; không phải sandbox nhận biểu thức tùy ý |
| Lab6 `bmc_engine.py` | Tự dựng chỉ số `base+i` theo JSON và từng bước | Minh họa BMC; không parse, kiểm chứng toàn bộ semantics C trong `array_access.c` |
| Lab1 P2 tamper→alarm | Nhãn tamper không xuất hiện đúng ở một số hành vi cần quan tâm | Thuộc tính có thể đúng vacuous dù mô hình bỏ mất sự kiện |
| Toolkit `satisfies_EF` | Xét từ mọi trạng thái đầu | Khác hàm lab 1 tìm witness từ bất kỳ trạng thái đầu; với multi-initial phải đọc contract |
| Toolkit `satisfies_AG_EF` | Kiểm tra các trạng thái khai báo, kể cả unreachable | Có thể mạnh hơn ngữ nghĩa AG từ tập đầu; cần giới hạn reachable để đúng mục tiêu |
| Lab2 `compute_branch_coverage` | Lấy dòng thực thi từ gcov | Tên hàm không làm số liệu thành branch coverage |
| Lab7 reference Python | Gần giống logic C | Hai bên có thể cùng lỗi; thêm oracle từ đặc tả độc lập |
| Lab7 giá | Guard `price<=0` chưa loại NaN | Kiểm tra giá hữu hạn và parser; test tổ hợp hiện có không bao phủ hết kiểu đầu vào |
| Lab7 “full” | JSON lưu59/64 dòng=92,19% | “Full” là tên bộ input, không có nghĩa100% line coverage |
| Lab8 white-box | Feedback gcov về dòng và mutation | Đây là coverage-guided grey-box theo phân loại đã nêu; không giải path constraint |
| Lab8 test so sánh | Budget500 và 1000; mutation khác | Không kết luận tác động độc lập của coverage từ một lượt |
| Fuzzer wrapper `atpm` | Return code âm được xem crash; timeout dùng mã sentinel âm | Có thể gộp hang với crash; dấu return code trên Windows/POSIX khác nhau |
| Fuzzer wrapper `atpm` | Không tự thêm ASan vào mọi lần build | Lỗi bộ nhớ không crash có thể không bị phát hiện; cần oracle/flags phù hợp |
| Toolkit `03_edge_coverage.py` | Nhãn minh họa chủ yếu theo lựa chọn/đích | Không coi là bitmap cạnh basic-block tương đương AFL |
| `pattern_scanner.py` | So khớp pattern cú pháp | Pattern không chứng minh reachability hoặc exploitability; dễ false positive/negative |
| Safe string helpers | Giới hạn destination không xác nhận toàn bộ source | Vẫn cần source hợp lệ/NUL, lifetime và quy tắc overlap |
| Một số bản “secure/fixed” | Sửa các lỗi mục tiêu của ví dụ | Tên file không chứng minh API hoàn chỉnh; vẫn xét NULL, count, đường lỗi, parser và ownership |
| Toolkit `08_student_module.c` | Comment padding chưa tính đúng vị trí `next`; ghi raw `StudentRecord` | Trên ABI con trỏ8 byte/alignment8 thường dùng: active ở44, padding3 byte, next ở48, sizeof56. Record không có con trỏ vẫn có thể có padding và khác endianness; kiểm tra fwrite và dùng serialization trường rõ ràng |
| Toolkit `09_product_list_extended.c` | Comment tổng36→40 byte bỏ qua con trỏ `next` | Trên ABI trên, next ở40 và sizeof48. Không lấy kích thước phần dữ liệu làm kích thước cả node |
| Toolkit `08_cbmc_packet_parser.c` | Bản fixed chặn chiều dài theo BUF_SIZE256 | Vẫn giả thiết source có đủ byte, output thực sự có 256 byte; API không nhận capacity. Clamp âm/quá dài còn có thể sai nghiệp vụ nếu yêu cầu từ chối dữ liệu malformed |

Các nhận xét trên phục vụ cách diễn giải tài liệu; đây không phải yêu cầu đã sửa toàn bộ chương trình hoặc triển khai một sản phẩm mới. Bản gốc giữ nguyên để người học đối chiếu.

## 8.5 Mô hình và đặc tả chưa khớp

1. **IoT mutex:** trực tiếp vi phạm chỉ `conflict`; bốn trạng thái có thể dẫn tới vi phạm là tập `EF(violation)`. Không trộn hai loại tập.
2. **ID16 ký tự và buffer 16 byte:** chuỗi C cần thêm NUL; tăng capacity hoặc giảm giới hạn.
3. **Tổng vượt 2 tỷ:** không đồng nghĩa tràn int 32; so đúng giới hạn kiểu và miền đầu vào.
4. **Expected khác actual:** test mô tả kết quả an toàn mong muốn, trong khi mô hình đang có lỗi, phải báo failed thay vì giữ nhãn “pass” chỉ vì đã điền template.
5. **Mô hình riêng và kết hợp:** số trạng thái khác nhau có thể hợp lệ khi mức trừu tượng khác nhau; không cộng lẫn hoặc coi tất cả là một đồ thị.
6. **NFR:** throughput, latency và durable logging cần workload/bằng chứng thực nghiệm hay thiết kế tương ứng; CTL của mutex không xác nhận chúng.
7. **Có khóa không đồng nghĩa công bằng:** starvation/fairness cần thuộc tính và giả thiết riêng.

## 8.6 Phiên bản tài liệu và kết quả lịch sử

- Hai PDF giới thiệu trùng hash; hai HTML đề ôn cũng trùng hash. Các ZIP là bản đóng gói của file đã giải nén, không thêm 186 nguồn độc lập.
- Giáo trình/slide có module không hiện diện trong toolkit này; bản đồ mã nguồn chỉ gắn với file thật.
- Hướng dẫn BTL, report guide và phụ lục giáo trình khác khung báo cáo, trọng số, thời gian hoặc hình thức bảo vệ. Giữ nguồn áp dụng tách biệt khi dùng để nộp bài.
- Số liệu fuzzing20.000/2.475 lượt trên slide, số liệu lab 8 1000/500 và số liệu Word mẫu thuộc các thử nghiệm khác nhau. Không ghép thành một phép so sánh.
- Kết quả JSON `expected` giống byte với `results` ở một số lab có thể là baseline/mẫu. Sự giống nhau không tự chứng minh công cụ đã được chạy lại trong môi trường hiện tại.
- Cache pytest/pyc không phải bằng chứng đầy đủ về chất lượng hoặc tính đúng. Cache ghi lại trạng thái chạy cũ, có thể phụ thuộc Python/phiên bản công cụ khác.

## 8.7 Lượt xác minh thực tế trong lần tổng hợp

| Nhóm | Kết quả | Phạm vi |
| --- | ---: | --- |
| Test Kripke `atpm` | 4 đạt | Dựng và kiểm tra mô hình Python |
| Test SMT `atpm` | 5 đạt, 5 bỏ qua | Test cần CBMC tự skip |
| Lab1 Python | 3 đạt, 2 loại khỏi lượt | Phần gọi C không nằm trong lượt Python |
| Lab5 Python | 2 đạt, 1 loại khỏi lượt | Không chạy brute-force executable C |
| Lab6 đối chiếu dataset | 1 đạt, 4 loại khỏi lượt | Xác nhận engine Python và nhãn JSON |
| Toolkit testing | 4 đạt | Tính coverage minh họa |
| Tổng | **19 đạt, 5 skip, 7 deselect** | Không phải toàn bộ test của thư mục |

Đã chạy thêm các phép tính rủi ro, kiểm tra 6 cặp SMT, 4 bài BMC và duyệt đồ thị của các mô hình chính/flow. Các phản ví dụ và số liệu được ghi tại Chương 5-7. GCC/gcov có trong môi trường; cppcheck/CBMC/Clang chưa có trong PATH, nên không khẳng định đã chạy lại ASan/cppcheck/CBMC/fuzzing C đầy đủ.

Chỉ thị unwind và kiểm tra của CBMC phụ thuộc phiên bản và cấu hình. Xem [manual chính thức CBMC](https://diffblue.github.io/cbmc/man/cbmc.html) khi chạy lại, đồng thời lưu phiên bản và lệnh cụ thể. Với harness libFuzzer, tham khảo [tài liệu LLVM](https://llvm.org/docs/LibFuzzer.html); mô tả công cụ trong tài liệu học không thay thế kiểm tra contract hiện hành.

## 8.8 Phạm vi chưa thể kết luận từ thư mục

Không có source tương ứng của hai EXE, nên chưa kiểm toán nội bộ parser, bộ sinh mã, cách chạy công cụ hoặc quản lý tiến trình của ứng dụng. Hash/PE chỉ nhận diện file, không chứng minh ứng dụng an toàn. Không chạy file EXE để suy rằng toàn bộ chức năng đã được thẩm định.

PDF đã được trích xuất toàn bộ 1095 trang. Đã kiểm tra hình ảnh đại diện cho đồ thị, layout bộ nhớ, coverage và Excel, chưa kiểm tra bằng mắt mọi hình nhỏ trên mọi trang. Những artefact phụ thuộc hình hoặc ký hiệu khó trích xuất cần đối chiếu PDF gốc qua chỉ mục trang. Không có lỗi đọc PDF/DOCX/XLSX trong lượt trích xuất.

Đáp án 1257 câu hỏi được bảo toàn theo nguồn và đánh dấu là đáp án gốc. Chưa thẩm định từng đáp án như một bài giải độc lập; các lỗi điển hình quan trọng đã được đính chính tại đây. Những câu yêu cầu tra cứu số liệu hiện hành hoặc “chuẩn” pháp lý không được coi là đã xác minh chỉ vì nằm trong HTML.

Giá trị chính của bộ tổng hợp là **khái niệm rõ, liên hệ code cụ thể, bằng chứng có phạm vi và khả năng truy vết về nguồn**. Khi gặp một kết luận, luôn xác định nó đang nói về đặc tả, mô hình, lần chạy hay toàn bộ chương trình.
