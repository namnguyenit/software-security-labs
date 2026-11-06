# Chương 3: Phát hiện lỗ hổng phần mềm – Phân tích tĩnh: ngân hàng câu hỏi gốc

**360câu.** Nguồn: `De-On-Tap.htm`, trường `QUIZ_DATA`; file `on-tap-an-toan-phan-mem_rutgon.html` giống byte. Đáp án/giải thích giữ theo nguồn, không mặc nhiên đã được xác minh.

[Mục lục ngân hàng](../11_Ngan_hang_cau_hoi.md) · [Đính chính](../08_Dinh_chinh_va_gioi_han.md)

Các đoạn nguồn có code/Markdown không hoàn chỉnh được đặt trong khối text để bảo toàn nội dung. Số thứ tự gốc có thể bắt đầu lại ở từng mục; ID bên dưới là duy nhất theo chương/mục/loại.

## Mục 3.1: Giới thiệu kiểm chứng và thẩm định phần mềm (V&V)

### Tóm tắt kiến thức nguyên bản

Chương 3 tập trung vào Verification (“chúng ta xây dựng sản phẩm đúng cách?”) bằng kỹ thuật phân tích tĩnh – kiểm tra mã nguồn mà KHÔNG thực thi nó. Phân tích tĩnh nằm giữa Testing (Ch.1.3, chạy chương trình với input cụ thể) và Formal Verification/Model Checking (Ch.1.5, xét đầy đủ nhưng cần mô hình trừu tượng). Model-based Verification (NuSMV, SPIN) xây tay mô hình Kripke K = (S, S0 , R, L): trừu tượng cao, dễ suy luận nhưng tốn công sức xây mô hình thủ công. Code-based Verification (CBMC, học ở Mục 3.5) sinh mô hình TỰ ĐỘNG trực tiếp từ mã C – đây là “cầu nối” từ lý thuyết Kripke (Ch.1) sang công cụ áp dụng thực tế. Quy trình V&V điển hình: Đặc tả thuộc tính + Mã nguồn → Công cụ phân tích tĩnh → kết luận “Sound: thuộc tính giữ” hoặc “Counterexample”. Verification Engineer cần: (1) định nghĩa đặc tả hình thức từ yêu cầu tự nhiên, (2) chọn công cụ phù hợp (Cppcheck nhanh vs. CBMC chặt chẽ), (3) diễn giải counterexample (lỗi thật hay false positive), (4) cân bằng độ phủ kiểm chứng với chi phí thời gian/tính toán. Các tiêu chuẩn công nghiệp như Common Criteria EAL6–7 và DO-178C Level A (hàng không) YÊU CẦU formal verification bắt buộc cho các module tới hạn.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C3-3.1-trac_nghiem-01 · Câu gốc 1

Verification trả lời câu hỏi nào?

**A.** Chúng ta xây dựng đúng sản phẩm?

**B.** Chúng ta xây dựng sản phẩm đúng cách?

**C.** Sản phẩm có bán được không?

**D.** Sản phẩm có đẹp không?

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-02 · Câu gốc 2

Chương 3 tập trung chủ yếu vào kỹ thuật nào?

**A.** Testing thủ công

**B.** Phân tích tĩnh (Static Analysis)

**C.** Thiết kế giao diện

**D.** Quản lý dự án

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-03 · Câu gốc 3

Phân tích tĩnh nằm ở vị trí nào trong phổ kỹ thuật QA?

**A.** Trước Testing, sau Formal Verification

**B.** Giữa Testing/Dynamic Analysis và Formal Verification

**C.** Sau Formal Verification

**D.** Không liên quan tới phổ kỹ thuật nào

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-04 · Câu gốc 4

Model-based Verification khác Code-based Verification ở điểm nào?

**A.** Model-based xây mô hình trừu tượng thủ công; Code-based tự động sinh từ mã nguồn

**B.** Hai khái niệm hoàn toàn giống nhau

**C.** Code- based luôn kém chính xác hơn

**D.** Model-based chỉ dùng cho Java

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-05 · Câu gốc 5

CBMC thuộc loại kiểm chứng nào?

**A.** Model-based, giống NuSMV

**B.** Code-based, sinh mô hình tự động từ mã

**C.** C. Không liên quan tới model checking

**D.** Chỉ dùng cho testing thủ công

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-06 · Câu gốc 6

Verification Engineer cần làm gì với đặc tả yêu cầu tự nhiên?

**A.** Bỏ qua hoàn toàn

**B.** Chuyển thành đặc tả hình thức (formal spec)

**C.** Chỉ cần đọc một lần

**D.** Không liên quan tới công việc của họ

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-07 · Câu gốc 7

Counterexample trong quy trình V&V dùng để làm gì?

**A.** Chứng minh thuộc tính luôn đúng

**B.** Chỉ ra lý do/đường dẫn cụ thể khi thuộc tính bị vi phạm

**C.** Không có tác dụng gì

**D.** Chỉ dùng để trang trí báo cáo

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-08 · Câu gốc 8

”False positive” trong ngữ cảnh V&V nghĩa là gì?

**A.** Cảnh báo lỗi không thực sự tồn tại

**B.** Bỏ sót lỗi thật

**C.** Chương trình chạy đúng

**D.** Không có ý nghĩa cụ thể

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-09 · Câu gốc 9

Yếu tố nào KHÔNG cần cân nhắc khi Verification Engineer chọn công cụ?

**A.** Mức độ tới hạn module

**B.** Chi phí thời gian/tính toán

**C.** Màu sắc giao diện IDE

**D.** Kỹ năng đội ngũ

**Đáp án gốc:** C

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-10 · Câu gốc 10

Quy trình V&V điển hình bắt đầu từ đâu?

**A.** Đặc tả thuộc tính và mã nguồn

**B.** Chỉ từ mã nguồn, không cần đặc tả

**C.** Chỉ từ đặc tả, không cần mã nguồn

**D.** Từ báo cáo lỗi của khách hàng

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-11 · Câu gốc 11

NuSMV/SPIN đòi hỏi điều gì mà CBMC không đòi hỏi?

**A.** Không đòi hỏi gì khác biệt

**B.** Xây dựng mô hình Kripke THỦ CÔNG

**C.** Cần license thương mại

**D.** Chỉ chạy trên Windows

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-12 · Câu gốc 12

”Sound trong giới hạn bound” là đặc điểm của công cụ nào?

**A.** NuSMV

**B.** CBMC

**C.** Cppcheck

**D.** Compiler warnings

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-13 · Câu gốc 13

Diễn giải kết quả CBMC ”VERIFICATION SUCCESSFUL” nghĩa là gì?

**A.** Chương trình hoàn toàn không có lỗi trong MỌI trường hợp

**B.** Không tìm thấy lỗi TRONG PHẠM VI đã unwind/kiểm tra

**C.** Chương trình chạy nhanh

**D.** Không có ý nghĩa gì

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-14 · Câu gốc 14

Common Criteria EAL cao yêu cầu kỹ thuật nào?

**A.** Chỉ cần unit test

**B.** Formal Verification

**C.** Không cần kiểm chứng gì thêm

**D.** Chỉ cần code review

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.1-trac_nghiem-15 · Câu gốc 15

DO-178C Level A áp dụng cho ngành nào?

**A.** Ngân hàng

**B.** Hàng không

**C.** Game

**D.** Mạng xã hội

**Đáp án gốc:** B

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C3-3.1-ly_thuyet-01 · Câu gốc 1

````text
Ôn lại và trình bày định nghĩa Verification và Validation, chỉ ra Chương

```
tập trung vào phần nào.
```
````

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-02 · Câu gốc 2

Giải thích vị trí của phân tích tĩnh trong phổ kỹ thuật QA (Testing → Static → Formal Verification).

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-03 · Câu gốc 3

Phân biệt Model-based Verification và Code-based Verification, cho ví dụ công cụ mỗi loại.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-04 · Câu gốc 4

Trình bày lý do CBMC được coi là ”cầu nối” giữa lý thuyết Model Checking (Ch.1.5) và thực hành trên mã C.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-05 · Câu gốc 5

Mô tả quy trình V&V điển hình: từ đặc tả thuộc tính, mã nguồn, tới kết quả (sound/counterexample).

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-06 · Câu gốc 6

Giải thích vai trò của Verification Engineer trong việc chuyển đặc tả tự nhiên thành đặc tả hình thức.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-07 · Câu gốc 7

Trình bày khái niệm Counterexample và giá trị thực tiễn của nó khi công cụ phát hiện vi phạm.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-08 · Câu gốc 8

Bàn luận: những yếu tố nào Verification Engineer cần cân nhắc khi chọn công cụ phù hợp?

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-09 · Câu gốc 9

Giải thích ý nghĩa ”sound trong giới hạn bound” của CBMC và tại sao đây không phải ”sound tuyệt đối”.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-10 · Câu gốc 10

Trình bày mối liên hệ giữa Common Criteria EAL cao, DO-178C Level A với yêu cầu formal verification.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-11 · Câu gốc 11

Mô tả cách diễn giải kết quả ”VERIFICATION SUCCESSFUL” của CBMC một cách chính xác, tránh hiểu lầm.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-12 · Câu gốc 12

Giải thích tại sao module xử lý input mạng thường được ưu tiên Verification cao hơn (liên hệ Risk Ch.2.1).

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-13 · Câu gốc 13

Bàn luận về đánh đổi giữa độ chính xác (Model Checking chặt chẽ) và chi phí thời gian khi chọn công cụ V&V.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-14 · Câu gốc 14

Trình bày ví dụ cụ thể một tổ chức lựa chọn kỹ thuật V&V dựa trên mức độ tới hạn của module.

**Trả lời gợi ý gốc:**



#### C3-3.1-ly_thuyet-15 · Câu gốc 15

Giải thích tại sao Model-based Verification (NuSMV) cần công sức xây mô hình tay trong khi Code-based (CBMC) thì không.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C3-3.1-thuc_hanh-01 · Câu gốc 1

Viết đặc tả hình thức bằng ngôn ngữ tự nhiên có cấu trúc cho thuộc tính ”không bao giờ dereference NULL” cho hàm fixed_null_deref.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-02 · Câu gốc 2

Cho hàm fixed_null_deref (Ch.2), chạy CBMC và ghi lại kết quả VERIFICATION SUCCESSFUL/FAILED.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-03 · Câu gốc 3

Với bug_null_deref (Ch.2), chạy CBMC và diễn giải counterexample tìm được.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-04 · Câu gốc 4

Viết bảng phân loại 5 module giả định theo mức độ ưu tiên Verification (Cao/TB/Thấp).

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-05 · Câu gốc 5

Thiết kế checklist (5 mục) đánh giá xem một module có cần CBMC hay chỉ cần Cppcheck.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-06 · Câu gốc 6

Viết đặc tả hình thức cho thuộc tính ”index luôn nằm trong biên mảng” cho một hàm truy cập mảng cụ thể.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-07 · Câu gốc 7

Cho 2 kết quả: Cppcheck báo ”possible null pointer” và CBMC báo ”VERIFICATION SUCCESSFUL” cho cùng hàm, giải thích không mâu thuẫn.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-08 · Câu gốc 8

Viết quy trình (flowchart) Verification Engineer xử lý khi nhận module mới: từ đặc tả tới kết luận.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-09 · Câu gốc 9

Thiết kế Risk Register kết hợp mức độ Verification cần thiết cho 4 module (parser, logger, crypto, UI).

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-10 · Câu gốc 10

Chạy CBMC với các mức --unwind khác nhau (2, 6, 12) trên cùng một hàm có vòng lặp, so sánh kết quả.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-11 · Câu gốc 11

Viết một bảng so sánh Model-based (NuSMV) và Code-based (CBMC) áp dụng cho MỘT ví dụ cụ thể (hệ thống đèn giao thông).

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-12 · Câu gốc 12

Cho một module xử lý input mạng, viết Risk Assessment (Ch.2.1) rồi đề xuất mức Verification tương ứng.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-13 · Câu gốc 13

Viết báo cáo ngắn (100 từ) giải thích cho quản lý dự án lý do cần đầu tư CBMC cho module thanh toán.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-14 · Câu gốc 14

Thiết kế bảng ánh xạ Common Criteria EAL level → công cụ Verification tương ứng cần dùng.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_hanh-15 · Câu gốc 15

Viết đặc tả hình thức cho thuộc tính ”không có 2 giao dịch cùng rút một số dư” (double-spending prevention).

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C3-3.1-thuc_te-01 · Câu gốc 1

Một công ty tài chính phải quyết định có đầu tư CBMC cho module giao dịch hay không. Phân tích chi phí-lợi ích và đưa ra khuyến nghị.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-02 · Câu gốc 2

Một dự án hàng không yêu cầu DO-178C Level A nhưng đội ngũ chưa từng dùng formal verification. Đề xuất lộ trình đào tạo và triển khai.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-03 · Câu gốc 3

Một tổ chức phát hiện một lỗi nghiêm trọng mà CBMC đã báo FAILURE từ lâu nhưng bị bỏ qua. Phân tích nguyên nhân quy trình và đề xuất khắc phục.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-04 · Câu gốc 4

Một công ty khởi nghiệp hỏi có cần CBMC ngay từ đầu hay có thể trì hoãn tới khi sản phẩm trưởng thành hơn. Tư vấn dựa trên giai đoạn phát triển.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-05 · Câu gốc 5

Một dự án ngân hàng phát hiện Cppcheck và CBMC cho kết quả MÂU THUẪN trên cùng một hàm. Phân tích và giải thích cho khách hàng.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-06 · Câu gốc 6

Một tổ chức tài chính lớn yêu cầu CHỨNG MINH mọi module core đã qua formal verification trước audit. Đề xuất quy trình thu thập bằng chứng.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-07 · Câu gốc 7

Một dự án ô tô tự lái cần verification cho module điều khiển phanh khẩn cấp. Phân tích mức độ ưu tiên và công cụ phù hợp.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-08 · Câu gốc 8

Một công ty phát hiện chi phí CBMC vượt ngân sách dự kiến do thời gian chạy quá lâu trên module lớn. Đề xuất giải pháp tối ưu.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-09 · Câu gốc 9

Một dự án chính phủ yêu cầu Common Criteria EAL6 cho hệ thống bỏ phiếu điện tử. Phân tích ý nghĩa và độ khó đạt được mức này.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-10 · Câu gốc 10

Một tổ chức y tế phát hiện thiết bị cấy ghép chưa từng qua formal verification. Phân tích mức độ khẩn cấp và đề xuất hành động.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-11 · Câu gốc 11

Một công ty bảo hiểm phải chọn giữa thuê chuyên gia CBMC bên ngoài hoặc đào tạo nội bộ. Phân tích ưu nhược điểm mỗi lựa chọn.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-12 · Câu gốc 12

Một dự án blockchain phát hiện lỗi smart contract SAU KHI deploy dù đã ”test kỹ”. Phân tích liệu formal verification có ngăn chặn được không.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-13 · Câu gốc 13

Một tổ chức phát hiện một Verification Engineer diễn giải SAI một counterexample, dẫn tới bỏ sót lỗi thật. Phân tích rủi ro và đề xuất quy trình review chéo.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-14 · Câu gốc 14

Một công ty startup AI dùng C++ cho inference engine, cân nhắc CBMC cho phần lõi. Phân tích tính khả thi với codebase lớn có nhiều thư viện phụ thuộc.

**Trả lời gợi ý gốc:**



#### C3-3.1-thuc_te-15 · Câu gốc 15

Một dự án vệ tinh yêu cầu MỌI dòng code qua formal verification trước phóng. Phân tích tính thực tế và đề xuất ưu tiên.

**Trả lời gợi ý gốc:**



## Mục 3.2: Tính đúng đắn và đầy đủ (Soundness & Completeness)

### Tóm tắt kiến thức nguyên bản

Soundness: một phân tích là sound nếu khi nó báo “thuộc tính φ ĐÚNG” (an toàn) thì φ chắc chắn đúng trên chương trình thực – KHÔNG có False Negative. Completeness: một phân tích là complete nếu mọi cảnh báo phát ra đều là lỗi thật – KHÔNG có False Positive (lưu ý: định nghĩa này khác với nghĩa “tìm được mọi lỗi” dùng ở một số tài liệu khác). Bảng chân trị 4 tình huống (TP/FP/TN/FN) là công cụ phân tích hiệu quả của một kỹ thuật QA. Over-approximation (xét tất cả hành vi thật + có thể thêm hành vi giả) → liên hệ Sound (không bỏ sót lỗi nhưng có thể sinh false positive). Under-approximation (chỉ xét một phần hành vi, VD: path đã test) → liên hệ Complete nhưng KHÔNG sound (mọi cảnh báo đều thật nhưng có thể bỏ sót lỗi). Theo hệ quả Định lý Rice: không công cụ thực tế nào vừa sound, vừa complete, vừa luôn dừng (terminate) trên MỌI chương trình – buộc phải đánh đổi ít nhất một trong ba. Cppcheck: không sound, không complete (heuristic). CBMC: sound VÀ complete trong giới hạn bound k đã unwind. Valgrind (dynamic): không sound (chỉ path đã chạy) nhưng complete trên path đó. Bốn trục phân loại static analysis: Sound/Heuristic, Sensitive/Insensitive (field, flow, path), Over/Under-approximation, Explicit/Symbolic.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C3-3.2-trac_nghiem-01 · Câu gốc 1

Một phân tích Sound có đặc điểm gì?

**A.** Không có false negative khi kết luận an toàn

**B.** Không có false positive

**C.** Luôn tìm ra mọi lỗi

**D.** Luôn chạy nhanh

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-02 · Câu gốc 2

Một phân tích Complete có đặc điểm gì?

**A.** Không có false negative

**B.** Không có false positive

**C.** Luôn sound

**D.** Luôn chậm

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-03 · Câu gốc 3

True Positive nghĩa là gì?

**A.** Công cụ báo có lỗi, và lỗi thực sự tồn tại

**B.** Công cụ báo có lỗi, nhưng không có lỗi

**C.** Công cụ báo an toàn, nhưng có lỗi

**D.** Công cụ báo an toàn, và thực sự an toàn

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-04 · Câu gốc 4

False Negative nghĩa là gì?

**A.** Công cụ báo có lỗi nhưng không có lỗi thật

**B.** Công cụ báo AN TOÀN nhưng THỰC RA có lỗi

**C.** Công cụ báo đúng hoàn toàn

**D.** Không có ý nghĩa cụ thể

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-05 · Câu gốc 5

Over-approximation liên hệ chặt chẽ với tính chất nào?

**A.** Complete

**B.** Sound

**C.** Nhanh

**D.** Không liên quan gì

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-06 · Câu gốc 6

Under-approximation liên hệ chặt chẽ với tính chất nào?

**A.** Sound

**B.** Complete (nhưng không sound)

**C.** Luôn cả hai

**D.** Không có tính chất nào

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-07 · Câu gốc 7

Định lý Rice liên quan tới điều gì?

**A.** Chứng minh MỌI thuộc tính chương trình đều decidable

**B.** Hầu hết thuộc tính ngữ nghĩa không tầm thường là undecidable

**C.** Không liên quan gì tới static analysis

**D.** Chỉ áp dụng cho ngôn ngữ functional

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-08 · Câu gốc 8

Hệ quả của Định lý Rice đối với công cụ QA là gì?

**A.** Không công cụ nào có thể vừa sound, vừa complete, vừa luôn dừng cho mọi chương trình

**B.** Mọi công cụ đều hoàn hảo

**C.** Không có hệ quả thực tế nào

**D.** Chỉ áp dụng cho lý thuyết, không ảnh hưởng thực hành

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-09 · Câu gốc 9

Cppcheck có tính chất Sound/Complete như thế nào?

**A.** Sound và Complete

**B.** Không sound, không complete (heuristic)

**C.** Chỉ sound

**D.** Chỉ complete

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-10 · Câu gốc 10

CBMC có tính chất gì (trong giới hạn bound)?

**A.** Sound và Complete trong bound đã chọn

**B.** Không sound, không complete

**C.** Chỉ complete

**D.** Không liên quan gì tới sound/complete

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-11 · Câu gốc 11

Valgrind (dynamic) có tính chất gì?

**A.** Sound trên toàn bộ chương trình

**B.** Không sound (chỉ path đã chạy), nhưng complete trên path đã chạy

**C.** Hoàn toàn sound và complete

**D.** Không có tính chất xác định

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-12 · Câu gốc 12

Một công cụ ”luôn báo an toàn” (không phân tích gì) có sound không?

**A.** Có, vì không bao giờ báo sai

**B.** Không, vì bỏ sót MỌI lỗi thật (toàn bộ false negative)

**C.** Có và cũng complete

**D.** Không xác định được

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-13 · Câu gốc 13

Tại sao ”false positive” gây hại cho sự CHẤP NHẬN công cụ trong thực tế?

**A.** Không gây hại gì

**B.** Gây ”alert fatigue” khiến dev bỏ qua cảnh báo

**C.** False positive luôn tốt hơn false negative

**D.** Chỉ ảnh hưởng tốc độ

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-14 · Câu gốc 14

Trade-off giữa Precision và Scalability thể hiện như thế nào?

**A.** Công cụ chính xác cao (CBMC) thường scale kém hơn công cụ heuristic (Cppcheck)

**B.** Không có trade-off nào

**C.** Precision luôn tỷ lệ thuận với Scalability

**D.** Chỉ áp dụng cho ngôn ngữ Python

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.2-trac_nghiem-15 · Câu gốc 15

Diễn giải kết quả CBMC ”SUCCESSFUL” đúng đắn là gì?

**A.** Không có lỗi trong TOÀN BỘ chương trình mọi trường hợp

**B.** Không có lỗi TRONG PHẠM VI đã unwind

**C.** Chương trình chạy nhanh

**D.** Không có ý nghĩa

**Đáp án gốc:** B

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C3-3.2-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa chính xác của Soundness và Completeness trong phân tích tĩnh.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-02 · Câu gốc 2

Giải thích bảng chân trị 4 tình huống (TP, FP, TN, FN) và liên hệ với Sound/Complete.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-03 · Câu gốc 3

Mô tả Over-approximation và Under-approximation, chỉ ra tính chất nào (sound/complete) mỗi loại thường đi kèm.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-04 · Câu gốc 4

Trình bày Định lý Rice và hệ quả của nó đối với việc thiết kế công cụ phân tích tĩnh thực tế.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-05 · Câu gốc 5

Giải thích tại sao KHÔNG có công cụ nào vừa sound, vừa complete, vừa luôn dừng cho MỌI chương trình.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-06 · Câu gốc 6

Áp dụng khung Sound/Complete để phân tích Cppcheck, Clang SA, CBMC, Valgrind (đã học Ch.2.5).

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-07 · Câu gốc 7

Giải thích ý nghĩa ”CBMC sound TRONG GIỚI HẠN BOUND” và tại sao đây khác với ”sound tuyệt đối”.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-08 · Câu gốc 8

Bàn luận: tại sao ”false positive” gây hại nhiều hơn về mặt THỰC TIỄN dù về lý thuyết ”an toàn hơn” false negative?

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-09 · Câu gốc 9

Trình bày ví dụ minh họa công cụ ”luôn báo an toàn không phân tích gì” – phân tích tính sound/complete/hữu dụng.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-10 · Câu gốc 10

Giải thích Field-sensitive và Field-insensitive Analysis, cho ví dụ minh họa khác biệt độ chính xác.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-11 · Câu gốc 11

Mô tả Flow-sensitive và Flow-insensitive Analysis, liên hệ với khả năng CBMC phân biệt ”trước/sau free”.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-12 · Câu gốc 12

Trình bày khái niệm Path-sensitive Analysis và phân biệt với Flow- sensitive.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-13 · Câu gốc 13

Giải thích 4 trục phân loại của Static Analysis: Sound/Heuristic, Sensitive/Insensitive, Over/Under-approx, Explicit/Symbolic.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-14 · Câu gốc 14

Bàn luận về Unsat Core trong SMT solving – giá trị thực tiễn khi debug đặc tả phức tạp.

**Trả lời gợi ý gốc:**



#### C3-3.2-ly_thuyet-15 · Câu gốc 15

Trình bày ví dụ cụ thể minh họa Over-approximation dẫn tới False Positive trong Alias Analysis.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C3-3.2-thuc_hanh-01 · Câu gốc 1

Viết một bảng phân tích Sound/Complete cho Cppcheck, Clang SA, CBMC, Valgrind (4 công cụ đã học Ch.2.5).

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-02 · Câu gốc 2

Cho một công cụ giả định X luôn trả về ”OK”, viết đoạn code Python minh họa và phân tích Sound/Complete.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-03 · Câu gốc 3

Với hàm fixed_null_deref, chạy Cppcheck VÀ CBMC, so sánh 2 kết quả và giải thích không mâu thuẫn (dựa Sound/Complete).

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-04 · Câu gốc 4

Viết bảng chân trị TP/FP/TN/FN cho một tình huống cụ thể: công cụ báo 8 lỗi, 5 lỗi thật, chương trình có 6 lỗi thực tế.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-05 · Câu gốc 5

Tính Precision và Recall cho ví dụ ở câu 4 (Precision=TP/(TP+FP), Recall=TP/(TP+FN)).

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-06 · Câu gốc 6

Viết một đoạn Python mô phỏng Over-approximation: tập ”có thể” luôn là superset của tập ”thực tế”.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-07 · Câu gốc 7

Cho 2 phiên bản phân tích alias (chính xác và over-approximate), viết ví dụ code minh họa khác biệt kết quả.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-08 · Câu gốc 8

Chạy CBMC với --unwind 3 và --unwind 10 trên cùng hàm có vòng lặp 8 lần, giải thích khác biệt kết quả.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-09 · Câu gốc 9

Viết một unsat core example bằng Z3 (3 điều kiện, chỉ ra 2 điều kiện gây mâu thuẫn thực sự).

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-10 · Câu gốc 10

Thiết kế bảng minh họa Field-sensitive vs Field-insensitive cho một struct 3 field.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-11 · Câu gốc 11

Viết đoạn code minh họa Flow-sensitive: một biến an toàn TRƯỚC một điểm code, KHÔNG an toàn SAU điểm đó.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-12 · Câu gốc 12

Cho danh sách 10 cảnh báo từ Cppcheck, phân loại thủ công thành TP/FP dựa trên code thực tế.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-13 · Câu gốc 13

Viết một script tính tỷ lệ False Positive của một công cụ dựa trên danh sách finding đã gắn nhãn.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-14 · Câu gốc 14

Thiết kế bảng ”4 trục phân loại” và xếp Cppcheck, Clang SA, CBMC, Valgrind vào từng vị trí trên 4 trục.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_hanh-15 · Câu gốc 15

Viết đoạn code Python minh họa ”công cụ complete nhưng không sound” (dùng testing giới hạn tập input).

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C3-3.2-thuc_te-01 · Câu gốc 1

Một công ty phát hiện công cụ static analysis mới mua báo QUÁ NHIỀU false positive, dev bắt đầu bỏ qua. Phân tích và đề xuất giải pháp dựa trên khái niệm Alert Fatigue.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-02 · Câu gốc 2

Một tổ chức tài chính yêu cầu ”chứng minh 100% không có lỗi bảo mật”. Phản biện yêu cầu này dựa trên Định lý Rice.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-03 · Câu gốc 3

Một dự án phát hiện CBMC báo ”SUCCESSFUL” nhưng sau đó vẫn có lỗi trong production do vòng lặp KHÔNG unwind đủ. Phân tích nguyên nhân và bài học.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-04 · Câu gốc 4

Một công ty bảo hiểm dùng 2 công cụ khác nhau cho cùng module, nhận 2 kết quả KHÁC NHAU. Phân tích cách giải thích hợp lý cho quản lý không chuyên kỹ thuật.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-05 · Câu gốc 5

Một tổ chức phát hiện một auditor bên ngoài yêu cầu ”công cụ phải sound VÀ complete”. Giải thích tại sao yêu cầu này không thực tế và đề xuất tiêu chí thay thế.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-06 · Câu gốc 6

Một dự án hàng không phát hiện lỗi mà MỌI công cụ static analysis đã dùng đều bỏ sót (false negative). Phân tích giới hạn công cụ và đề xuất bổ sung Theorem Proving.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-07 · Câu gốc 7

Một công ty startup chọn dùng CHỈ heuristic tool (không sound) để tiết kiệm chi phí. Phân tích rủi ro của quyết định này cho sản phẩm tới hạn cao.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-08 · Câu gốc 8

Một tổ chức phát hiện tỷ lệ false positive của Cppcheck tăng đột biến sau khi update phiên bản mới. Đề xuất quy trình đánh giá lại.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-09 · Câu gốc 9

Một dự án ngân hàng yêu cầu MỌI cảnh báo (kể cả false positive nghi ngờ) phải được review thủ công. Phân tích chi phí thời gian và đề xuất tối ưu quy trình.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-10 · Câu gốc 10

Một công ty phát hiện field-insensitive analysis (Cppcheck) bỏ sót lỗi cụ thể trên MỘT field của struct lớn. Đề xuất bổ sung công cụ field-sensitive.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-11 · Câu gốc 11

Một tổ chức tài chính yêu cầu bằng chứng ”flow-sensitive analysis đã được áp dụng” cho audit. Đề xuất cách chứng minh và tài liệu hóa.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-12 · Câu gốc 12

Một dự án phát hiện alias analysis quá thận trọng (over-approximate) khiến MỌI con trỏ bị coi là ”có thể alias”, gây hàng nghìn false positive. Đề xuất tinh chỉnh.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-13 · Câu gốc 13

Một công ty phần mềm y tế phải giải thích cho FDA về khái niệm ”sound trong giới hạn bound” của CBMC. Viết đoạn giải thích phù hợp.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-14 · Câu gốc 14

Một tổ chức phát hiện 2 kỹ sư verification tranh cãi về việc một cảnh báo là TP hay FP. Đề xuất quy trình phân xử khách quan.

**Trả lời gợi ý gốc:**



#### C3-3.2-thuc_te-15 · Câu gốc 15

Một dự án quốc phòng yêu cầu MỌI unsat result từ Z3 phải kèm unsat core để audit. Phân tích lý do yêu cầu này hợp lý.

**Trả lời gợi ý gốc:**



## Mục 3.3: Phân tích tĩnh vs. mô phỏng kiểm thử vs. gỡ lỗi

### Tóm tắt kiến thức nguyên bản

Ba kỹ thuật QA được so sánh có hệ thống: Static Analysis (không chạy chương trình, input là mã nguồn, chứng minh thuộc tính trên MỌI input), Testing (chạy chương trình, input là test case cụ thể, kiểm tra hành vi trên input đã chọn), Debugging (chạy 1 lần với lỗi cụ thể đã xảy ra, tìm NGUYÊN NHÂN của 1 sự cố). Debugging là reactive (sau khi lỗi xảy ra); Static Analysis là proactive (trước khi chạy). Abstract Interpretation: thực thi chương trình trên miền trừu tượng (Sign Domain, Interval Domain, Points-to Domain, Null Domain) thay vì giá trị cụ thể, để suy luận về TẬP trạng thái. Đây là nền tảng lý thuyết của Clang Static Analyzer (Ch.2.5). Symbolic Execution: thực thi với input là ký hiệu tượng trưng (symbol); mỗi nhánh sinh ra một path condition – công thức logic mô tả điều kiện đi theo đường đó. Nếu path condition UNSAT → đường đó infeasible, loại bỏ khỏi phân tích. Đây chính là cầu nối trực tiếp tới SAT/SMT solving (Mục 3.4). Path Explosion (tương tự State Explosion Ch.1.5): số path tăng theo cấp số nhân 2n với n điều kiện if độc lập – giải quyết bằng giới hạn độ sâu (tương tự BMC 3.5), path merging, heuristic search. Concolic Testing (CONCrete+symbOLIC): kết hợp giá trị cụ thể và biểu diễn tượng trưng song song – nền tảng của White-box Fuzzing (Ch.4.6). Công cụ thực tế: KLEE (LLVM bitcode), angr (Python, phân tích binary), cả hai đều dùng Z3 làm SMT backend. gdb (breakpoint, backtrace, core dump) kết hợp Valgrind là quy trình debug lỗi bộ nhớ kinh điển.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C3-3.3-trac_nghiem-01 · Câu gốc 1

Static Analysis khác Testing ở điểm cốt lõi nào?

**A.** Static Analysis không thực thi chương trình

**B.** Static Analysis luôn nhanh hơn

**C.** Không có khác biệt

**D.** Testing luôn chính xác hơn

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-02 · Câu gốc 2

Debugging khác Static Analysis và Testing ở điểm nào?

**A.** Debugging bắt đầu từ MỘT lỗi cụ thể đã xảy ra để tìm nguyên nhân

**B.** Debugging luôn nhanh hơn

**C.** Không có khác biệt

**D.** Debugging không cần công cụ gì

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-03 · Câu gốc 3

Abstract Interpretation là gì?

**A.** Thực thi chương trình trên miền trừu tượng để suy luận về tập trạng thái

**B.** Chỉ đọc comment trong code

**C.** Không liên quan tới static analysis

**D.** Chỉ áp dụng cho testing

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-04 · Câu gốc 4

Trong Sign Domain (ví dụ Abstract Interpretation), giá trị được biểu diễn bằng:

**A.** Giá trị cụ thể chính xác

**B.** Ký hiệu trừu tượng như {+, -, 0}

**C.** Chuỗi ký tự

**D.** Không biểu diễn gì

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-05 · Câu gốc 5

Interval Domain trong Abstract Interpretation dùng để phát hiện lỗi nào?

**A.** SQL Injection

**B.** Out-of-bounds access, integer overflow

**C.** Race condition

**D.** Không phát hiện lỗi nào

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-06 · Câu gốc 6

Points-to Domain trong Abstract Interpretation dùng để phát hiện lỗi nào?

**A.** Dangling pointer, UAF

**B.** SQL Injection

**C.** Format string

**D.** Race condition

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-07 · Câu gốc 7

Symbolic Execution thực thi chương trình với input như thế nào?

**A.** Giá trị cụ thể

**B.** Ký hiệu tượng trưng (symbol) thay vì giá trị cụ thể

**C.** Không có input

**D.** Chỉ input số nguyên

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-08 · Câu gốc 8

”Path condition” trong Symbolic Execution là gì?

**A.** Điều kiện logic mô tả yêu cầu để đi theo MỘT đường thi hành cụ thể

**B.** Tên biến trong code

**C.** Không có ý nghĩa gì

**D.** Chỉ áp dụng cho vòng lặp

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-09 · Câu gốc 9

Nếu path condition là UNSAT, điều đó có nghĩa gì?

**A.** Đường đó CÓ THỂ xảy ra trong thực tế

**B.** Đường đó KHÔNG BAO GIỜ xảy ra (infeasible path)

**C.** Chương trình có lỗi

**D.** Không có ý nghĩa gì

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-10 · Câu gốc 10

Symbolic Execution kết nối trực tiếp với kỹ thuật nào sẽ học ở Mục 3.4?

**A.** SAT/SMT solving

**B.** Alignment

**C.** Coverage

**D.** Fuzzing

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-11 · Câu gốc 11

gdb dùng để làm gì?

**A.** Biên dịch chương trình

**B.** Debug: xem breakpoint, stack trace, giá trị biến lúc crash

**C.** Chạy static analysis

**D.** Đo hiệu năng

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-12 · Câu gốc 12

gdb ./program core; (gdb) bt dùng để làm gì?

**A.** Biên dịch lại chương trình

**B.** Xem backtrace (stack trace) tại thời điểm crash

**C.** Xóa core dump

**D.** Không có tác dụng gì

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-13 · Câu gốc 13

Kết hợp Valgrind và gdb có lợi ích gì?

**A.** Valgrind chỉ ra VỊ TRÍ lỗi, gdb giúp hiểu NGUYÊN NHÂN sâu hơn

**B.** Không có lợi ích gì khi kết hợp

**C.** Hai công cụ xung đột nhau

**D.** Chỉ dùng được một trong hai

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-14 · Câu gốc 14

Path Explosion trong Symbolic Execution tương tự vấn đề nào đã học ở Ch.1.5?

**A.** State Explosion

**B.** Buffer Overflow

**C.** Memory Leak

**D.** Race Condition

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.3-trac_nghiem-15 · Câu gốc 15

KLEE là công cụ gì? A. Compiler C. B. Symbolic execution engine cho LLVM bitcode. C. Static analyzer đơn giản. D. Trình soạn thảo văn bản.

**Đáp án gốc:** B

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C3-3.3-ly_thuyet-01 · Câu gốc 1

So sánh Static Analysis, Testing/Simulation, và Debugging theo: có chạy chương trình không, input, mục tiêu.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-02 · Câu gốc 2

Trình bày ý tưởng cốt lõi của Abstract Interpretation, cho ví dụ Sign Domain.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-03 · Câu gốc 3

Giải thích Interval Domain và Points-to Domain, liên hệ với lỗi bộ nhớ đã học ở Chương 2.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-04 · Câu gốc 4

Mô tả Symbolic Execution và khái niệm ”path condition”.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-05 · Câu gốc 5

Giải thích ý nghĩa của path condition UNSAT (infeasible path) và giá trị của việc phát hiện điều này.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-06 · Câu gốc 6

Trình bày mối liên hệ giữa Symbolic Execution và SAT/SMT solving (sẽ học chi tiết Ch.3.4).

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-07 · Câu gốc 7

Giải thích khái niệm Debugging truyền thống và công cụ gdb, phân biệt với Static/Dynamic Analysis.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-08 · Câu gốc 8

Mô tả quy trình kết hợp Valgrind và gdb để debug một lỗi bộ nhớ thực tế.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-09 · Câu gốc 9

Trình bày vấn đề Path Explosion trong Symbolic Execution, liên hệ với State Explosion (Ch.1.5).

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-10 · Câu gốc 10

Giải thích các giải pháp cho Path Explosion: giới hạn độ sâu, path merging, heuristic search.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-11 · Câu gốc 11

Trình bày KLEE và angr như các công cụ Symbolic Execution thực tế.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-12 · Câu gốc 12

Giải thích Concolic Testing và cách nó kết hợp ưu điểm của Concrete và Symbolic execution.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-13 · Câu gốc 13

Bàn luận về mối liên hệ giữa Concolic Testing (Ch.3.3) và White-box Fuzzing (sẽ học Ch.4.6).

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-14 · Câu gốc 14

Trình bày bảng so sánh khi nào nên dùng Static Analysis, khi nào nên dùng Debugging.

**Trả lời gợi ý gốc:**



#### C3-3.3-ly_thuyet-15 · Câu gốc 15

Giải thích tại sao Abstract Interpretation có thể trả về False Positive, liên hệ Over-approximation (Ch.3.2).

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C3-3.3-thuc_hanh-01 · Câu gốc 1

Với hàm f(x): if(x>0)return x-1; else return -x;, viết path condition cho cả 2 nhánh.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-02 · Câu gốc 2

Xác định bằng tay xem mỗi path condition ở câu 1 có satisfiable không.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-03 · Câu gốc 3

Viết đoạn Python dùng Z3 giải path condition của nhánh x>0 trong hàm f(x) ở câu 1.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-04 · Câu gốc 4

Cho hàm có 3 điều kiện if lồng nhau, liệt kê TẤT CẢ path condition có thể (tối đa 8 path).

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-05 · Câu gốc 5

Dùng Z3 kiểm tra xem trong 8 path ở câu 4, có path nào UNSAT (infeasible) không.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-06 · Câu gốc 6

Viết đoạn code minh họa Abstract Interpretation với Sign Domain cho phép toán x=5;y=-3;z=x+y;.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-07 · Câu gốc 7

Cho biến với Interval Domain [0, 10] và [5, 20], tính Interval của phép cộng 2 biến.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-08 · Câu gốc 8

Viết một chương trình C nhỏ, biên dịch, chạy dưới gdb, đặt breakpoint và in giá trị biến.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-09 · Câu gốc 9

Cố ý tạo một core dump (chương trình crash), dùng gdb program core và chạy bt xem stack trace.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-10 · Câu gốc 10

Kết hợp Valgrind + gdb: chạy Valgrind tìm UAF, sau đó dùng gdb xem chi tiết trạng thái tại dòng lỗi.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-11 · Câu gốc 11

Viết một hàm Python mô phỏng Points-to Analysis đơn giản: trả về tập a,b cho con trỏ p có thể trỏ tới a hoặc b.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-12 · Câu gốc 12

Cho một hàm với vòng lặp 5 lần, tính số lượng path có thể nếu mỗi lần lặp có 1 điều kiện rẽ nhánh (path explosion).

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-13 · Câu gốc 13

Viết đoạn code minh họa Path Merging: 2 path hội tụ về cùng 1 điểm, gộp lại thành 1 trạng thái biểu diễn.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-14 · Câu gốc 14

Cài đặt (hoặc mô tả bằng pseudocode) một symbolic executor đơn giản cho hàm 1 biến, 2 nhánh if.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_hanh-15 · Câu gốc 15

Viết test case Concolic: chạy với giá trị cụ thể x=5, đồng thời track biểu thức symbolic tương ứng.

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C3-3.3-thuc_te-01 · Câu gốc 1

Một công ty phát hiện lỗi CHỈ xảy ra trên server production, KHÔNG tái tạo được ở môi trường dev. Đề xuất quy trình debug dùng core dump.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-02 · Câu gốc 2

Một dự án game phát hiện Symbolic Execution mất QUÁ NHIỀU thời gian trên game logic phức tạp (path explosion). Đề xuất giải pháp thực tế.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-03 · Câu gốc 3

Một tổ chức tài chính dùng KLEE để sinh test case tự động cho module tính lãi suất. Phân tích lợi ích so với viết test case thủ công.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-04 · Câu gốc 4

Một công ty phát hiện Abstract Interpretation báo QUÁ NHIỀU false positive trên module xử lý con trỏ phức tạp. Đề xuất tinh chỉnh độ chính xác alias analysis.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-05 · Câu gốc 5

Một đội DevOps nhận báo cáo crash production nhưng KHÔNG có core dump (đã bị xóa). Đề xuất chính sách lưu trữ core dump cho tương lai.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-06 · Câu gốc 6

Một dự án ô tô dùng Symbolic Execution để tìm input hiếm gây lỗi trong module xử lý cảm biến. Phân tích giá trị so với testing ngẫu nhiên.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-07 · Câu gốc 7

Một công ty bảo mật phân tích malware bằng angr (symbolic execution trên binary). Mô tả quy trình và giá trị của phương pháp này.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-08 · Câu gốc 8

Một tổ chức phát hiện lỗi RACE CONDITION chỉ xuất hiện dưới tải cao, không static analysis nào phát hiện được. Đề xuất kỹ thuật bổ sung (concolic/dynamic).

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-09 · Câu gốc 9

Một dự án fintech cần chứng minh KHÔNG CÓ path nào dẫn tới ”âm số dư”. Đề xuất dùng symbolic execution + Z3 để kiểm tra toàn diện.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-10 · Câu gốc 10

Một công ty phát hiện Debugging mất RẤT NHIỀU thời gian vì thiếu log chi tiết. Đề xuất cải thiện logging strategy để debug nhanh hơn tương lai.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-11 · Câu gốc 11

Một dự án nghiên cứu dùng Concolic Testing để đạt coverage cao hơn fuzzing thuần túy. Phân tích trade-off giữa 2 phương pháp.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-12 · Câu gốc 12

Một tổ chức phát hiện một lỗi bảo mật CHỈ kích hoạt qua MỘT path cụ thể hiếm khi được test. Phân tích cách Symbolic Execution có thể đã tìm ra path này.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-13 · Câu gốc 13

Một công ty game engine gặp Path Explosion khi cố Symbolic Execution toàn bộ game loop. Đề xuất giới hạn phạm vi phân tích (chỉ module cụ thể).

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-14 · Câu gốc 14

Một dự án blockchain dùng KLEE để tìm lỗi trong smart contract compiler. Phân tích tại sao đây là ứng dụng phù hợp của symbolic execution.

**Trả lời gợi ý gốc:**



#### C3-3.3-thuc_te-15 · Câu gốc 15

Một tổ chức phát hiện gdb không đủ để debug lỗi trong môi trường PRODUCTION (không thể attach debugger). Đề xuất công cụ/kỹ thuật thay thế.

**Trả lời gợi ý gốc:**



## Mục 3.4: SAT and SMT solving

### Tóm tắt kiến thức nguyên bản

SAT: xác định có tồn tại phép gán biến boolean làm công thức mệnh đề φ đúng hay không – là bài toán NP-Complete đầu tiên được chứng minh (Cook–Levin, 1971). CNF (Conjunctive Normal Form): hội (AND) của các mệnh đề tuyển (OR) – “ngôn ngữ máy” của SAT solver. Thuật toán DPLL: unit propagation (gán bắt buộc khi mệnh đề chỉ còn 1 literal), pure literal elimination, branching + backtracking. CDCL (Conflict-Driven Clause Learning) mở rộng DPLL bằng cách học từ xung đột để cắt tỉa không gian tìm kiếm – lý do SAT solver hiện đại giải được hàng triệu biến dù bài toán là NP-hard về lý thuyết. SMT (Satisfiability Modulo Theories) mở rộng SAT: literal có thể là công thức trong lý thuyết nền cụ thể – Linear Arithmetic (bounds check), Bitvector (mô hình chính xác int/unsigned kích thước cố định, kể cả overflow wrap-around), Array (đọc/ghi vùng nhớ tại chỉ số qua Select/Store), Uninterpreted Functions (trừu tượng hóa hàm). Z3 (Microsoft Research) là SMT solver dùng xuyên suốt học phần: s.check() trả về sat/unsat/unknown; unsat là bằng chứng TOÁN HỌC không tồn tại phản ví dụ; s.model() trả về phép gán cụ thể khi sat. Ví dụ buffer overflow: Or(index<0, index>=SIZE) sat (không an toàn) khi chưa kiểm tra biên, unsat (an toàn) khi đã thêm giả thiết kiểm tra biên trước. Unsat core: xác định tập điều kiện TỐI THIỂU gây mâu thuẫn, dùng assert_and_track để gắn nhãn ràng buộc. CBMC (Mục 3.5) quy bounded model checking về công thức SAT/SMT rồi giao cho Z3/MiniSat giải.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C3-3.4-trac_nghiem-01 · Câu gốc 1

Bài toán SAT là gì?

**A.** Xác định có tồn tại phép gán làm công thức mệnh đề đúng hay không

**B.** Sắp xếp một mảng số

**C.** Tìm đường đi ngắn nhất

**D.** Không liên quan tới logic

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-02 · Câu gốc 2

SAT là bài toán thuộc lớp độ phức tạp nào?

**A.** P

**B.** NP-Complete

**C.** Decidable trong O(n)

**D.** Không thể tính được

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-03 · Câu gốc 3

Ai chứng minh SAT là NP-Complete đầu tiên?

**A.** Alan Turing

**B.** Cook và Levin (1971)

**C.** Donald Knuth

**D.** John von Neumann

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-04 · Câu gốc 4

CNF là viết tắt của:

**A.** Conjunctive Normal Form

**B.** Common Notation Format

**C.** Complex Number Field

**D.** Certified Normal Function

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-05 · Câu gốc 5

CNF có cấu trúc như thế nào?

**A.** Hội (AND) của các mệnh đề tuyển (OR)

**B.** Tuyển của các mệnh đề hội

**C.** Chỉ dùng phép NOT

**D.** Không có cấu trúc cụ thể

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-06 · Câu gốc 6

DPLL là thuật toán dùng để làm gì?

**A.** Sắp xếp dữ liệu

**B.** Giải bài toán SAT

**C.** Mã hóa dữ liệu

**D.** Nén file

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-07 · Câu gốc 7

”Unit propagation” trong DPLL là gì?

**A.** Gán giá trị bắt buộc khi mệnh đề chỉ còn 1 literal chưa gán

**B.** Xóa toàn bộ biến

**C.** Không có ý nghĩa gì

**D.** Chỉ áp dụng cho SMT

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-08 · Câu gốc 8

CDCL là viết tắt của:

**A.** Conflict-Driven Clause Learning

**B.** Complete Data Clause Logic

**C.** Certified Decision Control Logic

**D.** Không có ý nghĩa cụ thể

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-09 · Câu gốc 9

SMT là viết tắt của:

**A.** Satisfiability Modulo Theories

**B.** Static Memory Test

**C.** System Model Tracker

**D.** Software Module Testing

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-10 · Câu gốc 10

SMT mở rộng SAT bằng cách nào?

**A.** Cho phép literal là công thức trong một lý thuyết nền cụ thể

**B.** Loại bỏ hoàn toàn logic mệnh đề

**C.** Chỉ dùng cho số thực

**D.** Không mở rộng gì

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-11 · Câu gốc 11

Lý thuyết Bitvector trong SMT dùng để mô hình hóa gì?

**A.** Số thực

**B.** Kiểu int/unsigned có kích thước cố định, bao gồm cả overflow

**C.** Chuỗi ký tự

**D.** Không mô hình hóa gì cụ thể

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-12 · Câu gốc 12

Lý thuyết Array trong SMT dùng để mô hình hóa gì?

**A.** Số nguyên đơn giản

**B.** Mảng/vùng nhớ (đọc/ghi tại chỉ số)

**C.** Chuỗi văn bản

**D.** Không liên quan tới bộ nhớ

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-13 · Câu gốc 13

Z3 là công cụ được phát triển bởi:

**A.** Google

**B.** Microsoft Research

**C.** Facebook

**D.** Apple

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-14 · Câu gốc 14

from z3 import *; s = Solver() dùng để làm gì?

**A.** Import thư viện vẽ đồ thị

**B.** Import Z3 và tạo một solver instance

**C.** Kết nối database

**D.** Không có tác dụng gì

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.4-trac_nghiem-15 · Câu gốc 15

s.check() trả về giá trị nào trong 3 giá trị có thể?

**A.** sat, unsat, unknown

**B.** true, false

**C.** 0, 1, 2

**D.** yes, no

**Đáp án gốc:** A

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C3-3.4-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa bài toán SAT và giải thích ý nghĩa NP-Complete của nó.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-02 · Câu gốc 2

Giải thích CNF (Conjunctive Normal Form) và tại sao hầu hết SAT solver nhận input dạng này.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-03 · Câu gốc 3

Trình bày thuật toán DPLL: unit propagation, pure literal elimination, branching.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-04 · Câu gốc 4

Giải thích CDCL và cách nó cải tiến DPLL bằng ”học từ xung đột”.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-05 · Câu gốc 5

Trình bày lý do cần mở rộng SAT thành SMT, cho ví dụ hạn chế của SAT thuần túy.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-06 · Câu gốc 6

Mô tả các lý thuyết SMT phổ biến: Linear Arithmetic, Bitvector, Array, Uninterpreted Functions.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-07 · Câu gốc 7

Giải thích tại sao Bitvector Theory quan trọng để mô hình hóa CHÍNH XÁC kiểu dữ liệu C (bao gồm integer overflow).

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-08 · Câu gốc 8

Trình bày cách dùng Z3 (Python API) để kiểm tra thuộc tính an toàn buffer bounds, với ví dụ cụ thể.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-09 · Câu gốc 9

Giải thích kết quả sat và unsat trong Z3, ý nghĩa của mỗi kết quả đối với việc chứng minh thuộc tính.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-10 · Câu gốc 10

Mô tả cách mã hóa Integer Overflow bằng Bitvector trong Z3 (liên hệ Ch.2.3).

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-11 · Câu gốc 11

Trình bày Array Theory trong SMT và cách nó mô hình hóa bộ nhớ (Store/Select).

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-12 · Câu gốc 12

Giải thích Unsat Core và giá trị thực tiễn khi debug đặc tả phức tạp có nhiều ràng buộc.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-13 · Câu gốc 13

Bàn luận: tại sao unsat là kết quả ”MẠNH” hơn nhiều so với việc chạy testing không tìm thấy lỗi?

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-14 · Câu gốc 14

Trình bày ví dụ cụ thể Z3 giải bài toán phi tuyến (nonlinear arithmetic) như x2 + y 2 = 25.

**Trả lời gợi ý gốc:**



#### C3-3.4-ly_thuyet-15 · Câu gốc 15

Giải thích tại sao SAT solver hiện đại giải được instance triệu biến dù bài toán về lý thuyết là NP-hard.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C3-3.4-thuc_hanh-01 · Câu gốc 1

Viết công thức CNF cho: ”ít nhất 2 trong 3 biến p,q,r là True”.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-02 · Câu gốc 2

Dùng Z3 kiểm tra công thức CNF ở câu 1, tìm một model thỏa mãn.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-03 · Câu gốc 3

Thực hiện DPLL thủ công (bằng tay) cho công thức (p ∨ q) ∧ (¬p ∨ r) ∧ (¬q ∨ ¬r).

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-04 · Câu gốc 4

Viết code Z3 kiểm tra buffer overflow cho mảng kích thước 128 (thay vì 64 như slide), với index BitVec 32-bit.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-05 · Câu gốc 5

Với bài toán ở câu 4, thêm giả thiết ”đã kiểm tra biên” và xác nhận kết quả chuyển từ sat sang unsat.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-06 · Câu gốc 6

Viết code Z3 kiểm tra integer overflow cho phép nhân với elem_size=8 (thay vì 4 như slide).

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-07 · Câu gốc 7

Viết công thức Z3 kiểm tra ”tồn tại x sao cho x/y gây chia cho 0” (y=0).

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-08 · Câu gốc 8

Thêm giả thiết y != 0 vào bài toán câu 7, xác nhận kết quả unsat.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-09 · Câu gốc 9

Viết code Z3 dùng Array Theory: ghi giá trị 0x42 tại địa chỉ 200, đọc lại xác nhận đúng giá trị.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-10 · Câu gốc 10

Dùng Z3 tìm 2 số nguyên x, y sao cho x · y = 24 và x + y = 10.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-11 · Câu gốc 11

Viết ví dụ assert_and_track với 4 ràng buộc, tìm unsat core (2 ràng buộc gây mâu thuẫn thực sự).

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-12 · Câu gốc 12

Viết công thức Z3 kiểm tra thuộc tính ”index luôn nhỏ hơn length của mảng” cho một hàm truy cập mảng động.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-13 · Câu gốc 13

Dùng BitVec 16-bit (thay vì 32-bit), lặp lại bài toán integer overflow và so sánh kết quả.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-14 · Câu gốc 14

Viết code Z3 kiểm tra ”không tồn tại 2 số nguyên dương a,b sao cho a-b âm nếu a>b” (sanity check).

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_hanh-15 · Câu gốc 15

Với ví dụ 2 số nguyên tổng bình phương bằng 25 (slide), tìm THÊM một cặp nghiệm khác ngoài (-3,4)/(3,4).

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C3-3.4-thuc_te-01 · Câu gốc 1

Một ngân hàng cần chứng minh module tính lãi suất KHÔNG BAO GIỜ cho kết quả âm. Đề xuất cách mã hóa bằng Z3 và quy trình xác nhận.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-02 · Câu gốc 2

Một công ty bảo mật phát hiện SMT solver mất QUÁ NHIỀU thời gian (giờ) trên một bài toán phức tạp. Đề xuất cách đơn giản hóa bài toán.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-03 · Câu gốc 3

Một dự án ô tô tự lái cần chứng minh ”xe không bao giờ tăng tốc khi phanh được nhấn”. Đề xuất mã hóa bằng SMT.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-04 · Câu gốc 4

Một tổ chức tài chính phát hiện Z3 báo unknown (không phải sat/unsat) cho một bài toán quan trọng. Phân tích nguyên nhân và đề xuất xử lý.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-05 · Câu gốc 5

Một công ty game dùng Z3 để kiểm tra game logic (không thể ”chết vô hạn”). Phân tích lợi ích so với test thủ công.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-06 · Câu gốc 6

Một dự án hàng không yêu cầu MỌI phép tính số học trong module điều khiển phải chứng minh không overflow. Đề xuất quy trình dùng Z3 hệ thống.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-07 · Câu gốc 7

Một tổ chức phát hiện một lỗi tương tự CVE (integer overflow) mà lẽ ra Z3 có thể đã ngăn chặn nếu áp dụng SỚM HƠN. Phân tích bài học.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-08 · Câu gốc 8

Một công ty blockchain dùng Z3 để verify smart contract TRƯỚC khi deploy (vì không thể sửa sau). Phân tích tầm quan trọng của bước này.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-09 · Câu gốc 9

Một dự án y tế cần chứng minh thuật toán tính liều lượng thuốc KHÔNG BAO GIỜ vượt ngưỡng an toàn. Đề xuất mã hóa bằng SMT và ý nghĩa unsat.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-10 · Câu gốc 10

Một tổ chức phát hiện 2 kỹ sư mã hóa CÙNG một thuộc tính bằng Z3 nhưng cho kết quả KHÁC NHAU. Phân tích khả năng lỗi trong encoding.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-11 · Câu gốc 11

Một công ty startup fintech mới học Z3, viết công thức SAI dẫn tới kết luận ”an toàn” trong khi thực tế có lỗi. Phân tích rủi ro của ”false sense of security” từ encoding sai.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-12 · Câu gốc 12

Một dự án quốc phòng yêu cầu MỌI công thức Z3 phải được review bởi 2 kỹ sư độc lập trước khi tin tưởng kết quả. Phân tích lý do yêu cầu này.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-13 · Câu gốc 13

Một tổ chức nghiên cứu dùng Z3 để tìm phản ví dụ cho một định lý toán học được đề xuất. Mô tả quy trình và giá trị học thuật.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-14 · Câu gốc 14

Một công ty phát hiện Z3 tìm ra lỗi CHỈ xảy ra với giá trị BIÊN cực đoan (INT_MAX, INT_MIN) mà testing thông thường bỏ sót. Phân tích giá trị của SMT so với testing.

**Trả lời gợi ý gốc:**



#### C3-3.4-thuc_te-15 · Câu gốc 15

Một dự án IoT với vi xử lý yếu không thể chạy Z3 trực tiếp trên thiết bị. Đề xuất chạy verification OFFLINE trên máy phát triển trước khi build.

**Trả lời gợi ý gốc:**



## Mục 3.5: Kiểm chứng mô hình có giới hạn (Bounded Model Checking)

### Tóm tắt kiến thức nguyên bản

Bounded Model Checking (BMC): giới hạn số lần unroll vòng lặp thành một hằng số k, quy toàn bộ bài toán kiểm chứng về công thức SAT/SMT. CBMC là công cụ BMC cho C/C++: cờ --unwind k giới hạn unroll tối đa k lần (quy tắc kinh nghiệm: k = số lần lặp tối đa + 1); --unwinding-assertions kiểm tra bound đã ĐỦ hay chưa (nếu thiếu, CBMC có thể báo SUCCESSFUL sai lầm dù chưa xét đủ vòng lặp). Các cờ kiểm tra thuộc tính: --bounds-check (truy cập ngoài biên mảng/con trỏ), --pointer-check (NULL deref, dangling), --div-by-zero-check, --signed-overflow-check. nondet_int() biểu diễn giá trị bất kỳ; __CPROVER_assume(cond) thêm giả thiết giới hạn không gian tìm kiếm. CBMC sound TRONG GIỚI HẠN bound đã unwind: kết quả “VERIFICATION SUCCESSFUL” (hay “0 of N failed”) nghĩa là KHÔNG có lỗi TRONG PHẠM VI đã kiểm tra, KHÔNG phải tuyệt đối trên mọi trường hợp. CBMC khác NuSMV/SPIN (Ch.1.5): nhận trực tiếp mã C, KHÔNG cần xây mô hình Kripke thủ công. Giới hạn chính: không mở rộng tốt cho hệ thống LỚN (state explosion tương tự Ch.1.5) – nên áp dụng CI/CD cho module lõi, tới hạn (parser, crypto) thay vì toàn bộ codebase. Nhờ symbolic execution tuần tự chính xác, CBMC vừa field-sensitive vừa flow-sensitive (Ch.3.2). cbmc --arch x86_64 chỉ định kiến trúc đích để mô hình hóa alignment/kích thước đúng.

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C3-3.5-trac_nghiem-01 · Câu gốc 1

Bounded Model Checking (BMC) là gì?

**A.** Giới hạn số lần unroll vòng lặp, quy về SAT/SMT

**B.** Kiểm tra không giới hạn số vòng lặp

**C.** Không liên quan tới SAT/SMT

**D.** Chỉ áp dụng cho Java

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-02 · Câu gốc 2

CBMC là công cụ dùng cho ngôn ngữ nào?

**A.** Java

**B.** C (và C++ ở mức độ nhất định)

**C.** Python

**D.** JavaScript

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-03 · Câu gốc 3

Cờ --unwind k trong CBMC dùng để làm gì?

**A.** Giới hạn số lần unroll vòng lặp tối đa là k

**B.** Tăng tốc độ biên dịch

**C.** Không có tác dụng gì

**D.** Chỉ dùng cho đệ quy

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-04 · Câu gốc 4

Nếu vòng lặp chạy tối đa 5 lần, cần --unwind bao nhiêu để đủ?

**A.** 5

**B.** Ít nhất 6

**C.** 1

**D.** Không cần unwind

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-05 · Câu gốc 5

--unwinding-assertions dùng để làm gì?

**A.** Kiểm tra xem bound đã unwind có ĐỦ hay chưa

**B.** Tắt toàn bộ kiểm tra

**C.** Chỉ áp dụng cho biến số nguyên

**D.** Không có tác dụng gì

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-06 · Câu gốc 6

Nếu KHÔNG dùng --unwinding-assertions, CBMC có thể báo gì SAI LẦM?

**A.** ”VERIFICATION SUCCESSFUL” dù chưa xét đủ số vòng lặp

**B.** Luôn báo FAILURE

**C.** Luôn crash

**D.** Không có rủi ro gì

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-07 · Câu gốc 7

--bounds-check trong CBMC kiểm tra gì?

**A.** Truy cập mảng/con trỏ ngoài biên object

**B.** Kiểm tra cú pháp

**C.** Kiểm tra tốc độ

**D.** Không liên quan tới bộ nhớ

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-08 · Câu gốc 8

--pointer-check trong CBMC kiểm tra gì?

**A.** Các vấn đề liên quan con trỏ (NULL deref, dangling...)

**B.** Chỉ kiểm tra kiểu dữ liệu

**C.** Không liên quan tới con trỏ

**D.** Chỉ dùng cho mảng

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-09 · Câu gốc 9

--div-by-zero-check trong CBMC dùng để làm gì?

**A.** Kiểm tra phép chia cho 0

**B.** Kiểm tra tốc độ

**C.** Không có tác dụng gì

**D.** Chỉ dùng cho số thực

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-10 · Câu gốc 10

Trong ví dụ off-by-one write_n, CBMC báo lỗi tại đâu?

**A.** Dòng gán buffer[i]=i khi i vượt biên

**B.** Dòng khai báo buffer

**C.** Không báo lỗi gì

**D.** Chỉ báo lỗi ở hàm main

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-11 · Câu gốc 11

--malloc-may-fail --malloc-fail-null dùng để làm gì?

**A.** Yêu cầu CBMC xét cả trường hợp malloc thất bại (trả NULL)

**B.** Tắt malloc hoàn toàn

**C.** Không có tác dụng gì

**D.** Chỉ áp dụng cho calloc

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-12 · Câu gốc 12

CBMC dùng nondet_int() để làm gì?

**A.** Biểu diễn giá trị ”bất kỳ” (không xác định) cho biến int

**B.** Sinh số ngẫu nhiên có seed cố định

**C.** Không có ý nghĩa gì

**D.** Chỉ dùng cho debug

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-13 · Câu gốc 13

__CPROVER_assume(cond) dùng để làm gì?

**A.** Thêm giả thiết (assumption) giới hạn không gian tìm kiếm

**B.** Xóa toàn bộ điều kiện

**C.** Không có tác dụng gì

**D.** Chỉ dùng cho vòng lặp

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-14 · Câu gốc 14

CBMC là sound trong điều kiện nào?

**A.** Sound tuyệt đối trong mọi trường hợp

**B.** Sound TRONG GIỚI HẠN bound đã unwind

**C.** Không bao giờ sound

**D.** Chỉ sound với số thực

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.5-trac_nghiem-15 · Câu gốc 15

Nếu CBMC báo ”unwinding assertion FAILURE”, điều đó có nghĩa gì?

**A.** Bound hiện tại CHƯA ĐỦ, cần tăng –unwind

**B.** Chương trình chắc chắn có lỗi bảo mật

**C.** Không có ý nghĩa gì

**D.** Cần giảm –unwind

**Đáp án gốc:** A

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C3-3.5-ly_thuyet-01 · Câu gốc 1

Trình bày ý tưởng cốt lõi của Bounded Model Checking: unroll vòng lặp, quy về SAT/SMT.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-02 · Câu gốc 2

Giải thích tại sao BMC chỉ ”sound có điều kiện” (trong bound k đã chọn).

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-03 · Câu gốc 3

Trình bày cờ --unwind, --unwinding-assertions của CBMC và tại sao PHẢI dùng cả hai cùng nhau.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-04 · Câu gốc 4

Giải thích rủi ro khi CBMC báo ”VERIFICATION SUCCESSFUL” nhưng KHÔNG dùng --unwinding-assertions.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-05 · Câu gốc 5

Mô tả các cờ --bounds-check, --pointer-check, --div-by-zero-check và loại lỗi mỗi cờ phát hiện.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-06 · Câu gốc 6

Trình bày ví dụ off-by-one (write_n) và giải thích cách CBMC định vị chính xác dòng lỗi.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-07 · Câu gốc 7

Giải thích nondet_int() và __CPROVER_assume(), cho ví dụ minh họa kiểm tra chia cho 0.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-08 · Câu gốc 8

Bàn luận: tại sao CBMC được coi là bước tiến từ NuSMV/SPIN (Ch.1.5) tới kiểm chứng mã nguồn thực tế?

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-09 · Câu gốc 9

Trình bày quy tắc kinh nghiệm chọn --unwind k phù hợp cho một vòng lặp cụ thể.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-10 · Câu gốc 10

Giải thích giới hạn của CBMC: khi nào KHÔNG có ”unwind k đủ tuyệt đối” (input không giới hạn).

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-11 · Câu gốc 11

Mô tả cách --malloc-may-fail --malloc-fail-null giúp CBMC mô hình hóa ĐÚNG ngữ nghĩa C thực tế.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-12 · Câu gốc 12

Trình bày cách tích hợp CBMC vào CI/CD, chỉ áp dụng cho module LÕI thay vì toàn bộ codebase.

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-13 · Câu gốc 13

Giải thích tại sao CBMC thường CHẬM hơn Cppcheck, liên hệ trade- off Precision/Scalability (Ch.3.2).

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-14 · Câu gốc 14

Bàn luận: CBMC field-sensitive/flow-sensitive như thế nào nhờ symbolic execution tuần tự?

**Trả lời gợi ý gốc:**



#### C3-3.5-ly_thuyet-15 · Câu gốc 15

Trình bày cbmc --arch và tầm quan trọng của việc chỉ định đúng kiến trúc đích (liên hệ Alignment Ch.2.4).

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C3-3.5-thuc_hanh-01 · Câu gốc 1

Chạy cbmc --unwind 6 --function check_sum bmc_demo.c và ghi lại kết quả.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-02 · Câu gốc 2

Chạy lại câu 1 với --unwind 2 --unwinding-assertions, giải thích khác biệt kết quả.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-03 · Câu gốc 3

Chạy cbmc --bounds-check --pointer-check --unwind 12 --function check_overflow bmc_demo.c, ghi lại FAILURE tìm được.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-04 · Câu gốc 4

Sửa lỗi off-by-one trong write_n, chạy lại CBMC xác nhận VERIFICATION SUCCESSFUL.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-05 · Câu gốc 5

Chạy cbmc --div-by-zero-check --function check_divide bmc_demo.c (chưa guard), ghi lại FAILURE.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-06 · Câu gốc 6

Chạy cbmc --div-by-zero-check --function check_divide_guarded bmc_demo.c (đã guard), xác nhận SUCCESSFUL.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-07 · Câu gốc 7

Chạy cbmc --bounds-check --pointer-check --malloc-may-fail --malloc-fail-null --function check_heap bmc_demo.c.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-08 · Câu gốc 8

Dùng Python wrapper run_cbmc() (project) để chạy CBMC trên check_sum, in ra kết quả verification_successful.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-09 · Câu gốc 9

Viết test pytest xác nhận run_cbmc trả về True cho check_overflow_fixed.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-10 · Câu gốc 10

Viết test pytest xác nhận run_cbmc trả về False với failed_properties chứa ”pointer_dereference” cho check_overflow.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-11 · Câu gốc 11

Cho một hàm C mới với vòng lặp chạy đúng 8 lần, chọn --unwind phù hợp và xác nhận bằng --unwinding-assertions.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-12 · Câu gốc 12

Viết hàm C có lỗi UAF, chạy CBMC với --pointer-check để phát hiện.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-13 · Câu gốc 13

Sửa lỗi UAF ở câu 12, chạy lại xác nhận VERIFICATION SUCCESSFUL.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-14 · Câu gốc 14

Viết Makefile với target verify chạy CBMC với cờ đầy đủ trên một hàm chỉ định qua biến FUNC.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_hanh-15 · Câu gốc 15

Chạy CBMC với --arch x86_64 và không chỉ định arch, so sánh kết quả cho một struct có alignment nhạy cảm.

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C3-3.5-thuc_te-01 · Câu gốc 1

Một ngân hàng phát hiện module tính lãi suất có vòng lặp phụ thuộc số ngày (tối đa 366). Đề xuất --unwind phù hợp và giải thích lựa chọn.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-02 · Câu gốc 2

Một công ty phát hiện CBMC báo ”SUCCESSFUL” nhưng KHÔNG dùng --unwinding-assertions, sau đó lỗi vẫn xảy ra production. Phân tích nguyên nhân và bài học.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-03 · Câu gốc 3

Một dự án hàng không cần verify module xử lý dữ liệu cảm biến với input KHÔNG GIỚI HẠN về mặt lý thuyết. Đề xuất chiến lược bound thực tế hợp lý.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-04 · Câu gốc 4

Một tổ chức phát hiện chạy CBMC trên MODULE LỚN (10000 dòng) mất hơn 24 giờ không xong. Đề xuất chia nhỏ phạm vi kiểm chứng.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-05 · Câu gốc 5

Một công ty bảo mật phát hiện một lỗi UAF mà CBMC với --pointer-check đã lẽ ra phát hiện được nếu được chạy sớm hơn. Phân tích quy trình QA thiếu sót.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-06 · Câu gốc 6

Một dự án ô tô yêu cầu CBMC verify module phanh khẩn cấp với TẤT CẢ cờ kiểm tra bật. Đề xuất quy trình CI tích hợp đầy đủ.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-07 · Câu gốc 7

Một tổ chức tài chính phát hiện 2 kỹ sư chọn --unwind KHÁC NHAU cho CÙNG một hàm, dẫn tới kết luận khác nhau. Đề xuất chuẩn hóa quy tắc chọn unwind.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-08 · Câu gốc 8

Một công ty IoT dùng CBMC OFFLINE (không tích hợp CI) do thiết bị tài nguyên hạn chế không thể chạy trực tiếp. Phân tích quy trình verify trước khi flash firmware.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-09 · Câu gốc 9

Một dự án blockchain dùng CBMC để verify smart contract compiler (viết bằng C++) TRƯỚC khi release. Phân tích tầm quan trọng của bước không thể bỏ qua này.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-10 · Câu gốc 10

Một tổ chức y tế cần verify thuật toán tính liều lượng thuốc bằng CBMC. Đề xuất các cờ (--bounds-check, --div-by-zero-check) cần bật và lý do.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-11 · Câu gốc 11

Một công ty phát hiện CBMC KHÔNG THỂ verify một hàm gọi thư viện ngoài không có source code. Đề xuất giải pháp (stub function, hoặc chuyển sang testing).

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-12 · Câu gốc 12

Một dự án quốc phòng yêu cầu MỌI kết quả CBMC phải kèm bằng chứng --unwinding-assertions PASS. Phân tích lý do yêu cầu nghiêm ngặt này.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-13 · Câu gốc 13

Một tổ chức phát hiện việc tăng --unwind từ 10 lên 50 làm lộ ra lỗi MỚI trước đó bị bỏ sót. Phân tích ý nghĩa và đề xuất quy trình tăng dần bound có hệ thống.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-14 · Câu gốc 14

Một công ty game engine cân nhắc dùng CBMC cho physics engine (nhiều vòng lặp phức tạp). Phân tích tính khả thi và giới hạn state explosion.

**Trả lời gợi ý gốc:**



#### C3-3.5-thuc_te-15 · Câu gốc 15

Một dự án hàng không vũ trụ dùng CBMC verify MỌI function trong module điều khiển TRƯỚC KHI phóng. Phân tích lý do đây là cơ hội DUY NHẤT để phát hiện lỗi.

**Trả lời gợi ý gốc:**



## Mục 3.6: Mô hình bộ nhớ (Memory Model)

### Tóm tắt kiến thức nguyên bản

Memory Model trừu tượng cần thiết vì bộ nhớ vật lý thực tế quá chi tiết cho SMT solving. CBMC mô hình hóa mỗi vùng cấp phát (biến local, malloc, mảng toàn cục) như một object riêng biệt (ID, kích thước, trạng thái); con trỏ được biểu diễn bằng cặp (object_id, offset) – ứng với Array Theory (Mục 3.4): object tương ứng mảng, offset tương ứng chỉ số, Select(object, offset) = đọc, Store(object, offset, value) = ghi. Points-to Analysis: xác định tập object mà một con trỏ CÓ THỂ trỏ tới – ứng dụng phát hiện dangling pointer, Use-After-Free (Ch.2.2). Alias Analysis: xác định hai biểu thức con trỏ có thể trỏ CÙNG vùng nhớ hay không; May-alias (CÓ THỂ trỏ cùng chỗ) khác Must-alias (CHẮC CHẮN trỏ cùng chỗ). Alias analysis quá thận trọng (over-approximate) → tăng false positive. Field-sensitive (CBMC): theo dõi RIÊNG từng field của struct, cần biết chính xác offsetof (Ch.2.4) để phát hiện đúng lỗi trên field cụ thể – khác Field-insensitive (Cppcheck heuristic đơn giản) coi cả struct là một object. Flow-sensitive: biết chính xác trạng thái TẠI TỪNG ĐIỂM trong chương trình – giúp CBMC phân biệt “trước free” và “sau free”. Alignment/Padding và Bitfields (Ch.2.4) gây khó khăn cho Memory Model hình thức vì layout phụ thuộc compiler/kiến trúc. Union type punning: cùng một vùng nhớ được diễn giải theo nhiều kiểu dữ liệu khác nhau. Mục 3.6 là nền tảng hội tụ toàn bộ Chương 3: SAT/SMT (3.4) biểu diễn bộ nhớ qua Array Theory, CBMC (3.5) áp dụng mô hình này thực tế, và kết nối sang Chương 4 (hiểu cấu trúc bộ nhớ giúp thiết kế fuzzing harness hiệu quả).

Tóm tắt này được giữ từ HTML; đối chiếu chương lý thuyết và đính chính trước khi dùng như kết luận.

### Trắc nghiệm (15 câu)

#### C3-3.6-trac_nghiem-01 · Câu gốc 1

Vì sao cần một Memory Model trừu tượng cho công cụ phân tích tĩnh?

**A.** Bộ nhớ vật lý thực tế quá chi tiết, cần trừu tượng hóa cho SMT solving

**B.** Không cần thiết, có thể dùng địa chỉ vật lý trực tiếp

**C.** Chỉ để tăng tốc độ biên dịch

**D.** Không liên quan tới SMT

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-02 · Câu gốc 2

CBMC mô hình hóa mỗi vùng nhớ cấp phát như thế nào?

**A.** Một object riêng biệt có ID, kích thước, trạng thái

**B.** Không phân biệt các vùng nhớ

**C.** Chỉ dùng địa chỉ số nguyên đơn giản

**D.** Không mô hình hóa gì

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-03 · Câu gốc 3

Con trỏ trong mô hình CBMC được biểu diễn bằng:

**A.** Chỉ một số nguyên duy nhất

**B.** Cặp (object_id, offset)

**C.** Chuỗi ký tự

**D.** Không biểu diễn được

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-04 · Câu gốc 4

Points-to Analysis xác định điều gì?

**A.** Tập hợp object mà một con trỏ CÓ THỂ trỏ tới

**B.** Giá trị chính xác của con trỏ

**C.** Kích thước của con trỏ

**D.** Không liên quan tới con trỏ

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-05 · Câu gốc 5

Alias Analysis xác định điều gì?

**A.** Hai biểu thức con trỏ có thể trỏ CÙNG vùng nhớ hay không

**B.** Tốc độ truy cập bộ nhớ

**C.** Kích thước bộ nhớ khả dụng

**D.** Không liên quan tới con trỏ

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-06 · Câu gốc 6

Alias Analysis ”quá thận trọng” (over-approximate nhiều) gây ra hậu quả gì?

**A.** Tăng false positive do nghĩ 2 con trỏ alias nhau dù thực tế không

**B.** Không có hậu quả gì

**C.** Luôn giảm false positive

**D.** Tăng tốc độ phân tích

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-07 · Câu gốc 7

CBMC dùng lý thuyết SMT nào để mô hình hóa bộ nhớ?

**A.** Array Theory (Ch.3.4)

**B.** Chỉ dùng số nguyên đơn giản

**C.** Không dùng lý thuyết SMT nào

**D.** Chỉ dùng Boolean logic

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-08 · Câu gốc 8

Select(object, offset) trong mô hình bộ nhớ tương ứng thao tác nào?

**A.** Đọc giá trị tại offset của object

**B.** Ghi giá trị

**C.** Xóa object

**D.** Không có ý nghĩa gì

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-09 · Câu gốc 9

Store(object, offset, value) tương ứng thao tác nào?

**A.** Đọc giá trị

**B.** Ghi giá trị vào offset của object

**C.** Xóa toàn bộ object

**D.** Không có ý nghĩa gì

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-10 · Câu gốc 10

Field-sensitive Analysis theo dõi điều gì khác Field-insensitive?

**A.** Theo dõi RIÊNG từng field của struct thay vì coi cả struct là 1 object

**B.** Không có khác biệt

**C.** Field-insensitive luôn chính xác hơn

**D.** Chỉ áp dụng cho union

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-11 · Câu gốc 11

CBMC có field-sensitive không?

**A.** Không bao giờ

**B.** Có, nhờ mô hình hóa offset chính xác từng field

**C.** Chỉ với mảng, không với struct

**D.** Chỉ với con trỏ NULL

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-12 · Câu gốc 12

Flow-sensitive Analysis có đặc điểm gì?

**A.** Không quan tâm thứ tự câu lệnh

**B.** Biết CHÍNH XÁC trạng thái tại từng điểm cụ thể trong chương trình

**C.** Chỉ áp dụng cho vòng lặp

**D.** Luôn kém chính xác hơn flow-insensitive

**Đáp án gốc:** B

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-13 · Câu gốc 13

CBMC phân biệt được ”trước free” và ”sau free” nhờ tính chất nào?

**A.** Flow-sensitive

**B.** Field-insensitive

**C.** Không phân biệt được

**D.** Chỉ dựa vào tên biến

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-14 · Câu gốc 14

Alignment/Padding (Ch.2.4) liên hệ thế nào với Memory Model của CBMC?

**A.** CBMC cần mô hình hóa CHÍNH XÁC offset để phát hiện đúng lỗi trên struct

**B.** Không liên quan gì

**C.** Chỉ ảnh hưởng tốc độ biên dịch

**D.** Chỉ áp dụng cho Python

**Đáp án gốc:** A

**Giải thích gốc:**



#### C3-3.6-trac_nghiem-15 · Câu gốc 15

cbmc --arch ảnh hưởng thế nào tới Memory Model?

**A.** Không ảnh hưởng gì

**B.** Xác định alignment/kích thước kiểu dữ liệu đúng theo kiến trúc đích

**C.** Chỉ ảnh hưởng tên hàm

**D.** Chỉ dùng cho ARM

**Đáp án gốc:** B

**Giải thích gốc:**



### Lý thuyết (15 câu)

#### C3-3.6-ly_thuyet-01 · Câu gốc 1

Trình bày lý do cần một Memory Model TRỪU TƯỢNG thay vì dùng địa chỉ bộ nhớ vật lý trực tiếp trong công cụ phân tích tĩnh.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-02 · Câu gốc 2

Giải thích cách CBMC mô hình hóa mỗi vùng nhớ cấp phát như một ”object” riêng biệt (ID, kích thước, trạng thái).

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-03 · Câu gốc 3

Mô tả cách con trỏ được biểu diễn trong CBMC qua cặp (object_id, offset).

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-04 · Câu gốc 4

Trình bày Points-to Analysis: định nghĩa, cách hoạt động, và ứng dụng phát hiện UAF/dangling pointer.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-05 · Câu gốc 5

Giải thích Alias Analysis và phân biệt May-alias với Must-alias.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-06 · Câu gốc 6

Bàn luận: tại sao Alias Analysis ”quá thận trọng” (over-approximate) là nguyên nhân phổ biến gây false positive.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-07 · Câu gốc 7

Trình bày cách CBMC dùng Array Theory (Ch.3.4) để mô hình hóa bộ nhớ qua Store/Select.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-08 · Câu gốc 8

Giải thích Field-sensitive Analysis và so sánh với Field-insensitive, cho ví dụ minh họa struct cụ thể.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-09 · Câu gốc 9

Mô tả Flow-sensitive Analysis và giải thích cách nó giúp CBMC phân biệt ”trước free” và ”sau free”.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-10 · Câu gốc 10

Trình bày mối liên hệ giữa Alignment/Padding (Ch.2.4) và độ chính xác của Memory Model trong CBMC.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-11 · Câu gốc 11

Giải thích tác dụng của cbmc --arch trong việc đảm bảo Memory Model đúng theo kiến trúc đích.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-12 · Câu gốc 12

Bàn luận về khó khăn của Bitfields (Ch.2.4) đối với việc xây dựng Memory Model hình thức portable.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-13 · Câu gốc 13

Mô tả Union Type Punning và cách nó thách thức Memory Model (một vùng nhớ, nhiều cách diễn giải).

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-14 · Câu gốc 14

Giải thích tại sao độ chính xác Memory Model ảnh hưởng TRỰC TIẾP tới cả độ chính xác VÀ tốc độ của toàn bộ công cụ phân tích.

**Trả lời gợi ý gốc:**



#### C3-3.6-ly_thuyet-15 · Câu gốc 15

Trình bày cách offsetof (Ch.2.4) được CBMC sử dụng để mô hình hóa CHÍNH XÁC vị trí field trong struct.

**Trả lời gợi ý gốc:**



### Thực hành (15 câu)

#### C3-3.6-thuc_hanh-01 · Câu gốc 1

Viết công thức Z3 dùng Array Theory biểu diễn một object bộ nhớ 32-bit address space, 8-bit value.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-02 · Câu gốc 2

Với struct {char flag; int value;}, viết ra offsetof từng field và giải thích CBMC dùng thông tin này thế nào.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-03 · Câu gốc 3

Viết đoạn code C với 2 con trỏ p,q có thể MAY-alias (tùy điều kiện runtime), minh họa bằng if/else.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-04 · Câu gốc 4

Cho code câu 3, dùng Z3 kiểm tra xem p,q CÓ THỂ trỏ cùng địa chỉ trong TRƯỜNG HỢP CỤ THỂ nào.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-05 · Câu gốc 5

Chạy CBMC trên hàm dùng union type punning, quan sát cách CBMC xử lý việc đọc lại dữ liệu qua kiểu khác.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-06 · Câu gốc 6

Viết đoạn code C minh họa Points-to: con trỏ p trỏ tới biến a hoặc b tùy điều kiện, liệt kê Points-to(p).

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-07 · Câu gốc 7

Chạy cbmc --arch x86_64 và cbmc --arch arm64 (nếu khả dụng) trên MỘT struct có bitfields, so sánh kết quả.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-08 · Câu gốc 8

Viết hàm C có lỗi off-by-one TRÊN MỘT FIELD CỤ THỂ của struct (không phải biến đơn), chạy CBMC field-sensitive xác nhận phát hiện đúng field.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-09 · Câu gốc 9

Cho một hàm free() một con trỏ rồi dùng lại (UAF), chạy CBMC với --pointer-check, xác nhận nó phân biệt trước/sau free (flow-sensitive).

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-10 · Câu gốc 10

Viết công thức Z3 Array Theory mô hình hóa memcpy: ghi N byte từ nguồn sang đích.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-11 · Câu gốc 11

Cho struct với padding, viết code C memset trước khi ghi, chạy CBMC xác nhận không có ”uninitialized” warning trên vùng padding.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-12 · Câu gốc 12

Thiết kế 2 phiên bản alias analysis (đơn giản/chính xác) cho cùng đoạn code, so sánh số false positive.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-13 · Câu gốc 13

Viết hàm C với con trỏ tới struct lồng nhau (struct trong struct), tính offsetof cho field trong struct con.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-14 · Câu gốc 14

Chạy CBMC trên hàm dùng cast pointer giữa 2 kiểu KHÔNG tương thích kích thước, quan sát cảnh báo (nếu có).

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_hanh-15 · Câu gốc 15

Viết một bảng minh họa Field-sensitive: struct 3 field, mỗi field theo dõi riêng, so với field-insensitive coi cả struct 1 object.

**Trả lời gợi ý gốc:**



### Tình huống thực tế (15 câu)

#### C3-3.6-thuc_te-01 · Câu gốc 1

Một công ty phát hiện một lỗi UAF chỉ xảy ra trên MỘT FIELD cụ thể của struct lớn, Cppcheck (field-insensitive) bỏ sót. Đề xuất dùng CBMC field-sensitive để xác định chính xác.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-02 · Câu gốc 2

Một tổ chức phát hiện kết quả CBMC KHÁC NHAU giữa kiến trúc x86_64 và ARM cho cùng module (do alignment). Phân tích và đề xuất verify riêng từng kiến trúc đích production.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-03 · Câu gốc 3

Một dự án dùng UNION type punning để tối ưu hiệu năng, gặp lỗi khó hiểu trên các platform khác nhau. Phân tích rủi ro Memory Model không nhất quán.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-04 · Câu gốc 4

Một công ty bảo mật phát hiện Alias Analysis quá thận trọng khiến báo cáo HÀNG NGHÌN false positive về ”có thể alias”. Đề xuất tinh chỉnh độ chính xác.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-05 · Câu gốc 5

Một tổ chức tài chính cần verify một struct giao dịch phức tạp (nhiều field lồng nhau) bằng CBMC. Đề xuất chiến lược verify từng field quan trọng riêng biệt.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-06 · Câu gốc 6

Một dự án ô tô phát hiện lỗi Points-to Analysis không chính xác dẫn tới bỏ sót một UAF nghiêm trọng trong module điều khiển. Phân tích và đề xuất bổ sung kỹ thuật khác.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-07 · Câu gốc 7

Một công ty game engine dùng type punning rộng rãi cho tối ưu vector math (float/int). Phân tích rủi ro Memory Model và đề xuất kiểm tra kỹ trước khi deploy đa platform.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-08 · Câu gốc 8

Một tổ chức phát hiện CBMC verify một struct packet network SAI do KHÔNG chỉ định đúng --arch. Phân tích hậu quả và đề xuất chuẩn hóa quy trình verify.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-09 · Câu gốc 9

Một dự án hàng không yêu cầu verify MỌI truy cập con trỏ trong module điều khiển với field-sensitive VÀ flow-sensitive đầy đủ. Phân tích chi phí thời gian và đề xuất ưu tiên.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-10 · Câu gốc 10

Một công ty phát hiện một lỗ hổng rò rỉ dữ liệu qua padding (Ch.2.4) mà KHÔNG công cụ nào trong bộ QA hiện tại phát hiện được. Đề xuất bổ sung initialization tracking.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-11 · Câu gốc 11

Một tổ chức nghiên cứu blockchain dùng Memory Model hình thức để verify smart contract compiler xử lý con trỏ ĐÚNG NGỮ NGHĨA C++ phức tạp. Phân tích thách thức.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-12 · Câu gốc 12

Một dự án IoT gặp lỗi CHỈ xảy ra trên thiết bị thực tế (kiến trúc ARM) nhưng không tái tạo được khi verify trên máy phát triển (x86). Phân tích nguyên nhân alignment.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-13 · Câu gốc 13

Một công ty phần mềm nhúng dùng bitfields cho protocol nội bộ, gặp lỗi không tương thích khi đổi compiler. Đề xuất chuyển sang biểu diễn Memory Model portable hơn.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-14 · Câu gốc 14

Một tổ chức tài chính lớn yêu cầu CHỨNG MINH toàn bộ hệ thống KHÔNG có 2 con trỏ nào alias trái phép (dùng chung buffer không mong muốn). Đề xuất verify bằng SMT.

**Trả lời gợi ý gốc:**



#### C3-3.6-thuc_te-15 · Câu gốc 15

Một dự án AI/ML dùng C cho inference engine, gặp lỗi Memory Model không chính xác khi xử lý tensor đa chiều (nhiều lớp con trỏ). Phân tích độ phức tạp.

**Trả lời gợi ý gốc:**
