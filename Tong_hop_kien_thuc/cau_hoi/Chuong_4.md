# Chương 4: Phát hiện lỗ hổng phần mềm – Phân tích động: ngân hàng câu hỏi gốc

**360câu.** Nguồn: `De-On-Tap.htm`, trường `QUIZ_DATA`; file `on-tap-an-toan-phan-mem_rutgon.html` giống byte. Đáp án/giải thích giữ theo nguồn, không mặc nhiên đã được xác minh.

[Mục lục ngân hàng](../11_Ngan_hang_cau_hoi.md) · [Đính chính](../08_Dinh_chinh_va_gioi_han.md)

Các đoạn nguồn có code/Markdown không hoàn chỉnh được đặt trong khối text để bảo toàn nội dung. Số thứ tự gốc có thể bắt đầu lại ở từng mục; ID bên dưới là duy nhất theo chương/mục/loại.

## Mục 4.1: Giới thiệu kiểm thử bảo mật

### Tóm tắt kiến thức nguyên bản

Chương 4 chuyển trọng tâm sang Dynamic Analysis – kỹ thuật tự động hóa việc sinh input bằng cách CHẠY chương trình, mở rộng quy mô so với Testing thủ công (Ch.1.3). Vị trí trong phổ kỹ thuật QA: Testing thủ công → Dynamic Analysis (Chương 4) → Static Analysis (Chương 3) → Formal Verification (Ch.1.5). Security Testing khác Functional Testing: Functional kiểm tra chương trình làm ĐÚNG chức năng (input theo đặc tả, oracle = so sánh kết quả mong đợi); Security kiểm tra chương trình KHÔNG làm những gì KHÔNG nên làm (input cố tình bất thường/độc hại, oracle = crash/hang/vi phạm invariant bộ nhớ). Bốn kỹ thuật của Chương 4: Code Coverage (4.2, đo lường), Theo dõi thực thi (4.3, instrumentation/tracing), Sinh đường thực thi (4.4, mutation/hill-climbing), Fuzzing (4.5–4.6, thực thi quy mô lớn) – kết hợp thành một pipeline hoàn chỉnh. Lịch sử: 1988 Barton Miller đặt ra thuật ngữ “fuzz”; 2007–2013 AFL phổ biến hóa coverage-guided fuzzing; 2016-nay OSS-Fuzz (Google) đã phát hiện hơn 50.000 lỗi. Fuzzing hiệu quả với CWE-119/125/476 (crash rõ ràng), kém hiệu quả với lỗi logic nghiệp vụ. Toàn chương minh họa bằng thực nghiệm THẬT trên fuzz_target.c: black-box thất bại sau 20.000 lần thử, coverage-guided thành công sau 2.475 lần.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C4-4.1-trac_nghiem-01 · Câu gốc 1

Dynamic Analysis nằm ở vị trí nào trong phổ kỹ thuật QA đã ôn ở Ch.1.4/Ch.3.1?

**A.** Giữa Testing thủ công và Static Analysis

**B.** Sau Formal Verification

**C.** Trước Testing thủ công

**D.** Không liên quan tới phổ kỹ thuật nào

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-02 · Câu gốc 2

Chương 4 tập trung chủ yếu vào kỹ thuật nào?

**A.** Formal Verification

**B.** Phân tích động (Dynamic Analysis)

**C.** Thiết kế giao diện người dùng

**D.** Quản lý dự án phần mềm

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-03 · Câu gốc 3

Điểm khác biệt cốt lõi giữa Security Testing và Functional Testing là gì?

**A.** Không có khác biệt, cả hai giống hệt nhau

**B.** Security Testing kiểm tra chương trình KHÔNG làm gì không nên làm; Functional Testing kiểm tra chương trình làm ĐÚNG chức năng

**C.** Functional Testing luôn dùng input độc hại

**D.** Security Testing chỉ áp dụng cho web

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-04 · Câu gốc 4

Oracle (tiêu chí đánh giá) của Security Testing thường là gì?

**A.** So sánh với kết quả mong đợi trong đặc tả

**B.** Crash, hang, hoặc vi phạm invariant bộ nhớ

**C.** Thời gian biên dịch chương trình

**D.** Số dòng code đã viết

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-05 · Câu gốc 5

Input của Security Testing có đặc điểm gì khác Functional Testing?

**A.** Luôn theo đúng đặc tả (happy path)

**B.** Cố tình bất thường, độc hại, ngoài đặc tả

**C.** Chỉ dùng edge case đã biết trước

**D.** Không có gì khác biệt

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-06 · Câu gốc 6

Vì sao Dynamic Analysis KHÔNG đầy đủ (không sound) như Formal Verification?

**A.** Vì nó không xét MỌI input có thể, chỉ xét một tập input đã sinh ra

**B.** Vì nó chạy chậm hơn Formal Verification

**C.** Vì nó không dùng compiler

**D.** Vì nó chỉ áp dụng được cho Java

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-07 · Câu gốc 7

Bốn kỹ thuật chính được trình bày trong Chương 4 là gì?

**A.** Model checking, SAT solving, SMT solving, BMC

**B.** Code coverage, theo dõi thực thi, sinh đường thực thi, fuzzing

**C.** Risk assessment, secure coding, code review, pentest

**D.** UML, thiết kế kiến trúc, refactoring, CI/CD

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-08 · Câu gốc 8

Ai là người đặt ra thuật ngữ ”fuzz” và vào năm nào?

**A.** Barton Miller, năm 1988

**B.** Michal Zalewski, năm 2007

**C.** Dennis Ritchie, năm 1972

**D.** Donald Knuth, năm 1995

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-09 · Câu gốc 9

AFL (American Fuzzy Lop) phổ biến hóa kỹ thuật gì trong giai đoạn 2007-2013?

**A.** Black-box fuzzing thuần túy

**B.** Coverage-guided fuzzing

**C.** Formal verification

**D.** Static analysis heuristic

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-10 · Câu gốc 10

OSS-Fuzz của Google đã phát hiện khoảng bao nhiêu lỗi kể từ 2016?

**A.** Hơn 50.000 lỗi

**B.** Khoảng 500 lỗi

**C.** Chỉ vài chục lỗi

**D.** Chưa phát hiện lỗi nào

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-11 · Câu gốc 11

Fuzzing đặc biệt hiệu quả với loại lỗi CWE nào?

**A.** CWE-119 (buffer overflow), CWE-125 (out-of-bounds read), CWE-476 (NULL deref)

**B.** Chỉ lỗi logic nghiệp vụ

**C.** Chỉ lỗi rò rỉ thông tin âm thầm

**D.** Không hiệu quả với loại lỗi nào

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-12 · Câu gốc 12

Fuzzing kém hiệu quả với loại lỗi nào?

**A.** Lỗi crash rõ ràng

**B.** Lỗi logic nghiệp vụ (business logic flaw) và rò rỉ thông tin âm thầm

**C.** Lỗi NULL pointer dereference

**D.** Lỗi buffer overflow

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-13 · Câu gốc 13

Kiến trúc tổng quan của một Fuzzing Campaign gồm các bước nào theo đúng thứ tự?

**A.** Báo cáo crash -> Mutation -> Seed corpus -> Thực thi target

**B.** Seed corpus ban đầu -> Mutation engine -> Thực thi target (instrumented) -> Phân loại crash -> Báo cáo

**C.** Thực thi target -> Seed corpus -> Báo cáo -> Mutation

**D.** Không có thứ tự cố định

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-14 · Câu gốc 14

Vòng lặp feedback trong kiến trúc Fuzzing Campaign phân biệt điều gì?

**A.** Phân biệt white-box fuzzing với black-box fuzzing

**B.** Phân biệt Windows với Linux

**C.** Phân biệt C với Python

**D.** Không có ý nghĩa gì đặc biệt

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.1-trac_nghiem-15 · Câu gốc 15

Target thực nghiệm xuyên suốt Chương 4 (fuzz_target.c) crash khi nào?

**A.** Khi input rỗng

**B.** Khi input CHÍNH XÁC bằng 4 byte ”FUZZ”

**C.** Khi input dài hơn 64 byte

**D.** Không bao giờ crash

**Đáp án gốc:** B

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C4-4.1-ly_thuyet-01 · Câu gốc 1

Ôn lại vị trí của Dynamic Analysis trong phổ kỹ thuật QA (Ch.1.4, Ch.3.1) và giải thích vì sao nó nằm giữa Testing thủ công và Static Analysis.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-02 · Câu gốc 2

Trình bày sự khác biệt cốt lõi giữa Security Testing và Functional Testing, minh họa bằng một ví dụ cụ thể.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-03 · Câu gốc 3

Giải thích vì sao Dynamic Analysis không đầy đủ (không sound) như Testing toàn diện lý thuyết, nhưng vẫn hiệu quả trong thực tế.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-04 · Câu gốc 4

Mô tả bốn kỹ thuật cấu thành Chương 4 và giải thích cách chúng liên kết với nhau thành một pipeline hoàn chỉnh.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-05 · Câu gốc 5

Trình bày ngắn gọn lịch sử của Fuzzing từ 1988 (Barton Miller) tới OSS-Fuzz hiện nay.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-06 · Câu gốc 6

Giải thích tại sao Fuzzing đặc biệt hiệu quả với các lớp lỗi gây crash (CWE-119, CWE-125, CWE-476) nhưng kém hiệu quả với lỗi logic nghiệp vụ.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-07 · Câu gốc 7

Mô tả kiến trúc tổng quan của một Fuzzing Campaign (seed corpus, mutation engine, thực thi target, phân loại crash, báo cáo).

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-08 · Câu gốc 8

Giải thích vai trò của vòng lặp feedback trong kiến trúc Fuzzing Campaign và mối liên hệ với sự khác biệt giữa black-box và white-box.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-09 · Câu gốc 9

Trình bày target thực nghiệm fuzz_target.c dùng xuyên suốt Chương 4 và giải thích vì sao nó phù hợp để minh họa nguyên lý coverage-guided fuzzing.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-10 · Câu gốc 10

Giải thích kết quả thực nghiệm: vì sao black-box fuzzing thất bại sau 3000-20000 lần thử trong khi coverage-guided thành công sau 2475 lần.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-11 · Câu gốc 11

Bàn luận: Chương 4 được gọi là ”mảnh ghép cuối” hoàn thiện bộ công cụ của học phần. Giải thích ý nghĩa của nhận định này.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-12 · Câu gốc 12

So sánh Testing thủ công (Ch.1.3) và Dynamic Analysis tự động (Ch.4) về khả năng mở rộng quy mô sinh input.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-13 · Câu gốc 13

Cho ví dụ MỘT test case functional và MỘT test case security testing cho chức năng ”đăng nhập”, giải thích sự khác biệt về mục đích.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-14 · Câu gốc 14

Giải thích tại sao Testing thủ công không đủ để tìm ra lỗi dạng fuzz_target.c khi crash chỉ xảy ra với 1 trong 2^32 giá trị 4-byte.

**Trả lời gợi ý gốc:**



#### C4-4.1-ly_thuyet-15 · Câu gốc 15

Trình bày bảng so sánh Functional Testing và Security Testing theo ba tiêu chí: mục đích, input, và oracle.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C4-4.1-thuc_hanh-01 · Câu gốc 1

Viết một bảng so sánh (3 tiêu chí) giữa một test case functional và một test case security cho chức năng đăng ký tài khoản.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-02 · Câu gốc 2

Biên dịch fuzz_target.c và chạy thử với input ”HELLO”, quan sát chương trình có crash không, giải thích vì sao.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-03 · Câu gốc 3

Chạy module atpm.ch4_dynamic_analysis.fuzzing với black_box_fuzz(max_iteratio và ghi lại kết quả.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-04 · Câu gốc 4

Viết một đặc tả ngắn (bằng ngôn ngữ tự nhiên có cấu trúc) cho một test case security testing của chức năng tìm kiếm sản phẩm.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-05 · Câu gốc 5

Thiết kế 5 input ”bất thường có chủ đích” cho một hàm nhận chuỗi tên người dùng (độ dài âm, ký tự NULL giữa chuỗi, ký tự Unicode đặc biệt).

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-06 · Câu gốc 6

Vẽ sơ đồ (flowchart) kiến trúc một Fuzzing Campaign gồm 5 bước đã học.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-07 · Câu gốc 7

Cho hàm check_magic trong fuzz_target.c, liệt kê 3 loại input có khả năng kích hoạt crash cao hơn input hoàn toàn ngẫu nhiên.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-08 · Câu gốc 8

Viết một bảng phân loại 5 CWE giả định theo mức độ phù hợp để phát hiện bằng fuzzing (cao/trung bình/thấp).

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-09 · Câu gốc 9

Thiết kế checklist 5 mục để quyết định một module có nên fuzzing hay không.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-10 · Câu gốc 10

Viết Makefile biên dịch fuzz_target.c với các cờ phù hợp để chuẩn bị cho fuzzing.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-11 · Câu gốc 11

Chạy lại thực nghiệm black-box fuzzing với seed khác (2, 3, 5), ghi lại số iterations mỗi lần và so sánh.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-12 · Câu gốc 12

Viết báo cáo ngắn (100 từ) giải thích cho một quản lý dự án không kỹ thuật về sự khác biệt giữa functional testing và security testing.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-13 · Câu gốc 13

Thiết kế 3 test case functional và 3 test case security cho một API đăng nhập bằng JWT.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-14 · Câu gốc 14

Viết đoạn code Python đơn giản mô phỏng bước ”seed corpus ban đầu” của kiến trúc fuzzing campaign.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_hanh-15 · Câu gốc 15

Cho danh sách 5 module trong một hệ thống ngân hàng, xếp hạng mức độ ưu tiên áp dụng Dynamic Analysis.

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C4-4.1-thuc_te-01 · Câu gốc 1

Một công ty phát hiện chức năng đăng nhập của mình bị brute-force do chỉ kiểm thử functional mà bỏ qua security testing. Phân tích nguyên nhân và đề xuất khắc phục.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-02 · Câu gốc 2

Một startup game gặp sự cố crash ngẫu nhiên khi người chơi nhập tên nhân vật chứa ký tự đặc biệt. Phân tích liên hệ với khái niệm input ”bất thường có chủ đích”.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-03 · Câu gốc 3

Một tổ chức tài chính quyết định đầu tư vào chương trình fuzzing liên tục sau khi đọc báo cáo OSS-Fuzz. Phân tích lợi ích kỳ vọng.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-04 · Câu gốc 4

Một đội phát triển tranh luận liệu 100% test case functional pass có đủ để release sản phẩm không. Phân tích và đưa ra quan điểm có cơ sở.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-05 · Câu gốc 5

Một công ty IoT phát hiện thiết bị của mình bị tấn công qua một input mạng chưa từng được test. Đề xuất áp dụng Dynamic Analysis cho module xử lý input mạng.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-06 · Câu gốc 6

Một dự án mã nguồn mở tham gia chương trình OSS-Fuzz của Google và phát hiện 20 lỗi trong tháng đầu tiên. Phân tích ý nghĩa của kết quả này.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-07 · Câu gốc 7

Một công ty phần mềm nhúng cho ngành y tế cân nhắc giữa đầu tư fuzzing và đầu tư formal verification cho cùng ngân sách hạn chế. Phân tích đánh đổi.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-08 · Câu gốc 8

Một tổ chức phát hiện lỗi bảo mật nghiêm trọng (CWE-476, NULL deref) chỉ xảy ra với một giá trị input cụ thể trong hàng tỷ khả năng. Phân tích vì sao testing thủ công đã bỏ sót.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-09 · Câu gốc 9

Một công ty an ninh mạng được thuê để đánh giá một ứng dụng ngân hàng, quyết định bắt đầu bằng security testing thay vì functional testing. Phân tích lý do lựa chọn này.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-10 · Câu gốc 10

Một sinh viên thực tập đề xuất dùng cùng bộ test case cho cả functional testing và security testing. Phân tích vì sao đề xuất này chưa phù hợp.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-11 · Câu gốc 11

Một công ty phát hiện một chức năng tìm kiếm bị SQL injection do chỉ kiểm thử với input hợp lệ điển hình. Đề xuất bổ sung quy trình security testing.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-12 · Câu gốc 12

Một dự án phần mềm hàng không (liên hệ DO-178C, Ch.3.1) cần quyết định mức độ áp dụng dynamic analysis kết hợp với formal verification. Phân tích đề xuất.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-13 · Câu gốc 13

Một công ty khởi nghiệp nhỏ không có ngân sách cho công cụ fuzzing thương mại, chỉ dùng module Python đơn giản như trong atpm_project. Phân tích tính khả thi.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-14 · Câu gốc 14

Một tổ chức phát hiện rằng lỗi họ tìm được qua fuzzing đã tồn tại trong code base suốt 3 năm mà không ai phát hiện qua testing thủ công. Phân tích nguyên nhân.

**Trả lời gợi ý gốc:**



#### C4-4.1-thuc_te-15 · Câu gốc 15

Một công ty game online bị tấn công DDoS thông qua một gói tin mạng có định dạng bất thường. Phân tích liên hệ với khái niệm input ngoài đặc tả.

**Trả lời gợi ý gốc:**



## Mục 4.2: Phủ mã nguồn (Code Coverage)

### Tóm tắt kiến thức nguyên bản

Code Coverage đo lường phần mã đã được thực thi. Ba loại: Statement/Line coverage (% câu lệnh chạy ≥ 1 lần), Branch/Decision coverage (% nhánh chạy cả hai chiều), Path coverage (thường bất khả thi đo đủ). Chương 4 dùng line coverage qua gcov: gcc --coverage -O0 -c file.c -o file.o rồi gcov file.c in báo cáo % dòng đã thực thi. Với target check_magic(), coverage tăng dần theo độ “gần đúng” của input: “A”=64.29%, “F”=71.43%, “FU”=78.57%, “FUZ”=85.71%, “FUZZ”=crash – đây chính là tính chất khiến coverage trở thành TÍN HIỆU hữu ích cho fuzzing (4.6). Ngộ nhận cần tránh: “100% coverage = không còn lỗi” là SAI – coverage chỉ đo dòng nào đã CHẠY QUA, không đo GIÁ TRỊ cụ thể đã thử (VD: hàm divide(a,b) có thể 100% covered nhưng vẫn crash nếu b=0 chưa được test). Công cụ CI/CD: gcov, llvm-cov, lcov (báo cáo HTML); ngưỡng tối thiểu thường 70–90%. .gcda tích lũy qua nhiều lần chạy (không tự reset) – tính chất mà coverage_guided_fuzz dựa vào để “nhớ” tiến triển, tương đương “global bitmap” của AFL++. Kết hợp Fuzzing + Unit test cho coverage VÀ khả năng phát hiện lỗi bảo mật cao nhất.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C4-4.2-trac_nghiem-01 · Câu gốc 1

Statement/Line coverage đo lường điều gì?

**A.** % câu lệnh được thực thi ít nhất 1 lần

**B.** % nhánh rẽ được thực thi cả hai chiều

**C.** % đường đi hoàn chỉnh qua chương trình

**D.** Số lượng biến trong chương trình

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-02 · Câu gốc 2

Branch/Decision coverage đo lường điều gì?

**A.** % câu lệnh được thực thi

**B.** % nhánh rẽ (if/else) được thực thi CẢ HAI chiều

**C.** Tổng số dòng code

**D.** Thời gian thực thi chương trình

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-03 · Câu gốc 3

Vì sao Path coverage thường bất khả thi để đo đủ?

**A.** Vì số đường đi hoàn chỉnh qua chương trình tăng theo cấp số nhân với số nhánh rẽ

**B.** Vì công cụ đo path coverage không tồn tại

**C.** Vì path coverage giống hệt line coverage

**D.** Vì path coverage chỉ áp dụng cho Python

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-04 · Câu gốc 4

Chương 4 dùng chủ yếu loại coverage nào và vì sao?

**A.** Path coverage, vì chính xác nhất

**B.** Line coverage (qua gcov), vì đơn giản, nhanh, đủ làm tín hiệu cho fuzzing

**C.** Branch coverage, vì miễn phí

**D.** Không dùng loại coverage nào

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-05 · Câu gốc 5

Lệnh nào dùng để biên dịch file C với hỗ trợ đo coverage bằng gcov?

**A.** gcc -O2 -o target target.c

**B.** gcc –coverage -O0 -c target.c -o target.o

**C.** gcc -fsanitize=address target.c

**D.** gcc -Wall target.c

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-06 · Câu gốc 6

Cờ –coverage của gcc tự động thêm những cờ nào?

**A.** -fprofile- arcs và -ftest-coverage

**B.** -fsanitize=address và -fsanitize=undefined

**C.** -O3 và -march=native

**D.** -Wall và -Wextra

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-07 · Câu gốc 7

Trong target check_magic(), coverage đạt bao nhiêu % khi input là ”F” (khớp 1/4 ký tự)?

**A.** 64.29%

**B.** 71.43%

**C.** 85.71%

**D.** 100%

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-08 · Câu gốc 8

Trong target check_magic(), coverage đạt bao nhiêu % khi input là ”FUZ” (khớp 3/4 ký tự)?

**A.** 78.57%

**B.** 71.43%

**C.** 85.71%

**D.** 64.29%

**Đáp án gốc:** C

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-09 · Câu gốc 9

Điều gì xảy ra khi input CHÍNH XÁC bằng ”FUZZ” (khớp cả 4 ký tự)?

**A.** Coverage đạt 100% và chương trình kết thúc bình thường

**B.** Chương trình CRASH do NULL pointer dereference

**C.** Coverage giảm xuống 0%

**D.** Không có gì thay đổi so với input ”FUZ”

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-10 · Câu gốc 10

Output thực tế của lệnh gcov cho biết điều gì trong dòng ”Lines executed:85.71% of 14”?

**A.** 85.71% trong tổng số 14 dòng thực thi được đã chạy qua ít nhất 1 lần

**B.** Chương trình chạy trong 85.71 giây

**C.** ````text
Có

```
lỗi được phát hiện
````

**D.** ````text
85.71% bộ nhớ được sử dụng.
```
````

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-11 · Câu gốc 11

File .gcov sinh ra sau khi chạy gcov chứa thông tin gì?

**A.** Mã nguồn gốc kèm số lần mỗi dòng được thực thi

**B.** Chỉ số dòng code, không có nội dung

**C.** Danh sách lỗi cú pháp

**D.** Biểu đồ gọi hàm (call graph)

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-12 · Câu gốc 12

Nhận định ”100% coverage nghĩa là không còn lỗi” là đúng hay sai? A. Đúng, coverage 100% đảm bảo không có lỗi. B. Sai, coverage chỉ đo mã đã chạy qua, không đo mọi giá trị input đã thử qua dòng đó. C. Chỉ đúng với ngôn ngữ C. D. Chỉ đúng khi dùng gcov.

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-13 · Câu gốc 13

Với hàm divide(a,b) chỉ có 1 dòng chia, test case nào đạt 100% line coverage nhưng vẫn để lọt lỗi chia cho 0?

**A.** Gọi divide(10, 0)

**B.** Gọi divide(10, 2) và không kiểm tra trường hợp b=0

**C.** Không có test case nào đạt 100% coverage cho hàm này

**D.** Gọi divide(0, 0) hai lần

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-14 · Câu gốc 14

Coverage cao là điều kiện gì cho một test suite tốt?

**A.** Điều kiện đủ, không cần thêm kỹ thuật khác

**B.** Điều kiện cần, không phải điều kiện đủ

**C.** Không liên quan gì tới chất lượng test suite

**D.** Điều kiện duy nhất cần quan tâm

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.2-trac_nghiem-15 · Câu gốc 15

Công cụ nào KHÔNG được nhắc tới như công cụ đo coverage phổ biến trong CI/CD?

**A.** gcov (GCC)

**B.** llvm-cov (Clang)

**C.** lcov (báo cáo HTML)

**D.** Wireshark

**Đáp án gốc:** D

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C4-4.2-ly_thuyet-01 · Câu gốc 1

Ôn lại ba loại coverage đã học ở Ch.1.3 (statement, branch, path) và giải thích khác biệt giữa chúng.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-02 · Câu gốc 2

Giải thích vì sao Chương 4 chọn dùng line coverage (qua gcov) thay vì path coverage đầy đủ.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-03 · Câu gốc 3

Trình bày quy trình 4 bước dùng gcov để đo coverage cho một file C (biên dịch, chạy, đọc báo cáo).

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-04 · Câu gốc 4

Giải thích ý nghĩa của cờ –coverage khi biên dịch với gcc và các cờ con nó tự động thêm vào.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-05 · Câu gốc 5

Trình bày kết quả thực nghiệm coverage tăng dần theo độ ”gần đúng” của input với target check_magic().

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-06 · Câu gốc 6

Giải thích tại sao coverage tăng dần theo số ký tự khớp lại là tín hiệu hữu ích cho fuzzing.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-07 · Câu gốc 7

Diễn giải chính xác ý nghĩa dòng output ”Lines executed:85.71% of 14” của gcov.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-08 · Câu gốc 8

Giải thích ngộ nhận phổ biến ”100% coverage nghĩa là không còn lỗi” và minh họa bằng ví dụ hàm divide(a,b).

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-09 · Câu gốc 9

Bàn luận: vì sao coverage cao là điều kiện CẦN nhưng không phải điều kiện ĐỦ cho một test suite tốt.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-10 · Câu gốc 10

Trình bày các công cụ coverage phổ biến trong CI/CD thực tế (gcov, llvm-cov, lcov) và vai trò của mỗi công cụ.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-11 · Câu gốc 11

Giải thích khái niệm ”coverage differential” và ứng dụng của nó trong quy trình review pull request.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-12 · Câu gốc 12

Mô tả cách lcov tạo báo cáo HTML trực quan từ dữ liệu gcov và lợi ích so với đọc terminal.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-13 · Câu gốc 13

Giải thích tính chất tích lũy của file .gcda và tầm quan trọng của nó đối với module coverage_guided_fuzz.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-14 · Câu gốc 14

Trình bày khái niệm tương đương ”global bitmap” trong AFL++ so với tính tích lũy của .gcda.

**Trả lời gợi ý gốc:**



#### C4-4.2-ly_thuyet-15 · Câu gốc 15

So sánh coverage và khả năng phát hiện lỗi bảo mật giữa unit test viết tay, fuzzing 24h, và kết hợp cả hai.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C4-4.2-thuc_hanh-01 · Câu gốc 1

Biên dịch c/ch4_dynamic/fuzz_target.c với –coverage, chạy với input ”XYZ” và ”FUZ”, so sánh % coverage thu được.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-02 · Câu gốc 2

Giải thích bằng số liệu cụ thể tại sao coverage của input ”A” và ”B” là giống nhau (64.29%) dù hai input khác nhau.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-03 · Câu gốc 3

Với hàm divide(a,b), viết 1 test case đạt 100% line coverage nhưng vẫn để lọt lỗi chia cho 0.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-04 · Câu gốc 4

Chạy gcov trên fuzz_target.c sau khi thử input ”FU”, ghi lại nội dung file .gcov sinh ra.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-05 · Câu gốc 5

Viết script bash tự động hóa quy trình: biên dịch –coverage, chạy 3 input khác nhau, in báo cáo gcov cho mỗi lần.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-06 · Câu gốc 6

Cài đặt lcov trên máy, tạo báo cáo HTML cho fuzz_target.c, mô tả những gì thấy được trên giao diện.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-07 · Câu gốc 7

Viết một pipeline CI đơn giản (giả định GitHub Actions) chạy gcov và cảnh báo nếu coverage giảm dưới 70%.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-08 · Câu gốc 8

Thiết kế 3 test case cho hàm check_magic() sao cho đạt coverage 100% mà KHÔNG cần tìm ra input gây crash.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-09 · Câu gốc 9

Viết đoạn code Python đọc output text của gcov và trích xuất % coverage bằng regex (tương tự measure_coverage_percent).

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-10 · Câu gốc 10

Cho một hàm C có 2 nhánh if lồng nhau, tính tay số dòng ”executable” và dự đoán % coverage với 3 input khác nhau.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-11 · Câu gốc 11

Chạy thực nghiệm: xóa file .gcda giữa hai lần chạy, so sánh coverage tích lũy có reset hay không.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-12 · Câu gốc 12

Viết báo cáo so sánh coverage của 3 test suite giả định (unit test, fuzzing 1h, kết hợp) theo bảng đã học.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-13 · Câu gốc 13

Thiết kế một quy trình 2 bước: đo coverage TRƯỚC khi thêm fuzzing, và SAU khi thêm 1000 lần fuzzing, ghi lại kết quả.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-14 · Câu gốc 14

Viết Makefile với target ”coverage” tự động biên dịch, chạy target, và in báo cáo gcov.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_hanh-15 · Câu gốc 15

Cho hàm với 5 điều kiện if liên tiếp (tương tự check_magic mở rộng), tính số bước coverage trung gian có thể quan sát được.

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C4-4.2-thuc_te-01 · Câu gốc 1

Một công ty tự hào báo cáo ”100% test coverage” nhưng vẫn gặp sự cố sản xuất nghiêm trọng. Phân tích nguyên nhân dựa trên giới hạn của coverage.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-02 · Câu gốc 2

Một đội DevOps thiết lập ngưỡng coverage tối thiểu 80% trong CI, chặn merge nếu không đạt. Phân tích lợi ích và rủi ro của chính sách này.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-03 · Câu gốc 3

Một dự án mã nguồn mở nhận phản hồi từ cộng đồng rằng coverage cao nhưng vẫn có nhiều lỗi bảo mật. Phân tích và đề xuất bổ sung fuzzing.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-04 · Câu gốc 4

Một công ty tài chính phát hiện một lỗi chia cho 0 trong module tính lãi suất dù coverage của module này là 100%. Phân tích nguyên nhân cụ thể.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-05 · Câu gốc 5

Một tổ chức yêu cầu mọi pull request phải kèm coverage differential report. Phân tích lợi ích của yêu cầu này trong quy trình review.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-06 · Câu gốc 6

Một nhóm phát triển dùng lcov để phát hiện một module logging chưa từng được test trong suốt 2 năm. Phân tích rủi ro tiềm ẩn.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-07 · Câu gốc 7

Một công ty startup không đủ nguồn lực để duy trì coverage cao, chọn tập trung coverage vào module lõi (core) thay vì toàn bộ hệ thống. Phân tích tính hợp lý.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-08 · Câu gốc 8

Một dự án phần mềm nhúng dùng gcov nhưng phát hiện .gcda không tích lũy đúng do lỗi cấu hình CI. Phân tích ảnh hưởng tới quy trình coverage- guided fuzzing.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-09 · Câu gốc 9

Một công ty game phát hiện module xử lý input mạng có coverage thấp nhất toàn hệ thống dù đây là module rủi ro cao nhất. Đề xuất hành động khắc phục.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-10 · Câu gốc 10

Một tổ chức kiểm toán an ninh yêu cầu báo cáo coverage trước và sau khi áp dụng fuzzing như bằng chứng cải thiện chất lượng. Phân tích ý nghĩa của yêu cầu này.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-11 · Câu gốc 11

Một công ty phát hiện một điều kiện checksum phức tạp có coverage 100% nhưng vẫn chứa lỗi logic nghiêm trọng. Phân tích liên hệ với giới hạn của line coverage.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-12 · Câu gốc 12

Một đội ngũ kỹ sư tranh luận nên đầu tư thời gian vào tăng coverage từ 85% lên 95% hay chuyển sang đầu tư fuzzing. Phân tích và đưa ra khuyến nghị.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-13 · Câu gốc 13

Một công ty phát hiện coverage của họ giảm đột ngột sau một đợt refactor lớn nhưng không ai chú ý kịp thời. Đề xuất quy trình giám sát coverage liên tục.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-14 · Câu gốc 14

Một tổ chức y tế yêu cầu coverage 100% cho mọi module xử lý dữ liệu bệnh nhân. Phân tích tính khả thi và giới hạn của yêu cầu này.

**Trả lời gợi ý gốc:**



#### C4-4.2-thuc_te-15 · Câu gốc 15

Một dự án mã nguồn mở dùng lcov để công khai báo cáo coverage trên README nhằm tăng độ tin cậy với cộng đồng. Phân tích hiệu quả của cách làm này.

**Trả lời gợi ý gốc:**



## Mục 4.3: Theo dõi thực thi chương trình

### Tóm tắt kiến thức nguyên bản

Instrumentation: chèn thêm mã (biên dịch hoặc runtime) để thu thập thông tin hành vi runtime mà không đổi logic nghiệp vụ. Compile-time (gcov, afl-gcc, ASan): cần source code, nhanh và chính xác hơn. Binary (QEMU mode, Intel Pin, DynamoRIO): không cần source, dùng cho phần mềm đóng gói, chậm hơn. Edge Coverage (AFL/AFL++) cải tiến so với Line Coverage: theo dõi CẶP chuyển tiếp (current_location ⊕ prev_location) giữa 2 basic block, phân biệt được A→B→C với A→C→B dù cùng tập dòng lệnh. AFL ghi vào shared memory bitmap (64KB) chia sẻ giữa fuzzer và target – rất nhanh vì không cần ghi file/log. Bảng overhead: gcov 10–30%, AFL edge coverage 20–50%, QEMU mode 2–5x, full symbolic execution (KLEE) 10–100x – trade-off giữa thông tin thu thập và tốc độ. Fork Server của AFL tránh chi phí exec() lặp lại (tăng tốc 2–5x). strace/ltrace là tracing THÔ ở mức hệ điều hành (system call/library call) – hữu ích phân tích malware không rõ nguồn gốc. LUÔN kết hợp coverage instrumentation với sanitizer (ASan) để bắt cả lỗi không crash ngay lập tức.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C4-4.3-trac_nghiem-01 · Câu gốc 1

Instrumentation là gì?

**A.** Xóa bớt code không cần thiết để tăng tốc độ

**B.** Chèn thêm mã (lúc biên dịch hoặc chạy) để thu thập thông tin về hành vi runtime

**C.** Một loại virus máy tính

**D.** Một công cụ quản lý phiên bản mã nguồn

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-02 · Câu gốc 2

Compile-time instrumentation khác Binary instrumentation ở điểm nào?

**A.** Compile-time cần source code, chèn mã lúc biên dịch; Binary chèn mã trực tiếp vào binary đã build

**B.** Không có khác biệt gì

**C.** Binary instrumentation luôn nhanh hơn compile-time

**D.** Compile-time chỉ dùng được cho Python

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-03 · Câu gốc 3

Ví dụ nào là compile-time instrumentation?

**A.** QEMU mode, Intel Pin

**B.** gcov, afl-gcc, ASan

**C.** strace, ltrace

**D.** Wireshark

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-04 · Câu gốc 4

Ví dụ nào là binary instrumentation?

**A.** gcov

**B.** ASan

**C.** QEMU mode (AFL++), Intel Pin, DynamoRIO

**D.** afl-gcc

**Đáp án gốc:** C

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-05 · Câu gốc 5

Edge Coverage khác Line Coverage ở điểm nào?

**A.** Edge coverage theo dõi cả cặp chuyển tiếp giữa 2 basic block, không chỉ dòng nào được thực thi

**B.** Không có khác biệt, chỉ là tên gọi khác nhau

**C.** Edge coverage chậm hơn nhưng kém chính xác hơn

**D.** Line coverage chính xác hơn edge coverage

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-06 · Câu gốc 6

Edge coverage phân biệt được điều gì mà line coverage không phân biệt được?

**A.** Phân biệt A→B→C với A→C→B dù cả hai phủ cùng tập dòng lệnh

**B.** Phân biệt ngôn ngữ lập trình

**C.** Phân biệt hệ điều hành

**D.** Không phân biệt được gì thêm

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-07 · Câu gốc 7

AFL/AFL++ dùng loại coverage nào?

**A.** Line coverage như gcov

**B.** Path coverage đầy đủ

**C.** Edge coverage

**D.** Không dùng coverage nào

**Đáp án gốc:** C

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-08 · Câu gốc 8

Trong đoạn giả lập __afl_area_ptr[current_location ^ prev_location]++, biến nào là vùng nhớ chia sẻ giữa fuzzer và target?

**A.** current_location

**B.** prev_location

**C.** __afl_area_ptr

**D.** candidate

**Đáp án gốc:** C

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-09 · Câu gốc 9

Fuzzer đọc bitmap __afl_area_ptr vào thời điểm nào?

**A.** Trước khi chạy target

**B.** Ngay SAU MỖI lần chạy target để biết có đường đi mới hay không

**C.** Chỉ đọc một lần duy nhất khi khởi động

**D.** Không bao giờ đọc bitmap này

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-10 · Câu gốc 10

Lệnh nào dùng để biên dịch target cho AFL++ (khuyến nghị hiện nay)?

**A.** gcc –coverage

**B.** afl-clang-fast

**C.** gcc -O3

**D.** python setup.py build

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-11 · Câu gốc 11

Overhead điển hình của gcov line coverage là bao nhiêu?

**A.** 10-30% chậm hơn

**B.** 2-5x chậm hơn

**C.** 10-100x chậm hơn

**D.** Không có overhead

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-12 · Câu gốc 12

Overhead điển hình của AFL/AFL++ edge coverage (compile- time) là bao nhiêu?

**A.** 10-30%

**B.** 20-50% chậm hơn

**C.** 2-5x chậm hơn

**D.** 10-100x chậm hơn

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-13 · Câu gốc 13

Overhead của QEMU mode (binary, không có source) là bao nhiêu?

**A.** 10-30%

**B.** 20-50%

**C.** 2-5x chậm hơn

**D.** Không có overhead

**Đáp án gốc:** C

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-14 · Câu gốc 14

Full symbolic execution (KLEE) có overhead điển hình là bao nhiêu?

**A.** 10-30%

**B.** 2-5x chậm hơn

**C.** 10-100x chậm hơn

**D.** Không có overhead đáng kể

**Đáp án gốc:** C

**Giải thích gốc:**



#### C4-4.3-trac_nghiem-15 · Câu gốc 15

Trade-off cốt lõi của instrumentation là gì?

**A.** Càng nhiều thông tin thu thập, overhead càng cao, ảnh hưởng số lượng input thử được

**B.** Không có trade-off nào

**C.** Instrumentation luôn miễn phí về hiệu năng

**D.** Overhead chỉ phụ thuộc vào ngôn ngữ lập trình

**Đáp án gốc:** A

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C4-4.3-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa Instrumentation và phân biệt với các khái niệm khác đã học (coverage, tracing).

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-02 · Câu gốc 2

So sánh Compile-time Instrumentation và Binary Instrumentation, cho ví dụ công cụ mỗi loại.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-03 · Câu gốc 3

Giải thích khái niệm Edge Coverage và vì sao nó cải tiến so với Line Coverage đã học ở Mục 4.2.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-04 · Câu gốc 4

Trình bày cách AFL/AFL++ chèn mã vào mỗi basic block để theo dõi edge coverage (khái niệm bitmap).

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-05 · Câu gốc 5

Giải thích vai trò của vùng nhớ chia sẻ (shared memory bitmap) 64KB giữa fuzzer và target trong AFL.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-06 · Câu gốc 6

Trình bày bảng overhead của các kỹ thuật instrumentation khác nhau (gcov, AFL, QEMU mode, KLEE) và giải thích trade-off.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-07 · Câu gốc 7

Giải thích vì sao sanitizers (ASan, UBSan) được coi là một dạng instrumentation chuyên biệt.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-08 · Câu gốc 8

Bàn luận lý do LUÔN kết hợp coverage instrumentation với sanitizer trong một fuzzing campaign thực tế.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-09 · Câu gốc 9

Trình bày sự khác biệt giữa tracing ở mức hệ điều hành (strace/ltrace) và instrumentation biên dịch.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-10 · Câu gốc 10

Giải thích khái niệm Fork Server của AFL và cách nó tối ưu tốc độ so với gọi execve mới mỗi lần.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-11 · Câu gốc 11

Bàn luận vì sao module Python đơn giản của học phần chậm hơn nhiều so với AFL thực tế, và đây có phải là vấn đề trong bối cảnh giảng dạy không.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-12 · Câu gốc 12

Trình bày cách chọn kỹ thuật instrumentation phù hợp khi fuzzing một phần mềm đóng gói không có source code.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-13 · Câu gốc 13

Giải thích mối liên hệ giữa overhead của instrumentation và tốc độ (số lần thử/giây) của một fuzzing campaign.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-14 · Câu gốc 14

Trình bày vai trò của tracing như một ”cảm biến” cung cấp tín hiệu cho fuzzer quyết định mutation nào nên giữ lại.

**Trả lời gợi ý gốc:**



#### C4-4.3-ly_thuyet-15 · Câu gốc 15

Giải thích tại sao edge coverage phân biệt được A→B→C với A→C→B trong khi line coverage thì không.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C4-4.3-thuc_hanh-01 · Câu gốc 1

Chạy strace trên một chương trình bất kỳ và liệt kê 5 system call quan trọng được ghi lại.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-02 · Câu gốc 2

Chạy ltrace trên cùng chương trình đó, so sánh thông tin thu được với strace.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-03 · Câu gốc 3

Biên dịch fuzz_target.c với -fsanitize=address, chạy lại thực nghiệm và ghi lại thông báo lỗi ASan (nếu có).

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-04 · Câu gốc 4

Viết bảng so sánh overhead của 4 kỹ thuật instrumentation đã học, sắp xếp theo thứ tự tăng dần.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-05 · Câu gốc 5

Thiết kế sơ đồ minh họa luồng dữ liệu giữa target (đã instrument) và fuzzer qua shared memory bitmap.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-06 · Câu gốc 6

Cho một hàm C giả định với 3 basic block, vẽ sơ đồ edge coverage minh họa các cặp chuyển tiếp có thể có.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-07 · Câu gốc 7

Viết đoạn giả mã Python mô phỏng cách AFL ghi vào bitmap khi target chạy qua từng basic block.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-08 · Câu gốc 8

Nếu có afl-clang-fast trong môi trường, biên dịch fuzz_target.c bằng công cụ này và so sánh với gcc thông thường.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-09 · Câu gốc 9

Thiết kế checklist 4 mục để chọn giữa compile-time và binary instrumentation cho một dự án cụ thể.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-10 · Câu gốc 10

Viết báo cáo 100 từ giải thích Fork Server cho một lập trình viên mới học về fuzzing.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-11 · Câu gốc 11

Cho một target không có source code, đề xuất công cụ binary instrumentation phù hợp và giải thích lý do.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-12 · Câu gốc 12

Thiết kế bảng ước tính số lần thử/giây có thể đạt được với 3 mức overhead khác nhau (10%, 50%, 300%) trong 1 giờ campaign.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-13 · Câu gốc 13

Viết một kịch bản (script) kết hợp AFL với ASan cho một target C giả định (mô tả các bước, không cần chạy thật nếu môi trường hạn chế).

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-14 · Câu gốc 14

Cho kết quả strace của một chương trình mở file không tồn tại, phân tích system call nào cho thấy lỗi này.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_hanh-15 · Câu gốc 15

Thiết kế sơ đồ so sánh trực quan giữa line coverage và edge coverage cho cùng một đoạn code có vòng lặp.

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C4-4.3-thuc_te-01 · Câu gốc 1

Một công ty phần mềm bảo mật cần fuzzing một ứng dụng của đối tác không cung cấp source code. Đề xuất kỹ thuật instrumentation phù hợp.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-02 · Câu gốc 2

Một tổ chức phát hiện việc thêm ASan vào production làm chậm hệ thống 3 lần, gây tranh cãi giữa đội bảo mật và đội vận hành. Phân tích và đề xuất giải pháp.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-03 · Câu gốc 3

Một công ty game engine muốn tối ưu tốc độ fuzzing, chuyển từ afl-gcc sang afl-clang-fast và ghi nhận cải thiện đáng kể. Phân tích lý do.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-04 · Câu gốc 4

Một nhóm nghiên cứu bảo mật phân tích malware không rõ nguồn gốc bằng strace/ltrace thay vì biên dịch lại với instrumentation. Phân tích lý do lựa chọn này.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-05 · Câu gốc 5

Một tổ chức phát hiện một lỗi heap overflow nhỏ không gây crash ngay lập tức, chỉ được phát hiện nhờ kết hợp AFL với ASan. Phân tích giá trị của việc kết hợp.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-06 · Câu gốc 6

Một công ty ô tô cần fuzzing firmware nhúng không có khả năng biên dịch lại dễ dàng với AFL. Đề xuất công cụ binary instrumentation phù hợp.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-07 · Câu gốc 7

Một đội DevOps nhận thấy pipeline CI chạy fuzzing quá chậm do overhead instrumentation cao. Đề xuất cách cân bằng giữa tốc độ và độ phủ.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-08 · Câu gốc 8

Một tổ chức phát hiện Fork Server giúp giảm thời gian chạy fuzzing campaign từ 10 giờ xuống 3 giờ. Phân tích cơ chế mang lại cải thiện này.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-09 · Câu gốc 9

Một công ty startup dùng module Python đơn giản (không có shared memory bitmap) và chấp nhận tốc độ chậm hơn AFL để dễ bảo trì. Phân tích đánh đổi này.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-10 · Câu gốc 10

Một tổ chức bảo mật phát hiện một binary đóng gói (không có source) có lỗ hổng nghiêm trọng qua QEMU mode fuzzing. Phân tích quy trình đã áp dụng.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-11 · Câu gốc 11

Một công ty phần mềm phát hiện instrumentation của họ vô tình làm thay đổi hành vi timing của chương trình (che giấu race condition). Phân tích rủi ro Heisenbug này.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-12 · Câu gốc 12

Một nhóm phát triển IoT chọn compile-time instrumentation vì có toàn quyền truy cập source code nội bộ. Phân tích lý do lựa chọn hợp lý này.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-13 · Câu gốc 13

Một tổ chức nghiên cứu công bố rằng edge coverage giúp AFL tìm ra lỗi mà một fuzzer chỉ dùng line coverage bỏ sót. Phân tích ý nghĩa của kết quả này.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-14 · Câu gốc 14

Một công ty phát hiện việc dùng ltrace trên production server gây rò rỉ thông tin nhạy cảm trong log. Phân tích rủi ro và đề xuất kiểm soát truy cập.

**Trả lời gợi ý gốc:**



#### C4-4.3-thuc_te-15 · Câu gốc 15

Một đội an ninh mạng dùng strace để điều tra một tiến trình đáng ngờ mở kết nối mạng bất thường. Phân tích cách tracing hỗ trợ điều tra sự cố.

**Trả lời gợi ý gốc:**



## Mục 4.4: Sinh đường thực thi chương trình

### Tóm tắt kiến thức nguyên bản

Bài toán cốt lõi: input ngẫu nhiên hầu như không bao giờ khớp điều kiện phức tạp một cách tình cờ – cần chiến lược thông minh hơn random thuần túy. Mutation-based (AFL, module học phần): bắt đầu từ seed, biến đổi dần (flip byte, chèn/xóa). Generation-based (Peach Fuzzer): sinh input từ đầu theo grammar định dạng – phù hợp định dạng phức tạp (JSON/XML/protocol). Thuật toán Hill-Climbing: giữ lại mutation làm TĂNG coverage tích lũy, loại bỏ mutation không cải thiện – biến bài toán “đoán 4 byte cùng lúc” (O(2564 )) thành “đoán từng byte” (O(4 × 256)), giảm độ phức tạp từ hàm mũ xuống tuyến tính KHI mỗi byte độc lập mở coverage riêng (như check_magic). Symbolic Execution (+ Z3) GIẢI trực tiếp phương trình thay vì đoán – chậm hơn mỗi bước nhưng có thể “nhảy thẳng” tới lời giải. Với điều kiện PHI TUYẾN (checksum/hash), hill- climbing KHÔNG có lợi thế này. Kỹ thuật tăng tốc: Dictionary-based Mutation (-x dictionary.txt), Splice Mutation (kết hợp đầu seed A + cuối seed B), Havoc Mode (2–32 phép biến đổi liên tiếp ngẫu nhiên).

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C4-4.4-trac_nghiem-01 · Câu gốc 1

Thách thức cốt lõi khi sinh input mới cho target như check_magic() là gì?

**A.** Input ngẫu nhiên hầu như không bao giờ khớp điều kiện buf[i]==’F’/’U’/’Z’/’Z’ một cách tình cờ

**B.** Không có thách thức nào, random input luôn hiệu quả

**C.** Chương trình quá đơn giản để cần chiến lược gì

**D.** Chỉ cần tăng số lượng CPU là giải quyết được

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-02 · Câu gốc 2

Mutation-based fuzzing hoạt động theo nguyên lý nào?

**A.** Sinh input từ đầu dựa trên đặc tả định dạng (grammar)

**B.** Bắt đầu từ seed hợp lệ, biến đổi dần (bit flip, byte thay thế, chèn/xóa)

**C.** Không cần seed ban đầu

**D.** Chỉ áp dụng được cho định dạng JSON

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-03 · Câu gốc 3

Generation-based fuzzing hoạt động theo nguyên lý nào?

**A.** Biến đổi ngẫu nhiên từ seed có sẵn

**B.** Sinh input TỪ ĐẦU dựa trên đặc tả định dạng (grammar)

**C.** Không sinh input mới, chỉ tái sử dụng input cũ

**D.** Luôn chậm hơn mutation-based trong mọi trường hợp

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-04 · Câu gốc 4

Peach Fuzzer là ví dụ của chiến lược nào?

**A.** Mutation- based fuzzing

**B.** Generation-based (grammar-based) fuzzing

**C.** Model checking

**D.** Static analysis

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-05 · Câu gốc 5

Module coverage_guided_fuzz của học phần dùng chiến lược nào?

**A.** Generation-based

**B.** Mutation-based

**C.** Không dùng chiến lược nào cụ thể

**D.** Symbolic execution

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-06 · Câu gốc 6

Thuật toán Hill-Climbing giữ lại mutation nào trong corpus?

**A.** Chỉ giữ lại mutation NGẪU NHIÊN bất kỳ

**B.** Giữ lại mutation làm TĂNG coverage so với best_coverage hiện tại

**C.** Giữ lại mọi mutation không phân biệt

**D.** Không giữ lại gì, luôn bắt đầu lại từ đầu

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-07 · Câu gốc 7

Trong thuật toán hill-climbing, điều gì xảy ra ngay khi phát hiện crashed=True?

**A.** Tiếp tục vòng lặp cho tới hết max_iterations

**B.** Trả về ngay candidate gây crash (return candidate)

**C.** Bỏ qua candidate này và thử lại

**D.** Reset corpus về ban đầu

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-08 · Câu gốc 8

Vì sao Hill-Climbing hiệu quả với check_magic(): mỗi bước chỉ cần tìm đúng bao nhiêu byte tiếp theo?

**A.** Toàn bộ 4 byte cùng lúc

**B.** Chỉ 1 byte tiếp theo (xác suất 1/256 mỗi lần thử)

**C.** 8 byte cùng lúc

**D.** 0 byte, không cần tìm gì thêm

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-09 · Câu gốc 9

Symbolic Execution khác Hill-Climbing ở cách tiếp cận nào?

**A.** Thay vì đoán byte tiếp theo, symbolic execution GIẢI phương trình để tìm chính xác giá trị cần thiết

**B.** Cả hai đều đoán ngẫu nhiên giống hệt nhau

**C.** Symbolic execution không liên quan gì tới Ch.3

**D.** Symbolic execution luôn nhanh hơn hill-climbing trên mọi bước

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-10 · Câu gốc 10

Symbolic execution kết hợp với công cụ nào (đã học ở Ch.3.4) có thể giải trực tiếp ”FUZZ” trong một lần?

**A.** CBMC không cần Z3

**B.** Z3

**C.** gcov

**D.** AFL++

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-11 · Câu gốc 11

Đánh đổi của symbolic execution so với hill-climbing/random là gì?

**A.** Chậm hơn nhiều trên mỗi bước, nhưng có thể ”nhảy thẳng” tới lời giải

**B.** Luôn nhanh hơn về mọi mặt

**C.** Không có đánh đổi nào

**D.** Chỉ áp dụng được cho Java

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-12 · Câu gốc 12

Dictionary-based Mutation cung cấp gì cho fuzzer?

**A.** Danh sách token quan trọng (VD: magic number, từ khóa định dạng) thay vì chỉ random byte

**B.** Một cuốn từ điển tiếng Anh

**C.** Danh sách các lỗi đã biết

**D.** Không có tác dụng gì

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-13 · Câu gốc 13

AFL hỗ trợ cờ nào để cung cấp dictionary cho fuzzer?

**A.** -d dictionary.txt

**B.** -x dictionary.txt

**C.** –dict=dictionary.txt

**D.** -D dict.txt

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-14 · Câu gốc 14

Splice Mutation kết hợp điều gì?

**A.** Kết hợp phần ĐẦU của seed A với phần SAU của seed

**B.** B. Xóa hoàn toàn một seed

**C.** Nhân đôi một seed

**D.** Không liên quan tới seed nào

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.4-trac_nghiem-15 · Câu gốc 15

Splice mutation có thể tạo ra input khám phá được gì mà mỗi seed riêng lẻ chưa đạt tới?

**A.** Không có gì đặc biệt

**B.** Tổ hợp nhánh (combination of branches) mới

**C.** Chỉ tạo ra input trùng lặp

**D.** Làm giảm coverage

**Đáp án gốc:** B

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C4-4.4-ly_thuyet-01 · Câu gốc 1

Trình bày bài toán ’sinh đường thực thi mới’ trong fuzzing và giải thích vì sao input ngẫu nhiên thuần túy không hiệu quả.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-02 · Câu gốc 2

Ôn lại Symbolic Execution và Concolic Testing từ Ch.3.3 và giải thích vai trò của chúng trong sinh đường dẫn ở Ch.4.4.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-03 · Câu gốc 3

So sánh Mutation-based và Generation-based fuzzing, cho ví dụ công cụ/module tương ứng mỗi loại.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-04 · Câu gốc 4

Trình bày chi tiết thuật toán Hill-Climbing đã cài đặt trong coverage_guided_fuzz, giải thích từng bước.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-05 · Câu gốc 5

Giải thích vì sao Hill-Climbing biến bài toán ’đoán 4 byte cùng lúc’ thành ’đoán từng byte’, và lợi ích về mặt xác suất.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-06 · Câu gốc 6

Trình bày cách Symbolic Execution (kết hợp Z3) có thể giải trực tiếp giá trị ’FUZZ’ trong một lần thay vì đoán mò từng bước.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-07 · Câu gốc 7

Bàn luận đánh đổi giữa Symbolic Execution (chậm mỗi bước, ít bước) và Hill-Climbing (nhanh mỗi bước, nhiều bước).

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-08 · Câu gốc 8

Giải thích khái niệm Dictionary-based Mutation và cách nó tăng tốc quá trình fuzzing khi biết trước các token quan trọng.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-09 · Câu gốc 9

Trình bày cơ chế Splice Mutation và giải thích vì sao nó có thể khám phá tổ hợp nhánh mà từng seed riêng lẻ chưa đạt tới.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-10 · Câu gốc 10

Giải thích Havoc Mode của AFL và so sánh với hai loại mutation đơn giản (flip 1 byte / thêm 1 byte) của module học phần.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-11 · Câu gốc 11

Trình bày ước lượng lý thuyết số lần thử của Random thuần túy so với Hill-Climbing cho magic 16-byte, giải thích ý nghĩa thực tiễn.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-12 · Câu gốc 12

Bàn luận điều kiện để ước lượng hill-climbing (16×256) đúng, và trường hợp nó KHÔNG còn đúng (điều kiện phi tuyến).

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-13 · Câu gốc 13

Giải thích vì sao hill-climbing không có lợi thế với điều kiện phi tuyến như checksum/hash, dự đoán điều gì xảy ra khi áp dụng cho check_checksum.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-14 · Câu gốc 14

Dự đoán điều gì xảy ra với số iterations cần thiết nếu sửa coverage_guided_fuzz để mutation thay thế 2 byte cùng lúc thay vì 1 byte.

**Trả lời gợi ý gốc:**



#### C4-4.4-ly_thuyet-15 · Câu gốc 15

Trình bày vai trò của biến best_coverage trong thuật toán hill-climbing và cách nó quyết định việc giữ lại hay loại bỏ một mutation.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C4-4.4-thuc_hanh-01 · Câu gốc 1

Sửa coverage_guided_fuzz để dùng mutation ’thay thế 2 byte cùng lúc’ thay vì 1 byte, chạy thử và ghi lại số iterations cần thiết.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-02 · Câu gốc 2

Với target có magic string dài hơn (16 byte), ước lượng theo lý thuyết xác suất số iterations trung bình hill-climbing cần, so với random thuần túy.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-03 · Câu gốc 3

````text
Viết hàm Python splice_mutate(seed_a, seed_b) hoàn chỉnh và test với

```
seed mẫu.
```
````

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-04 · Câu gốc 4

Cài đặt thêm chiến lược ’xóa 1 byte’ vào coverage_guided_fuzz (ngoài flip và thêm byte hiện có), chạy thử và so sánh kết quả.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-05 · Câu gốc 5

Thiết kế một dictionary 5 token cho một định dạng file XML đơn giản, giải thích lý do chọn từng token.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-06 · Câu gốc 6

Viết bảng so sánh (theo lý thuyết) số lần thử kỳ vọng cho magic string độ dài 4, 8, 16 byte với cả random và hill-climbing.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-07 · Câu gốc 7

Cài đặt target check_checksum (từ tài liệu Ch.4.6) và thử chạy coverage_guided_fu ghi lại xem có tìm ra crash trong 5000 lần thử không.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-08 · Câu gốc 8

Thiết kế thuật toán giả (pseudocode) kết hợp cả hill-climbing VÀ splice mutation trong cùng một vòng lặp.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-09 · Câu gốc 9

Viết một mini-experiment: chạy coverage_guided_fuzz với 5 seed ngẫu nhiên khác nhau (1,2,3,7,42), tính trung bình số iterations.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-10 · Câu gốc 10

Thiết kế bảng phân loại 5 target C giả định theo mức độ phù hợp với mutation-based fuzzing (dễ/trung bình/khó).

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-11 · Câu gốc 11

Viết đoạn code Python mô phỏng Havoc Mode đơn giản: áp dụng 2-5 phép biến đổi ngẫu nhiên liên tiếp lên một input.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-12 · Câu gốc 12

Cho một hàm C với điều kiện lồng nhau 3 cấp, dự đoán hill-climbing có dễ tìm ra input kích hoạt crash hay không, giải thích.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-13 · Câu gốc 13

Thiết kế một seed corpus đa dạng (5 seed khác nhau về độ dài và nội dung) cho một target xử lý header giao thức mạng.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-14 · Câu gốc 14

Viết báo cáo so sánh thời gian chạy thực tế giữa mutation-based fuzzing đơn giản và mutation-based có dictionary hỗ trợ.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_hanh-15 · Câu gốc 15

Cài đặt một phiên bản coverage_guided_fuzz dùng generation-based (sinh input theo grammar đơn giản: 4 ký tự chữ cái in hoa).

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C4-4.4-thuc_te-01 · Câu gốc 1

Một công ty phát hiện fuzzer của họ ’mắc kẹt’ không tìm ra lỗi trong một module kiểm tra checksum suốt nhiều tuần. Phân tích nguyên nhân và đề xuất giải pháp.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-02 · Câu gốc 2

Một đội bảo mật quyết định bổ sung dictionary chứa các magic number phổ biến của định dạng file ảnh để tăng tốc fuzzing. Phân tích lợi ích của quyết định này.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-03 · Câu gốc 3

Một tổ chức nghiên cứu áp dụng Hybrid Fuzzing (kết hợp coverage- guided với concolic execution) để vượt qua điều kiện checksum phức tạp. Phân tích cách tiếp cận này.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-04 · Câu gốc 4

Một công ty phát triển parser cho một giao thức mạng tùy chỉnh, chọn Generation-based Fuzzing (Peach Fuzzer) thay vì Mutation-based. Phân tích lý do lựa chọn.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-05 · Câu gốc 5

Một nhóm phát triển phát hiện thêm splice mutation vào fuzzer giúp tìm ra một lớp lỗi mới mà trước đó chưa từng phát hiện. Phân tích cơ chế mang lại kết quả này.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-06 · Câu gốc 6

Một công ty an ninh mạng sử dụng Z3 (kết hợp Ch.3.4) để giải trực tiếp một điều kiện magic number phức tạp thay vì chờ hill-climbing dò dẫm. Phân tích hiệu quả của cách tiếp cận.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-07 · Câu gốc 7

Một tổ chức phát hiện rằng fuzzer của họ tìm crash rất nhanh trên module A (điều kiện tuyến tính) nhưng gần như không tìm ra gì trên module B (điều kiện checksum). Phân tích nguyên nhân khác biệt.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-08 · Câu gốc 8

Một dự án mã nguồn mở áp dụng Havoc Mode của AFL và ghi nhận tăng đáng kể số lỗi phát hiện so với chỉ dùng flip 1 byte đơn giản. Phân tích lý do cải thiện.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-09 · Câu gốc 9

Một công ty startup không đủ nguồn lực triển khai symbolic execution phức tạp, chấp nhận hill-climbing đơn giản dù chậm hơn với một số target. Phân tích đánh đổi.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-10 · Câu gốc 10

Một tổ chức nghiên cứu công bố Driller (Hybrid Fuzzing) giúp vượt qua các checkpoint mà fuzzing thuần túy không vượt qua được. Phân tích ý tưởng cốt lõi của phương pháp này.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-11 · Câu gốc 11

Một công ty phát triển game phát hiện input magic 16-byte trong file save game khiến black-box fuzzing hoàn toàn bất khả thi. Đề xuất chuyển sang coverage-guided hoặc symbolic execution.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-12 · Câu gốc 12

Một đội ngũ kỹ sư bảo mật tranh luận liệu nên đầu tư xây dựng dictionary chuyên biệt cho từng target hay dùng dictionary chung. Phân tích ưu nhược điểm mỗi phương án.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-13 · Câu gốc 13

Một tổ chức phát hiện rằng splice mutation giữa 2 seed từ 2 module khác nhau vô tình tạo ra input khai thác được lỗ hổng liên module. Phân tích ý nghĩa của phát hiện này.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-14 · Câu gốc 14

Một công ty tài chính dùng symbolic execution cho module xác thực checksum giao dịch (nơi hill-climbing thất bại) nhưng vẫn dùng coverage- guided cho phần còn lại. Phân tích chiến lược kết hợp.

**Trả lời gợi ý gốc:**



#### C4-4.4-thuc_te-15 · Câu gốc 15

Một nhóm nghiên cứu ML đề xuất dùng mô hình học máy để dự đoán mutation nào có khả năng tăng coverage cao, thay vì chọn ngẫu nhiên như hill-climbing truyền thống. Phân tích tiềm năng của hướng đi này.

**Trả lời gợi ý gốc:**



## Mục 4.5: Kiểm thử hộp đen (Black-box Fuzzing)

### Tóm tắt kiến thức nguyên bản

Black-box Fuzzing: sinh input KHÔNG dùng bất kỳ thông tin nội bộ nào (mã nguồn, coverage, luồng thực thi) – chỉ quan sát output/hành vi bên ngoài. Ưu điểm: đơn giản, áp dụng cho MỌI target kể cả không có source. Nhược điểm: không có “la bàn” – hiệu quả phụ thuộc hoàn toàn may rủi. Thực nghiệm THẬT trên fuzz_target.c: 20.000 lần thử ngẫu nhiên KHÔNG tìm ra crash (39.9s) – xác suất khớp “FUZZ” (4 byte) mỗi lần chỉ 1/2564 ≈ 1/4.3 tỷ. Với magic 2-byte, xác suất mỗi lần 1/65536, kỳ vọng 65.536 lần thử – HOÀN TOÀN khả thi, minh họa tác động CẤP SỐ NHÂN của độ dài magic value. Black-box vẫn hiệu quả với lỗi “nông” (shallow bugs: crash khi input rỗng/quá dài), chi phí triển khai thấp, thường dùng làm “sanity check” trước khi đầu tư coverage-guided phức tạp hơn. Công cụ: zzuf (nhiễu file), Radamsa (mutation thông minh hơn), Burp Suite Intruder (web/HTTP), boofuzz (giao thức mạng). Seed đa dạng vẫn quan trọng dù không dùng feedback.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C4-4.5-trac_nghiem-01 · Câu gốc 1

Định nghĩa Black-box Fuzzing là gì?

**A.** Sinh input dựa trên coverage feedback từ chương trình

**B.** Sinh input để thử nghiệm chương trình MÀ KHÔNG dùng bất kỳ thông tin nào về cấu trúc bên trong

**C.** Chỉ áp dụng được khi có source code

**D.** Luôn nhanh hơn white-box fuzzing

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-02 · Câu gốc 2

Black-box fuzzing chỉ quan sát điều gì từ target?

**A.** Mã nguồn và cấu trúc bên trong

**B.** Output/hành vi bên ngoài (crash, mã lỗi, thời gian phản hồi)

**C.** Coverage tích lũy

**D.** Luồng thực thi chi tiết

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-03 · Câu gốc 3

Ưu điểm chính của Black-box Fuzzing là gì?

**A.** Luôn tìm ra lỗi nhanh nhất

**B.** Đơn giản, áp dụng được cho MỌI loại target kể cả không có source

**C.** Cần source code để hoạt động

**D.** Chỉ áp dụng cho web application

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-04 · Câu gốc 4

Nhược điểm chính của Black-box Fuzzing là gì? A. Không có ’la bàn’ – hiệu quả phụ thuộc hoàn toàn vào may rủi. B. Cần biên dịch lại chương trình. C. Chỉ áp dụng được cho C. D. Quá phức tạp để cài đặt.

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-05 · Câu gốc 5

Trong hàm black_box_fuzz(), input candidate được sinh ra như thế nào?

**A.** Dựa trên coverage của lần thử trước

**B.** bytes(random.randint(0, 255) for _ in range(input_len)) – hoàn toàn ngẫu nhiên

**C.** Sao chép từ file mẫu có sẵn

**D.** Dùng grammar định dạng JSON

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-06 · Câu gốc 6

Returncode âm (VD: -11) trong hàm _run_target nghĩa là gì?

**A.** Chương trình chạy thành công

**B.** Chương trình bị kill bởi signal (VD: SIGSEGV) – tức là đã crash

**C.** Chương trình timeout

**D.** Không có ý nghĩa gì đặc biệt

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-07 · Câu gốc 7

Kết quả thực nghiệm chạy black_box_fuzz(binary, max_iterations=20000, seed=1) trên fuzz_target.c là gì?

**A.** Crashed: True sau vài lần thử

**B.** Crashed: False sau 20000 lần thử, mất 39.9 giây

**C.** Crashed: True ngay lần thử đầu tiên

**D.** Chương trình bị lỗi biên dịch

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-08 · Câu gốc 8

Xác suất khớp CHÍNH XÁC ’FUZZ’ (4 byte) ở mỗi lần thử ngẫu nhiên là bao nhiêu?

**A.** 1/256

**B.** 1/(256^4) = 1/4,294,967,296

**C.** 1/1000

**D.** 50%

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-09 · Câu gốc 9

Với 20.000 lần thử, xác suất tìm ra ’FUZZ’ bằng black-box thuần túy là khoảng bao nhiêu?

**A.** Khoảng 50%

**B.** Khoảng 0.0000047% – gần như không thể trong thời gian hợp lý

**C.** 100%, luôn tìm ra

**D.** Khoảng 10%

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-10 · Câu gốc 10

Black-box fuzzing hiệu quả nhất với loại lỗi nào?

**A.** Lỗi ’nông’ (shallow bugs) không cần khớp điều kiện phức tạp (VD: crash khi input rỗng/quá dài)

**B.** Lỗi checksum/hash phức tạp

**C.** Lỗi magic number 4- byte chính xác

**D.** Lỗi logic nghiệp vụ phức tạp

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-11 · Câu gốc 11

Black-box fuzzing KHÔNG yêu cầu điều gì mà white-box fuzzing yêu cầu?

**A.** Không yêu cầu source code hay khả năng biên dịch lại với instrumentation

**B.** Không yêu cầu bất kỳ input nào

**C.** Không yêu cầu máy tính để chạy

**D.** Không có sự khác biệt về yêu cầu

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-12 · Câu gốc 12

Black-box fuzzing thường đóng vai trò gì trước khi đầu tư vào coverage-guided fuzzing?

**A.** Bước ’sanity check’ đầu tiên

**B.** Bước cuối cùng trong pipeline

**C.** Không có vai trò gì đặc biệt

**D.** Thay thế hoàn toàn cho coverage-guided fuzzing

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-13 · Câu gốc 13

zzuf là công cụ dùng để làm gì? A. Fuzzing nhanh bằng cách ’nhiễu’ (bit-flip ngẫu nhiên) file input có sẵn. B. Đo code coverage. C. Biên dịch chương trình C. D. Quản lý phiên bản mã nguồn.

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-14 · Câu gốc 14

Radamsa khác zzuf ở điểm nào?

**A.** Radamsa sinh mutation thông minh hơn zzuf, dùng nhiều trong test giao thức

**B.** Radamsa và zzuf giống hệt nhau

**C.** Radamsa chỉ dùng cho Windows

**D.** zzuf mạnh hơn Radamsa trong mọi trường hợp

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.5-trac_nghiem-15 · Câu gốc 15

Burp Suite Intruder dùng cho mục đích gì?

**A.** Black-box fuzzing cho web application (tham số HTTP)

**B.** Đo coverage cho code

**C.** C. Biên dịch chương trình Java

**D.** Quản lý dependency

**Đáp án gốc:** A

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C4-4.5-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa Black-box Fuzzing và giải thích vì sao nó không dùng bất kỳ thông tin nội bộ nào của chương trình.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-02 · Câu gốc 2

Giải thích ưu và nhược điểm của Black-box Fuzzing so với các kỹ thuật khác đã học trong chương.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-03 · Câu gốc 3

Trình bày chi tiết hàm black_box_fuzz() và giải thích cách nó sinh input hoàn toàn ngẫu nhiên không có feedback.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-04 · Câu gốc 4

Giải thích kết quả thực nghiệm THẬT: black_box_fuzz thất bại sau 20.000 lần thử trên fuzz_target.c, phân tích bằng xác suất.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-05 · Câu gốc 5

Tính và giải thích ý nghĩa xác suất 1/256^4 khi tìm ’FUZZ’ bằng black- box fuzzing thuần túy.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-06 · Câu gốc 6

Bàn luận: vì sao Black-box Fuzzing vẫn được dùng rộng rãi trong thực tế dù có hạn chế rõ rệt với input dài.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-07 · Câu gốc 7

Trình bày các công cụ Black-box Fuzzing phổ biến (zzuf, Radamsa, Burp Suite Intruder, boofuzz) và mục đích sử dụng mỗi công cụ.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-08 · Câu gốc 8

Giải thích cách zzuf thực hiện fuzzing cho định dạng file mà không cần hiểu cấu trúc định dạng đó.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-09 · Câu gốc 9

Trình bày cách Black-box Fuzzing áp dụng cho Web API: loại request nào được gửi và dấu hiệu bất thường nào được quan sát.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-10 · Câu gốc 10

Phân biệt Random Testing truyền thống và Fuzzing (bảo mật) về mục tiêu và loại input được sử dụng.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-11 · Câu gốc 11

Giải thích tầm quan trọng của Seed Selection ngay cả với Black-box Fuzzing, dù về lý thuyết nó không dùng feedback.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-12 · Câu gốc 12

Trình bày lời giải bài tập: giải thích tại sao input_len=2 cho kết quả khả thi hoàn toàn khác với input_len=4.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-13 · Câu gốc 13

Bàn luận tác động cấp số nhân của độ dài magic value lên độ khó của Black-box Fuzzing, minh họa bằng con số cụ thể.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-14 · Câu gốc 14

Giải thích vì sao Black-box Fuzzing vẫn hiệu quả với lỗi ’crash khi input rỗng’ dù thất bại với check_magic.

**Trả lời gợi ý gốc:**



#### C4-4.5-ly_thuyet-15 · Câu gốc 15

Trình bày các tình huống thực tế mà Black-box Fuzzing là lựa chọn phù hợp hơn White-box Fuzzing.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C4-4.5-thuc_hanh-01 · Câu gốc 1

Chạy black_box_fuzz với input_len=2 thay vì 4 (sửa target để magic chỉ còn 2 byte) – so sánh số iterations trung bình với lý thuyết xác suất.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-02 · Câu gốc 2

Giải thích tại sao Black-box fuzzing vẫn hiệu quả để tìm lỗi ’crash khi input rỗng’ dù không hiệu quả với check_magic.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-03 · Câu gốc 3

Viết một target C đơn giản crash khi input rỗng, chạy black_box_fuzz và ghi lại số iterations cần thiết để tìm ra.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-04 · Câu gốc 4

Cài đặt zzuf (nếu có trong môi trường) và fuzz một file ảnh PNG mẫu, quan sát kết quả.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-05 · Câu gốc 5

Viết một black-box fuzzer đơn giản cho một API HTTP giả định (mô tả các bước, gửi request với tham số biến đổi ngẫu nhiên).

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-06 · Câu gốc 6

Thiết kế 5 test case black-box cho một form đăng ký gồm trường tên, email, mật khẩu.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-07 · Câu gốc 7

Chạy lại black_box_fuzz với 5 seed khác nhau (1,2,3,7,42) trên fuzz_target.c với max_iterations=20000, ghi lại kết quả từng lần.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-08 · Câu gốc 8

Viết báo cáo so sánh chi phí triển khai giữa zzuf và một fuzzer Python tự viết cho cùng mục đích.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-09 · Câu gốc 9

Thiết kế checklist 5 mục đánh giá xem một target có phù hợp để bắt đầu với Black-box Fuzzing hay không.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-10 · Câu gốc 10

Viết đoạn giải thích 100 từ cho quản lý dự án về lý do nên chạy Black-box Fuzzing như bước sanity-check đầu tiên.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-11 · Câu gốc 11

Cho một API đăng nhập, thiết kế 5 payload black-box điển hình (SQL injection, giá trị rỗng, chuỗi rất dài, ký tự đặc biệt, Unicode).

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-12 · Câu gốc 12

Viết pseudocode cho một black-box fuzzer test giao thức mạng đơn giản (gửi packet ngẫu nhiên tới cổng TCP).

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-13 · Câu gốc 13

Tính xác suất lý thuyết tìm ra magic string 3-byte bằng black-box fuzzing, so sánh với kết quả 2-byte và 4-byte đã học.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-14 · Câu gốc 14

Thiết kế bảng so sánh 4 công cụ black-box (zzuf, Radamsa, Burp Suite Intruder, boofuzz) theo tiêu chí: lĩnh vực áp dụng, độ phức tạp cài đặt.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_hanh-15 · Câu gốc 15

Viết một script Python đơn giản gửi 100 request HTTP GET với tham số query ngẫu nhiên tới một endpoint giả định, ghi lại mã trạng thái trả về.

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C4-4.5-thuc_te-01 · Câu gốc 1

Một công ty bảo mật được thuê kiểm thử một API không có tài liệu kỹ thuật, buộc phải dùng Black-box Fuzzing. Phân tích quy trình họ có thể áp dụng.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-02 · Câu gốc 2

Một tổ chức phát hiện Black-box Fuzzing tìm ra lỗi ’crash khi input rỗng’ trong 5 phút nhưng không tìm ra lỗi magic-number sau nhiều giờ. Phân tích nguyên nhân dựa trên lý thuyết xác suất.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-03 · Câu gốc 3

Một công ty startup dùng zzuf để fuzz một trình xem ảnh của bên thứ ba (không có source) và phát hiện một lỗ hổng crash nghiêm trọng. Phân tích giá trị của Black-box Fuzzing trong trường hợp này.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-04 · Câu gốc 4

Một đội bảo mật web dùng Burp Suite Intruder để test tham số HTTP của một ứng dụng ngân hàng, phát hiện lỗi SQL injection. Phân tích quy trình đã áp dụng.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-05 · Câu gốc 5

Một tổ chức tranh luận liệu Black-box Fuzzing có còn cần thiết khi họ đã đầu tư đầy đủ vào Coverage-guided Fuzzing (Ch.4.6). Phân tích và đưa ra quan điểm.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-06 · Câu gốc 6

Một công ty phát hiện rằng Black-box Fuzzing 20.000 lần thử không tìm ra lỗi trong module xác thực magic number 8-byte của họ. Đề xuất chuyển hướng sang kỹ thuật khác.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-07 · Câu gốc 7

Một nhóm phát triển game dùng boofuzz để test giao thức mạng multiplayer tùy chỉnh và phát hiện một lỗi denial-of-service. Phân tích vai trò của black-box trong phát hiện này.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-08 · Câu gốc 8

Một tổ chức chính phủ yêu cầu mọi phần mềm mua từ bên thứ ba phải qua Black-box Fuzzing tối thiểu trước khi triển khai (do không có source code). Phân tích tính hợp lý của chính sách này.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-09 · Câu gốc 9

Một công ty phần mềm nhúng chỉ có quyền truy cập vào binary đã đóng gói của module bên thứ ba, buộc dùng black-box fuzzing thay vì coverage- guided. Phân tích giới hạn kỳ vọng của cách tiếp cận này.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-10 · Câu gốc 10

Một tổ chức bảo mật phát hiện rằng Radamsa hiệu quả hơn zzuf trong việc phát hiện lỗi trên một parser giao thức phức tạp. Phân tích lý do có thể dẫn tới khác biệt này.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-11 · Câu gốc 11

Một công ty startup vừa ra mắt sản phẩm quyết định chạy Black-box Fuzzing như bước sanity-check trước khi đầu tư vào hạ tầng fuzzing phức tạp hơn. Phân tích quyết định này.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-12 · Câu gốc 12

Một tổ chức phát hiện lỗ hổng nghiêm trọng trong một thư viện mã đóng nguồn (closed-source) chỉ qua quan sát crash bên ngoài, không có source code. Phân tích đây là ví dụ điển hình của kỹ thuật nào.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-13 · Câu gốc 13

Một công ty tài chính lo ngại về chi phí pháp lý khi black-box fuzzing một API công khai của đối tác mà không xin phép trước. Phân tích rủi ro và đề xuất quy trình phù hợp.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-14 · Câu gốc 14

Một đội DevOps tích hợp zzuf vào pipeline CI để tự động fuzz mọi file input mẫu trước khi release. Phân tích lợi ích của việc tự động hóa này.

**Trả lời gợi ý gốc:**



#### C4-4.5-thuc_te-15 · Câu gốc 15

Một tổ chức phát hiện rằng black-box fuzzing một module xử lý ảnh JPEG tìm ra 3 lỗi crash trong tuần đầu tiên nhờ seed đa dạng ban đầu. Phân tích vai trò của seed selection.

**Trả lời gợi ý gốc:**



## Mục 4.6: Kiểm thử hộp trắng (White-box Fuzzing)

### Tóm tắt kiến thức nguyên bản

White-box (Coverage-guided) Fuzzing: sinh input dựa trên THÔNG TIN NỘI BỘ (coverage từ gcov) để hướng dẫn mutation tiếp theo – chính là coverage_guided_fuzz đã cài đặt ở Mục 4.4. Thực nghiệm THẬT: tìm ra crash (“FUZZ”) chỉ sau 2.475 lần thử (9.3s), so với Black-box thất bại sau 20.000 lần – nhanh hơn ít nhất 8 lần và tìm được lỗi mà black-box hoàn toàn bất lực. AFL++ (edge coverage) và libFuzzer (chạy in-process, nhanh hơn AFL vì không fork mỗi lần) là hiện thực công nghiệp; OSS-Fuzz (Google) chạy liên tục trên hàng nghìn dự án, tìm hàng chục nghìn lỗi. Hạn chế: cần source code; có thể “mắc kẹt” với điều kiện PHI TUYẾN (VD: check_checksum với sum==buf[3]*100) – coverage KHÔNG tăng dần theo từng byte, suy biến gần giống black-box ngẫu nhiên – cần kết hợp Symbolic/Concolic Execution. Thực hành: Corpus Minimization (afl-cmin), Crash Triage (nhóm theo nguyên nhân gốc), Regression Testing (thêm input gây crash vào bộ test), Continuous Fuzzing trong CI/CD (ngắn mỗi commit, dài định kỳ). Chiến lược tổng thể: module lõi nhỏ tới hạn → CBMC; ứng dụng lớn → Fuzzing liên tục; codebase mới → Fuzzing trước, CBMC sau cho module rủi ro cao. Bài học toàn học phần: không MỘT kỹ thuật đơn lẻ nào đủ – luôn cần KẾT HỢP.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C4-4.6-trac_nghiem-01 · Câu gốc 1

Định nghĩa White-box Fuzzing (Coverage-guided Fuzzing) là gì?

**A.** Sinh input hoàn toàn ngẫu nhiên không dùng feedback

**B.** Sinh input dựa trên THÔNG TIN NỘI BỘ của chương trình (coverage, cấu trúc mã, symbolic execution) để hướng dẫn mutation

**C.** Chỉ áp dụng được cho phần mềm đóng gói

**D.** Không liên quan gì tới coverage

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-02 · Câu gốc 2

coverage_guided_fuzz dùng thông tin gì từ gcov (Ch.4.2) làm tín hiệu ’phần thưởng’?

**A.** Thời gian biên dịch

**B.** % coverage

**C.** Số dòng code

**D.** Tên hàm được gọi

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-03 · Câu gốc 3

Kết quả thực nghiệm coverage_guided_fuzz trên fuzz_target.c là gì?

**A.** Crashed: False sau 20000 lần thử

**B.** Crashed: True, Iterations: 2475, input ’FUZZ’, time: 9.3s

**C.** Crashed: True ngay lần thử đầu tiên

**D.** Không crash trong bất kỳ trường hợp nào

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-04 · Câu gốc 4

So với Black-box (20.000 lần, không thành công), White-box nhanh hơn về SỐ ITERATIONS như thế nào?

**A.** Chậm hơn nhiều

**B.** Nhanh hơn ít nhất 8 lần và tìm ra được lỗi mà black-box hoàn toàn bất lực

**C.** Bằng nhau về số iterations

**D.** Chỉ nhanh hơn 10%

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-05 · Câu gốc 5

Coverage feedback biến bài toán O(256^4) thành bài toán độ phức tạp nào trong trường hợp tốt?

**A.** O(256^4) không đổi

**B.** O(4×256) – giảm từ hàm mũ xuống tuyến tính

**C.** O(1), giải quyết ngay lập tức

**D.** O(256^8), tăng lên

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-06 · Câu gốc 6

AFL++ dùng loại coverage nào (đã học ở Ch.4.3)?

**A.** Line coverage như gcov

**B.** Edge coverage

**C.** Không dùng coverage nào

**D.** Path coverage đầy đủ

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-07 · Câu gốc 7

libFuzzer khác AFL ở điểm nào về cách thực thi?

**A.** libFuzzer chạy IN-PROCESS (nhanh hơn, không cần fork mỗi lần); AFL fork mỗi lần

**B.** Không có khác biệt nào

**C.** AFL chạy in-process còn libFuzzer thì không

**D.** libFuzzer chỉ dùng được cho Python

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-08 · Câu gốc 8

OSS-Fuzz (Google) làm gì?

**A.** Chạy AFL++/libFuzzer liên tục trên hàng nghìn dự án mã nguồn mở, đã tìm ra hàng chục nghìn lỗi

**B.** Chỉ là một công cụ biên dịch

**C.** Là một ngôn ngữ lập trình mới

**D.** Chỉ dùng nội bộ tại Google, không công khai

**Đáp án gốc:** A

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-09 · Câu gốc 9

Hạn chế chính của White-box/Coverage-guided Fuzzing là gì?

**A.** Không có hạn chế nào

**B.** Cần source code; có thể mắc kẹt ở local optimum với điều kiện phi tuyến (checksum/hash)

**C.** Chỉ áp dụng được cho C++

**D.** Luôn chậm hơn Black-box Fuzzing

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-10 · Câu gốc 10

Trong ví dụ check_checksum(), điều kiện sum == buf[3]*100 có đặc điểm gì khiến coverage-guided khó xử lý?

**A.** Điều kiện tuyến tính từng byte như check_magic

**B.** Điều kiện phi tuyến, không ’mở dần’ qua từng byte đúng riêng lẻ

**C.** Điều kiện luôn đúng

**D.** Điều kiện chỉ phụ thuộc 1 byte duy nhất

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-11 · Câu gốc 11

Khi coverage-guided fuzzing gặp điều kiện phi tuyến như checksum, cần kết hợp với kỹ thuật nào?

**A.** Chỉ cần tăng số CPU

**B.** Symbolic/Concolic Execution (Ch.3.3, Ch.4.4) để ’giải’ trực tiếp thay vì đoán mò

**C.** Không có giải pháp nào

**D.** Chỉ cần đổi ngôn ngữ lập trình

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-12 · Câu gốc 12

libFuzzer harness (LLVMFuzzerTestOneInput) dùng để làm gì?

**A.** Biên dịch chương trình

**B.** Gọi trực tiếp hàm cần fuzz IN-PROCESS với input do libFuzzer sinh ra

**C.** Đo thời gian chạy chương trình

**D.** Quản lý bộ nhớ heap

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-13 · Câu gốc 13

Corpus Minimization dùng để làm gì?

**A.** Tăng kích thước corpus lên tối đa

**B.** Loại bỏ input THỪA không đóng góp coverage riêng biệt, giữ tập nhỏ nhất vẫn bao phủ coverage đã đạt

**C.** Mã hóa corpus để bảo mật

**D.** Không có tác dụng thực tế

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-14 · Câu gốc 14

Lệnh afl-cmin dùng để làm gì?

**A.** Biên dịch chương trình với AFL

**B.** Thực hiện Corpus Minimization

**C.** Chạy fuzzing chính

**D.** Đo coverage bằng gcov

**Đáp án gốc:** B

**Giải thích gốc:**



#### C4-4.6-trac_nghiem-15 · Câu gốc 15

Crash Triage là quá trình gì?

**A.** Xóa toàn bộ crash tìm được

**B.** Nhóm các crash theo stack trace/nguyên nhân gốc, ưu tiên xử lý theo mức độ nghiêm trọng

**C.** Tăng tốc độ fuzzing

**D.** Biên dịch lại chương trình sau mỗi crash

**Đáp án gốc:** B

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C4-4.6-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa White-box Fuzzing (Coverage-guided Fuzzing) và vai trò của coverage feedback trong việc hướng dẫn mutation.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-02 · Câu gốc 2

Nhắc lại thuật toán coverage_guided_fuzz đã học ở Mục 4.4, giải thích ý nghĩa từng dòng.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-03 · Câu gốc 3

Trình bày và phân tích kết quả thực nghiệm THẬT: White-box Fuzzing tìm crash sau 2475 lần thử, so với Black-box thất bại sau 20.000 lần.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-04 · Câu gốc 4

Giải thích bản chất toán học vì sao coverage feedback biến bài toán O(256^4) thành O(4×256) trong trường hợp tốt.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-05 · Câu gốc 5

Trình bày AFL++ và libFuzzer là hiện thực công nghiệp của nguyên lý coverage-guided fuzzing, so sánh đặc điểm mỗi công cụ.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-06 · Câu gốc 6

Giải thích vì sao libFuzzer chạy in-process nhanh hơn AFL (vốn fork mỗi lần chạy).

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-07 · Câu gốc 7

Trình bày vai trò của OSS-Fuzz trong việc phát hiện hàng chục nghìn lỗi trên các dự án mã nguồn mở.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-08 · Câu gốc 8

Giải thích hạn chế của White-box/Coverage-guided Fuzzing: cần source code và có thể mắc kẹt ở local optimum.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-09 · Câu gốc 9

Trình bày ví dụ check_checksum() và giải thích vì sao điều kiện phi tuyến khiến coverage-guided fuzzing thất bại.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-10 · Câu gốc 10

Giải thích lời giải bài tập: vì sao coverage KHÔNG tăng dần theo từng byte đúng riêng lẻ với check_checksum.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-11 · Câu gốc 11

Bàn luận giải pháp khi coverage-guided fuzzing thất bại trước điều kiện phi tuyến: kết hợp với Symbolic/Concolic Execution.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-12 · Câu gốc 12

Trình bày cấu trúc một libFuzzer harness (LLVMFuzzerTestOneInput) và giải thích cách nó gọi trực tiếp hàm cần fuzz.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-13 · Câu gốc 13

Giải thích khái niệm Corpus Minimization và lợi ích của việc loại bỏ input thừa không đóng góp coverage riêng biệt.

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-14 · Câu gốc 14

Trình bày quy trình Crash Triage: nhóm crash theo nguyên nhân gốc và ưu tiên xử lý theo mức độ nghiêm trọng (liên hệ CVSS, Ch.1.1).

**Trả lời gợi ý gốc:**



#### C4-4.6-ly_thuyet-15 · Câu gốc 15

Bàn luận chiến lược kết hợp Fuzzing với CBMC (Ch.3.5) tùy theo đặc điểm module (lõi nhỏ tới hạn vs. ứng dụng lớn).

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C4-4.6-thuc_hanh-01 · Câu gốc 1

Chạy lại coverage_guided_fuzz với seed khác (2, 3, 7), ghi nhận số iterations cần thiết mỗi lần, tính trung bình.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-02 · Câu gốc 2

Cài đặt target check_checksum, thử chạy coverage_guided_fuzz, xác nhận nó khó tìm crash hơn nhiều so với check_magic.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-03 · Câu gốc 3

Dùng Z3 (Ch.3.4) viết công thức giải trực tiếp check_checksum, so sánh tốc độ với coverage-guided fuzzing.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-04 · Câu gốc 4

Viết một libFuzzer harness đơn giản cho hàm check_magic (mô tả code, không cần biên dịch nếu môi trường hạn chế).

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-05 · Câu gốc 5

Thiết kế bảng so sánh thực nghiệm: thời gian và số iterations của Black-box vs White-box trên cùng target, dùng số liệu đã có (39.9s/20000 vs 9.3s/2475).

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-06 · Câu gốc 6

Viết script chạy afl-cmin (hoặc mô tả các bước tương đương) để giảm kích thước corpus sau một campaign giả định.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-07 · Câu gốc 7

Thiết kế quy trình Crash Triage cho 20 crash giả định, nhóm theo 4 nguyên nhân gốc khác nhau.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-08 · Câu gốc 8

Viết Regression Test bổ sung input ’FUZZ’ vào bộ test sau khi xác nhận lỗi NULL deref của fuzz_target.c.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-09 · Câu gốc 9

Thiết kế pipeline CI/CD: chạy fuzzing 5 phút mỗi commit và 2 giờ mỗi đêm (nightly), viết file cấu hình workflow.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-10 · Câu gốc 10

Cho check_input() (điều kiện ngoài + điều kiện trong), dự đoán số iterations cần thiết và giải thích dựa trên lý thuyết đã học.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-11 · Câu gốc 11

Viết bảng phân tích chi phí/lợi ích khi đầu tư CBMC (Ch.3.5) cho module lõi so với fuzzing liên tục cho toàn ứng dụng.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-12 · Câu gốc 12

Thiết kế một Hybrid Fuzzing đơn giản (concept): khi coverage-guided không tiến triển sau N lần thử, chuyển sang gọi Z3.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-13 · Câu gốc 13

Viết báo cáo Bài tập lớn mẫu: chọn 1 chương trình C, áp dụng cả Cppcheck+CBMC (static) và coverage-guided fuzzing (dynamic), so sánh loại lỗi tìm được.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-14 · Câu gốc 14

Cho bảng so sánh 4 kỹ thuật (Model Checking, CBMC, Coverage- guided, Black-box), điền vào 1 dòng mới cho kỹ thuật Symbolic Execution.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_hanh-15 · Câu gốc 15

Thiết kế thí nghiệm Differential Fuzzing: so sánh 2 cài đặt hàm parse ngày tháng khác nhau để tìm sai lệch hành vi.

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C4-4.6-thuc_te-01 · Câu gốc 1

Một công ty phát hiện coverage-guided fuzzing của họ tìm ra một lỗi bảo mật nghiêm trọng trong module xử lý magic number chỉ sau vài nghìn lần thử, trong khi black-box đã thử hàng chục nghìn lần không thành công. Phân tích ý nghĩa thực tiễn.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-02 · Câu gốc 2

Một tổ chức phát hiện coverage-guided fuzzing của họ ’mắc kẹt’ hoàn toàn khi gặp module kiểm tra checksum giao dịch tài chính. Đề xuất giải pháp dựa trên Ch.4.6.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-03 · Câu gốc 3

Một dự án mã nguồn mở lớn tích hợp OSS-Fuzz và phát hiện 200 lỗi trong năm đầu tiên tham gia chương trình. Phân tích giá trị của continuous fuzzing quy mô lớn.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-04 · Câu gốc 4

Một công ty phần mềm bảo mật chọn libFuzzer thay vì AFL vì cần tốc độ thực thi cao hơn cho một hàm parse nhỏ, đơn giản. Phân tích lý do lựa chọn phù hợp.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-05 · Câu gốc 5

Một tổ chức nghiên cứu phát hiện Hybrid Fuzzing (kết hợp AFL với concolic execution) giúp tìm ra lỗi mà AFL thuần túy không thể tìm trong benchmark chuẩn. Phân tích đóng góp của phương pháp lai.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-06 · Câu gốc 6

Một công ty tài chính quyết định đầu tư CBMC (Ch.3.5) cho module core banking nhỏ, đồng thời chạy coverage-guided fuzzing liên tục cho toàn bộ ứng dụng lớn hơn. Phân tích chiến lược kết hợp này.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-07 · Câu gốc 7

Một đội bảo mật phát hiện rằng sau khi sửa một crash tìm được qua fuzzing, lỗi tương tự tái xuất hiện 6 tháng sau do thiếu regression test. Phân tích nguyên nhân và bài học.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-08 · Câu gốc 8

Một tổ chức triển khai continuous fuzzing trong CI/CD: 5 phút mỗi commit, 2 giờ mỗi đêm. Phân tích lý do của chiến lược phân tầng thời gian này.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-09 · Câu gốc 9

Một công ty phát hiện coverage-guided fuzzing tìm ra 50 crash trong một campaign dài, nhưng phần lớn là cùng một lỗi gốc. Phân tích vai trò của Crash Triage trong xử lý tình huống này.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-10 · Câu gốc 10

Một nhóm nghiên cứu bảo mật dùng afl-cmin để giảm corpus từ 10.000 xuống 200 seed mà không mất coverage. Phân tích lợi ích cho các campaign tiếp theo.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-11 · Câu gốc 11

Một tổ chức chính phủ về an ninh mạng yêu cầu chứng minh: mọi module rủi ro cao đã qua CẢ static analysis VÀ dynamic fuzzing. Phân tích tính hợp lý của yêu cầu kết hợp này.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-12 · Câu gốc 12

Một công ty phát hiện rằng đối thủ dùng OSS-Fuzz để liên tục quét dự án mã nguồn mở của họ và phát hiện lỗi trước cả đội nội bộ. Phân tích và đề xuất hành động chủ động.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-13 · Câu gốc 13

Một nhóm sinh viên trong bài tập lớn áp dụng cả Cppcheck+CBMC (Ch.2-3) và coverage-guided fuzzing (Ch.4) trên cùng chương trình, phát hiện static tìm ra lỗi mà dynamic bỏ sót và ngược lại. Phân tích ý nghĩa của kết quả này.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-14 · Câu gốc 14

Một tổ chức nghiên cứu công bố Differential Fuzzing phát hiện sai lệch giữa 2 cài đặt TLS khác nhau của cùng một đặc tả. Phân tích giá trị của kỹ thuật này trong đảm bảo tính nhất quán.

**Trả lời gợi ý gốc:**



#### C4-4.6-thuc_te-15 · Câu gốc 15

Một công ty phần mềm nhúng ô tô kết hợp coverage-guided fuzzing với formal verification (CBMC) cho firmware điều khiển an toàn. Phân tích lý do không chỉ dùng một kỹ thuật duy nhất.

**Trả lời gợi ý gốc:**
