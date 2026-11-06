# Chương 2: Lập trình C an toàn – Quản lý bộ nhớ: ngân hàng câu hỏi gốc

**270câu.** Nguồn: `De-On-Tap.htm`, trường `QUIZ_DATA`; file `on-tap-an-toan-phan-mem_rutgon.html` giống byte. Đáp án/giải thích giữ theo nguồn, không mặc nhiên đã được xác minh.

[Mục lục ngân hàng](../11_Ngan_hang_cau_hoi.md) · [Đính chính](../08_Dinh_chinh_va_gioi_han.md)

Các đoạn nguồn có code/Markdown không hoàn chỉnh được đặt trong khối text để bảo toàn nội dung. Số thứ tự gốc có thể bắt đầu lại ở từng mục; ID bên dưới là duy nhất theo chương/mục/loại.

## Mục 2.1: Đánh giá rủi ro (Risk Assessment)

### Trắc nghiệm (9 câu)

#### C2-2.1-trac_nghiem-01 · Câu gốc 1

Vì sao C có rủi ro bộ nhớ cao hơn Python/Java?

**A.** C chậm hơn

**B.** Không có garbage collector, không tự động kiểm tra biên mảng

**C.** C không hỗ trợ con trỏ

**D.** C không thể biên dịch được

**Đáp án gốc:** B

**Giải thích gốc:**

Không GC, không tự động kiểm tra biên mảng.

#### C2-2.1-trac_nghiem-02 · Câu gốc 2

Undefined Behavior (UB) trong C nghĩa là gì?

**A.** Compiler được phép làm BẤT KỲ điều gì

**B.** Chương trình luôn crash

**C.** Compiler báo lỗi ngay lập tức

**D.** Không liên quan gì tới an toàn phần mềm

**Đáp án gốc:** A

**Giải thích gốc:**

UB: compiler được phép làm bất kỳ điều gì.

#### C2-2.1-trac_nghiem-03 · Câu gốc 3

Theo số liệu thực tế (Microsoft, Google), tỷ lệ lỗ hổng nghiêm trọng trong C/C++ do memory safety khoảng:

**A.** 10%

**B.** 30%

**C.** 65–70%

**D.** 100%

**Đáp án gốc:** C

**Giải thích gốc:**

Khoảng 65-70% lỗ hổng nghiêm trọng C/C++ là memory safety.

#### C2-2.1-trac_nghiem-04 · Câu gốc 4

Rủi ro của Stack Buffer Overflow từ input mạng thường ở mức nào?

**A.** Thấp

**B.** Trung bình

**C.** Nghiêm trọng

**D.** Không có rủi ro

**Đáp án gốc:** C

**Giải thích gốc:**

Stack overflow từ input mạng: risk nghiêm trọng.

#### C2-2.1-trac_nghiem-05 · Câu gốc 5

Attack surface của chương trình C KHÔNG bao gồm:

**A.** argv/argc

**B.** Biến môi trường

**C.** stdin/mạng

**D.** Comment trong mã nguồn

**Đáp án gốc:** D

**Giải thích gốc:**

Comment trong mã nguồn KHÔNG phải attack surface.

#### C2-2.1-trac_nghiem-06 · Câu gốc 6

Thứ tự mức độ nghiêm trọng tăng dần của hậu quả lỗi bộ nhớ là:

**A.** RCE → Info leak → Crash

**B.** Crash → Info leak → RCE

**C.** Info leak → Crash → RCE

**D.** Không có thứ tự nhất định

**Đáp án gốc:** B

**Giải thích gốc:**

Crash → Info leak → RCE (tăng dần).

#### C2-2.1-trac_nghiem-07 · Câu gốc 7

Risk của một lỗi bộ nhớ trong thư viện dùng chung so với script chạy một lần:

**A.** Thấp hơn

**B.** Cao hơn (ảnh hưởng nhiều nơi sử dụng)

**C.** Bằng nhau

**D.** Không thể so sánh

**Đáp án gốc:** B

**Giải thích gốc:**

Risk cao hơn vì ảnh hưởng nhiều nơi sử dụng.

#### C2-2.1-trac_nghiem-08 · Câu gốc 8

Memory leak (không phải UAF) thường có Impact ở mức nào theo bài giảng?

**A.** Cao (RCE ngay lập tức)

**B.** Trung bình (DoS dài hạn)

**C.** Không có impact

**D.** Luôn nghiêm trọng nhất

**Đáp án gốc:** B

**Giải thích gốc:**

Memory leak: Impact trung bình (DoS dài hạn).

#### C2-2.1-trac_nghiem-09 · Câu gốc 9

Vì sao cần LUÔN kiểm tra giá trị trả về của malloc?

**A.** Để tăng tốc độ chương trình

**B.** Vì malloc có thể thất bại và trả về NULL

**C.** Vì đó là yêu cầu bắt buộc của trình biên dịch

**D.** Không cần thiết trong C hiện đại

**Đáp án gốc:** B

**Giải thích gốc:**

malloc có thể thất bại, trả về NULL.

### Lý thuyết (15 câu)

#### C2-2.1-ly_thuyet-01 · Câu gốc 1

Trình bày các lý do khiến C có rủi ro bộ nhớ cao hơn các ngôn ngữ có garbage collector.

**Trả lời gợi ý gốc:**

C thiếu GC (phải tự malloc/free) và không tự động kiểm tra biên mảng như Python/Java – lỗi index/con trỏ dễ xảy ra và không được ngôn ngữ ngăn chặn.

#### C2-2.1-ly_thuyet-02 · Câu gốc 2

Giải thích khái niệm Undefined Behavior trong C và tại sao nó nguy hiểm về mặt bảo mật.

**Trả lời gợi ý gốc:**

UB nghĩa là hành vi không được đặc tả, compiler được phép tối ưu hóa với giả định UB không xảy ra – có thể dẫn tới hành vi không dự đoán được, kể cả bị kẻ tấn công lợi dụng.

#### C2-2.1-ly_thuyet-03 · Câu gốc 3

Bàn luận về số liệu thực tế cho thấy phần lớn lỗ hổng nghiêm trọng trong C/C++ là lỗi bộ nhớ – điều này có ý nghĩa gì cho việc phân bổ nguồn lực QA?

**Trả lời gợi ý gốc:**

Ý nghĩa: nên ưu tiên phần lớn thời gian/công cụ QA cho việc phát hiện lỗi bộ nhớ (Cppcheck, ASan, CBMC) thay vì dàn trải đều cho mọi loại lỗi.

#### C2-2.1-ly_thuyet-04 · Câu gốc 4

Trình bày cách áp dụng khung Risk = f(Threat, Vulnerability, Impact) cụ thể cho lỗi bộ nhớ trong C.

**Trả lời gợi ý gốc:**

Threat: kẻ tấn công kiểm soát input; Vulnerability: lỗi cụ thể (VD buffer overflow); Impact: mức độ thiệt hại (crash/leak/RCE) – Risk là hàm kết hợp cả ba.

#### C2-2.1-ly_thuyet-05 · Câu gốc 5

Giải thích tại sao Stack Buffer Overflow từ input mạng có risk cao hơn nhiều so với lỗi tương tự trong tool CLI nội bộ.

**Trả lời gợi ý gốc:**

Vì input mạng có thể bị kẻ tấn công BẤT KỲ ĐÂU kiểm soát tùy ý và tự động hóa quy mô lớn, trong khi tool CLI chỉ chạy bởi người vận hành tin cậy cụ thể.

#### C2-2.1-ly_thuyet-06 · Câu gốc 6

Mô tả attack surface điển hình của một chương trình C và liên hệ với khái niệm đã học ở Chương 1.

**Trả lời gợi ý gốc:**

Attack surface: mọi điểm nhận input (argv, env, stdin/mạng, file); liên hệ Attack Surface tổng quát đã học Ch.1.1, áp dụng cụ thể cho ngữ cảnh C.

#### C2-2.1-ly_thuyet-07 · Câu gốc 7

Trình bày phổ mức độ nghiêm trọng của hậu quả lỗi bộ nhớ: Crash, Info leak, RCE.

**Trả lời gợi ý gốc:**

Crash (DoS, ít nghiêm trọng) → Info leak (rò rỉ dữ liệu) → RCE (kiểm soát hoàn toàn, nghiêm trọng nhất).

#### C2-2.1-ly_thuyet-08 · Câu gốc 8

Giải thích vì sao lỗi bộ nhớ trong một thư viện dùng chung có risk cao hơn lỗi tương tự trong ứng dụng độc lập.

**Trả lời gợi ý gốc:**

Vì lỗi trong thư viện dùng chung ảnh hưởng MỌI dự án phụ thuộc vào nó, trong khi lỗi ứng dụng độc lập chỉ ảnh hưởng chính ứng dụng đó.

#### C2-2.1-ly_thuyet-09 · Câu gốc 9

Bàn luận về case study CVE-2021-3156 (Sudo) – bài học gì rút ra cho việc đánh giá rủi ro phần mềm hệ thống nền tảng?

**Trả lời gợi ý gốc:**

Bài học: lỗi đơn giản (thiếu escape ký tự) trong công cụ hệ thống PHỔ BIẾN có thể tồn tại nhiều năm và gây rủi ro cực cao (root escalation) do phạm vi triển khai rộng.

#### C2-2.1-ly_thuyet-10 · Câu gốc 10

Trình bày cách xây dựng một Risk Register cho một dự án C cụ thể.

**Trả lời gợi ý gốc:**

Risk Register: bảng liệt kê từng module/thành phần với Likelihood, Impact, Risk tổng hợp, và biện pháp giảm thiểu – giúp phân bổ nguồn lực QA hợp lý.

#### C2-2.1-ly_thuyet-11 · Câu gốc 11

Giải thích tại sao ”ai kiểm soát input, từ đâu” là câu hỏi cốt lõi khi đánh giá risk của một lỗ hổng.

**Trả lời gợi ý gốc:**

Vì risk phụ thuộc vào AI có thể kiểm soát input và TỪ ĐÂU (Internet công khai risk cao hơn nhiều so với chỉ admin nội bộ).

#### C2-2.1-ly_thuyet-12 · Câu gốc 12

Mô tả vì sao C vẫn được lựa chọn rộng rãi cho OS/firmware dù có rủi ro bộ nhớ cao.

**Trả lời gợi ý gốc:**

C cho hiệu năng cao và kiểm soát bộ nhớ chi tiết cần thiết cho OS/firmware/embedded – đổi lại chấp nhận rủi ro bộ nhớ cao hơn ngôn ngữ có GC.

#### C2-2.1-ly_thuyet-13 · Câu gốc 13

Bàn luận: một lỗi memory leak có nên được coi là ”ít nghiêm trọng” hơn buffer overflow trong mọi trường hợp không?

**Trả lời gợi ý gốc:**

Không nên coi thường tuyệt đối – memory leak dài hạn có thể dẫn tới DoS nghiêm trọng (hệ thống hết bộ nhớ, crash toàn bộ) dù không trực tiếp dẫn tới RCE.

#### C2-2.1-ly_thuyet-14 · Câu gốc 14

Trình bày ma trận Risk Assessment (Likelihood x Impact) và cách áp dụng cho các loại lỗi bộ nhớ khác nhau.

**Trả lời gợi ý gốc:**

Ma trận 3x3 (Likelihood x Impact) với các mức Thấp/TB/Cao, áp dụng: buffer overflow qua mạng (Cao,Cao)=Nghiêm trọng; memory leak nội bộ (Thấp,TB)=Thấp.

#### C2-2.1-ly_thuyet-15 · Câu gốc 15

Giải thích tại sao cùng một lỗi kỹ thuật (VD: buffer overflow) có thể có risk RẤT KHÁC NHAU tùy theo threat model.

**Trả lời gợi ý gốc:**

VD: buffer overflow trong parser xử lý file người dùng upload có risk RẤT CAO; cùng lỗi kỹ thuật trong tool debug nội bộ chỉ risk thấp.

### Thực hành (15 câu)

#### C2-2.1-thuc_hanh-01 · Câu gốc 1

Viết một hàm Python compute_risk(likelihood, impact) trả về nhãn Risk (Thấp/Trung bình/Nghiêm trọng) dựa trên bảng đã học.

**Trả lời gợi ý gốc:**

def compute_risk(l,i): score=l*i; return "Nghiem trong" if score>=6 else "Trung binh" if score>=3 else "Thap".

#### C2-2.1-thuc_hanh-02 · Câu gốc 2

Cho 3 tình huống lỗi bộ nhớ khác nhau, xếp hạng theo Risk Matrix (Likelihood x Impact) và giải thích.

**Trả lời gợi ý gốc:**

VD: (Cao,Cao)=Nghiêm trọng RCE qua mạng; (TB,Cao)=Cao lỗi UAF logging; (Thấp,Thấp)=Thấ lỗi UI.

#### C2-2.1-thuc_hanh-03 · Câu gốc 3

Viết một Risk Register (bảng) cho 4 module giả định của một ứng dụng C: network parser, config loader, logger, crypto module.

**Trả lời gợi ý gốc:**

Bảng: network parser(Nghiêm trọng), config loader(TB), logger(Thấp), crypto(Nghiêm trọng).

#### C2-2.1-thuc_hanh-04 · Câu gốc 4

Cho một hàm C nhận input trực tiếp từ argv, liệt kê attack surface và đánh giá risk sơ bộ.

**Trả lời gợi ý gốc:**

Attack surface: argv[1], argv[2]...; risk phụ thuộc: ai chạy chương trình này và với quyền gì.

#### C2-2.1-thuc_hanh-05 · Câu gốc 5

Viết đoạn mô tả CVSS vector giả định (AV, AC, PR) cho một lỗi buffer overflow qua API công khai.

**Trả lời gợi ý gốc:**

AV:N (qua API mạng), AC:L (dễ khai thác), PR:N (không cần đăng nhập) – điểm CVSS ước tính rất cao (8-10).

#### C2-2.1-thuc_hanh-06 · Câu gốc 6

Thiết kế một checklist (5 mục) đánh giá risk trước khi merge code C mới vào nhánh chính.

**Trả lời gợi ý gốc:**

Checklist: (1) Đã chạy Cppcheck? (2) Đã check malloc NULL? (3) Input đã validate? (4) Test case biên đã có? (5) Risk level đã xác định?

#### C2-2.1-thuc_hanh-07 · Câu gốc 7

Cho một chương trình C xử lý file cấu hình cục bộ, đánh giá risk so với chương trình xử lý input mạng tương tự.

**Trả lời gợi ý gốc:**

File cấu hình cục bộ: risk thấp hơn (chỉ admin sửa được); input mạng: risk cao hơn (bất kỳ ai cũng gửi được). 4

#### C2-2.1-thuc_hanh-08 · Câu gốc 8

Viết một hàm Python phân loại danh sách lỗ hổng theo mức Risk và sắp xếp giảm dần.

**Trả lời gợi ý gốc:**

sorted(vulns, key=lambda v: v.risk_score, reverse=True).

#### C2-2.1-thuc_hanh-09 · Câu gốc 9

Cho tình huống CVE-2021-3156, viết một bảng phân tích Risk (Threat, Vulnerability, Impact) theo khung đã học.

**Trả lời gợi ý gốc:**

Threat: kẻ tấn công local có shell access; Vulnerability: heap overflow trong xử lý escape; Impact: leo thang lên root – Risk: Nghiêm trọng dù cần điều kiện local trước.

#### C2-2.1-thuc_hanh-10 · Câu gốc 10

Thiết kế 3 câu hỏi cần đặt ra khi đánh giá attack surface của một daemon C mới.

**Trả lời gợi ý gốc:**

Câu hỏi: (1) Cổng nào đang mở? (2) Giao thức nào được hỗ trợ? (3) Ai/từ đâu có thể kết nối tới?

#### C2-2.1-thuc_hanh-11 · Câu gốc 11

Viết một đoạn mã C minh họa thiếu kiểm tra malloc, sau đó đánh giá risk của lỗi này. 5

**Trả lời gợi ý gốc:**

int *p = malloc(sizeof(int)); *p = 5; – risk: Nghiêm trọng nếu p thường xuyên NULL do hệ thống thiếu RAM.

#### C2-2.1-thuc_hanh-12 · Câu gốc 12

Cho một thư viện C được 1000+ dự án phụ thuộc, viết phân tích risk so với thư viện chỉ 1 dự án dùng.

**Trả lời gợi ý gốc:**

Thư viện 1000+ dự án: risk RẤT CAO (một lỗi ảnh hưởng toàn bộ hệ sinh thái); thư viện 1 dự án: risk thấp hơn nhiều (phạm vi hẹp).

#### C2-2.1-thuc_hanh-13 · Câu gốc 13

Thiết kế bảng so sánh Risk giữa: (a) UAF trong module core, (b) memory leak trong module logging.

**Trả lời gợi ý gốc:**

Bảng: UAF module core(Nghiêm trọng, ảnh hưởng trực tiếp chức năng chính); leak module logging(Trung bình, chỉ gây DoS dài hạn).

#### C2-2.1-thuc_hanh-14 · Câu gốc 14

Viết một đoạn Python đọc danh sách CVE (giả định JSON) và tính điểm risk trung bình theo CVSS.

**Trả lời gợi ý gốc:**

avg_risk = sum(cve["cvss"] for cve in cves) / len(cves).

#### C2-2.1-thuc_hanh-15 · Câu gốc 15

Cho một API HTTPS nhận JSON payload, liệt kê toàn bộ attack surface liên quan tới xử lý bộ nhớ C phía backend.

**Trả lời gợi ý gốc:**

Attack surface: JSON payload fields, Content-Length header, Content-Type header, nested object depth.

### Tình huống thực tế (15 câu)

#### C2-2.1-thuc_te-01 · Câu gốc 1

Một công ty phát hiện thư viện C lõi của họ (dùng bởi 50 sản phẩm) có lỗ hổng UAF. Phân tích risk và đề xuất chiến lược vá lỗi trên diện rộng. 6

**Trả lời gợi ý gốc:**

Risk cực cao do ảnh hưởng 50 sản phẩm; chiến lược: vá thư viện lõi TRƯỚC, sau đó rebuild/redeploy TOÀN BỘ 50 sản phẩm theo lịch ưu tiên (internet-facing trước).

#### C2-2.1-thuc_te-02 · Câu gốc 2

Một startup IoT dùng C cho firmware thiết bị không thể cập nhật OTA. Phân tích risk dài hạn của quyết định này.

**Trả lời gợi ý gốc:**

Risk dài hạn rất cao: lỗ hổng phát hiện sau này KHÔNG THỂ vá được trên thiết bị đã bán – cần thiết kế lại có OTA update ngay từ đầu cho sản phẩm tương lai.

#### C2-2.1-thuc_te-03 · Câu gốc 3

Một tổ chức phát hiện daemon C xử lý thanh toán (payment) có lỗi buffer overflow tiềm ẩn nhưng chưa xác nhận khai thác được. Đề xuất mức độ ưu tiên xử lý.

**Trả lời gợi ý gốc:**

Ưu tiên cao dù chưa xác nhận khai thác được – module thanh toán luôn risk cao, nên audit/vá phòng ngừa ngay cả khi chưa có bằng chứng exploit cụ thể.

#### C2-2.1-thuc_te-04 · Câu gốc 4

Một công ty game phát hiện lỗi memory leak trong server game online, gây crash sau 48h chạy liên tục. Phân tích risk và đề xuất giải pháp tạm thời.

**Trả lời gợi ý gốc:**

Giải pháp tạm: restart định kỳ service (workaround), đồng thời điều tra bằng Valgrind để tìm root cause và vá triệt để.

#### C2-2.1-thuc_te-05 · Câu gốc 5

Một dự án mã nguồn mở phổ biến (như OpenSSL) phát hiện lỗi tương tự Heartbleed. Phân tích vì sao risk lại cực kỳ cao dù lỗi ”chỉ” là thiếu kiểm tra độ dài.

**Trả lời gợi ý gốc:**

Risk cực cao vì: (1) OpenSSL dùng RẤT RỘNG RÃI, (2) lỗi đơn giản (thiếu length check) nhưng hậu quả nghiêm trọng (rò rỉ khóa riêng) – minh chứng ”lỗi nhỏ, impact khổng lồ”.

#### C2-2.1-thuc_te-06 · Câu gốc 6

Một công ty ô tô phát hiện module điều khiển (viết bằng C) có lỗi bộ nhớ tiềm ẩn nhưng chỉ kích hoạt trong điều kiện cực hiếm. Phân tích risk theo an toàn tính mạng.

**Trả lời gợi ý gốc:**

Risk theo an toàn tính mạng luôn ở mức CAO NHẤT dù likelihood thấp (điều kiện hiếm) – ngành ô tô cần formal verification bất kể tần suất xảy ra thực tế.

#### C2-2.1-thuc_te-07 · Câu gốc 7

Một tổ chức tài chính dùng thư viện C cũ (không còn bảo trì) cho module tính toán lãi suất. Đề xuất đánh giá risk và hướng xử lý.

**Trả lời gợi ý gốc:**

Đề xuất: đánh giá risk cao do thư viện không còn ai vá (nếu có lỗ hổng mới sẽ tồn tại vĩnh viễn); nên thay thế bằng thư viện đang bảo trì hoặc audit/fork tự vá.

#### C2-2.1-thuc_te-08 · Câu gốc 8

Một công ty phát hiện lỗ hổng UAF trong module xử lý log, KHÔNG ảnh hưởng tới dữ liệu khách hàng trực tiếp. Phân tích risk thực tế so với lỗi trong module thanh toán.

**Trả lời gợi ý gốc:**

Risk thực tế THẤP HƠN module thanh toán nhiều (dù cùng loại lỗi UAF) vì không trực tiếp ảnh hưởng dữ liệu/tiền của khách hàng – vẫn cần vá nhưng có thể ưu tiên thấp hơn.

#### C2-2.1-thuc_te-09 · Câu gốc 9

Một hacker mũ trắng báo cáo lỗ hổng buffer overflow trong API công khai của một ngân hàng. Đề xuất quy trình đánh giá risk và phản hồi.

**Trả lời gợi ý gốc:**

Quy trình: xác nhận lỗ hổng (không tự khai thác thêm), đánh giá CVSS+impact thực tế, thông báo nội bộ khẩn, phát triển vá, test kỹ, deploy, cảm ơn/thưởng người báo cáo.

#### C2-2.1-thuc_te-10 · Câu gốc 10

Một tổ chức phát hiện toàn bộ hệ thống dùng chung một phiên bản thư viện C có CVE nghiêm trọng (tương tự Baron Samedit). Đề xuất chiến lược vá lỗi quy mô lớn.

**Trả lời gợi ý gốc:**

Chiến lược: kiểm kê TOÀN BỘ hệ thống dùng phiên bản lỗi (inventory), ưu tiên vá hệ thống internet-facing trước, dùng automation để vá hàng loạt, theo dõi tiến độ.

#### C2-2.1-thuc_te-11 · Câu gốc 11

Một công ty phát triển thiết bị y tế dùng C cho phần mềm điều khiển. Phân tích risk và đề xuất mức độ kiểm chứng cần thiết (liên hệ Ch.1.4).

**Trả lời gợi ý gốc:**

Risk cực cao (an toàn tính mạng trực tiếp); đề xuất mức kiểm chứng: Formal Verification bắt buộc (liên hệ Common Criteria/DO-178C tương đương ngành y tế: FDA class III).

#### C2-2.1-thuc_te-12 · Câu gốc 12

Một dự án drone giao hàng phát hiện lỗi bộ nhớ trong module xử lý tín hiệu GPS. Phân tích risk khi drone hoạt động trong khu vực đông dân cư.

**Trả lời gợi ý gốc:**

Risk cực cao khi hoạt động khu đông dân cư (tăng Impact); đề xuất: formal verification cho module GPS + redundancy (dự phòng) + fail-safe (hạ cánh khẩn cấp khi lỗi).

#### C2-2.1-thuc_te-13 · Câu gốc 13

Một công ty phát hiện tool nội bộ (chỉ admin dùng) có lỗi buffer overflow nghiêm trọng về mặt kỹ thuật. Phân tích vì sao risk thực tế có thể thấp hơn CVSS score.

**Trả lời gợi ý gốc:**

Risk THỰC TẾ thấp hơn CVSS thuần túy vì: chỉ admin tin cậy chạy tool, không expose ra ngoài – CVSS không tính tới ngữ cảnh triển khai cụ thể.

#### C2-2.1-thuc_te-14 · Câu gốc 14

Một tổ chức chính phủ phát hiện hệ thống bỏ phiếu điện tử (viết bằng C) có lỗ hổng bộ nhớ. Phân tích risk đặc thù của hệ thống này.

**Trả lời gợi ý gốc:**

Risk đặc thù: cần đảm bảo Integrity TUYỆT ĐỐI (không thể sửa phiếu bầu) + Confidentiality (ẩn danh) – lỗi bộ nhớ có thể vi phạm CẢ HAI đồng thời, risk cực cao.

#### C2-2.1-thuc_te-15 · Câu gốc 15

Một công ty cloud phát hiện hypervisor (viết bằng C/C++) có lỗi UAF cho phép thoát khỏi VM (VM escape). Phân tích risk cực cao của loại lỗi này.

**Trả lời gợi ý gốc:**

````text
Risk cực cao (CVSS thường 9.0+) vì VM escape phá vỡ toàn bộ mô hình cô lập (isolation) của cloud, ảnh hưởng MỌI khách hàng dùng chung hypervisor. 6

```
MỤC 2.2 – CẤU TRÚC DỮ LIỆU ĐỘNG (DYNAMIC DATA
```

STRUCTURES) – An toàn phần mềm
````

## Mục 2.2: Cấu trúc dữ liệu động (Dynamic Data Structures)

### Trắc nghiệm (9 câu)

#### C2-2.2-trac_nghiem-01 · Câu gốc 1

Stack và Heap khác nhau chủ yếu ở điểm nào?

**A.** Stack cấp phát tự động, Heap cấp phát thủ công

**B.** Stack chậm hơn Heap

**C.** Heap luôn nhỏ hơn Stack

**D.** Không có khác biệt thực sự

**Đáp án gốc:** A

**Giải thích gốc:**

Stack tự động, Heap thủ công.

#### C2-2.2-trac_nghiem-02 · Câu gốc 2

Kích thước Stack thường có đặc điểm gì?

**A.** Không giới hạn

**B.** Giới hạn (thường vài MB)

**C.** Luôn lớn hơn Heap

**D.** Bằng đúng kích thước RAM

**Đáp án gốc:** B

**Giải thích gốc:**

````text
Stack giới hạn (vài MB). 7

```
MỤC 2.2 – CẤU TRÚC DỮ LIỆU ĐỘNG (DYNAMIC DATA
```

STRUCTURES) – An toàn phần mềm
````

#### C2-2.2-trac_nghiem-03 · Câu gốc 3

Lỗi điển hình của Heap là gì?

**A.** Chỉ có stack overflow

**B.** UAF, double- free, memory leak

**C.** Không có lỗi nào

**D.** Chỉ liên quan tới tốc độ

**Đáp án gốc:** B

**Giải thích gốc:**

Heap: UAF, double-free, memory leak.

#### C2-2.2-trac_nghiem-04 · Câu gốc 4

Sau khi gọi malloc, điều đầu tiên cần làm là gì?

**A.** Dùng ngay con trỏ trả về

**B.** Kiểm tra con trỏ có NULL không

**C.** Gọi free() ngay lập tức

**D.** In giá trị con trỏ ra màn hình

**Đáp án gốc:** B

**Giải thích gốc:**

Kiểm tra NULL sau malloc.

#### C2-2.2-trac_nghiem-05 · Câu gốc 5

realloc(p, new_size) nếu thất bại sẽ:

**A.** Trả về NULL, vùng nhớ CŨ vẫn còn nguyên

**B.** Tự động giải phóng vùng nhớ cũ

**C.** Luôn thành công

**D.** Làm crash chương trình ngay lập tức

**Đáp án gốc:** A

**Giải thích gốc:**

realloc thất bại: trả NULL, vùng cũ còn nguyên.

#### C2-2.2-trac_nghiem-06 · Câu gốc 6

Lỗi kinh điển với realloc là gì?

**A.** Gán trực tiếp p = realloc(p, size) làm mất con trỏ cũ nếu thất bại

**B.** Không thể dùng realloc trong

**C.** C. realloc luôn nhanh hơn malloc

**D.** realloc không tồn tại trong chuẩn C

**Đáp án gốc:** A

**Giải thích gốc:**

Gán trực tiếp p=realloc(p,size) mất con trỏ cũ nếu fail.

#### C2-2.2-trac_nghiem-07 · Câu gốc 7

Use-After-Free (UAF) xảy ra khi nào?

**A.** Trước khi gọi malloc

**B.** Truy cập vùng nhớ SAU KHI đã free

**C.** Khi chương trình khởi động

**D.** Chỉ xảy ra với biến toàn cục

**Đáp án gốc:** B

**Giải thích gốc:**

UAF: truy cập sau khi free.

#### C2-2.2-trac_nghiem-08 · Câu gốc 8

Trong hàm free_list, lỗi UAF điển hình là gì?

**A.** free(current); current = current->next;

**B.** next = current->next; free(current); current = next;

**C.** Không free node nào cả

**D.** Free hai lần liên tiếp cùng node

**Đáp án gốc:** A

**Giải thích gốc:**

free(current); current=current->next; là UAF.

#### C2-2.2-trac_nghiem-09 · Câu gốc 9

Memory Leak xảy ra khi nào?

**A.** Khi free() được gọi đúng cách

**B.** Khi mất con trỏ tới vùng nhớ đã cấp phát mà chưa free

**C.** Khi chương trình chạy quá nhanh

**D.** Chỉ xảy ra trên Windows

**Đáp án gốc:** B

**Giải thích gốc:**

Mất con trỏ tới vùng đã cấp phát chưa free.

### Lý thuyết (15 câu)

#### C2-2.2-ly_thuyet-01 · Câu gốc 1

Trình bày sự khác biệt giữa Stack và Heap về cách cấp phát, giải phóng, và lỗi điển hình.

**Trả lời gợi ý gốc:**

Stack: cấp phát/giải phóng tự động theo scope hàm, nhanh, giới hạn kích thước, lỗi: stack overflow; Heap: thủ công malloc/free, linh hoạt, lỗi: UAF/leak/double- free.

#### C2-2.2-ly_thuyet-02 · Câu gốc 2

Giải thích vì sao luôn cần kiểm tra kết quả trả về của malloc trước khi sử dụng.

**Trả lời gợi ý gốc:**

Vì malloc có thể THẤT BẠI (hết bộ nhớ) và trả về NULL – dùng con trỏ NULL mà không kiểm tra sẽ gây crash (NULL deref).

#### C2-2.2-ly_thuyet-03 · Câu gốc 3

Mô tả cấu trúc Linked List cơ bản trong C và giải thích cách cấp phát/giải phóng đúng cách.

**Trả lời gợi ý gốc:**

````text
Node struct gồm data + con trỏ next; cấp phát bằng malloc kiểm tra NULL; giải phóng bằng free_list lưu next TRƯỚC khi free current để tránh UAF. 8

```
MỤC 2.2 – CẤU TRÚC DỮ LIỆU ĐỘNG (DYNAMIC DATA
```

STRUCTURES) – An toàn phần mềm
````

#### C2-2.2-ly_thuyet-04 · Câu gốc 4

Giải thích lỗi UAF điển hình khi giải phóng Linked List và cách viết đúng free_list.

**Trả lời gợi ý gốc:**

Lỗi: free(current); current=current->next; là UAF vì truy cập current->next SAU KHI free; đúng: lưu next = current->next TRƯỚC, rồi free(current), rồi current=next.

#### C2-2.2-ly_thuyet-05 · Câu gốc 5

Trình bày định nghĩa Memory Leak và cho ví dụ code minh họa lỗi này.

**Trả lời gợi ý gốc:**

Memory Leak: vùng nhớ cấp phát nhưng mất tham chiếu (không thể free được nữa). VD: p=malloc(100); p=malloc(200); mất con trỏ tới vùng 100 đầu.

#### C2-2.2-ly_thuyet-06 · Câu gốc 6

Phân biệt Dangling Pointer và Wild Pointer, cho ví dụ mỗi loại.

**Trả lời gợi ý gốc:**

Dangling Pointer: con trỏ TỪNG hợp lệ nhưng vùng nhớ đã bị free; Wild Pointer: con trỏ CHƯA TỪNG khởi tạo, trỏ tới địa chỉ ngẫu nhiên.

#### C2-2.2-ly_thuyet-07 · Câu gốc 7

Giải thích tại sao gán NULL sau free là thực hành tốt để phòng tránh UAF.

**Trả lời gợi ý gốc:**

Vì nếu p vẫn giữ địa chỉ cũ sau free, code sau có thể VÔ TÌNH dùng lại p (UAF); gán NULL khiến mọi truy cập sau đó crash NGAY (dễ debug) thay vì hành vi không xác định.

#### C2-2.2-ly_thuyet-08 · Câu gốc 8

Mô tả cơ chế Double Free và hậu quả tiềm ẩn của nó (liên hệ tới khả năng RCE).

**Trả lời gợi ý gốc:**

Double Free có thể làm HỎNG cấu trúc quản lý heap nội bộ (metadata) của allocator, kẻ tấn công có thể lợi dụng để kiểm soát bộ nhớ tùy ý, dẫn tới RCE.

#### C2-2.2-ly_thuyet-09 · Câu gốc 9

Trình bày ”dòng thời gian” của lỗi UAF: từ malloc, free, tới việc allocator tái sử dụng vùng nhớ.

**Trả lời gợi ý gốc:**

Dòng thời gian: malloc(p)→free(p) trả vùng nhớ về allocator→malloc(q) allocator TÁI SỬ DỤNG cùng vùng nhớ cho object khác→dùng lại p (dangling) thực chất đọc/ghi object mới.

#### C2-2.2-ly_thuyet-10 · Câu gốc 10

Giải thích khái niệm ”type confusion” và tại sao nó khiến UAF trở thành lớp lỗi đặc biệt nguy hiểm.

**Trả lời gợi ý gốc:**

Type confusion: chương trình TƯỞNG đang thao tác object A (qua con trỏ p cũ) nhưng thực chất vùng nhớ đó giờ là object B khác – gây đọc/ghi sai ngữ nghĩa, có thể khai thác.

#### C2-2.2-ly_thuyet-11 · Câu gốc 11

Bàn luận: NULL Pointer Dereference có nguy hiểm bằng UAF/Double- free không? Vì sao?

**Trả lời gợi ý gốc:**

NULL Pointer Dereference thường CHỈ gây crash (ít nguy hiểm hơn UAF/double- free vốn có thể dẫn RCE); tuy vậy vẫn là CWE-476 phổ biến cần tránh vì DoS vẫn có tác động.

#### C2-2.2-ly_thuyet-12 · Câu gốc 12

Trình bày cách cài đặt Dynamic Array (Vector) trong C, tập trung vào việc xử lý realloc an toàn.

**Trả lời gợi ý gốc:**

Cài đặt Vector: mảng động với size/capacity; khi đầy, gọi realloc với capacity mới (thường x2), dùng biến TẠM để kiểm tra realloc thành công trước khi cập nhật con trỏ chính.

#### C2-2.2-ly_thuyet-13 · Câu gốc 13

Giải thích bẫy kinh điển khi dùng realloc và cách viết code an toàn để tránh bẫy này.

**Trả lời gợi ý gốc:**

Bẫy: p=realloc(p,size); nếu thất bại trả NULL, gán trực tiếp làm MẤT con trỏ vùng cũ (leak) và p giờ là NULL (mất toàn bộ dữ liệu); đúng: dùng tmp=realloc(...); if(tmp) p=tmp;

#### C2-2.2-ly_thuyet-14 · Câu gốc 14

So sánh chiến lược tăng trưởng x2 và +N cố định cho Dynamic Array, phân tích độ phức tạp thời gian.

**Trả lời gợi ý gốc:**

x2: số lần realloc là O(log n), tổng chi phí copy O(n) amortized; +N cố định: số lần realloc O(n/N ), tổng chi phí copy O(n2 /N ) – chậm hơn nhiều với n lớn.

#### C2-2.2-ly_thuyet-15 · Câu gốc 15

Mô tả rủi ro bổ sung khi làm việc với Double-linked List so với Single- linked List.

**Trả lời gợi ý gốc:**

````text
Double-linked có CẢ prev và next, mỗi thao tác chèn/xóa cần cập nhật ĐÚNG cả

```
hướng – tăng gấp đôi khả năng sai sót logic con trỏ so với single-linked chỉ có
```

next.
````

### Thực hành (15 câu)

#### C2-2.2-thuc_hanh-01 · Câu gốc 1

Viết hàm C create_node(int value) cấp phát và khởi tạo một node linked list, có kiểm tra NULL.

**Trả lời gợi ý gốc:**

Node* create_node(int v){Node *n=malloc(sizeof(Node)); if(!n)return NULL; n->data=v; n->next=NULL; return n;}

#### C2-2.2-thuc_hanh-02 · Câu gốc 2

Viết hàm free_list(Node *head) giải phóng đúng cách toàn bộ danh sách, tránh UAF.

**Trả lời gợi ý gốc:**

void free_list(Node *h){while(h){Node *nx=h->next; free(h); h=nx;}}

#### C2-2.2-thuc_hanh-03 · Câu gốc 3

Cho đoạn code có lỗi free(current); current = current->next;, sửa lại cho đúng.

**Trả lời gợi ý gốc:**

Sửa: Node *nx = current->next; free(current); current = nx;

#### C2-2.2-thuc_hanh-04 · Câu gốc 4

Viết hàm C minh họa memory leak (mất con trỏ khi gán lại mà chưa free) và bản đã sửa.

**Trả lời gợi ý gốc:**

````text
Leak: p=malloc(100); p=malloc(200); mất con trỏ đầu; sửa: free(p); p=malloc(200); free trước khi gán lại. 10

```
MỤC 2.2 – CẤU TRÚC DỮ LIỆU ĐỘNG (DYNAMIC DATA
```

STRUCTURES) – An toàn phần mềm
````

#### C2-2.2-thuc_hanh-05 · Câu gốc 5

Viết đoạn code minh họa dangling pointer và cách sửa bằng cách gán NULL sau free.

**Trả lời gợi ý gốc:**

int *p=malloc(4); free(p); p=NULL; – sau đó mọi truy cập p sẽ crash rõ ràng thay vì UB.

#### C2-2.2-thuc_hanh-06 · Câu gốc 6

Viết đoạn code minh họa double free và giải thích 2 hậu quả có thể xảy ra.

**Trả lời gợi ý gốc:**

free(p); free(p); – hậu quả: (1) crash ngay do heap corruption check, (2) hoặc bị khai thác để ghi tùy ý vào heap metadata.

#### C2-2.2-thuc_hanh-07 · Câu gốc 7

Cài đặt Vector (dynamic array) trong C với hàm vector_push xử lý realloc an toàn.

**Trả lời gợi ý gốc:**

void vector_push(Vector*v,int x){if(v->size==v->cap){...realloc x2...} v->data[v->size++ (đã có sẵn trong slide).

#### C2-2.2-thuc_hanh-08 · Câu gốc 8

Sửa lỗi p = realloc(p, new_size); thành phiên bản an toàn dùng biến tạm.

**Trả lời gợi ý gốc:**

int *tmp=realloc(p,ns); if(tmp) p=tmp; else /*giu p cu, xu ly loi*/.

#### C2-2.2-thuc_hanh-09 · Câu gốc 9

Viết hàm find_and_remove(Node **head, int value) loại bỏ node an toàn khỏi linked list.

**Trả lời gợi ý gốc:**

Node* find_and_remove(Node**h,int v){...} (cài đặt như trong slide 2.2, dùng prev để cập nhật liên kết).

#### C2-2.2-thuc_hanh-10 · Câu gốc 10

Chạy chương trình linked list qua Valgrind (--leak-check=full) và diễn giải output mẫu.

**Trả lời gợi ý gốc:**

Output mẫu: ”definitely lost: 40 bytes in 1 blocks” kèm stack trace dòng malloc gây leak.

#### C2-2.2-thuc_hanh-11 · Câu gốc 11

Cài đặt Hash Table đơn giản với separate chaining (mảng bucket + linked list).

**Trả lời gợi ý gốc:**

Entry *table[SIZE]; void insert(char*k,int v){int idx=hash(k)%SIZE; Entry*e=malloc(...); e->next=table[idx]; table[idx]=e;}

#### C2-2.2-thuc_hanh-12 · Câu gốc 12

````text
Viết hàm giải phóng toàn bộ Hash Table (bao gồm mọi bucket và node bên trong). 11

```
MỤC 2.2 – CẤU TRÚC DỮ LIỆU ĐỘNG (DYNAMIC DATA
```

STRUCTURES) – An toàn phần mềm
````

**Trả lời gợi ý gốc:**

for(i=0;i<SIZE;i++){Entry*e=table[i]; while(e){Entry*nx=e->next; free(e); e=nx;}}

#### C2-2.2-thuc_hanh-13 · Câu gốc 13

Cài đặt Double-linked List với các hàm insert/delete cập nhật ĐÚNG cả prev và next.

**Trả lời gợi ý gốc:**

Insert: cập nhật newNode->prev, newNode->next, prevNode->next, nextNode- >prev – đủ 4 liên kết theo đúng thứ tự.

#### C2-2.2-thuc_hanh-14 · Câu gốc 14

Viết đoạn code duyệt Circular Linked List với điều kiện dừng ĐÚNG (so sánh với head).

**Trả lời gợi ý gốc:**

Node*cur=head; do{process(cur); cur=cur->next;}while(cur!=head);

#### C2-2.2-thuc_hanh-15 · Câu gốc 15

Cho một Circular Linked List với điều kiện dừng SAI, sửa lại và giải thích tại sao lỗi cũ gây lặp vô hạn.

**Trả lời gợi ý gốc:**

Lỗi cũ dùng cur!=NULL (không bao giờ NULL trong circular list) – sửa thành cur!=head để dừng đúng sau 1 vòng.

### Tình huống thực tế (15 câu)

#### C2-2.2-thuc_te-01 · Câu gốc 1

Một công ty phát hiện server C của họ tăng dần bộ nhớ sử dụng suốt nhiều ngày (memory leak). Đề xuất quy trình chẩn đoán bằng Valgrind.

**Trả lời gợi ý gốc:**

Quy trình: chạy Valgrind với --leak-check=full trên workload thực tế trong thời gian dài, phân tích stack trace các leak để xác định module gây leak.

#### C2-2.2-thuc_te-02 · Câu gốc 2

````text
Một ứng dụng crash ngẫu nhiên sau khi chạy vài giờ, nghi ngờ UAF. Đề xuất quy trình debug từng bước. 12

```
MỤC 2.2 – CẤU TRÚC DỮ LIỆU ĐỘNG (DYNAMIC DATA
```

STRUCTURES) – An toàn phần mềm
````

**Trả lời gợi ý gốc:**

Debug UAF: dùng ASan để bắt lỗi ngay khi xảy ra (thay vì đợi crash ngẫu nhiên), kết hợp core dump + gdb để xem stack trace chi tiết.

#### C2-2.2-thuc_te-03 · Câu gốc 3

Một hệ thống game server dùng linked list quản lý người chơi online, gặp crash khi người chơi disconnect đột ngột giữa lúc xử lý. Phân tích khả năng UAF.

**Trả lời gợi ý gốc:**

Khả năng UAF cao: nếu disconnect xử lý xóa dữ liệu người chơi TRONG KHI một luồng khác vẫn đang truy cập – cần đồng bộ hóa (mutex) hoặc dùng reference counting.

#### C2-2.2-thuc_te-04 · Câu gốc 4

Một thư viện C phổ biến bị phát hiện double-free trong một trường hợp edge case hiếm. Phân tích mức độ nghiêm trọng và đề xuất vá.

**Trả lời gợi ý gốc:**

Nghiêm trọng: edge case hiếm vẫn có thể bị khai thác có chủ đích bởi kẻ tấn công biết cách kích hoạt – cần vá ngay dù tần suất tự nhiên thấp.

#### C2-2.2-thuc_te-05 · Câu gốc 5

Một công ty phát hiện Hash Table nội bộ của họ chậm dần theo thời gian dùng, nghi ngờ memory leak khi resize. Đề xuất kiểm tra.

**Trả lời gợi ý gốc:**

Đề xuất: dùng Valgrind định kỳ + theo dõi memory usage theo thời gian (monitoring) để phát hiện xu hướng tăng bất thường khi resize.

#### C2-2.2-thuc_te-06 · Câu gốc 6

Một hệ thống nhúng (embedded, RAM giới hạn 64KB) gặp lỗi hết bộ nhớ sau vài giờ chạy. Phân tích khả năng memory leak và đề xuất công cụ phù hợp (Valgrind có khả dụng trên embedded không?).

**Trả lời gợi ý gốc:**

Valgrind có overhead RAM lớn, khó dùng trực tiếp trên embedded 64KB; đề xuất: dùng static analysis (Cppcheck) kỹ hơn, hoặc test trên simulator/emulator có nhiều RAM hơn trước khi deploy.

#### C2-2.2-thuc_te-07 · Câu gốc 7

Một ứng dụng đa luồng (multi-thread) dùng chung một linked list không có khóa (lock), gặp crash ngẫu nhiên. Phân tích nguyên nhân có thể (race condition + UAF).

**Trả lời gợi ý gốc:**

Race condition kết hợp UAF: một luồng free node trong khi luồng khác đang đọc – cần mutex/lock bảo vệ truy cập chung, hoặc dùng lock-free data structure chuyên dụng.

#### C2-2.2-thuc_te-08 · Câu gốc 8

Một dự án mã nguồn mở nhận báo cáo lỗi ”segfault khi xóa item khỏi danh sách”. Đề xuất các bước để tái tạo và debug lỗi.

**Trả lời gợi ý gốc:**

Bước debug: (1) thu thập core dump, (2) chạy dưới Valgrind/ASan để tái tạo, (3) dùng gdb xem stack trace, (4) xác định dòng code gây UAF/double-free.

#### C2-2.2-thuc_te-09 · Câu gốc 9

Một công ty phát hiện dynamic array của họ tốn quá nhiều bộ nhớ do chiến lược tăng trưởng không tối ưu. Đề xuất cải thiện.

**Trả lời gợi ý gốc:**

Đề xuất cải thiện: chuyển sang chiến lược x2 thay vì +N cố định, hoặc cache- friendly resize dựa trên pattern sử dụng thực tế.

#### C2-2.2-thuc_te-10 · Câu gốc 10

Một hệ thống ngân hàng phát hiện double-free trong module xử lý giao dịch dưới tải cao (concurrent). Phân tích mức độ khẩn cấp.

**Trả lời gợi ý gốc:**

Mức độ khẩn cấp CAO NHẤT: double-free dưới tải cao trong module giao dịch tài chính có thể bị khai thác để thao túng số dư – cần vá và deploy khẩn cấp.

#### C2-2.2-thuc_te-11 · Câu gốc 11

Một ứng dụng IoT với circular buffer bị lặp vô hạn trong điều kiện hiếm gặp. Phân tích nguyên nhân và đề xuất sửa.

**Trả lời gợi ý gốc:**

Nguyên nhân: buffer wraparound logic sai (không xử lý đúng khi index quay vòng); sửa: kiểm tra kỹ điều kiện modulo/wraparound trong code.

#### C2-2.2-thuc_te-12 · Câu gốc 12

````text
Một công ty phát hiện memory leak trong code C đã chạy production

```
năm không ai phát hiện. Phân tích vì sao lỗi này ”sống sót” lâu như vậy.
```
````

**Trả lời gợi ý gốc:**

Lý do ”sống sót”: leak nhỏ, không gây crash rõ ràng trong thời gian ngắn, chỉ tích lũy chậm – cần restart định kỳ (workaround) che giấu vấn đề thực sự.

#### C2-2.2-thuc_te-13 · Câu gốc 13

Một ứng dụng xử lý ảnh dùng cấu trúc dữ liệu động cho pixel data, gặp UAF khi resize ảnh giữa chừng. Phân tích và đề xuất sửa.

**Trả lời gợi ý gốc:**

Phân tích: UAF khi resize giữa chừng thường do giữ con trỏ tới buffer CŨ sau khi realloc trả về địa chỉ MỚI; sửa: cập nhật MỌI con trỏ liên quan ngay sau realloc.

#### C2-2.2-thuc_te-14 · Câu gốc 14

Một dự án blockchain node viết bằng C++ gặp lỗi UAF trong cấu trúc dữ liệu quản lý transaction pool. Phân tích mức độ nghiêm trọng.

**Trả lời gợi ý gốc:**

Nghiêm trọng cao: transaction pool là cấu trúc dữ liệu TỚI HẠN của blockchain node, UAF có thể dẫn tới double-spending hoặc DoS toàn mạng.

#### C2-2.2-thuc_te-15 · Câu gốc 15

Một công ty phát hiện thư viện Hash Table bên thứ ba họ dùng có lỗi memory leak đã biết nhưng chưa vá. Đề xuất giải pháp tạm thời.

**Trả lời gợi ý gốc:**

````text
Giải pháp tạm: wrapper/patch riêng để fix leak trong khi chờ thư viện chính thức vá, hoặc chuyển sang thư viện thay thế nếu có. 12

```
MỤC 2.3 – LẬP TRÌNH C AN TOÀN (SECURE C CODING)
```
````

## Mục 2.3: Lập trình C an toàn (Secure C Coding)

### Trắc nghiệm (9 câu)

#### C2-2.3-trac_nghiem-01 · Câu gốc 1

Hàm nào sau đây đã bị loại khỏi chuẩn C11 vì quá nguy hiểm?

**A.** strcpy

**B.** gets

**C.** printf

**D.** malloc

**Đáp án gốc:** B

**Giải thích gốc:**

gets() bị loại khỏi C11.

#### C2-2.3-trac_nghiem-02 · Câu gốc 2

Điểm chung của strcpy, sprintf, strcat là gì? A. Đều tự động kiểm tra kích thước buffer. B. Đều KHÔNG kiểm tra kích thước buffer đích. C. Đều đã bị loại bỏ khỏi C. D. Đều chỉ dùng được với số nguyên.

**Đáp án gốc:** B

**Giải thích gốc:**

Đều không kiểm tra kích thước buffer đích.

#### C2-2.3-trac_nghiem-03 · Câu gốc 3

Hàm nào thay thế an toàn cho gets()?

**A.** scanf()

**B.** fgets()

**C.** strcpy()

**D.** sprintf()

**Đáp án gốc:** B

**Giải thích gốc:**

fgets() thay thế an toàn cho gets().

#### C2-2.3-trac_nghiem-04 · Câu gốc 4

Khi dùng strncpy, cần lưu ý điều gì?

**A.** Không cần lưu ý gì đặc biệt

**B.** Có thể KHÔNG tự thêm null-terminator nếu input vừa khít buffer

**C.** strncpy luôn an toàn tuyệt đối

**D.** strncpy nhanh hơn memcpy trong mọi trường hợp

**Đáp án gốc:** B

**Giải thích gốc:**

strncpy có thể không tự thêm null-terminator.

#### C2-2.3-trac_nghiem-05 · Câu gốc 5

Trong stack layout, Return Address thường nằm ở đâu so với buffer local?

**A.** Trước buffer (địa chỉ thấp hơn)

**B.** Sau buffer, có thể bị ghi đè khi tràn

**C.** Không liên quan gì tới buffer

**D.** Luôn nằm trong heap

**Đáp án gốc:** B

**Giải thích gốc:**

````text
Return Address nằm sau buffer, có thể bị ghi đè. 13

```
MỤC 2.3 – LẬP TRÌNH C AN TOÀN (SECURE C CODING)
```
````

#### C2-2.3-trac_nghiem-06 · Câu gốc 6

Stack Buffer Overflow nguy hiểm nhất khi nào?

**A.** Khi ghi đè được Return Address để kiểm soát luồng thực thi

**B.** Khi chỉ ghi đè biến local khác không quan trọng

**C.** Không bao giờ nguy hiểm

**D.** Chỉ nguy hiểm trên Windows

**Đáp án gốc:** A

**Giải thích gốc:**

Nguy hiểm nhất khi ghi đè Return Address.

#### C2-2.3-trac_nghiem-07 · Câu gốc 7

Integer Overflow trong malloc(count * size) có thể dẫn tới:

**A.** Không có vấn đề gì

**B.** Cấp phát buffer NHỎ HƠN dự kiến, gây heap overflow sau đó

**C.** Luôn làm chương trình nhanh hơn

**D.** Compiler tự động ngăn chặn hoàn toàn

**Đáp án gốc:** B

**Giải thích gốc:**

Integer Overflow gây cấp phát buffer nhỏ hơn dự kiến.

#### C2-2.3-trac_nghiem-08 · Câu gốc 8

calloc(count, size) có ưu điểm gì so với malloc(count*size)?

**A.** Không có ưu điểm gì

**B.** calloc có kiểm tra overflow nội bộ khi nhân

**C.** calloc luôn chậm hơn

**D.** calloc không khởi tạo bộ nhớ

**Đáp án gốc:** B

**Giải thích gốc:**

calloc kiểm tra overflow nội bộ.

#### C2-2.3-trac_nghiem-09 · Câu gốc 9

Format String Vulnerability xảy ra khi nào?

**A.** Khi dùng printf("%s", input)

**B.** Khi dùng printf(input) trực tiếp với input người dùng

**C.** Khi không dùng printf

**D.** Chỉ xảy ra với scanf

**Đáp án gốc:** B

**Giải thích gốc:**

printf(input) trực tiếp là Format String Vuln.

### Lý thuyết (15 câu)

#### C2-2.3-ly_thuyet-01 · Câu gốc 1

Liệt kê các hàm C nguy hiểm kinh điển và giải thích điểm chung khiến chúng nguy hiểm.

**Trả lời gợi ý gốc:**

Hàm nguy hiểm: gets, strcpy, sprintf, strcat – điểm chung: KHÔNG nhận/kiểm tra kích thước buffer đích, ghi tràn nếu input dài hơn dự kiến.

#### C2-2.3-ly_thuyet-02 · Câu gốc 2

Trình bày các hàm thay thế an toàn cho gets, strcpy, sprintf, strcat.

**Trả lời gợi ý gốc:**

Thay thế: gets→fgets(buf,size,stdin); strcpy→strncpy hoặc snprintf; sprintf→snprintf; strcat→strncat với kích thước đúng.

#### C2-2.3-ly_thuyet-03 · Câu gốc 3

Giải thích cơ chế Stack Buffer Overflow ở mức khái niệm, liên hệ với stack layout (buffer, saved FP, return address).

**Trả lời gợi ý gốc:**

Stack layout: buffer local → saved frame pointer → return address; nếu input ghi tràn buffer, dữ liệu tiếp tục ghi đè FP rồi RA, kẻ tấn công có thể kiểm soát địa chỉ nhảy tới khi hàm return.

#### C2-2.3-ly_thuyet-04 · Câu gốc 4

Mô tả cách Integer Overflow trong phép nhân cấp phát bộ nhớ dẫn tới Heap Overflow.

**Trả lời gợi ý gốc:**

````text
Integer Overflow: count*sizeof(int) có thể ”wrap around” thành số RẤT NHỎ nếu count lớn, malloc cấp phát buffer NHỎ nhưng code sau ghi theo count GỐC (lớn) – gây heap overflow. 14

```
MỤC 2.3 – LẬP TRÌNH C AN TOÀN (SECURE C CODING)
```
````

#### C2-2.3-ly_thuyet-05 · Câu gốc 5

Giải thích tại sao calloc an toàn hơn malloc(count*size) tự viết.

**Trả lời gợi ý gốc:**

calloc(count,size) có kiểm tra overflow NỘI BỘ khi nhân hai tham số, trong khi tự viết malloc(count*size) không có bảo vệ này, dễ bị integer overflow.

#### C2-2.3-ly_thuyet-06 · Câu gốc 6

Trình bày Format String Vulnerability và giải thích cơ chế nguy hiểm của specifier %n.

**Trả lời gợi ý gốc:**

Format String Vuln: printf(user_input) dùng input làm FORMAT thay vì DATA; %n đặc biệt nguy hiểm vì GHI số ký tự đã in vào địa chỉ chỉ định bởi tham số tương ứng trên stack, có thể dẫn tới RCE.

#### C2-2.3-ly_thuyet-07 · Câu gốc 7

Mô tả Off-by-one Error và nguyên nhân phổ biến gây ra lỗi này.

**Trả lời gợi ý gốc:**

Off-by-one: thường do nhầm <= với <, hoặc quên chỗ cho null-terminator khi tính kích thước buffer chuỗi – gây ghi/đọc vượt biên đúng 1 phần tử.

#### C2-2.3-ly_thuyet-08 · Câu gốc 8

Giải thích chi tiết cơ chế hoạt động của Stack Canary, bao gồm vai trò của __stack_chk_fail().

**Trả lời gợi ý gốc:**

Stack Canary: compiler chèn giá trị NGẪU NHIÊN trước return address lúc vào hàm, kiểm tra giá trị này KHÔNG ĐỔI trước khi return; nếu đổi (do overflow), gọi __stack_chk_fail() và abort.

#### C2-2.3-ly_thuyet-09 · Câu gốc 9

Trình bày giới hạn của Stack Canary – những loại tấn công nào KHÔNG bị canary ngăn chặn.

**Trả lời gợi ý gốc:**

Giới hạn Canary: chỉ bảo vệ chống ghi tràn TUẦN TỰ từ buffer lên return address; KHÔNG bảo vệ nếu kẻ tấn công ghi TRỰC TIẾP vào địa chỉ tùy ý qua lỗi con trỏ khác.

#### C2-2.3-ly_thuyet-10 · Câu gốc 10

Giải thích ASLR và cách nó kết hợp với DEP/NX để tăng độ khó khai thác.

**Trả lời gợi ý gốc:**

ASLR ngẫu nhiên hóa vị trí stack/heap/thư viện mỗi lần chạy, khiến kẻ tấn công không đoán trước địa chỉ; kết hợp DEP/NX (vùng dữ liệu không thực thi được) buộc kẻ tấn công dùng kỹ thuật phức tạp hơn (ROP).

#### C2-2.3-ly_thuyet-11 · Câu gốc 11

Mô tả FORTIFY_SOURCE và cách nó bảo vệ chương trình ở mức compiler.

**Trả lời gợi ý gốc:**

FORTIFY_SOURCE: compiler thay thế các hàm nguy hiểm (strcpy, sprintf...) bằng phiên bản kiểm tra kích thước RUNTIME dựa trên thông tin biết được lúc biên dịch (VD sizeof buffer).

#### C2-2.3-ly_thuyet-12 · Câu gốc 12

Trình bày các cờ biên dịch GCC quan trọng cho secure coding (-Wall -Wextra -fstack-protector-strong etc).

**Trả lời gợi ý gốc:**

Cờ quan trọng: -Wall -Wextra (cảnh báo tối đa), -fstack-protector-strong (canary), -D_FORTIFY_SOURCE=2 (hàm an toàn), -fsanitize=address,undefined (runtime check khi test).

#### C2-2.3-ly_thuyet-13 · Câu gốc 13

Giải thích AddressSanitizer (ASan) hoạt động như thế nào và khi nào nên/không nên dùng.

**Trả lời gợi ý gốc:**

ASan chèn mã kiểm tra MỖI truy cập bộ nhớ lúc runtime để phát hiện overflow/UAF NGAY khi xảy ra; nên dùng khi TEST (overhead 2-3x chấp nhận được), KHÔNG dùng production (ảnh hưởng hiệu năng).

#### C2-2.3-ly_thuyet-14 · Câu gốc 14

Trình bày các quy tắc CERT C: STR31-C, ARR30-C, MEM31-C, EXP34-C, INT30-C.

**Trả lời gợi ý gốc:**

CERT C: STR31-C (buffer chuỗi đủ lớn), ARR30-C (không vượt biên mảng), MEM31- C (không dùng lại vùng đã free), EXP34-C (không deref NULL), INT30-C (không tràn số nguyên unsigned ngoài ý muốn).

#### C2-2.3-ly_thuyet-15 · Câu gốc 15

Giải thích sự khác biệt giữa strncpy và strlcpy về đảm bảo null- termination.

**Trả lời gợi ý gốc:**

strncpy: KHÔNG tự thêm null-terminator nếu input vừa khít buffer (cần code thủ công đảm bảo); strlcpy: LUÔN null-terminate và trả về độ dài THỰC của nguồn để phát hiện truncation.

### Thực hành (15 câu)

#### C2-2.3-thuc_hanh-01 · Câu gốc 1

Sửa đoạn code dùng gets(buf) thành fgets(buf, sizeof(buf), stdin).

**Trả lời gợi ý gốc:**

fgets(buf, sizeof(buf), stdin); thay cho gets(buf);.

#### C2-2.3-thuc_hanh-02 · Câu gốc 2

Sửa đoạn code strcpy(dst, src) thành phiên bản dùng snprintf an toàn.

**Trả lời gợi ý gốc:**

snprintf(dst, sizeof(dst), "%s", src); thay strcpy(dst,src);.

#### C2-2.3-thuc_hanh-03 · Câu gốc 3

Viết hàm C nối 2 chuỗi an toàn bằng strncat với kiểm tra kích thước đúng.

**Trả lời gợi ý gốc:**

strncat(dst, src, sizeof(dst)-strlen(dst)-1); đảm bảo không tràn.

#### C2-2.3-thuc_hanh-04 · Câu gốc 4

Tìm và sửa lỗi trong: int *buf = malloc(count * sizeof(int)); khi count do người dùng nhập.

**Trả lời gợi ý gốc:**

Sửa: kiểm tra if(count > SIZE_MAX/sizeof(int)) return NULL; trước malloc.

#### C2-2.3-thuc_hanh-05 · Câu gốc 5

Viết hàm safe_alloc_array(count, elem_size) kiểm tra overflow trước khi cấp phát.

**Trả lời gợi ý gốc:**

void* safe_alloc_array(size_t c, size_t s){if(s!=0 && c>SIZE_MAX/s)return NULL; return calloc(c,s);}

#### C2-2.3-thuc_hanh-06 · Câu gốc 6

Sửa lỗi printf(user_input) thành printf("%s", user_input) và giải thích rủi ro đã loại bỏ.

**Trả lời gợi ý gốc:**

Sửa: printf("%s", user_input); loại bỏ rủi ro user_input được diễn giải làm format string (đặc biệt %n).

#### C2-2.3-thuc_hanh-07 · Câu gốc 7

Tìm lỗi off-by-one trong: for(i=0; i<=10; i++) buf[i]='A'; với buf[10].

**Trả lời gợi ý gốc:**

Lỗi ở điều kiện i<=10 với buf[10] (index hợp lệ 0-9); sửa i<10.

#### C2-2.3-thuc_hanh-08 · Câu gốc 8

Biên dịch một chương trình C với đầy đủ cờ bảo vệ (-Wall -Wextra -fstack-protector-strong -fsanitize=address,undefined) và ghi lại warning tìm được.

**Trả lời gợi ý gốc:**

Warning tìm được thường gồm: unused variable, sign-compare, format mismatch, use-after-free (nếu có -fanalyzer).

#### C2-2.3-thuc_hanh-09 · Câu gốc 9

Viết đoạn code minh họa và kích hoạt Stack Canary (biên dịch với canary, cố ý overflow nhỏ để thấy __stack_chk_fail).

**Trả lời gợi ý gốc:**

````text
Minh họa: overflow buffer nhỏ ghi đè canary, chạy chương trình in ra ”*** stack smashing detected ***” và abort. 16

```
MỤC 2.3 – LẬP TRÌNH C AN TOÀN (SECURE C CODING)
```
````

#### C2-2.3-thuc_hanh-10 · Câu gốc 10

Cho struct Person với trường name/age, viết hàm set_name tuân thủ ARR30-C/STR31-C.

**Trả lời gợi ý gốc:**

void set_name(Person*p, const char*n){size_t l=strlen(n); if(l>=MAX_NAME)l=MAX_NAME-1; memcpy(p->name,n,l); p->name[l]=0;}

#### C2-2.3-thuc_hanh-11 · Câu gốc 11

Viết đoạn code C minh họa và sửa lỗi CWE-476 (NULL pointer dereference) sau khi free.

**Trả lời gợi ý gốc:**

int *p=malloc(4); free(p); p=NULL; if(p)*p=1; – kiểm tra p trước khi dùng, không bao giờ dereference NULL.

#### C2-2.3-thuc_hanh-12 · Câu gốc 12

Cho một hàm dùng strncpy không đảm bảo null-termination, sửa lại cho an toàn.

**Trả lời gợi ý gốc:**

strncpy(buf,src,n-1); buf[n-1]=0; đảm bảo null-terminate thủ công.

#### C2-2.3-thuc_hanh-13 · Câu gốc 13

Viết một macro hoặc hàm wrapper kiểm tra overflow trước khi thực hiện phép nhân hai số size_t.

**Trả lời gợi ý gốc:**

int safe_mul(size_t a,size_t b,size_t*r){if(a!=0&&b>SIZE_MAX/a)return -1; *r=a*b; return 0;}

#### C2-2.3-thuc_hanh-14 · Câu gốc 14

````text
Tìm tất cả lỗi bảo mật trong đoạn code sau và sửa: char msg[50]; sprintf(msg,"Hi "); strcat(msg,name); printf(msg); 17

```
MỤC 2.3 – LẬP TRÌNH C AN TOÀN (SECURE C CODING)
```
````

**Trả lời gợi ý gốc:**

Lỗi: sprintf không check size, strcat không check size, printf(msg) là format string vuln; sửa dùng snprintf+printf(”%s”,msg).

#### C2-2.3-thuc_hanh-15 · Câu gốc 15

Viết Makefile với target check chạy gcc -Wall -Wextra -Wpedantic -fanalyzer trên toàn bộ file .c.

**Trả lời gợi ý gốc:**

check: gcc -Wall -Wextra -Wpedantic -fanalyzer -fsyntax-only *.c

### Tình huống thực tế (15 câu)

#### C2-2.3-thuc_te-01 · Câu gốc 1

Một công ty phát hiện code C cũ (10 năm) dùng gets() trong module xử lý input người dùng. Phân tích rủi ro và đề xuất kế hoạch vá.

**Trả lời gợi ý gốc:**

Rủi ro nghiêm trọng (gets đã bị loại khỏi C11 vì quá nguy hiểm); kế hoạch: thay ngay bằng fgets, ưu tiên module xử lý input trực tiếp từ người dùng/mạng.

#### C2-2.3-thuc_te-02 · Câu gốc 2

Một tổ chức phát hiện một API công khai bị exploit qua Format String Vulnerability. Phân tích cách kẻ tấn công có thể đã khai thác và đề xuất vá khẩn cấp.

**Trả lời gợi ý gốc:**

Kẻ tấn công có thể dùng %n để ghi tùy ý vào bộ nhớ, dẫn tới RCE; vá khẩn cấp: thay printf(input) bằng printf(”%s”,input) trên TOÀN BỘ codebase.

#### C2-2.3-thuc_te-03 · Câu gốc 3

````text
Một game server C bị crash hàng loạt do một client gửi input dài bất thường. Phân tích khả năng buffer overflow và đề xuất kiểm tra. 18

```
MỤC 2.3 – LẬP TRÌNH C AN TOÀN (SECURE C CODING)
```
````

**Trả lời gợi ý gốc:**

Khả năng cao là buffer overflow do thiếu kiểm tra độ dài input; đề xuất: audit toàn bộ hàm nhận input mạng, thêm giới hạn độ dài + validate trước xử lý.

#### C2-2.3-thuc_te-04 · Câu gốc 4

Một ngân hàng phát hiện lỗi Integer Overflow trong module tính lãi suất dẫn tới cấp phát sai kích thước. Phân tích mức độ nghiêm trọng.

**Trả lời gợi ý gốc:**

Nghiêm trọng cao (tài chính): số tiền tính sai do buffer cấp sai kích thước có thể dẫn tới thất thoát/lỗi giao dịch; cần vá và audit lại toàn bộ phép tính liên quan tới kích thước động.

#### C2-2.3-thuc_te-05 · Câu gốc 5

Một công ty bảo mật phát hiện binary của đối thủ KHÔNG bật Stack Canary. Phân tích rủi ro và đề xuất họ nên làm gì.

**Trả lời gợi ý gốc:**

Rủi ro cao: dễ bị khai thác buffer overflow thành RCE; đề xuất họ nên public disclosure có trách nhiệm hoặc tự khắc phục và benchmark lại.

#### C2-2.3-thuc_te-06 · Câu gốc 6

Một hệ thống nhúng (embedded) không hỗ trợ ASLR do giới hạn phần cứng. Phân tích rủi ro tăng thêm và đề xuất biện pháp bù đắp.

**Trả lời gợi ý gốc:**

Rủi ro tăng đáng kể (thiếu 1 lớp phòng thủ quan trọng); bù đắp: tăng cường code review, static analysis kỹ hơn, cân nhắc thêm software-based ASLR nếu khả thi.

#### C2-2.3-thuc_te-07 · Câu gốc 7

Một tổ chức phát hiện off-by-one error trong module xử lý log đã tồn tại 3 năm, gây crash ngẫu nhiên hiếm gặp. Phân tích vì sao khó phát hiện bằng testing thông thường.

**Trả lời gợi ý gốc:**

Khó phát hiện vì off-by-one chỉ kích hoạt với ĐIỀU KIỆN CỤ THỂ hiếm gặp (input đúng độ dài biên) – testing ngẫu nhiên khó chạm đúng edge case, cần Boundary Value Analysis có chủ đích.

#### C2-2.3-thuc_te-08 · Câu gốc 8

Một công ty an ninh mạng phân tích một malware khai thác Format String Vulnerability trong phần mềm phổ biến. Mô tả cách STR31-C có thể đã ngăn chặn lỗ hổng này.

**Trả lời gợi ý gốc:**

STR31-C yêu cầu buffer đủ lớn CHO KÝ TỰ + NULL TERMINATOR – nếu tuân thủ nghiêm ngặt (dùng snprintf thay vì sprintf không kiểm tra), format string cụ thể này không thể ghi tràn.

#### C2-2.3-thuc_te-09 · Câu gốc 9

Một dự án hàng không phát hiện code C không tuân thủ CERT C. Phân tích tại sao tiêu chuẩn CERT C đặc biệt quan trọng cho ngành này.

**Trả lời gợi ý gốc:**

CERT C cung cấp checklist CỤ THỂ, đã kiểm chứng qua nhiều năm cho ngành an toàn tính mạng cao (hàng không) – giúp chuẩn hóa và audit được thay vì dựa vào kinh nghiệm cá nhân.

#### C2-2.3-thuc_te-10 · Câu gốc 10

Một công ty phát hiện thư viện mã hóa tự viết bằng C có lỗi buffer overflow trong hàm xử lý key. Phân tích mức độ nghiêm trọng đặc biệt của lỗi này.

**Trả lời gợi ý gốc:**

Nghiêm trọng đặc biệt: lỗi bộ nhớ trong module xử lý KEY (khóa mã hóa) có thể dẫn tới rò rỉ khóa qua overflow/side-channel, làm sụp đổ TOÀN BỘ hệ thống bảo mật dựa trên khóa đó.

#### C2-2.3-thuc_te-11 · Câu gốc 11

Một tổ chức yêu cầu MIGRATE một module C tới hạn sang Rust. Phân tích lợi ích cụ thể liên quan tới các lỗi đã học ở Mục 2.3.

**Trả lời gợi ý gốc:**

Lợi ích Rust: loại bỏ UAF/double-free/buffer overflow qua compile-time check (Ownership), không cần thêm sanitizer runtime – giảm hẳn lớp lỗi Mục 2.2-2.3 đã học.

#### C2-2.3-thuc_te-12 · Câu gốc 12

Một công ty phát hiện DEP/NX bị TẮT trên server production do cấu hình sai. Phân tích rủi ro tăng thêm khi có buffer overflow.

**Trả lời gợi ý gốc:**

Rủi ro tăng cao đáng kể: nếu có buffer overflow, không có DEP/NX nghĩa là kẻ tấn công có thể thực thi mã injected trực tiếp trong vùng dữ liệu – cần bật lại NGAY LẬP TỨC.

#### C2-2.3-thuc_te-13 · Câu gốc 13

Một dự án IoT phát hiện firmware không dùng bất kỳ compiler protection nào (canary, ASLR, DEP). Đề xuất ưu tiên bật protection nào trước.

**Trả lời gợi ý gốc:**

Ưu tiên: Stack Canary trước (rẻ, hiệu quả tức thì với stack overflow), sau đó DEP/NX, cuối cùng ASLR nếu phần cứng hỗ trợ.

#### C2-2.3-thuc_te-14 · Câu gốc 14

Một pentester tìm thấy buffer overflow trong ứng dụng nhưng không khai thác được do ASLR+DEP+Canary đều bật. Phân tích ý nghĩa thực tế của việc ”có lỗi nhưng khó khai thác”.

**Trả lời gợi ý gốc:**

Ý nghĩa: các lớp bảo vệ (Canary+ASLR+DEP) LÀM TĂNG ĐỘ KHÓ khai thác đáng kể dù lỗi vẫn tồn tại – đây là giá trị thực tế của Defense in Depth, dù vẫn cần vá lỗi gốc.

#### C2-2.3-thuc_te-15 · Câu gốc 15

Một công ty phát hiện struct dùng để giao tiếp giữa 2 hệ thống có vấn đề alignment gây lỗi parse dữ liệu. Phân tích và đề xuất dùng #pragma pack.

**Trả lời gợi ý gốc:**

Vấn đề alignment giữa 2 hệ thống khác kiến trúc; giải pháp: dùng #pragma pack(1) cho struct giao tiếp để đảm bảo layout nhất quán bất kể platform.

## Mục 2.4: Sắp xếp cấu trúc dữ liệu (Data Structure Alignment)

### Trắc nghiệm (9 câu)

#### C2-2.4-trac_nghiem-01 · Câu gốc 1

Alignment là yêu cầu gì?

**A.** Một giá trị kiểu T phải đặt tại địa chỉ là bội số của alignof(T)

**B.** Mọi biến phải có cùng kích thước

**C.** Không có yêu cầu gì đặc biệt

**D.** Chỉ áp dụng cho số thực

**Đáp án gốc:** A

**Giải thích gốc:**

Giá trị T đặt tại địa chỉ bội số của alignof(T).

#### C2-2.4-trac_nghiem-02 · Câu gốc 2

Vì sao CPU cần truy cập bộ nhớ theo alignment?

**A.** Để tiết kiệm điện

**B.** Để đọc/ghi hiệu quả nhất theo các ”word” căn chỉnh

**C.** Không có lý do kỹ thuật

**D.** Chỉ vì quy ước lập trình

**Đáp án gốc:** B

**Giải thích gốc:**

CPU đọc/ghi hiệu quả nhất theo word căn chỉnh.

#### C2-2.4-trac_nghiem-03 · Câu gốc 3

Padding trong struct C là gì?

**A.** Dữ liệu người dùng nhập vào

**B.** Byte đệm compiler tự thêm để đảm bảo alignment

**C.** Lỗi biên dịch

**D.** Chỉ xuất hiện trong Python

**Đáp án gốc:** B

**Giải thích gốc:**

Padding: byte đệm compiler tự thêm.

#### C2-2.4-trac_nghiem-04 · Câu gốc 4

Với struct {char a; int b; char c;}, sizeof thường KHÔNG bằng:

**A.** ````text
```
(tổng đơn giản 1+4+1)
````

**B.** 12 (có padding)

**C.** ````text
Cả A và B đều có thể đúng
```

tùy hệ thống
````

**D.** Không thể xác định

**Đáp án gốc:** C

**Giải thích gốc:**

````text
Cả A và B đúng tùy hệ thống (thường 12 do padding). 19

```
MỤC 2.4 – SẮP XẾP CẤU TRÚC DỮ LIỆU (DATA STRUCTURE
```

ALIGNMENT) – An toàn phần mềm
````

#### C2-2.4-trac_nghiem-05 · Câu gốc 5

Cách giảm padding hiệu quả là gì?

**A.** Sắp xếp field theo kích thước GIẢM DẦN

**B.** Sắp xếp field theo bảng chữ cái

**C.** Không thể giảm padding

**D.** Luôn dùng #pragma pack(1) trong mọi trường hợp

**Đáp án gốc:** A

**Giải thích gốc:**

Sắp xếp field theo kích thước giảm dần.

#### C2-2.4-trac_nghiem-06 · Câu gốc 6

Padding có thể gây ra lỗi bảo mật nào?

**A.** Buffer overflow

**B.** Rò rỉ dữ liệu ”rác” qua CWE-457/CWE-200

**C.** SQL Injection

**D.** Race condition

**Đáp án gốc:** B

**Giải thích gốc:**

Rò rỉ dữ liệu rác qua CWE-457/CWE-200.

#### C2-2.4-trac_nghiem-07 · Câu gốc 7

Giải pháp cho lỗi rò rỉ padding là gì?

**A.** Không có giải pháp

**B.** memset(&s, 0, sizeof(s)) trước khi điền dữ liệu

**C.** Tăng kích thước struct

**D.** Chỉ dùng union thay vì struct

**Đáp án gốc:** B

**Giải thích gốc:**

memset(&s,0,sizeof(s)) trước khi điền dữ liệu.

#### C2-2.4-trac_nghiem-08 · Câu gốc 8

#pragma pack(push, 1) có tác dụng gì?

**A.** Tăng padding lên tối đa

**B.** Tắt padding, dùng 1-byte alignment

**C.** Xóa toàn bộ struct

**D.** Không có tác dụng thực tế

**Đáp án gốc:** B

**Giải thích gốc:**

#pragma pack(push,1): tắt padding.

#### C2-2.4-trac_nghiem-09 · Câu gốc 9

Khi nào thường cần #pragma pack(1)?

**A.** Khi cần khớp định dạng binary chính xác (network protocol, file format)

**B.** Luôn luôn cần dùng

**C.** Không bao giờ cần dùng

**D.** Chỉ khi lập trình game

**Đáp án gốc:** A

**Giải thích gốc:**

Cần khi khớp định dạng binary chính xác.

### Lý thuyết (15 câu)

#### C2-2.4-ly_thuyet-01 · Câu gốc 1

Trình bày khái niệm Memory Alignment và giải thích tại sao CPU yêu cầu nó.

**Trả lời gợi ý gốc:**

Alignment: yêu cầu giá trị kiểu T đặt tại địa chỉ là bội số của alignof(T); CPU cần điều này để đọc/ghi hiệu quả theo các ”word” phần cứng, tránh truy cập chia làm nhiều lần.

#### C2-2.4-ly_thuyet-02 · Câu gốc 2

Giải thích Padding trong struct C và lý do compiler tự động thêm padding.

**Trả lời gợi ý gốc:**

Padding: byte đệm compiler tự thêm giữa/sau các field để đảm bảo mỗi field bắt đầu ĐÚNG alignment yêu cầu và tổng kích thước struct là bội số alignment lớn nhất.

#### C2-2.4-ly_thuyet-03 · Câu gốc 3

Mô tả ví dụ cụ thể struct với 3 field (char, int, char) và giải thích vì sao sizeof KHÔNG bằng tổng đơn giản.

**Trả lời gợi ý gốc:**

struct{char a;int b;char c;}: a(1B)+pad(3B)+b(4B)+c(1B)+pad(3B)=12B, KHÔNG phải 1+4+1=6B vì cần padding để b căn chỉnh 4-byte và tổng struct là bội số 4.

#### C2-2.4-ly_thuyet-04 · Câu gốc 4

Trình bày nguyên tắc sắp xếp field theo kích thước giảm dần để giảm padding.

**Trả lời gợi ý gốc:**

````text
Nguyên tắc: đặt field LỚN NHẤT trước, NHỎ NHẤT sau – giúp gom các field nhỏ lại gần nhau, giảm số lượng padding ”lẻ” xen giữa. 20

```
MỤC 2.4 – SẮP XẾP CẤU TRÚC DỮ LIỆU (DATA STRUCTURE
```

ALIGNMENT) – An toàn phần mềm
````

#### C2-2.4-ly_thuyet-05 · Câu gốc 5

Giải thích hệ quả bảo mật của padding: rò rỉ dữ liệu qua CWE-457/CWE- 200.

**Trả lời gợi ý gốc:**

Padding KHÔNG được khởi tạo tự động, chứa dữ liệu ”rác” còn sót từ lần cấp phát trước; nếu serialize/gửi TOÀN BỘ struct (bao gồm padding) qua mạng/file, dữ liệu rác này có thể rò rỉ (CWE-457/CWE-200).

#### C2-2.4-ly_thuyet-06 · Câu gốc 6

Mô tả giải pháp memset(&s, 0, sizeof(s)) và tại sao nó ngăn được rò rỉ padding.

**Trả lời gợi ý gốc:**

memset xóa TOÀN BỘ byte của struct (kể cả padding) về 0 TRƯỚC KHI điền dữ liệu thực – đảm bảo không còn ”rác” từ lần cấp phát trước khi serialize.

#### C2-2.4-ly_thuyet-07 · Câu gốc 7

Trình bày cách dùng #pragma pack và alignas để kiểm soát alignment.

**Trả lời gợi ý gốc:**

#pragma pack(push,N) đặt alignment tối đa N byte (thường N=1 để tắt padding hoàn toàn); alignas(N) bắt buộc MỘT biến/field align theo N byte cụ thể (C11).

#### C2-2.4-ly_thuyet-08 · Câu gốc 8

Giải thích khi nào cần dùng #pragma pack(1) và đánh đổi hiệu năng đi kèm.

**Trả lời gợi ý gốc:**

Dùng khi cần khớp CHÍNH XÁC định dạng binary với hệ thống khác (network protocol, file format cố định) – đánh đổi: giảm hiệu năng do CPU phải xử lý truy cập misaligned.

#### C2-2.4-ly_thuyet-09 · Câu gốc 9

Phân biệt sizeof và offsetof, cho ví dụ minh họa ứng dụng thực tế.

**Trả lời gợi ý gốc:**

sizeof trả tổng kích thước CẢ struct; offsetof trả VỊ TRÍ BYTE cụ thể của MỘT field – offsetof hữu ích khi cần debug layout hoặc thao tác trực tiếp với buffer binary.

#### C2-2.4-ly_thuyet-10 · Câu gốc 10

Trình bày ví dụ struct PacketHeader cho network protocol dùng #pragma pack(1).

**Trả lời gợi ý gốc:**

PacketHeader dùng pack(1) với version(1B)+flags(1B)+length(2B)+seq(4B)=8B không padding, khớp CHÍNH XÁC với wire format của giao thức mạng.

#### C2-2.4-ly_thuyet-11 · Câu gốc 11

Giải thích tại sao cần kiểm tra kích thước buffer trước khi ép kiểu con trỏ thành struct khi parse dữ liệu mạng.

**Trả lời gợi ý gốc:**

Vì nếu buffer nhận được NHỎ HƠN sizeof(struct), việc ép kiểu con trỏ và truy cập field sẽ ĐỌC NGOÀI BIÊN buffer – gây crash hoặc đọc dữ liệu rác/nhạy cảm.

#### C2-2.4-ly_thuyet-12 · Câu gốc 12

Mô tả Bitfields trong C và giải thích tại sao chúng KHÔNG PHÙ HỢP cho network protocol.

**Trả lời gợi ý gốc:**

Bitfields có layout (thứ tự bit, padding) PHỤ THUỘC trình biên dịch/kiến trúc cụ thể (implementation-defined) – không đảm bảo giống nhau giữa các hệ thống khác nhau.

#### C2-2.4-ly_thuyet-13 · Câu gốc 13

Trình bày giải pháp thay thế Bitfields bằng bit-mask thủ công cho network protocol.

**Trả lời gợi ý gốc:**

Giải pháp: dùng kiểu uint8_t với các phép AND/OR/SHIFT thủ công để trích xuất/thiết lập từng bit, đảm bảo hành vi NHẤT QUÁN trên mọi compiler/kiến trúc.

#### C2-2.4-ly_thuyet-14 · Câu gốc 14

Bàn luận: tại sao việc sắp xếp lại field không PHẢI LÚC NÀO CŨNG giảm được kích thước struct?

**Trả lời gợi ý gốc:**

KHÔNG phải lúc nào cũng giảm được vì alignment TỔNG THỂ của struct quyết định bởi field có alignment LỚN NHẤT (VD double 8-byte) – nếu field đó luôn cần padding theo sau, sắp xếp lại các field nhỏ khác không ảnh hưởng tổng kích thước.

#### C2-2.4-ly_thuyet-15 · Câu gốc 15

Giải thích quy tắc ”sizeof struct luôn là bội số của alignment lớn nhất trong các field”.

**Trả lời gợi ý gốc:**

sizeof struct luôn là BỘI SỐ của alignment LỚN NHẤT trong các field – đảm bảo khi đặt struct trong MẢNG, mọi phần tử đều alignment đúng.

### Thực hành (15 câu)

#### C2-2.4-thuc_hanh-01 · Câu gốc 1

Tính sizeof của struct {char a; int b; char c;} trên hệ 64-bit và vẽ layout với padding.

**Trả lời gợi ý gốc:**

struct{char a;int b;char c;}: a(1)+pad(3)+b(4)+c(1)+pad(3) = 12 byte trên hệ 64-bit.

#### C2-2.4-thuc_hanh-02 · Câu gốc 2

Sắp xếp lại field của struct câu 1 để giảm padding, tính lại sizeof.

**Trả lời gợi ý gốc:**

Sắp xếp lại int b;char a;char c;: 4+1+1+2(pad) = 8 byte – giảm từ 12 xuống 8.

#### C2-2.4-thuc_hanh-03 · Câu gốc 3

````text
Viết đoạn code in ra sizeof và offsetof của từng field trong một struct

```
field.
```
````

**Trả lời gợi ý gốc:**

In offsetof từng field bằng printf("%zu",offsetof(S,field)); cho 4 field.

#### C2-2.4-thuc_hanh-04 · Câu gốc 4

Cho struct {double d; char c; int i;}, tính sizeof trên hệ 64-bit, giải thích padding.

**Trả lời gợi ý gốc:**

struct{double d;char c;int i;}: d(8)+c(1)+pad(3)+i(4) = 16 byte (alignment lớn nhất là 8 của double).

#### C2-2.4-thuc_hanh-05 · Câu gốc 5

Viết struct PacketHeader dùng #pragma pack(1) với version(uint8), flags(uint8), length(uint16), seq(uint32), tính sizeof.

**Trả lời gợi ý gốc:**

PacketHeader pack(1): version(1)+flags(1)+length(2)+seq(4) = 8 byte, không padding.

#### C2-2.4-thuc_hanh-06 · Câu gốc 6

Viết đoạn code minh họa memset trước khi gửi struct qua socket (giả lập bằng write vào buffer).

**Trả lời gợi ý gốc:**

memset(&rec,0,sizeof(rec)); rec.field=val; write(fd,&rec,sizeof(rec));

#### C2-2.4-thuc_hanh-07 · Câu gốc 7

Cho một struct chứa bitfields, viết bản thay thế dùng bit-mask thủ công với uint8_t.

**Trả lời gợi ý gốc:**

Bitfield thay bằng: uint8_t flags; #define IS_ADMIN(f) ((f)&0x01) và các macro tương tự cho từng bit.

#### C2-2.4-thuc_hanh-08 · Câu gốc 8

Viết hàm struct_has_padding(size_t naive_sum, size_t actual_sizeof) kiểm tra struct có padding hay không.

**Trả lời gợi ý gốc:**

bool has_padding(size_t naive, size_t actual){return naive != actual;}

#### C2-2.4-thuc_hanh-09 · Câu gốc 9

Cho một struct 5 field kích thước khác nhau, sắp xếp lại theo giảm dần và so sánh sizeof trước/sau.

**Trả lời gợi ý gốc:**

Struct 5 field (double,int,short,char,char) sắp xếp giảm dần: giảm padding so với thứ tự ngẫu nhiên ban đầu.

#### C2-2.4-thuc_hanh-10 · Câu gốc 10

Viết đoạn code dùng alignas(16) cho một buffer, giải thích ứng dụng thực tế (SIMD alignment).

**Trả lời gợi ý gốc:**

alignas(16) char buf[64]; dùng cho SIMD instructions cần dữ liệu align 16-byte.

#### C2-2.4-thuc_hanh-11 · Câu gốc 11

Cho một struct network protocol, viết code parse buffer nhận được thành struct với kiểm tra kích thước trước.

**Trả lời gợi ý gốc:**

````text
if(recv_len < sizeof(Header)) return ERROR; Header *h = (Header*)buffer; 22

```
MỤC 2.4 – SẮP XẾP CẤU TRÚC DỮ LIỆU (DATA STRUCTURE
```

ALIGNMENT) – An toàn phần mềm
````

#### C2-2.4-thuc_hanh-12 · Câu gốc 12

Viết đoạn code minh họa lỗi: cast buffer nhỏ hơn sizeof(struct) thành con trỏ struct, gây đọc ngoài biên.

**Trả lời gợi ý gốc:**

Minh họa lỗi: Header *h = (Header*)small_buffer; khi sizeof(small_buffer) < sizeof(Header) – đọc ngoài biên.

#### C2-2.4-thuc_hanh-13 · Câu gốc 13

````text
Tính offsetof cho tất cả field trong struct {char a; double b; char c; int d;}. 23

```
MỤC 2.4 – SẮP XẾP CẤU TRÚC DỮ LIỆU (DATA STRUCTURE
```

ALIGNMENT) – An toàn phần mềm
````

**Trả lời gợi ý gốc:**

offsetof(a)=0, offsetof(b)=8(pad 7 sau a), offsetof(c)=16, offsetof(d)=20(pad giữa c,d nếu cần).

#### C2-2.4-thuc_hanh-14 · Câu gốc 14

Viết đoạn code so sánh sizeof của cùng một struct với và không có #pragma pack(1).

**Trả lời gợi ý gốc:**

So sánh: không pack thường lớn hơn (VD 12 vs 8 byte) do padding.

#### C2-2.4-thuc_hanh-15 · Câu gốc 15

Cho struct chứa thông tin nhạy cảm (VD password field + padding), viết bản đã sửa dùng memset trước serialize.

**Trả lời gợi ý gốc:**

memset(&rec,0,sizeof(rec)); rec.password_hash=...; trước khi serialize.

### Tình huống thực tế (15 câu)

#### C2-2.4-thuc_te-01 · Câu gốc 1

Một công ty phát hiện dữ liệu nhạy cảm bị rò rỉ qua padding khi struct được ghi trực tiếp ra file log. Phân tích nguyên nhân và đề xuất khắc phục.

**Trả lời gợi ý gốc:**

Nguyên nhân: thiếu memset trước khi ghi log; khắc phục: thêm memset(&s,0,sizeof(s)) TRƯỚC MỌI serialize/log struct chứa dữ liệu nhạy cảm.

#### C2-2.4-thuc_te-02 · Câu gốc 2

Một hệ thống giao tiếp giữa server 64-bit và thiết bị nhúng 32-bit gặp lỗi parse dữ liệu do khác biệt alignment. Phân tích và đề xuất giải pháp.

**Trả lời gợi ý gốc:**

Giải pháp: dùng #pragma pack(1) cho struct giao tiếp để đảm bảo layout NHẤT QUÁN bất kể alignment mặc định khác nhau giữa 2 kiến trúc.

#### C2-2.4-thuc_te-03 · Câu gốc 3

````text
Một dự án game network dùng struct không pack để gửi packet, gây lãng phí băng thông đáng kể. Phân tích và đề xuất tối ưu. 24

```
MỤC 2.4 – SẮP XẾP CẤU TRÚC DỮ LIỆU (DATA STRUCTURE
```

ALIGNMENT) – An toàn phần mềm
````

**Trả lời gợi ý gốc:**

````text
Tối ưu: thêm #pragma pack(1) cho struct packet, giảm đáng kể overhead băng thông khi gửi số lượng lớn packet. 23

```
MỤC 2.4 – SẮP XẾP CẤU TRÚC DỮ LIỆU (DATA STRUCTURE
```

ALIGNMENT) – An toàn phần mềm
````

#### C2-2.4-thuc_te-04 · Câu gốc 4

Một công ty bảo mật phát hiện một ứng dụng rò rỉ một phần khóa mã hóa qua padding của struct gửi qua mạng. Phân tích mức độ nghiêm trọng.

**Trả lời gợi ý gốc:**

Mức độ nghiêm trọng CAO: rò rỉ một phần khóa mã hóa qua padding tương đương một dạng side-channel – cần vá NGAY và audit toàn bộ struct liên quan crypto.

#### C2-2.4-thuc_te-05 · Câu gốc 5

Một hệ thống IoT dùng bitfields cho protocol riêng, gặp lỗi không tương thích khi đổi sang compiler khác. Phân tích nguyên nhân và đề xuất sửa.

**Trả lời gợi ý gốc:**

Nguyên nhân: bitfield layout implementation-defined, khác nhau giữa compiler; sửa: chuyển sang bit-mask thủ công với uint8_t đảm bảo tính portable.

#### C2-2.4-thuc_te-06 · Câu gốc 6

Một tổ chức tài chính phát hiện struct giao dịch có padding chứa dữ liệu từ giao dịch TRƯỚC đó (do tái sử dụng vùng nhớ không memset). Phân tích rủi ro nghiêm trọng.

**Trả lời gợi ý gốc:**

Rủi ro nghiêm trọng: dữ liệu giao dịch cũ rò rỉ qua padding của bản ghi mới (tái sử dụng vùng nhớ); khắc phục khẩn: memset MỌI struct giao dịch trước khi ghi/gửi.

#### C2-2.4-thuc_te-07 · Câu gốc 7

Một công ty phát hiện việc thêm #pragma pack(1) không cần thiết cho một struct chỉ dùng nội bộ đã làm CHẬM chương trình. Phân tích và đề xuất khi nào nên/không nên pack.

**Trả lời gợi ý gốc:**

Không nên pack(1) không cần thiết cho struct chỉ dùng NỘI BỘ – pack chỉ nên dùng khi thực sự cần khớp binary format bên ngoài (network/file).

#### C2-2.4-thuc_te-08 · Câu gốc 8

Một dự án firmware phát hiện lỗi crash khi struct network header được cast từ buffer QUÁ NHỎ (thiếu vài byte). Phân tích và đề xuất validate trước khi parse.

**Trả lời gợi ý gốc:**

Đề xuất: LUÔN validate buffer_size >= sizeof(struct) trước khi ép kiểu con trỏ, trả lỗi rõ ràng nếu không đủ thay vì cast liều lĩnh.

#### C2-2.4-thuc_te-09 · Câu gốc 9

Một hệ thống trading tần suất cao cần tối ưu CẢ tốc độ VÀ kích thước struct cho dữ liệu thị trường. Đề xuất chiến lược cân bằng.

**Trả lời gợi ý gốc:**

Chiến lược: pack(1) cho phần HEADER cố định (tối ưu băng thông truyền), nhưng có thể để mặc định alignment cho phần xử lý nội bộ (tối ưu tốc độ tính toán).

#### C2-2.4-thuc_te-10 · Câu gốc 10

Một công ty phát hiện struct dùng cho save file game bị lỗi khi load trên platform khác (khác alignment mặc định). Phân tích và đề xuất giải pháp portable.

**Trả lời gợi ý gốc:**

Giải pháp portable: dùng #pragma pack(1) HOẶC serialize/deserialize thủ công từng field (đọc/ghi byte theo thứ tự cố định) thay vì dựa vào memory layout tự nhiên.

#### C2-2.4-thuc_te-11 · Câu gốc 11

Một hệ thống y tế phát hiện dữ liệu bệnh nhân cũ bị lộ qua padding của struct record mới được cấp phát lại từ cùng vùng nhớ. Phân tích và đề xuất khắc phục khẩn cấp.

**Trả lời gợi ý gốc:**

Khắc phục khẩn cấp: memset TOÀN BỘ struct record trước khi tái sử dụng vùng nhớ cho bệnh nhân mới, audit toàn bộ hệ thống quản lý record.

#### C2-2.4-thuc_te-12 · Câu gốc 12

Một công ty phát hiện một CVE liên quan tới đọc ngoài biên do thiếu kiểm tra kích thước trước khi cast buffer thành struct. Phân tích chuỗi lỗi và đề xuất vá.

**Trả lời gợi ý gốc:**

Chuỗi lỗi: thiếu validate size→cast buffer nhỏ thành struct lớn→đọc ngoài biên→crash/leak; vá: thêm size check trước MỌI cast.

#### C2-2.4-thuc_te-13 · Câu gốc 13

Một dự án vệ tinh dùng struct pack(1) cho toàn bộ telemetry data để tối ưu băng thông truyền tín hiệu. Phân tích đánh đổi hiệu năng xử lý trên board.

**Trả lời gợi ý gốc:**

Đánh đổi: pack(1) giảm băng thông truyền (quan trọng cho vệ tinh) nhưng tăng chi phí xử lý misaligned trên board – cần benchmark cụ thể để cân bằng.

#### C2-2.4-thuc_te-14 · Câu gốc 14

Một hệ thống ngân hàng phát hiện lỗi so sánh 2 struct bằng memcmp cho kết quả sai do padding chứa giá trị rác khác nhau dù dữ liệu logic giống nhau. Phân tích và đề xuất sửa.

**Trả lời gợi ý gốc:**

Sửa: viết hàm so sánh TỪNG FIELD thay vì memcmp toàn bộ struct (memcmp so sánh CẢ padding có thể khác giá trị dù data logic giống nhau).

#### C2-2.4-thuc_te-15 · Câu gốc 15

Một công ty phần cứng phát hiện misaligned access gây lỗi bus error trên một dòng CPU nhúng cụ thể. Phân tích và đề xuất kiểm tra alignment kỹ hơn.

**Trả lời gợi ý gốc:**

Đề xuất: kiểm tra kỹ tài liệu alignment requirement của CPU đích, dùng alignas hoặc test kỹ trên hardware thật trước khi deploy.

## Mục 2.5: Công cụ phân tích tĩnh tìm lỗi bảo mật

### Trắc nghiệm (9 câu)

#### C2-2.5-trac_nghiem-01 · Câu gốc 1

Compiler warnings được coi là tuyến phòng thủ nào?

**A.** Phân tích động duy nhất

**B.** Static analysis cơ bản, rẻ nhất

**C.** Không liên quan tới static analysis

**D.** Chỉ có tác dụng thẩm mỹ

**Đáp án gốc:** B

**Giải thích gốc:**

Static analysis cơ bản, rẻ nhất.

#### C2-2.5-trac_nghiem-02 · Câu gốc 2

Cờ nào cảnh báo lỗi format string trong GCC?

**A.** -O2

**B.** -Wformat=2

**C.** -c

**D.** -shared

**Đáp án gốc:** B

**Giải thích gốc:**

-Wformat=2 cảnh báo lỗi format string.

#### C2-2.5-trac_nghiem-03 · Câu gốc 3

-fanalyzer (GCC 10+) có tác dụng gì?

**A.** Tăng tốc biên dịch

**B.** Static analyzer tích hợp phát hiện UAF, double-free, NULL deref

**C.** Chỉ dùng cho C++

**D.** Xóa toàn bộ warning

**Đáp án gốc:** B

**Giải thích gốc:**

-fanalyzer: phát hiện UAF, double-free, NULL deref.

#### C2-2.5-trac_nghiem-04 · Câu gốc 4

Cppcheck có đặc điểm gì nổi bật?

**A.** Cần build toàn bộ project mới chạy được

**B.** Không cần build, phân tích trực tiếp mã nguồn, tỷ lệ false positive thấp

**C.** Chỉ hoạt động trên Windows

**D.** Chỉ phát hiện lỗi cú pháp

**Đáp án gốc:** B

**Giải thích gốc:**

Không cần build, false positive thấp.

#### C2-2.5-trac_nghiem-05 · Câu gốc 5

cppcheck --enable=all dùng để làm gì?

**A.** Tắt toàn bộ cảnh báo

**B.** Bật tất cả loại kiểm tra có sẵn

**C.** Chỉ kiểm tra cú pháp

**D.** Xóa file tạm

**Đáp án gốc:** B

**Giải thích gốc:**

--enable=all: bật tất cả loại kiểm tra.

#### C2-2.5-trac_nghiem-06 · Câu gốc 6

Trong output Cppcheck, mã lỗi [memleak] nghĩa là gì?

**A.** Lỗi cú pháp

**B.** Phát hiện memory leak

**C.** Lỗi định dạng

**D.** Không có ý nghĩa gì

**Đáp án gốc:** B

**Giải thích gốc:**

[memleak]: phát hiện memory leak.

#### C2-2.5-trac_nghiem-07 · Câu gốc 7

Clang Static Analyzer dùng kỹ thuật gì?

**A.** Chỉ đọc comment

**B.** Symbolic execution (path-sensitive)

**C.** Chỉ đếm dòng code

**D.** Không phân tích gì cả

**Đáp án gốc:** B

**Giải thích gốc:**

Clang SA dùng symbolic execution (path-sensitive).

#### C2-2.5-trac_nghiem-08 · Câu gốc 8

”Path-sensitive” trong Clang Static Analyzer nghĩa là gì?

**A.** Không quan tâm đường thi hành

**B.** Mô phỏng các đường thi hành có thể để phát hiện lỗi theo điều kiện cụ thể

**C.** Chỉ áp dụng cho file path

**D.** Chỉ kiểm tra tên biến

**Đáp án gốc:** B

**Giải thích gốc:**

Path-sensitive: mô phỏng đường thi hành có thể.

#### C2-2.5-trac_nghiem-09 · Câu gốc 9

scan-build dùng để làm gì?

**A.** Quét virus

**B.** Chạy Clang Static Analyzer tích hợp với quá trình build

**C.** Xóa build cache

**D.** Tăng tốc linker

**Đáp án gốc:** B

**Giải thích gốc:**

scan-build: chạy Clang SA tích hợp build.

### Lý thuyết (15 câu)

#### C2-2.5-ly_thuyet-01 · Câu gốc 1

Trình bày vai trò của Compiler Warnings như tuyến phòng thủ static analysis đầu tiên, rẻ nhất.

**Trả lời gợi ý gốc:**

Compiler Warnings tích hợp SẴN trong quá trình biên dịch, không cần công cụ thêm, phát hiện lỗi cú pháp/kiểu dữ liệu cơ bản – rẻ nhất vì không tốn chi phí bổ sung.

#### C2-2.5-ly_thuyet-02 · Câu gốc 2

Giải thích các cờ GCC quan trọng cho static analysis: -Wformat=2, -Wconversion, -fanalyzer.

**Trả lời gợi ý gốc:**

-Wformat=2: cảnh báo lỗi format string (như printf(input)); -Wconversion: cảnh báo mất dữ liệu ép kiểu ngầm (liên quan integer overflow); -fanalyzer: phân tích sâu hơn phát hiện UAF/double-free/NULL deref.

#### C2-2.5-ly_thuyet-03 · Câu gốc 3

Mô tả Cppcheck: ưu điểm, cách hoạt động, và lý do phù hợp CI/CD hàng ngày.

**Trả lời gợi ý gốc:**

Cppcheck: mã nguồn mở, KHÔNG CẦN build project (phân tích trực tiếp source), tỷ lệ false positive THẤP hơn nhiều tool khác – phù hợp chạy tự động mỗi commit trong CI/CD.

#### C2-2.5-ly_thuyet-04 · Câu gốc 4

Trình bày ví dụ output Cppcheck và giải thích ý nghĩa các mã lỗi (VD [memleak], [nullPointer]).

**Trả lời gợi ý gốc:**

VD output: [uninitvar] biến chưa khởi tạo, [memleak] rò rỉ bộ nhớ, [nullPointer] có thể NULL deref – mỗi mã lỗi giúp tra cứu chi tiết và có thể suppress riêng nếu false positive.

#### C2-2.5-ly_thuyet-05 · Câu gốc 5

Giải thích Clang Static Analyzer và kỹ thuật symbolic execution/path- sensitive analysis nó sử dụng.

**Trả lời gợi ý gốc:**

Clang SA dùng SYMBOLIC EXECUTION: mô phỏng các đường thi hành CÓ THỂ của chương trình với giá trị tượng trưng, phát hiện lỗi PHỤ THUỘC ĐIỀU KIỆN cụ thể mà Cppcheck (heuristic đơn giản) có thể bỏ sót.

#### C2-2.5-ly_thuyet-06 · Câu gốc 6

So sánh Cppcheck và Clang Static Analyzer về độ chính xác và tốc độ.

**Trả lời gợi ý gốc:**

Cppcheck: nhanh, false positive thấp, heuristic; Clang SA: chậm hơn, path-sensitive nên chính xác hơn với lỗi phức tạp (UAF theo điều kiện cụ thể).

#### C2-2.5-ly_thuyet-07 · Câu gốc 7

Trình bày cách Valgrind hoạt động (instrumentation, CPU ảo) và giải thích tại sao nó chậm.

**Trả lời gợi ý gốc:**

Valgrind chạy chương trình trong MỘT CPU ẢO (instrumentation toàn bộ), theo dõi MỌI thao tác bộ nhớ – đây chính là lý do chậm (10-50x) nhưng cho kết quả CHÍNH XÁC trên đường đã chạy.

#### C2-2.5-ly_thuyet-08 · Câu gốc 8

Giải thích --leak-check=full --track-origins=yes của Valgrind và ý nghĩa từng tham số.

**Trả lời gợi ý gốc:**

--leak-check=full: hiển thị chi tiết TỪNG memory leak; --track-origins=yes: theo dõi NGUỒN GỐC của giá trị chưa khởi tạo được dùng (giúp debug uninitialized read). 26 MẬT – An toàn phần mềm

#### C2-2.5-ly_thuyet-09 · Câu gốc 9

Mô tả bảng so sánh 4 công cụ: Compiler Warnings, Cppcheck, Clang SA, Valgrind theo tiêu chí loại/tốc độ/độ chính xác.

**Trả lời gợi ý gốc:**

Bảng: Warnings(nhanh nhất,ít chính xác nhất)→Cppcheck(nhanh,TB-cao chính xác)→Clang SA(chậm hơn,cao chính xác)→Valgrind(chậm nhất,rất cao chính xác nhưng chỉ trên path đã chạy).

#### C2-2.5-ly_thuyet-10 · Câu gốc 10

Bàn luận: tại sao ”kết hợp nhiều công cụ ở nhiều giai đoạn” là best practice thay vì chỉ chọn một công cụ ”tốt nhất”?

**Trả lời gợi ý gốc:**

Vì mỗi công cụ có ĐIỂM MẠNH/YẾU riêng (tốc độ vs độ chính xác, static vs dynamic) – không công cụ nào ”tốt nhất tuyệt đối”, kết hợp giúp phủ được nhiều loại lỗi hơn.

#### C2-2.5-ly_thuyet-11 · Câu gốc 11

Trình bày AddressSanitizer (ASan) và giải thích tại sao nó nhanh hơn Valgrind đáng kể.

**Trả lời gợi ý gốc:**

ASan CHÈN MÃ instrumentation NGAY LÚC BIÊN DỊCH (compile-time) thay vì mô phỏng CPU runtime như Valgrind – overhead thấp hơn nhiều (2-3x vs 10-50x) mà vẫn phát hiện chính xác.

#### C2-2.5-ly_thuyet-12 · Câu gốc 12

Giải thích UndefinedBehaviorSanitizer (UBSan) và loại lỗi đặc trưng nó phát hiện (liên hệ Integer Overflow đã học ở 2.3).

**Trả lời gợi ý gốc:**

UBSan phát hiện: integer overflow (signed), shift vượt quá số bit, chia cho 0, và các Undefined Behavior khác theo chuẩn C – trực tiếp liên hệ Integer Overflow đã học ở Mục 2.3.

#### C2-2.5-ly_thuyet-13 · Câu gốc 13

Mô tả lợi ích của việc kết hợp -fsanitize=address,undefined trong một lần chạy test.

**Trả lời gợi ý gốc:**

Kết hợp -fsanitize=address,undefined: một lần chạy TEST phát hiện được CẢ lỗi memory safety (ASan) LẪN undefined behavior (UBSan), tiết kiệm thời gian test so với chạy riêng lẻ.

#### C2-2.5-ly_thuyet-14 · Câu gốc 14

Trình bày khái niệm SARIF và vai trò chuẩn hóa báo cáo static analysis.

**Trả lời gợi ý gốc:**

SARIF: định dạng JSON CHUẨN HÓA để trao đổi kết quả giữa CÁC static analysis tool khác nhau, cho phép tích hợp thống nhất vào GitHub Code Scanning, IDE, dashboard nội bộ.

#### C2-2.5-ly_thuyet-15 · Câu gốc 15

Giải thích False Positive và False Negative, cho ví dụ minh họa mỗi loại trong ngữ cảnh static analysis.

**Trả lời gợi ý gốc:**

False Positive: công cụ báo ”có lỗi” nhưng THỰC TẾ không có lỗi (báo động giả); False Negative: công cụ báo ”an toàn” nhưng THỰC TẾ có lỗi (bỏ sót) – False Negative nguy hiểm hơn về mặt bảo mật.

### Thực hành (15 câu)

#### C2-2.5-thuc_hanh-01 · Câu gốc 1

Chạy gcc -Wall -Wextra -Wpedantic -Wconversion -Wshadow -Wformat=2 trên một file C và ghi lại toàn bộ warning.

**Trả lời gợi ý gốc:**

Chạy lệnh và ghi lại toàn bộ output warning, phân loại theo mức độ nghiêm trọng.

#### C2-2.5-thuc_hanh-02 · Câu gốc 2

Chạy cppcheck --enable=all trên c/ch2_memory/vulnerable.c và liệt kê toàn bộ cảnh báo.

**Trả lời gợi ý gốc:**

cppcheck --enable=all vulnerable.c liệt kê: deallocuse, doubleFree, memleak, nullPointer như đã xác nhận thực tế.

#### C2-2.5-thuc_hanh-03 · Câu gốc 3

Sửa ít nhất 2 cảnh báo tìm được từ câu 2 và chạy lại để xác nhận cảnh báo biến mất.

**Trả lời gợi ý gốc:**

Sửa 2 lỗi (VD null check + free đúng cách), chạy lại xác nhận cảnh báo tương ứng biến mất khỏi output.

#### C2-2.5-thuc_hanh-04 · Câu gốc 4

So sánh số lượng lỗi phát hiện được giữa -Wall -Wextra và Cppcheck trên cùng một file.

**Trả lời gợi ý gốc:**

So sánh: -Wall -Wextra thường phát hiện lỗi cú pháp/kiểu; Cppcheck phát hiện thêm UAF/leak – Cppcheck thường phát hiện NHIỀU hơn cho lỗi ngữ nghĩa.

#### C2-2.5-thuc_hanh-05 · Câu gốc 5

Chạy scan-build gcc -c program.c và mô tả báo cáo HTML sinh ra.

**Trả lời gợi ý gốc:**

scan-build gcc -c program.c sinh báo cáo HTML với đường dẫn (path) dẫn tới lỗi được highlight trực quan.

#### C2-2.5-thuc_hanh-06 · Câu gốc 6

Chạy valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes trên một chương trình có memory leak cố ý, diễn giải output.

**Trả lời gợi ý gốc:**

Output Valgrind: ”definitely lost: N bytes” kèm stack trace dòng malloc gây leak – diễn giải theo function/line cụ thể.

#### C2-2.5-thuc_hanh-07 · Câu gốc 7

Biên dịch một chương trình với -fsanitize=address và chạy với input gây buffer overflow, quan sát output ASan.

**Trả lời gợi ý gốc:**

Compile với -fsanitize=address, chạy input gây overflow: ASan in ra ”heap-buffer- overflow” kèm địa chỉ và stack trace chính xác.

#### C2-2.5-thuc_hanh-08 · Câu gốc 8

Biên dịch với -fsanitize=undefined và chạy với input gây integer overflow, quan sát output UBSan.

**Trả lời gợi ý gốc:**

Compile với -fsanitize=undefined, chạy input overflow: UBSan in ”signed integer overflow” kèm dòng code cụ thể.

#### C2-2.5-thuc_hanh-09 · Câu gốc 9

Viết Makefile với target check chạy cả compiler warnings và Cppcheck liên tiếp.

**Trả lời gợi ý gốc:**

check: n tgcc -Wall -Wextra -fsyntax-only *.c n tcppcheck --enable=all *.c

#### C2-2.5-thuc_hanh-10 · Câu gốc 10

Viết Makefile với target test-memory chạy chương trình dưới Valgrind, trả về error nếu có leak.

**Trả lời gợi ý gốc:**

test-memory: prog n tvalgrind --leak-check=full --error-exitcode=1 ./prog 28 MẬT – An toàn phần mềm

#### C2-2.5-thuc_hanh-11 · Câu gốc 11

Dùng Python (atpm.ch2_secure_c.static_check) chạy Cppcheck trên một thư mục và in ra summary.

**Trả lời gợi ý gốc:**

from atpm.ch2_secure_c.static_check import scan_directory; print(scan_directory("c/ch2_m

#### C2-2.5-thuc_hanh-12 · Câu gốc 12

Viết test pytest xác nhận fixed.c không có finding severity=”error” từ Cppcheck.

**Trả lời gợi ý gốc:**

assert [f for f in report.findings if f.severity=="error"] == []

#### C2-2.5-thuc_hanh-13 · Câu gốc 13

Viết test pytest xác nhận vulnerable.c CÓ ít nhất 3 loại lỗi cụ thể (deallocuse, doubleFree, memleak) từ Cppcheck. 29 MẬT – An toàn phần mềm

**Trả lời gợi ý gốc:**

assert "deallocuse","doubleFree","memleak" <= f.check_id for f in report.findings

#### C2-2.5-thuc_hanh-14 · Câu gốc 14

Cho một file C với UAF, chạy cả Cppcheck VÀ -fanalyzer, so sánh kết quả 2 công cụ.

**Trả lời gợi ý gốc:**

Cppcheck báo UAF cụ thể theo pattern; -fanalyzer có thể báo tương tự hoặc khác cách diễn đạt – so sánh độ chi tiết.

#### C2-2.5-thuc_hanh-15 · Câu gốc 15

Viết script Python parse output XML của Cppcheck (--xml) thành cấu trúc dữ liệu Python.

**Trả lời gợi ý gốc:**

import xml.etree.ElementTree as ET; root = ET.fromstring(xml_output) parse thành list finding.

### Tình huống thực tế (15 câu)

#### C2-2.5-thuc_te-01 · Câu gốc 1

Một công ty phát hiện Cppcheck báo QUÁ NHIỀU false positive khiến dev bắt đầu bỏ qua mọi cảnh báo. Đề xuất cách khắc phục ”alert fatigue”.

**Trả lời gợi ý gốc:**

Khắc phục alert fatigue: dùng --suppress cho false positive đã xác nhận, review định kỳ để tinh chỉnh config, không tắt hoàn toàn công cụ.

#### C2-2.5-thuc_te-02 · Câu gốc 2

Một tổ chức chỉ dùng Compiler Warnings, chưa từng dùng Cppcheck/Valgrind. Đề xuất lộ trình tích hợp dần các công cụ. 30 MẬT – An toàn phần mềm

**Trả lời gợi ý gốc:**

Lộ trình: (1) Warnings hiện tại giữ nguyên, (2) thêm Cppcheck vào CI trong 1 tháng, (3) thêm ASan vào test suite, (4) cuối cùng thêm Valgrind cho nightly build. 29 MẬT – An toàn phần mềm

#### C2-2.5-thuc_te-03 · Câu gốc 3

Một dự án CI/CD chạy Valgrind trên MỌI commit, làm pipeline chậm 10x. Phân tích vấn đề và đề xuất tối ưu.

**Trả lời gợi ý gốc:**

Vấn đề: Valgrind quá chậm cho mỗi commit; tối ưu: chuyển Valgrind sang nightly/weekly build, giữ Warnings+Cppcheck cho mỗi commit (nhanh).

#### C2-2.5-thuc_te-04 · Câu gốc 4

Một công ty phát hiện một lỗi UAF nghiêm trọng đã tồn tại nhiều năm mà Cppcheck KHÔNG phát hiện được. Phân tích giới hạn công cụ và đề xuất bổ sung.

**Trả lời gợi ý gốc:**

Giới hạn Cppcheck: heuristic không track được toàn bộ data-flow phức tạp; bổ sung: thêm Clang SA (path-sensitive) hoặc CBMC (Ch.3) cho module tới hạn.

#### C2-2.5-thuc_te-05 · Câu gốc 5

Một startup nhỏ không đủ ngân sách cho công cụ thương mại, chỉ dùng công cụ miễn phí. Đề xuất bộ công cụ tối ưu chi phí (Cppcheck, ASan, GCC warnings).

**Trả lời gợi ý gốc:**

Bộ công cụ tối ưu chi phí: GCC Warnings (miễn phí, có sẵn) + Cppcheck (mã nguồn mở) + ASan (tích hợp GCC/Clang, miễn phí) – đủ mạnh mà không tốn chi phí license.

#### C2-2.5-thuc_te-06 · Câu gốc 6

Một dự án hàng không yêu cầu ZERO warning từ TẤT CẢ công cụ static analysis trước khi release. Phân tích tính khả thi và đề xuất quy trình.

**Trả lời gợi ý gốc:**

Không hoàn toàn khả thi 100% (static analysis luôn có giới hạn); đề xuất: ZERO warning từ TOOLS đã chọn + formal verification (CBMC) bổ sung cho phần tới hạn nhất.

#### C2-2.5-thuc_te-07 · Câu gốc 7

Một công ty phát hiện ASan làm chương trình chậm 3x khi họ VÔ TÌNH build production với sanitizer bật. Phân tích hậu quả và đề xuất quy trình build tách biệt.

**Trả lời gợi ý gốc:**

Hậu quả: hiệu năng giảm đáng kể ảnh hưởng người dùng; đề xuất: tách biệt RÕ build script cho test (có sanitizer) và production (không sanitizer), dùng CI riêng biệt.

#### C2-2.5-thuc_te-08 · Câu gốc 8

Một tổ chức tài chính yêu cầu MỌI PR phải pass Cppcheck trước khi merge. Phân tích lợi ích và rủi ro của quy định cứng nhắc này.

**Trả lời gợi ý gốc:**

Lợi ích: đảm bảo chất lượng tối thiểu cho mọi code; rủi ro: có thể làm chậm velocity nếu Cppcheck có false positive cao – cần tinh chỉnh suppress list cẩn thận.

#### C2-2.5-thuc_te-09 · Câu gốc 9

Một dự án mã nguồn mở nhận đóng góp từ nhiều lập trình viên, chất lượng code không đồng đều. Đề xuất tích hợp static analysis vào quy trình review.

**Trả lời gợi ý gốc:**

Đề xuất: bắt buộc chạy Cppcheck TRONG pre-commit hook hoặc CI pipeline, review bắt buộc trước merge, kèm hướng dẫn cho contributor mới.

#### C2-2.5-thuc_te-10 · Câu gốc 10

Một công ty phát hiện Valgrind báo ”possibly lost” (không phải ”definitely lost”) cho một số block bộ nhớ. Giải thích ý nghĩa và mức độ cần quan tâm.

**Trả lời gợi ý gốc:**

”Possibly lost”: Valgrind không chắc chắn 100% (có thể còn con trỏ ẩn trỏ tới, VD trong container phức tạp); vẫn cần điều tra nhưng ưu tiên thấp hơn ”definitely lost”.

#### C2-2.5-thuc_te-11 · Câu gốc 11

Một hệ thống nhúng không đủ tài nguyên để chạy Valgrind (yêu cầu nhiều RAM). Đề xuất chiến lược test memory safety thay thế.

**Trả lời gợi ý gốc:**

Chiến lược thay thế: dùng static analysis kỹ hơn (Cppcheck+Clang SA), test trên simulator có nhiều RAM trước khi deploy lên thiết bị thật, careful manual review.

#### C2-2.5-thuc_te-12 · Câu gốc 12

Một dự án game engine phát hiện UBSan báo integer overflow trong một phép tính ”cố ý” (wrap-around mong muốn). Phân tích và đề xuất xử lý false positive hợp lệ này.

**Trả lời gợi ý gốc:**

Xử lý: xác nhận đây là hành vi MONG MUỐN (wrap-around cố ý), dùng __attribute__((no_saniti hoặc suppress cụ thể cho dòng đó, ghi comment giải thích rõ.

#### C2-2.5-thuc_te-13 · Câu gốc 13

Một công ty bảo mật phát hiện một binary sản phẩm đối thủ không hề dùng bất kỳ sanitizer nào khi test. Phân tích rủi ro và viết báo cáo đánh giá.

**Trả lời gợi ý gốc:**

Rủi ro: sản phẩm đối thủ có khả năng cao chứa lỗi memory safety chưa phát hiện; báo cáo: khuyến nghị KHÔNG dựa vào sản phẩm đó cho ứng dụng tới hạn cao.

#### C2-2.5-thuc_te-14 · Câu gốc 14

Một tổ chức yêu cầu chứng minh coverage của static analysis cho auditor bên ngoài. Đề xuất cách đo lường và báo cáo ”độ phủ” của Cppcheck/Clang SA.

**Trả lời gợi ý gốc:**

Đề xuất đo lường: % dòng code đã pass Cppcheck+Clang SA không lỗi, kết hợp coverage report từ ASan test suite làm bằng chứng cho auditor.

#### C2-2.5-thuc_te-15 · Câu gốc 15

Một dự án lớn (1 triệu dòng code) phát hiện chạy Cppcheck mất quá nhiều thời gian (giờ). Đề xuất chiến lược tối ưu (incremental analysis, parallel).

**Trả lời gợi ý gốc:**

Chiến lược: chạy Cppcheck INCREMENTAL (chỉ file thay đổi) cho mỗi commit, full scan định kỳ (weekly) cho toàn bộ codebase, dùng parallel processing.
