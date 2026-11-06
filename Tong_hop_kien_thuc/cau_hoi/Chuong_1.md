# Chương 1: Giới thiệu về An toàn phần mềm: ngân hàng câu hỏi gốc

**267câu.** Nguồn: `De-On-Tap.htm`, trường `QUIZ_DATA`; file `on-tap-an-toan-phan-mem_rutgon.html` giống byte. Đáp án/giải thích giữ theo nguồn, không mặc nhiên đã được xác minh.

[Mục lục ngân hàng](../11_Ngan_hang_cau_hoi.md) · [Đính chính](../08_Dinh_chinh_va_gioi_han.md)

Các đoạn nguồn có code/Markdown không hoàn chỉnh được đặt trong khối text để bảo toàn nội dung. Số thứ tự gốc có thể bắt đầu lại ở từng mục; ID bên dưới là duy nhất theo chương/mục/loại.

## Mục 1.1: Các khái niệm về an toàn phần mềm

### Trắc nghiệm (8 câu)

#### C1-1.1-trac_nghiem-01 · Câu gốc 1

An toàn phần mềm (software security) được định nghĩa là khả năng của phần mềm:

**A.** Chạy nhanh trong mọi điều kiện phần cứng

**B.** Tiếp tục hoạt động đúng đắn và chống chịu được tấn công có chủ đích

**C.** Không bao giờ có lỗi lập trình

**D.** Tương thích với mọi hệ điều hành

**Đáp án gốc:** B

**Giải thích gốc:**

Security là khả năng chống chịu tấn công chủ đích, không phải chạy nhanh hay không có lỗi.

#### C1-1.1-trac_nghiem-02 · Câu gốc 2

Sự khác biệt cốt lõi giữa Reliability và Security là gì?

**A.** Reliability chỉ áp dụng cho phần cứng

**B.** Security đối phó với đối thủ chủ động, Reliability đối phó với lỗi ngẫu nhiên

**C.** Không có sự khác biệt, hai khái niệm đồng nhất

**D.** Security chỉ liên quan tới mã hóa dữ liệu

**Đáp án gốc:** B

**Giải thích gốc:**

Security đối phó đối thủ chủ động; Reliability đối phó lỗi ngẫu nhiên.

#### C1-1.1-trac_nghiem-03 · Câu gốc 3

Đâu là ví dụ về hệ thống vừa cần Safety vừa cần Security?

**A.** Máy tính cá nhân dùng để soạn thảo văn bản

**B.** Ô tô tự lái

**C.** Máy in văn phòng

**D.** Đồng hồ báo thức

**Đáp án gốc:** B

**Giải thích gốc:**

Ô tô tự lái cần Safety (không gây hại vật lý) và Security (chống hack).

#### C1-1.1-trac_nghiem-04 · Câu gốc 4

Thuộc tính nào trong CIA Triad bị vi phạm khi kẻ tấn công đọc trộm dữ liệu nhạy cảm?

**A.** Confidentiality

**B.** Integrity

**C.** Availability

**D.** Authentication

**Đáp án gốc:** A

**Giải thích gốc:**

Đọc trộm dữ liệu vi phạm Confidentiality.

#### C1-1.1-trac_nghiem-05 · Câu gốc 5

Một cuộc tấn công DDoS chủ yếu vi phạm thuộc tính nào?

**A.** Confidentiality

**B.** Integrity

**C.** Availability

**D.** Non-repudiation

**Đáp án gốc:** C

**Giải thích gốc:**

DDoS làm hệ thống không khả dụng, vi phạm Availability.

#### C1-1.1-trac_nghiem-06 · Câu gốc 6

SQL Injection sửa đổi dữ liệu trái phép trong CSDL vi phạm thuộc tính nào?

**A.** Confidentiality

**B.** Integrity

**C.** Availability

**D.** Authorization

**Đáp án gốc:** B

**Giải thích gốc:**

Sửa dữ liệu trái phép vi phạm Integrity.

#### C1-1.1-trac_nghiem-07 · Câu gốc 7

Non-repudiation có nghĩa là gì?

**A.** Không thể chối bỏ hành động đã thực hiện

**B.** Không thể truy cập hệ thống

**C.** Không thể mã hóa dữ liệu

**D.** Không thể sao lưu dữ liệu

**Đáp án gốc:** A

**Giải thích gốc:**

Non-repudiation = không thể chối bỏ hành động.

#### C1-1.1-trac_nghiem-08 · Câu gốc 8

Accountability trong an toàn thông tin nhấn mạnh điều gì?

**A.** Khả năng truy vết trách nhiệm của hành động

**B.** Tốc độ xử lý giao dịch

**C.** Khả năng mở rộng của hệ thống

**D.** Chi phí vận hành hệ thống

**Đáp án gốc:** A

**Giải thích gốc:**

Accountability = khả năng truy vết trách nhiệm.

### Lý thuyết (15 câu)

#### C1-1.1-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa của an toàn phần mềm (software security) và chỉ ra điểm khác biệt với độ tin cậy (reliability).

**Trả lời gợi ý gốc:**

An toàn phần mềm là khả năng phần mềm tiếp tục hoạt động đúng khi bị tấn công chủ đích, khác Reliability (chỉ đối phó lỗi ngẫu nhiên) vì phải tính đến đối thủ thông minh, thích nghi.

#### C1-1.1-ly_thuyet-02 · Câu gốc 2

Mô tả bộ ba CIA (Confidentiality, Integrity, Availability) và cho ví dụ vi phạm mỗi thuộc tính.

**Trả lời gợi ý gốc:**

CIA: Confidentiality (chỉ người được phép mới đọc được), Integrity (dữ liệu không bị sửa trái phép), Availability (hệ thống sẵn sàng phục vụ). VD vi phạm: rò rỉ dữ liệu (C), SQL injection sửa DB (I), DDoS (A).

#### C1-1.1-ly_thuyet-03 · Câu gốc 3

Giải thích mối quan hệ giữa Threat, Vulnerability và Risk. Vẽ sơ đồ minh họa nếu cần.

**Trả lời gợi ý gốc:**

Threat là tác nhân có khả năng gây hại; Vulnerability là điểm yếu bị khai thác; Risk = hàm số của Likelihood (threat khai thác được vuln) và Impact.

#### C1-1.1-ly_thuyet-04 · Câu gốc 4

Bàn luận: tại sao ”Risk = Likelihood × Impact” chỉ là công thức định tính, không phải công thức toán học chính xác?

**Trả lời gợi ý gốc:**

Công thức chỉ định tính vì Likelihood và Impact không đo lường được chính xác bằng số học chặt chẽ – thường dựa trên đánh giá chuyên gia, thang định tính (thấp/trung bình/cao).

#### C1-1.1-ly_thuyet-05 · Câu gốc 5

Phân biệt Security và Safety. Cho ví dụ một hệ thống cần cả hai và giải thích vì sao.

**Trả lời gợi ý gốc:**

Safety: không gây hại cho người/môi trường dù có lỗi ngẫu nhiên. Security: chống chịu tấn công chủ đích. VD: ô tô tự lái cần cả hai vì lỗi phần mềm có thể gây tai nạn (safety) và có thể bị hack để gây tai nạn cố ý (security).

#### C1-1.1-ly_thuyet-06 · Câu gốc 6

Giải thích khái niệm Attack Surface và Attack Vector, chỉ ra mối quan hệ giữa chúng.

**Trả lời gợi ý gốc:**

Attack Surface là tổng mọi điểm tương tác có thể; Attack Vector là con đường/kỹ thuật cụ thể khai thác MỘT điểm trên attack surface đó.

#### C1-1.1-ly_thuyet-07 · Câu gốc 7

Mô tả nguyên lý Least Privilege và giải thích tại sao nó giảm thiểu thiệt hại khi hệ thống bị xâm nhập.

**Trả lời gợi ý gốc:**

Least Privilege: mỗi thực thể chỉ có quyền tối thiểu cần thiết, giúp giới hạn phạm vi thiệt hại nếu một thành phần bị xâm nhập (không lan rộng ra toàn hệ thống).

#### C1-1.1-ly_thuyet-08 · Câu gốc 8

Trình bày khái niệm Defense in Depth. Tại sao không nên chỉ dựa vào một lớp bảo vệ duy nhất?

**Trả lời gợi ý gốc:**

Defense in Depth dùng nhiều lớp bảo vệ độc lập (mạng, OS, ứng dụng, dữ liệu) vì không lớp nào là tuyệt đối – nếu một lớp bị vượt qua, lớp khác vẫn có thể chặn.

#### C1-1.1-ly_thuyet-09 · Câu gốc 9

Giải thích nguyên lý Kerckhoffs và ý nghĩa của nó đối với thiết kế hệ thống mật mã hiện đại.

**Trả lời gợi ý gốc:**

Kerckhoffs: hệ mật mã phải an toàn dù lộ toàn bộ thiết kế, trừ khóa bí mật – ý nghĩa: không nên dựa vào việc giấu thuật toán để đảm bảo an toàn.

#### C1-1.1-ly_thuyet-10 · Câu gốc 10

Bàn luận về sự khác biệt giữa Security by Design và Security by Obscurity. Có nên kết hợp cả hai không?

**Trả lời gợi ý gốc:**

Security by Design dựa trên kiến trúc/kiểm chứng chặt chẽ, chịu được khi công khai; Security by Obscurity dựa giấu chi tiết, sụp đổ khi lộ. Có thể kết hợp Obscurity như lớp BỔ SUNG, không phải lớp DUY NHẤT.

#### C1-1.1-ly_thuyet-11 · Câu gốc 11

Trình bày định nghĩa CVE, CWE, CVSS và giải thích mối quan hệ giữa ba khái niệm này.

**Trả lời gợi ý gốc:**

CVE định danh MỘT lỗ hổng cụ thể; CWE phân loại LOẠI điểm yếu; CVSS cho điểm số mức độ nghiêm trọng của một CVE cụ thể.

#### C1-1.1-ly_thuyet-12 · Câu gốc 12

Giải thích tại sao một CWE (loại lỗi) có thể sinh ra nhiều CVE (lỗ hổng cụ thể) trong các phần mềm khác nhau.

**Trả lời gợi ý gốc:**

Vì CWE là một MẪU lỗi tổng quát (VD buffer overflow), mẫu này có thể xuất hiện độc lập trong nhiều phần mềm khác nhau, mỗi lần xuất hiện với ngữ cảnh riêng được cấp một CVE riêng.

#### C1-1.1-ly_thuyet-13 · Câu gốc 13

Mô tả khái niệm Trust Boundary và giải thích vì sao mọi input đi qua ranh giới này cần được kiểm tra.

**Trả lời gợi ý gốc:**

Trust Boundary là nơi mức tin cậy dữ liệu thay đổi (VD: từ Internet vào server nội bộ); cần kiểm tra vì dữ liệu từ vùng kém tin cậy có thể chứa nội dung độc hại.

#### C1-1.1-ly_thuyet-14 · Câu gốc 14

Bàn luận: ”Ẩn URL quản trị” có phải là biện pháp an toàn đáng tin cậy không? Giải thích bằng khái niệm đã học.

**Trả lời gợi ý gốc:**

Không đáng tin cậy – đây là Security by Obscurity, kẻ tấn công chỉ cần quét/dò URL là phát hiện; cần cơ chế xác thực/phân quyền thực sự.

#### C1-1.1-ly_thuyet-15 · Câu gốc 15

Giải thích khái niệm Fail-Safe Default và cho ví dụ code minh họa lỗi ”fail-open”.

**Trả lời gợi ý gốc:**

Fail-Safe Default: khi lỗi, mặc định từ chối truy cập. VD lỗi: except: return True (fail-open); sửa: except: return False (fail-closed/fail-safe).

### Thực hành (15 câu)

#### C1-1.1-thuc_hanh-01 · Câu gốc 1

Viết một đoạn Python mô tả một class RiskAssessment với thuộc tính likelihood và impact (thang 1–3), có phương thức compute_risk() trả về tích hai giá trị.

**Trả lời gợi ý gốc:**

class RiskAssessment: def __init__(self, likelihood, impact): self.likelihood=likelihood self.impact=impact def compute_risk(self): return self.likelihood * self.impact

#### C1-1.1-thuc_hanh-02 · Câu gốc 2

````text
Cho đoạn code:

```
def check_permission (user):
try:
return db. get_role (user) == "admin "
except Exception :
return True
```

Sửa lại đoạn code trên để áp dụng nguyên lý Fail-Safe Default.
````

**Trả lời gợi ý gốc:**

Sửa except Exception: return True thành except Exception: return False – mặc định từ chối khi có lỗi.

#### C1-1.1-thuc_hanh-03 · Câu gốc 3

Viết một bảng (dùng Markdown hoặc LaTeX) liệt kê ít nhất 4 attack surface của một ứng dụng web đăng nhập bằng email/mật khẩu.

**Trả lời gợi ý gốc:**

Bảng gồm: (1) Form đăng nhập, (2) API endpoint, (3) Cookie/session token, (4) Header HTTP – mỗi dòng là 1 attack surface. 4

#### C1-1.1-thuc_hanh-04 · Câu gốc 4

Cho một API ”đổi email” của người dùng, vẽ Data Flow Diagram đơn giản gồm: người dùng, API, database, và đánh dấu trust boundary.

**Trả lời gợi ý gốc:**

DFD: [Người dùng] –HTTP–> [API] –SQL–> [Database]; trust boundary 1 giữa người dùng-API, trust boundary 2 giữa API-database.

#### C1-1.1-thuc_hanh-05 · Câu gốc 5

Tính điểm risk định tính (thang 1–3 cho likelihood và impact) cho tình huống: ”lỗi buffer overflow trong công cụ CLI chỉ chạy bởi root, không nhận input mạng”.

**Trả lời gợi ý gốc:**

Likelihood=1 (thấp, cần quyền local), Impact=3 (cao, RCE) → Risk = 3 (trung bình theo thang 1-9).

#### C1-1.1-thuc_hanh-06 · Câu gốc 6

Viết một đoạn code Python minh họa vi phạm Least Privilege (một service chạy với quyền admin không cần thiết) và bản đã sửa.

**Trả lời gợi ý gốc:**

VD vi phạm: service log chạy với quyền root để ghi file; sửa: tạo user riêng chỉ có quyền ghi vào thư mục log cụ thể.

#### C1-1.1-thuc_hanh-07 · Câu gốc 7

Tra cứu (giả lập, không cần internet) và trình bày cấu trúc của một mã CVE giả định, gồm: năm, số thứ tự, mô tả ngắn, CWE liên quan.

**Trả lời gợi ý gốc:**

CVE-20XX-NNNNN: năm phát hành, số thứ tự duy nhất trong năm, mô tả ngắn (VD: buffer overflow trong module X), CWE-120 liên quan.

#### C1-1.1-thuc_hanh-08 · Câu gốc 8

Với hệ thống ”Cambridge IT 9626 Hub” (nhắc trong project), liệt kê 3 trust boundary có thể tồn tại trong kiến trúc MVC. 5

**Trả lời gợi ý gốc:**

Trust boundary: (1) Client browser – Controller, (2) Controller – Model/Database, (3) AiController – external AI API.

#### C1-1.1-thuc_hanh-09 · Câu gốc 9

Viết một hàm Python is_fail_safe(func) kiểm tra (bằng cách gọi thử với input lỗi) xem một hàm có tuân thủ fail-safe default hay không.

**Trả lời gợi ý gốc:**

Hàm gọi func với input cố ý gây lỗi (None, giá trị âm...), kiểm tra kết quả trả về có phải giá trị ”an toàn” (False/deny) hay không.

#### C1-1.1-thuc_hanh-10 · Câu gốc 10

Cho một hệ thống chấm điểm CVSS đơn giản (chỉ dùng AV, AC, PR với trọng số cho trước), viết công thức tính điểm tổng hợp.

**Trả lời gợi ý gốc:**

Điểm = w1 × AV + w2 × AC + w3 × P R với wi là trọng số định trước cho từng mức giá trị của mỗi thành phần.

#### C1-1.1-thuc_hanh-11 · Câu gốc 11

Vẽ sơ đồ Defense in Depth cho một ứng dụng di động (mobile app) kết nối tới backend API.

**Trả lời gợi ý gốc:**

Sơ đồ: Lớp Network (firewall) → Lớp OS (patch) → Lớp App (input validation) → Lớp Data (mã hóa) bao quanh app mobile-backend.

#### C1-1.1-thuc_hanh-12 · Câu gốc 12

Viết đoạn mã C minh họa một hàm không kiểm tra kết quả malloc (vi phạm fail-safe) và bản đã sửa.

**Trả lời gợi ý gốc:**

int *p = malloc(sizeof(int)); *p = 5; (không kiểm tra NULL); sửa: thêm if (p == NULL) return -1; trước khi dùng.

#### C1-1.1-thuc_hanh-13 · Câu gốc 13

Với ví dụ đăng nhập trong atpm.ch1_concepts.kripke, chỉ ra Attack Surface tương ứng với mô hình đó.

**Trả lời gợi ý gốc:**

Attack Surface: input tại các hàm add_transition, tham số unsafe_label trong check_invariant (nếu lấy từ input người dùng).

#### C1-1.1-thuc_hanh-14 · Câu gốc 14

Viết một checklist (5 mục) để đánh giá xem một thiết kế hệ thống có tuân thủ Security by Design hay không.

**Trả lời gợi ý gốc:**

Checklist: (1) Kiến trúc có kiểm chứng hình thức? (2) Input validation ở mọi trust boundary? (3) Least Privilege áp dụng? (4) Có threat model? (5) Có defense in depth?

#### C1-1.1-thuc_hanh-15 · Câu gốc 15

Cho 3 tình huống lỗi bảo mật, xếp hạng risk (thấp/trung bình/cao) và giải thích ngắn gọn lý do.

**Trả lời gợi ý gốc:**

VD: (1) XSS trên form công khai = trung bình, (2) RCE qua API không xác thực = cao, (3) thông tin lộ trong log nội bộ = thấp.

### Tình huống thực tế (15 câu)

#### C1-1.1-thuc_te-01 · Câu gốc 1

Một công ty phát hiện lỗ hổng CVE mới trong thư viện họ đang dùng, nhưng bản vá làm chậm hệ thống 20%. Bàn luận cách ra quyết định (áp dụng khái niệm Risk).

**Trả lời gợi ý gốc:**

Cân nhắc Risk (nếu lỗ hổng dễ khai thác + impact cao thì ưu tiên vá dù giảm hiệu năng); có thể áp dụng mitigation tạm trong lúc tối ưu bản vá.

#### C1-1.1-thuc_te-02 · Câu gốc 2

Một startup thương mại điện tử nhỏ hỏi bạn nên ưu tiên đầu tư vào Confidentiality, Integrity hay Availability trước. Tư vấn dựa trên loại hình kinh doanh.

**Trả lời gợi ý gốc:**

Ưu tiên theo mô hình kinh doanh: thương mại điện tử ưu tiên Integrity (giá/đơn hàng đúng) và Availability (luôn bán được); dữ liệu thanh toán ưu tiên Confidentiality.

#### C1-1.1-thuc_te-03 · Câu gốc 3

Một nhân viên IT ẩn URL trang quản trị thay vì triển khai xác thực – sếp cho rằng ”vậy là đủ an toàn”. Phản biện quan điểm này.

**Trả lời gợi ý gốc:**

Phản biện: đây chỉ là Security by Obscurity, không phải giải pháp thực sự – kẻ tấn công có công cụ dò URL (dirb, gobuster) dễ dàng tìm ra; cần xác thực/phân quyền thật.

#### C1-1.1-thuc_te-04 · Câu gốc 4

Một hệ thống y tế cần cả Safety và Security. Đề xuất 3 biện pháp cụ thể đáp ứng đồng thời cả hai.

**Trả lời gợi ý gốc:**

Đề xuất: (1) hệ thống dự phòng (redundancy) cho Safety, (2) mã hóa kênh điều khiển cho Security, (3) formal verification cho module lái tự động tới hạn.

#### C1-1.1-thuc_te-05 · Câu gốc 5

Một ứng dụng ngân hàng bị tấn công qua lỗ hổng CWE đã biết từ 2 năm trước nhưng chưa vá. Phân tích nguyên nhân quy trình có thể dẫn tới tình huống này.

**Trả lời gợi ý gốc:**

Nguyên nhân: thiếu quy trình patch management, thiếu theo dõi CVE database, có thể thiếu trách nhiệm rõ ràng (ai chịu trách nhiệm vá lỗi).

#### C1-1.1-thuc_te-06 · Câu gốc 6

Một tổ chức cấp quyền admin cho TẤT CẢ nhân viên IT ”cho tiện”. Phân tích rủi ro và đề xuất áp dụng Least Privilege.

**Trả lời gợi ý gốc:**

Rủi ro: một tài khoản bị xâm nhập = toàn bộ hệ thống bị xâm nhập; đề xuất phân quyền theo vai trò cụ thể (RBAC) thay vì admin chung.

#### C1-1.1-thuc_te-07 · Câu gốc 7

Với hệ thống ”Cambridge IT 9626 Hub”, đề xuất một threat mà sinh viên (người dùng) có thể gây ra nếu tài khoản bị đánh cắp.

**Trả lời gợi ý gốc:**

Threat: tài khoản sinh viên bị đánh cắp có thể dùng để gian lận điểm số, xem đáp án trước hạn, hoặc mạo danh nộp bài hộ người khác.

#### C1-1.1-thuc_te-08 · Câu gốc 8

Một công ty bảo hiểm cần chứng minh Non-repudiation cho hợp đồng điện tử. Đề xuất giải pháp kỹ thuật.

**Trả lời gợi ý gốc:**

Giải pháp: chữ ký số (digital signature) + timestamp server tin cậy (trusted timestamping) cho mỗi hợp đồng ký kết.

#### C1-1.1-thuc_te-09 · Câu gốc 9

Phân tích một tình huống thực tế (giả định) nơi Defense in Depth đã ngăn chặn một cuộc tấn công dù một lớp bảo vệ đã bị vượt qua.

**Trả lời gợi ý gốc:**

VD: kẻ tấn công vượt qua firewall (lớp 1) nhưng bị chặn bởi input validation ở tầng ứng dụng (lớp 2) nhờ Defense in Depth.

#### C1-1.1-thuc_te-10 · Câu gốc 10

Một CVE mới công bố có điểm CVSS 9.8 (Critical) nhưng ảnh hưởng một tính năng ít dùng. Bàn luận cách ưu tiên vá lỗi.

**Trả lời gợi ý gốc:**

Cân nhắc: dù CVSS cao, impact thực tế thấp do ít người dùng tính năng đó – vẫn nên vá nhưng có thể không cần ”khẩn cấp tuyệt đối”, ưu tiên theo exposure thực tế.

#### C1-1.1-thuc_te-11 · Câu gốc 11

Một hệ thống IoT (thiết bị gia dụng thông minh) không cập nhật firmware được. Phân tích attack surface và đề xuất giảm thiểu risk.

**Trả lời gợi ý gốc:**

Attack surface: giao diện web quản lý, giao thức kết nối thiết bị (thường không mã hóa); giảm risk bằng cách cô lập mạng IoT (network segmentation) và giám sát bất thường.

#### C1-1.1-thuc_te-12 · Câu gốc 12

Một nhân viên cũ vẫn còn quyền truy cập hệ thống 6 tháng sau khi nghỉ việc. Phân tích vi phạm nguyên lý nào và hậu quả tiềm ẩn.

**Trả lời gợi ý gốc:**

Vi phạm Least Privilege và thiếu Accountability trong quy trình offboarding; hậu quả: cựu nhân viên có thể truy cập/đánh cắp dữ liệu nhạy cảm.

#### C1-1.1-thuc_te-13 · Câu gốc 13

Một trường đại học lưu trữ điểm số sinh viên. Xác định thuộc tính CIA nào QUAN TRỌNG NHẤT cần bảo vệ và giải thích.

**Trả lời gợi ý gốc:**

````text
Integrity quan trọng nhất (điểm số bị sửa sai ảnh hưởng trực tiếp quyền lợi học tập), dù Confidentiality cũng cần thiết cho quyền riêng tư. 6

```
MỤC 1.2 – MỘT SỐ VẤN ĐỀ VỀ AN TOÀN PHẦN MỀM
```
````

#### C1-1.1-thuc_te-14 · Câu gốc 14

Một ứng dụng mạng xã hội bị lộ dữ liệu người dùng do thiếu mã hóa khi lưu trữ. Phân loại CWE liên quan và đề xuất khắc phục.

**Trả lời gợi ý gốc:**

CWE-311 (Missing Encryption of Sensitive Data); khắc phục: mã hóa dữ liệu at-rest bằng AES, xem xét format-preserving encryption nếu cần.

#### C1-1.1-thuc_te-15 · Câu gốc 15

Một tổ chức từ chối công bố lỗ hổng đã fix (không xin CVE) vì sợ ảnh hưởng danh tiếng. Bàn luận về đạo đức và trách nhiệm.

**Trả lời gợi ý gốc:**

Bàn luận: minh bạch (công bố CVE) giúp cộng đồng phòng vệ tốt hơn dù ảnh hưởng danh tiếng ngắn hạn; trách nhiệm đạo đức nên ưu tiên an toàn người dùng hơn danh tiếng.

## Mục 1.2: Một số vấn đề về an toàn phần mềm

### Trắc nghiệm (9 câu)

#### C1-1.2-trac_nghiem-01 · Câu gốc 1

Vì sao phần mềm được coi là ”mắt xích yếu nhất” trong bảo mật hệ thống?

**A.** Vì phần mềm luôn chậm hơn phần cứng

**B.** Vì độ phức tạp cao, áp lực thời gian, và legacy code

**C.** Vì phần mềm không thể mã hóa dữ liệu

**D.** Vì phần mềm luôn miễn phí

**Đáp án gốc:** B

**Giải thích gốc:**

Độ phức tạp cao, áp lực thời gian, legacy code.

#### C1-1.2-trac_nghiem-02 · Câu gốc 2

Nguyên lý ”shift-left” trong an toàn phần mềm có nghĩa là gì?

**A.** Dịch chuyển việc phát hiện lỗi sang giai đoạn SỚM hơn trong SDLC

**B.** Chuyển đội ngũ phát triển sang múi giờ khác

**C.** Ưu tiên tính năng mới hơn bảo mật

**D.** Dịch chuyển trách nhiệm bảo mật cho khách hàng

**Đáp án gốc:** A

**Giải thích gốc:**

Shift-left: phát hiện lỗi sớm hơn trong SDLC.

#### C1-1.2-trac_nghiem-03 · Câu gốc 3

Theo biểu đồ chi phí sửa lỗi, giai đoạn nào có chi phí sửa lỗi CAO NHẤT?

**A.** Giai đoạn yêu cầu

**B.** Giai đoạn thiết kế

**C.** Giai đoạn mã hóa

**D.** Giai đoạn vận hành (sau khi phát hành)

**Đáp án gốc:** D

**Giải thích gốc:**

Giai đoạn vận hành có chi phí sửa lỗi cao nhất.

#### C1-1.2-trac_nghiem-04 · Câu gốc 4

CWE-120 tương ứng với loại lỗi nào?

**A.** SQL Injection

**B.** Buffer Overflow

**C.** Use-After-Free

**D.** Hard-coded credentials

**Đáp án gốc:** B

**Giải thích gốc:**

CWE-120 = Buffer Overflow.

#### C1-1.2-trac_nghiem-05 · Câu gốc 5

CWE-89 tương ứng với loại lỗi nào?

**A.** Buffer Overflow

**B.** SQL Injection

**C.** Race Condition

**D.** Weak cryptography

**Đáp án gốc:** B

**Giải thích gốc:**

CWE-89 = SQL Injection.

#### C1-1.2-trac_nghiem-06 · Câu gốc 6

CWE-416 (Use-After-Free) thuộc nhóm lỗi nào?

**A.** Injection

**B.** Memory corruption

**C.** Cryptographic Issues

**D.** Broken Access Control

**Đáp án gốc:** B

**Giải thích gốc:**

CWE-416 thuộc nhóm Memory corruption.

#### C1-1.2-trac_nghiem-07 · Câu gốc 7

CWE-362 liên quan tới loại lỗi nào?

**A.** Race Condition (TOCTOU)

**B.** SQL Injection

**C.** Buffer Overflow

**D.** Hard-coded credentials

**Đáp án gốc:** A

**Giải thích gốc:**

CWE-362 = Race Condition (TOCTOU).

#### C1-1.2-trac_nghiem-08 · Câu gốc 8

STRIDE là viết tắt của các loại đe dọa nào?

**A.** Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege

**B.** Security, Testing, Risk, Integrity, Development, Evaluation

**C.** Static, Trace, Reachability, Input, Debug, Execution

**D.** Software, Testing, Review, Inspection, Design, Engineering

**Đáp án gốc:** A

**Giải thích gốc:**

STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege.

#### C1-1.2-trac_nghiem-09 · Câu gốc 9

Trong STRIDE, ”Tampering” vi phạm thuộc tính nào?

**A.** Confidentiality

**B.** Integrity

**C.** Availability

**D.** Authentication

**Đáp án gốc:** B

**Giải thích gốc:**

Tampering vi phạm Integrity.

### Lý thuyết (15 câu)

#### C1-1.2-ly_thuyet-01 · Câu gốc 1

Trình bày các nguyên nhân chính khiến phần mềm trở thành ”mắt xích yếu nhất” trong bảo mật hệ thống.

**Trả lời gợi ý gốc:**

````text
Nguyên nhân: độ phức tạp tăng cấp số nhân, áp lực time-to-market, legacy code không theo kịp đe dọa mới, chuỗi cung ứng phức tạp, lỗi con người có hệ thống. 8

```
MỤC 1.2 – MỘT SỐ VẤN ĐỀ VỀ AN TOÀN PHẦN MỀM
```
````

#### C1-1.2-ly_thuyet-02 · Câu gốc 2

Giải thích nguyên lý ”shift-left” và mối liên hệ với biểu đồ chi phí sửa lỗi theo giai đoạn SDLC.

**Trả lời gợi ý gốc:**

Shift-left nghĩa là phát hiện lỗi CÀNG SỚM CÀNG TỐT trong SDLC; liên hệ biểu đồ chi phí: sửa lỗi ở giai đoạn yêu cầu rẻ hơn rất nhiều so với sau khi phát hành.

#### C1-1.2-ly_thuyet-03 · Câu gốc 3

Mô tả ít nhất 4 nhóm lỗ hổng phổ biến (memory corruption, injection, broken access control, crypto issues) kèm ví dụ CWE.

**Trả lời gợi ý gốc:**

Memory corruption (CWE-120 buffer overflow), Injection (CWE-89 SQLi), Broken Access Control (CWE-284), Cryptographic Issues (CWE-327 weak crypto).

#### C1-1.2-ly_thuyet-04 · Câu gốc 4

Trình bày mô hình STRIDE và giải thích ý nghĩa của từng chữ cái.

**Trả lời gợi ý gốc:**

STRIDE: Spoofing (giả mạo danh tính), Tampering (sửa đổi trái phép), Repudiation (chối bỏ hành động), Information Disclosure (rò rỉ), DoS (từ chối dịch vụ), Elevation of Privilege (leo thang quyền).

#### C1-1.2-ly_thuyet-05 · Câu gốc 5

Giải thích cách áp dụng STRIDE kết hợp với Data Flow Diagram trong threat modeling.

**Trả lời gợi ý gốc:**

DFD xác định các thành phần và trust boundary; tại mỗi trust boundary, áp dụng STRIDE để liệt kê đe dọa tương ứng có thể xảy ra khi dữ liệu đi qua ranh giới đó.

#### C1-1.2-ly_thuyet-06 · Câu gốc 6

Bàn luận: vì sao SQL Injection vẫn là một trong những lỗ hổng phổ biến nhất dù đã được biết đến hàng chục năm?

**Trả lời gợi ý gốc:**

Vì lập trình viên vẫn tiếp tục nối chuỗi SQL trực tiếp do thiếu đào tạo/awareness, và nhiều framework cũ không mặc định dùng parameterized query.

#### C1-1.2-ly_thuyet-07 · Câu gốc 7

Trình bày cơ chế gây lỗi của Heartbleed (CVE-2014-0160) và bài học rút ra.

**Trả lời gợi ý gốc:**

Heartbleed: thiếu kiểm tra độ dài trong xử lý heartbeat TLS, cho phép đọc vượt biên bộ nhớ tiến trình, rò rỉ khóa riêng/session token; bài học: lỗi kiểm tra độ dài đơn giản có thể gây hậu quả toàn cầu.

#### C1-1.2-ly_thuyet-08 · Câu gốc 8

Giải thích khái niệm Supply Chain Security và tại sao nó ngày càng quan trọng trong phát triển phần mềm hiện đại.

**Trả lời gợi ý gốc:**

Supply Chain Security quan trọng vì phần mềm hiện đại phụ thuộc hàng trăm thư viện bên thứ ba, một thư viện bị xâm nhập ảnh hưởng MỌI dự án dùng nó.

#### C1-1.2-ly_thuyet-09 · Câu gốc 9

Mô tả vai trò của SBOM (Software Bill of Materials) trong quản lý rủi ro chuỗi cung ứng.

**Trả lời gợi ý gốc:**

SBOM là danh sách đầy đủ các thành phần/dependency trong phần mềm, giúp nhanh chóng xác định có bị ảnh hưởng bởi một CVE mới hay không.

#### C1-1.2-ly_thuyet-10 · Câu gốc 10

Trình bày tổng quan OWASP Top 10 và giải thích vì sao ”Broken Access Control” thường đứng đầu danh sách.

**Trả lời gợi ý gốc:**

OWASP Top 10 là 10 lỗ hổng phổ biến nhất cho web app; Broken Access Control đứng đầu vì lỗi phân quyền dễ mắc phải và hậu quả trực tiếp (truy cập trái phép dữ liệu/chức năng).

#### C1-1.2-ly_thuyet-11 · Câu gốc 11

Giải thích Microsoft SDL (Security Development Lifecycle) và cách nó tích hợp bảo mật vào từng giai đoạn phát triển.

**Trả lời gợi ý gốc:**

Microsoft SDL tích hợp hoạt động bảo mật (threat modeling, code review, testing) vào TỪNG giai đoạn SDLC thay vì chỉ kiểm tra cuối cùng.

#### C1-1.2-ly_thuyet-12 · Câu gốc 12

Bàn luận về case study ”event-stream npm package” – bài học gì rút ra cho quản lý dependency?

**Trả lời gợi ý gốc:**

Bài học: cần kiểm tra kỹ dependency (kể cả gián tiếp), dùng lockfile, giám sát thay đổi bất thường trong package đã tin tưởng trước đó.

#### C1-1.2-ly_thuyet-13 · Câu gốc 13

Trình bày sự khác biệt giữa CWE Top 25 và OWASP Top 10 về phạm vi áp dụng.

**Trả lời gợi ý gốc:**

OWASP Top 10 chỉ áp dụng cho ứng dụng WEB; CWE Top 25 tổng quát hơn, áp dụng cho MỌI loại phần mềm (desktop, embedded, web...).

#### C1-1.2-ly_thuyet-14 · Câu gốc 14

Giải thích tại sao ”áp lực thời gian ra thị trường” thường mâu thuẫn với đầu tư cho an toàn phần mềm.

**Trả lời gợi ý gốc:**

Áp lực thời gian khiến đội phát triển bỏ qua bước bảo mật (threat modeling, code review) để kịp deadline, tích lũy nợ kỹ thuật bảo mật (security debt).

#### C1-1.2-ly_thuyet-15 · Câu gốc 15

Mô tả cách vẽ một Data Flow Diagram đơn giản, chỉ ra các thành phần: external entity, process, data store, data flow.

**Trả lời gợi ý gốc:**

DFD gồm: external entity (hình chữ nhật, tác nhân ngoài), process (hình tròn, xử lý), data store (hình chữ nhật hở, lưu trữ), data flow (mũi tên, luồng dữ liệu).

### Thực hành (15 câu)

#### C1-1.2-thuc_hanh-01 · Câu gốc 1

````text
Viết lại đoạn code SQL injection sau bằng parameterized query (Python + sqlite3):

```
query = " SELECT * FROM users WHERE name = '" + user_input + "'"
cursor . execute (query)
```
````

**Trả lời gợi ý gốc:**

cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,)).

#### C1-1.2-thuc_hanh-02 · Câu gốc 2

Vẽ Data Flow Diagram cho hệ thống đăng nhập của ”Cambridge IT 9626 Hub” và xác định các trust boundary.

**Trả lời gợi ý gốc:**

DFD: User –HTTP–> Web App –Query–> Database; boundary tại User-WebApp và WebApp-DB.

#### C1-1.2-thuc_hanh-03 · Câu gốc 3

Áp dụng STRIDE cho một API ”đổi mật khẩu” – liệt kê ít nhất 3 đe dọa tương ứng với 3 chữ cái khác nhau.

**Trả lời gợi ý gốc:**

S (Spoofing session), T (sửa payload đổi user_id), E (bỏ qua check mật khẩu cũ).

#### C1-1.2-thuc_hanh-04 · Câu gốc 4

Viết một bảng ánh xạ 5 CWE phổ biến với ví dụ CVE tương ứng (có thể dùng thông tin giả định có cấu trúc hợp lệ).

**Trả lời gợi ý gốc:**

CWE-120→CVE giả định ”Buffer overflow trong parser X (2023)”; tương tự cho 4 CWE khác.

#### C1-1.2-thuc_hanh-05 · Câu gốc 5

Cho một đoạn mã C có lỗi buffer overflow (dùng strcpy), chỉ ra dòng lỗi và viết bản đã sửa dùng snprintf.

**Trả lời gợi ý gốc:**

Dòng lỗi: strcpy(buf, input); sửa: snprintf(buf, sizeof(buf), "%s", input).

#### C1-1.2-thuc_hanh-06 · Câu gốc 6

Thiết kế một checklist Secure SDLC (5 giai đoạn, mỗi giai đoạn 1 hoạt động bảo mật cụ thể).

**Trả lời gợi ý gốc:**

````text
```
giai đoạn: Yêu cầu (threat model), Thiết kế (kiến trúc), Coding (secure coding +
```

SAST), Test (DAST), Vận hành (patch).
````

#### C1-1.2-thuc_hanh-07 · Câu gốc 7

Viết một đoạn Python mô phỏng kiểm tra ”Security Misconfiguration”: kiểm tra xem một web server có bật debug mode không nên có trong production.

**Trả lời gợi ý gốc:**

def check_debug(config): return not config.get("DEBUG", False) kiểm tra debug mode tắt.

#### C1-1.2-thuc_hanh-08 · Câu gốc 8

Vẽ DFD cho một hệ thống thanh toán trực tuyến đơn giản (người dùng - web app - payment gateway - database).

**Trả lời gợi ý gốc:**

````text
DFD: User → WebApp → Payment Gateway → Database, 3 trust boundary tương ứng. 10

```
MỤC 1.2 – MỘT SỐ VẤN ĐỀ VỀ AN TOÀN PHẦN MỀM
```
````

#### C1-1.2-thuc_hanh-09 · Câu gốc 9

Áp dụng STRIDE đầy đủ (6 loại đe dọa) cho một API ”tải lên file avatar người dùng”.

**Trả lời gợi ý gốc:**

STRIDE cho upload avatar: S (giả file của người khác), T (thay nội dung file), I (đọc file người khác), D (upload file khổng lồ gây DoS), E (upload file thực thi giành quyền).

#### C1-1.2-thuc_hanh-10 · Câu gốc 10

````text
Viết một bảng SBOM đơn giản (giả định) cho một dự án Python nhỏ, liệt kê 5 dependency và version. 11

```
MỤC 1.2 – MỘT SỐ VẤN ĐỀ VỀ AN TOÀN PHẦN MỀM
```
````

**Trả lời gợi ý gốc:**

SBOM: {”requests”: ”2.28.0”, ”flask”: ”2.2.0”, ”numpy”: ”1.23.0”, ”pillow”: ”9.2.0”, ”sqlalchemy”: ”1.4.0”}.

#### C1-1.2-thuc_hanh-11 · Câu gốc 11

Cho một danh sách 5 lỗ hổng với CVSS score, sắp xếp theo độ ưu tiên vá lỗi và giải thích.

**Trả lời gợi ý gốc:**

Ưu tiên theo CVSS giảm dần, đồng thời cân nhắc exposure thực tế (internet-facing trước, internal sau).

#### C1-1.2-thuc_hanh-12 · Câu gốc 12

Viết một script Python đơn giản quét một thư mục dự án và liệt kê các file có chứa chuỗi ”password =” trực tiếp trong mã nguồn (hard-coded credentials).

**Trả lời gợi ý gốc:**

import os; for f in files: if "password =" in open(f).read(): print(f).

#### C1-1.2-thuc_hanh-13 · Câu gốc 13

Thiết kế một biểu mẫu (form) threat model đơn giản (STRIDE + DFD) áp dụng cho tính năng ”quên mật khẩu”.

**Trả lời gợi ý gốc:**

Form: mục tiêu (STRIDE cho reset password), phạm vi (API + email flow), constraint (không có source code bên email provider).

#### C1-1.2-thuc_hanh-14 · Câu gốc 14

Viết đoạn mã minh họa một Race Condition (TOCTOU) đơn giản trong Python (kiểm tra file tồn tại rồi mở file).

**Trả lời gợi ý gốc:**

if os.path.exists(f): ...(gian delay)...; open(f) – file có thể bị thay đổi giữa check và open.

#### C1-1.2-thuc_hanh-15 · Câu gốc 15

Cho đoạn mã sử dụng eval() với input người dùng trong Python, chỉ ra rủi ro và viết bản thay thế an toàn.

**Trả lời gợi ý gốc:**

Rủi ro eval(user_input): RCE tùy ý; thay bằng ast.literal_eval() nếu chỉ cần parse literal.

### Tình huống thực tế (15 câu)

#### C1-1.2-thuc_te-01 · Câu gốc 1

Một công ty phát hiện website của họ bị SQL Injection sau 3 năm vận hành không phát hiện. Phân tích nguyên nhân quy trình và đề xuất cải thiện.

**Trả lời gợi ý gốc:**

Thiếu quy trình security testing định kỳ/SAST trong CI; đề xuất tích hợp Cppcheck/SonarQube vào pipeline.

#### C1-1.2-thuc_te-02 · Câu gốc 2

Một dự án phần mềm outsource không có bước threat modeling. Đề xuất cách tích hợp STRIDE vào quy trình hiện tại của họ.

**Trả lời gợi ý gốc:**

Đề xuất workshop STRIDE 1 buổi/sprint, yêu cầu vẽ DFD tối thiểu cho mọi API mới trước khi code.

#### C1-1.2-thuc_te-03 · Câu gốc 3

Một tổ chức dùng lại thư viện mã nguồn mở đã ngừng bảo trì (unmaintained) từ 5 năm trước. Phân tích rủi ro Supply Chain và đề xuất giải pháp.

**Trả lời gợi ý gốc:**

Rủi ro cao vì không ai vá lỗi/theo dõi CVE cho thư viện đó; đề xuất thay thế bằng thư viện đang bảo trì hoặc tự fork và vá.

#### C1-1.2-thuc_te-04 · Câu gốc 4

Một startup phát hiện có ”backdoor” (hard-coded credentials) trong code do một cựu nhân viên để lại. Phân tích CWE liên quan và quy trình xử lý.

**Trả lời gợi ý gốc:**

CWE-798 (hard-coded credentials); quy trình: thu hồi ngay credential, rà soát toàn bộ commit history, áp dụng secret scanning tool.

#### C1-1.2-thuc_te-05 · Câu gốc 5

Một hệ thống chính phủ bị tấn công qua lỗ hổng Heartbleed sau 2 năm công bố CVE. Phân tích lý do quy trình patch management có thể đã thất bại.

**Trả lời gợi ý gốc:**

Quy trình patch management thất bại: có thể thiếu inventory hệ thống bị ảnh hưởng, thiếu ưu tiên hóa dựa trên CVSS, hoặc thiếu ngân sách/nhân lực vá.

#### C1-1.2-thuc_te-06 · Câu gốc 6

Một công ty game online bị tố cáo lưu mật khẩu người dùng dạng plaintext. Phân tích vi phạm CWE và đề xuất khắc phục khẩn cấp.

**Trả lời gợi ý gốc:**

Vi phạm CWE-256/259 (lưu mật khẩu không mã hóa); khắc phục khẩn: hash bằng bcrypt/Argon2, buộc reset mật khẩu toàn bộ người dùng.

#### C1-1.2-thuc_te-07 · Câu gốc 7

Một tổ chức tài chính phải tuân thủ PCI-DSS, yêu cầu threat modeling định kỳ. Đề xuất tần suất và phạm vi threat modeling phù hợp.

**Trả lời gợi ý gốc:**

Tần suất: threat modeling mỗi khi có tính năng mới quan trọng, và review định kỳ hàng quý toàn bộ hệ thống.

#### C1-1.2-thuc_te-08 · Câu gốc 8

Một nhóm phát triển ưu tiên ”ra mắt đúng deadline” và bỏ qua bước security review. Phân tích hậu quả tiềm ẩn dựa trên biểu đồ chi phí sửa lỗi.

**Trả lời gợi ý gốc:**

Hậu quả: lỗi phát hiện muộn (production) có chi phí gấp hàng chục-trăm lần so với phát hiện ở thiết kế; có thể dẫn tới security incident tốn kém hơn deadline bị trễ.

#### C1-1.2-thuc_te-09 · Câu gốc 9

Một ứng dụng di động gửi dữ liệu vị trí người dùng không mã hóa qua HTTP. Phân tích CWE và tư vấn khắc phục.

**Trả lời gợi ý gốc:**

CWE-319 (Cleartext Transmission); khắc phục: bắt buộc HTTPS/TLS cho mọi kết nối truyền dữ liệu vị trí.

#### C1-1.2-thuc_te-10 · Câu gốc 10

Một công ty phát hiện chuỗi cung ứng phần mềm của họ bị xâm nhập qua một CI/CD pipeline bị chiếm quyền. Đề xuất biện pháp phòng ngừa (SBOM, ký số).

**Trả lời gợi ý gốc:**

Biện pháp: ký số artifact trong CI/CD, giới hạn quyền truy cập pipeline, audit log mọi thay đổi cấu hình CI/CD, dùng SBOM theo dõi dependency.

#### C1-1.2-thuc_te-11 · Câu gốc 11

````text
Một tổ chức y tế bị tấn công ransomware qua lỗ hổng chưa vá đã biết

```
tháng. Phân tích lỗi quy trình patch management.
```
````

**Trả lời gợi ý gốc:**

Lỗi quy trình: thiếu inventory tài sản, thiếu quy trình patch bắt buộc trong SLA, có thể thiếu giám sát cảnh báo CVE tự động.

#### C1-1.2-thuc_te-12 · Câu gốc 12

Một dự án mã nguồn mở phổ biến (dùng bởi hàng nghìn công ty) phát hiện lỗ hổng nghiêm trọng. Bàn luận trách nhiệm của: (a) maintainer, (b) công ty sử dụng.

**Trả lời gợi ý gốc:**

(a) Maintainer: công bố minh bạch, vá nhanh nhất có thể; (b) Công ty: chủ động theo dõi CVE của mọi dependency, không chỉ dựa vào maintainer.

#### C1-1.2-thuc_te-13 · Câu gốc 13

Một hệ thống trường học lưu trữ hồ sơ học sinh bị truy cập trái phép qua API thiếu access control. Phân tích OWASP category và đề xuất khắc phục.

**Trả lời gợi ý gốc:**

OWASP category: Broken Access Control (A01); khắc phục: kiểm tra authorization ở MỌI endpoint, không chỉ ở giao diện.

#### C1-1.2-thuc_te-14 · Câu gốc 14

Một công ty bảo hiểm phát hiện nhân viên cũ vẫn truy cập được hệ thống nội bộ qua VPN. Phân tích nguyên nhân và STRIDE category liên quan.

**Trả lời gợi ý gốc:**

Nguyên nhân: thiếu quy trình offboarding chuẩn; STRIDE category: Elevation of Privilege / Spoofing (truy cập trái phép danh nghĩa cũ).

#### C1-1.2-thuc_te-15 · Câu gốc 15

Một ứng dụng thương mại điện tử gặp sự cố Race Condition khi nhiều người dùng cùng mua sản phẩm số lượng có hạn cuối cùng. Phân tích và đề xuất giải pháp.

**Trả lời gợi ý gốc:**

Đây là Race Condition (TOCTOU); giải pháp: dùng transaction có khóa (locking) hoặc atomic decrement khi kiểm tra và trừ tồn kho.

## Mục 1.3: Kiểm thử và kiểm chứng phần mềm I

### Trắc nghiệm (8 câu)

#### C1-1.3-trac_nghiem-01 · Câu gốc 1

Theo ISTQB, testing bao gồm những hoạt động nào?

**A.** Chỉ chạy chương trình và quan sát kết quả

**B.** Lập kế hoạch, thiết kế test case, thực thi, và cả hoạt động tĩnh như review

**C.** Chỉ viết tài liệu đặc tả

**D.** Chỉ áp dụng sau khi phần mềm phát hành

**Đáp án gốc:** B

**Giải thích gốc:**

Testing bao gồm cả hoạt động tĩnh như review, không chỉ chạy chương trình.

#### C1-1.3-trac_nghiem-02 · Câu gốc 2

Nguyên tắc ”Testing shows presence of defects” có nghĩa là gì?

**A.** Testing chứng minh phần mềm không có lỗi

**B.** Testing chỉ cho thấy SỰ HIỆN DIỆN của lỗi, không chứng minh không có lỗi

**C.** Testing luôn tìm ra 100% lỗi

**D.** Testing không có giá trị thực tiễn

**Đáp án gốc:** B

**Giải thích gốc:**

Testing chỉ cho thấy sự hiện diện của lỗi.

#### C1-1.3-trac_nghiem-03 · Câu gốc 3

”Exhaustive testing is impossible” đề cập tới nguyên tắc nào?

**A.** Kiểm thử toàn bộ (mọi input) là bất khả thi

**B.** Luôn cần kiểm thử tự động hoàn toàn

**C.** Kiểm thử thủ công luôn tốt hơn tự động

**D.** Không cần kiểm thử nếu code ngắn

**Đáp án gốc:** A

**Giải thích gốc:**

Kiểm thử toàn bộ là bất khả thi.

#### C1-1.3-trac_nghiem-04 · Câu gốc 4

”Defect clustering” (80/20) đề cập tới hiện tượng gì?

**A.** Lỗi phân bố đều trên toàn bộ mã nguồn

**B.** Phần lớn lỗi tập trung ở một số phần nhỏ của hệ thống

**C.** Lỗi chỉ xảy ra vào cuối dự án

**D.** Lỗi luôn liên quan tới giao diện người dùng

**Đáp án gốc:** B

**Giải thích gốc:**

Lỗi thường tập trung ở một số phần nhỏ (80/20).

#### C1-1.3-trac_nghiem-05 · Câu gốc 5

”Pesticide paradox” trong testing muốn nói điều gì?

**A.** Test case cũ dần mất hiệu quả, cần làm mới thường xuyên

**B.** Càng test nhiều càng ít lỗi

**C.** Không nên test lại cùng một chức năng

**D.** Thuốc trừ sâu có thể diệt được mọi loại côn trùng

**Đáp án gốc:** A

**Giải thích gốc:**

Test case cũ mất hiệu quả dần, cần làm mới.

#### C1-1.3-trac_nghiem-06 · Câu gốc 6

V-Model trong kiểm thử phần mềm thể hiện điều gì?

**A.** Mối quan hệ giữa các giai đoạn phát triển và các mức kiểm thử tương ứng

**B.** Biểu đồ hiệu năng hệ thống

**C.** Sơ đồ mạng máy tính

**D.** Cấu trúc dữ liệu dạng cây

**Đáp án gốc:** A

**Giải thích gốc:**

V-Model thể hiện quan hệ giữa giai đoạn phát triển và mức kiểm thử.

#### C1-1.3-trac_nghiem-07 · Câu gốc 7

Unit Test tương ứng với giai đoạn nào trong V-Model?

**A.** Yêu cầu

**B.** Thiết kế kiến trúc

**C.** Coding (mã hóa)

**D.** Thiết kế chi tiết

**Đáp án gốc:** C

**Giải thích gốc:**

Unit Test tương ứng giai đoạn Coding.

#### C1-1.3-trac_nghiem-08 · Câu gốc 8

Security Testing là một nhánh của loại kiểm thử nào?

**A.** Functional Testing

**B.** Non-functional Testing

**C.** Chỉ là một công cụ riêng biệt không thuộc phân loại nào

**D.** Unit Testing

**Đáp án gốc:** B

**Giải thích gốc:**

Security Testing thuộc Non-functional Testing.

### Lý thuyết (15 câu)

#### C1-1.3-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa Testing theo ISTQB và các hoạt động bao gồm trong đó.

**Trả lời gợi ý gốc:**

Testing theo ISTQB: tập hợp hoạt động phát hiện lỗi và đánh giá chất lượng, gồm lập kế hoạch, thiết kế, thực thi, VÀ cả hoạt động tĩnh (review) không cần chạy chương trình.

#### C1-1.3-ly_thuyet-02 · Câu gốc 2

Liệt kê và giải thích ngắn gọn 7 nguyên tắc kiểm thử theo ISTQB.

**Trả lời gợi ý gốc:**

````text
```
nguyên tắc: (1) Testing cho thấy có lỗi chứ không chứng minh hết lỗi, (2)
```

exhaustive testing bất khả thi, (3) early testing, (4) defect clustering, (5) pesticide paradox, (6) context dependent, (7) absence-of-errors fallacy.
````

#### C1-1.3-ly_thuyet-03 · Câu gốc 3

Giải thích nguyên tắc ”Testing shows presence of defects, not their absence” bằng ví dụ cụ thể.

**Trả lời gợi ý gốc:**

VD: dù chạy 1000 test case pass, chương trình vẫn có thể có lỗi ở test case thứ 1001 chưa thử – testing không chứng minh ”không có lỗi” một cách tuyệt đối.

#### C1-1.3-ly_thuyet-04 · Câu gốc 4

Bàn luận: vì sao ”exhaustive testing bất khả thi” là động lực cho các kỹ thuật phân tích tĩnh và formal verification.

**Trả lời gợi ý gốc:**

Vì không thể thử mọi input, cần công cụ CHỨNG MINH toán học (static analysis, formal verification) để đảm bảo tính đúng đắn vượt ra ngoài các case đã test.

#### C1-1.3-ly_thuyet-05 · Câu gốc 5

Trình bày mô hình V-Model và giải thích mối quan hệ giữa các mức kiểm thử và các giai đoạn phát triển.

**Trả lời gợi ý gốc:**

V-Model: Yêu cầu↔Acceptance Test, Thiết kế kiến trúc↔System Test, Thiết kế chi tiết↔Integration Test, Coding↔Unit Test.

#### C1-1.3-ly_thuyet-06 · Câu gốc 6

Giải thích sự khác biệt giữa Functional Testing và Non-functional Testing, cho ví dụ minh họa Security Testing.

**Trả lời gợi ý gốc:**

Functional kiểm tra ĐÚNG chức năng theo đặc tả; Non-functional kiểm tra thuộc tính chất lượng (hiệu năng, bảo mật); Security Testing là nhánh Non-functional tập trung tìm lỗ hổng.

#### C1-1.3-ly_thuyet-07 · Câu gốc 7

Phân biệt Static Testing và Dynamic Testing, chỉ ra ưu/nhược điểm của mỗi loại.

**Trả lời gợi ý gốc:**

Static: không chạy chương trình (code review, static analysis) – phát hiện sớm, rẻ; Dynamic: chạy chương trình với input cụ thể – phát hiện hành vi runtime thực tế. 14

#### C1-1.3-ly_thuyet-08 · Câu gốc 8

Trình bày định nghĩa Verification và Validation, giải thích bằng ví dụ cụ thể về chức năng ”xác thực OTP”.

**Trả lời gợi ý gốc:**

Verification: ”xây dựng đúng cách” (tuân thủ đặc tả kỹ thuật); Validation: ”xây dựng đúng sản phẩm” (đáp ứng nhu cầu người dùng). VD OTP: Verification kiểm tra code sinh OTP đúng thuật toán đã đặc tả; Validation kiểm tra người dùng có thực sự nhận và dùng được OTP thuận tiện không.

#### C1-1.3-ly_thuyet-09 · Câu gốc 9

Mô tả kỹ thuật Equivalence Partitioning và Boundary Value Analysis, cho ví dụ áp dụng cho trường ”tuổi” (0-150).

**Trả lời gợi ý gốc:**

Equivalence Partitioning: chia input thành lớp tương đương (VD tuổi: âm/hợp lệ/quá lớn); Boundary Value: test tại biên (0, 150, -1, 151).

#### C1-1.3-ly_thuyet-10 · Câu gốc 10

Giải thích tại sao lớp ”input không hợp lệ” trong Equivalence Partitioning có liên hệ trực tiếp với input validation (CWE-20).

**Trả lời gợi ý gốc:**

Lớp ”không hợp lệ” trong Equivalence Partitioning chính là nơi input validation (CWE-20) phải chặn được – thiếu xử lý lớp này là nguồn gốc lỗ hổng.

#### C1-1.3-ly_thuyet-11 · Câu gốc 11

Trình bày các loại white-box coverage (statement, branch, path) và giải thích mối quan hệ giữa chúng.

**Trả lời gợi ý gốc:**

Statement⊂Branch⊂Path về độ chặt: Statement chỉ cần chạm dòng lệnh; Branch cần cả hai nhánh; Path cần mọi tổ hợp đường đi (thường không khả thi đo đủ).

#### C1-1.3-ly_thuyet-12 · Câu gốc 12

Bàn luận: tại sao Path Coverage đầy đủ thường bất khả thi với chương trình có vòng lặp?

**Trả lời gợi ý gốc:**

Vì vòng lặp tạo số lượng path tăng theo cấp số nhân/vô hạn (mỗi lần lặp thêm là một path riêng) – không thể liệt kê hết trong thời gian hữu hạn.

#### C1-1.3-ly_thuyet-13 · Câu gốc 13

Mô tả Defect Lifecycle và giải thích ý nghĩa của từng trạng thái (New, Assigned, Fixed, Retest, Closed, Reopened).

**Trả lời gợi ý gốc:**

Defect Lifecycle: New (mới phát hiện) → Assigned (giao xử lý) → Fixed (đã sửa) → Retest (kiểm tra lại) → Closed (đóng) hoặc Reopened (mở lại nếu retest fail).

#### C1-1.3-ly_thuyet-14 · Câu gốc 14

Trình bày quy trình kiểm thử cơ bản theo ISTQB (Fundamental Test Process) với 6 giai đoạn.

**Trả lời gợi ý gốc:**

Fundamental Test Process: Test Planning → Analysis&Design → Implementation → Execution → Evaluating&Reporting → Test Closure.

#### C1-1.3-ly_thuyet-15 · Câu gốc 15

Giải thích khái niệm Decision Table Testing và khi nào nên áp dụng kỹ thuật này.

**Trả lời gợi ý gốc:**

Decision Table phù hợp khi có NHIỀU điều kiện kết hợp ảnh hưởng tới kết quả (VD: nhiều rule nghiệp vụ đan xen) – giúp đảm bảo phủ hết tổ hợp logic.

### Thực hành (15 câu)

#### C1-1.3-thuc_hanh-01 · Câu gốc 1

Thiết kế test case theo Boundary Value Analysis cho trường ”điểm số” (thang 0–10).

**Trả lời gợi ý gốc:**

Test case: -1 (invalid), 0 (biên hợp lệ), 10 (biên hợp lệ), 11 (invalid).

#### C1-1.3-thuc_hanh-02 · Câu gốc 2

````text
Với hàm sau, viết test case đạt path coverage đầy đủ:

```
int check_access (int age , int has_permission ) {
if (age >= 18) {
if ( has_permission ) return 1;
}
return 0;
}
```
````

**Trả lời gợi ý gốc:**

````text
```
test case: (17,0), (18,0), (18,1) – phủ mọi nhánh của 2 điều kiện lồng nhau.
```
````

#### C1-1.3-thuc_hanh-03 · Câu gốc 3

Viết 4 test case theo Equivalence Partitioning cho trường ”email” (hợp lệ, thiếu @, thiếu domain, rỗng).

**Trả lời gợi ý gốc:**

````text
```
case: ”a@b.com” (hợp lệ), ”ab.com” (thiếu @), ”a@” (thiếu domain), ”” (rỗng).
```
````

#### C1-1.3-thuc_hanh-04 · Câu gốc 4

````text
Xây dựng Decision Table đầy đủ cho chức năng ”áp dụng giảm giá” với

```
điều kiện: là thành viên VIP, đơn hàng trên 500k.
```
````

**Trả lời gợi ý gốc:**

Decision Table 4 rule: (VIP,>500k)=giảm nhiều nhất; (VIP,≤500k)=giảm vừa; (thường,>500k)= ít; (thường,≤500k)=không giảm.

#### C1-1.3-thuc_hanh-05 · Câu gốc 5

Viết một bộ 3 test case đạt Branch Coverage 100% cho hàm classify(x) với if x<0 ... elif x==0 ... else ....

**Trả lời gợi ý gốc:**

Test: x = −5 (elif nhánh âm... thực ra if x<0), x = 0, x = 5 (else) – 3 case phủ 3 nhánh.

#### C1-1.3-thuc_hanh-06 · Câu gốc 6

Thiết kế một Defect Report mẫu (theo lifecycle) cho lỗi ”nút Submit không phản hồi khi click nhanh liên tiếp”.

**Trả lời gợi ý gốc:**

Defect Report: Title, Steps to reproduce (click nhanh 5 lần), Expected (chỉ 1 request), Actual (nhiều request), Severity, trạng thái New.

#### C1-1.3-thuc_hanh-07 · Câu gốc 7

Viết test case Verification (kiểm tra đúng đặc tả) và Validation (kiểm tra đúng nhu cầu) khác nhau cho chức năng ”đặt lại mật khẩu”.

**Trả lời gợi ý gốc:**

Verification: kiểm tra token reset đúng định dạng/thời hạn theo đặc tả; Validation: khảo sát người dùng có dễ dàng thực hiện reset không.

#### C1-1.3-thuc_hanh-08 · Câu gốc 8

Cho một hàm Python tính giai thừa, viết test case bao gồm Boundary Value (0, 1, số âm, số lớn).

**Trả lời gợi ý gốc:**

Test case: n = 0 (biên, kết quả 1), n = 1, n = −1 (invalid), n = 20 (số lớn, kiểm tra overflow).

#### C1-1.3-thuc_hanh-09 · Câu gốc 9

Thiết kế 5 test case Security Testing (không phải Functional) cho chức năng đăng nhập. 17

**Trả lời gợi ý gốc:**

````text
```
test: SQL injection payload, XSS trong username, brute-force nhiều lần sai,
```

session fixation, timing attack đo phản hồi.
````

#### C1-1.3-thuc_hanh-10 · Câu gốc 10

Viết một bảng Equivalence Partitioning cho trường ”số điện thoại Việt Nam” (10 số, bắt đầu bằng 0).

**Trả lời gợi ý gốc:**

Bảng: ”0123456789”(hợp lệ), ”123456789”(thiếu số đầu, 9 số), ”01234567890”(11 số), ”abc1234567”(chứa chữ).

#### C1-1.3-thuc_hanh-11 · Câu gốc 11

Tính toán số lượng test case tối thiểu cần thiết để đạt Branch Coverage cho một hàm có 3 điều kiện if độc lập.

**Trả lời gợi ý gốc:**

Với 3 điều kiện if độc lập: tối thiểu 4 test case (dùng kỹ thuật MC/DC hoặc đơn giản mỗi điều kiện đúng/sai ít nhất 1 lần).

#### C1-1.3-thuc_hanh-12 · Câu gốc 12

Viết Test Plan tóm tắt (mục tiêu, phạm vi, tiêu chí dừng) cho việc kiểm thử một API ”tìm kiếm sản phẩm”.

**Trả lời gợi ý gốc:**

Test Plan: Mục tiêu (đảm bảo tìm đúng sản phẩm), Phạm vi (API search only), Tiêu chí dừng (100% test case pass, 0 Critical bug).

#### C1-1.3-thuc_hanh-13 · Câu gốc 13

Cho hàm is_leap_year(year), thiết kế test case bao gồm các trường hợp biên đặc biệt (năm chia hết 100 nhưng không chia hết 400).

**Trả lời gợi ý gốc:**

Test: year=1900(chia hết 100 không chia hết 400, không nhuận), year=2000(chia hết 400, nhuận), year=2023(thường), year=2024(chia hết 4).

#### C1-1.3-thuc_hanh-14 · Câu gốc 14

Viết đoạn code Python đơn giản đo Statement Coverage thủ công (đếm dòng đã ”chạm” qua) cho một hàm nhỏ.

**Trả lời gợi ý gốc:**

covered = set(); def track(line): covered.add(line) – gọi track() tại mỗi điểm cần đo.

#### C1-1.3-thuc_hanh-15 · Câu gốc 15

Thiết kế 3 test case Regression cho một chức năng đã sửa lỗi ”tính tổng giỏ hàng sai khi có mã giảm giá”.

**Trả lời gợi ý gốc:**

````text
```
test: giỏ hàng với mã giảm giá hợp lệ, mã giảm giá hết hạn, nhiều mã giảm giá
```

cùng lúc.
````

### Tình huống thực tế (15 câu)

#### C1-1.3-thuc_te-01 · Câu gốc 1

Một công ty phát hành phần mềm với Coverage 95% nhưng vẫn gặp lỗi nghiêm trọng ngay tuần đầu ra mắt. Phân tích nguyên nhân có thể.

**Trả lời gợi ý gốc:**

Coverage cao không đảm bảo hết lỗi logic/tích hợp; có thể do thiếu test case cho tình huống thực tế cụ thể (VD: dữ liệu người dùng thật khác dữ liệu test).

#### C1-1.3-thuc_te-02 · Câu gốc 2

Một đội QA chỉ test ”happy path” trước deadline gấp. Phân tích rủi ro và đề xuất chiến lược kiểm thử tối thiểu cần có.

**Trả lời gợi ý gốc:**

Rủi ro cao (bỏ sót edge case/security); tối thiểu cần: happy path + vài edge case quan trọng + 1 security test cơ bản.

#### C1-1.3-thuc_te-03 · Câu gốc 3

Một hệ thống ngân hàng yêu cầu Validation nghiêm ngặt hơn Verification. Giải thích lý do và đề xuất quy trình phù hợp.

**Trả lời gợi ý gốc:**

Validation cần nghiêm ngặt hơn vì hậu quả sai sót tài chính trực tiếp ảnh hưởng tiền bạc khách hàng, cần xác nhận đúng NHU CẦU không chỉ đúng đặc tả.

#### C1-1.3-thuc_te-04 · Câu gốc 4

Một dự án outsource giao nộp sản phẩm ”đã test” nhưng khách hàng phát hiện không đáp ứng nhu cầu thực tế. Phân tích đây là thất bại của Verification hay Validation.

**Trả lời gợi ý gốc:**

Thất bại của Validation – vì ”đã test” (verification pass theo đặc tả nội bộ) nhưng KHÔNG đáp ứng nhu cầu thực tế khách hàng.

#### C1-1.3-thuc_te-05 · Câu gốc 5

Một lỗi được đóng (Closed) nhưng xuất hiện lại sau 2 tháng trong bản release mới. Phân tích nguyên nhân liên quan Regression Testing.

**Trả lời gợi ý gốc:**

Do thiếu Regression Testing khi thay đổi mã nguồn liên quan, hoặc do fix không đúng root cause ban đầu.

#### C1-1.3-thuc_te-06 · Câu gốc 6

Một đội phát triển tin rằng ”code của chúng tôi không cần test vì đã rất đơn giản”. Phản biện quan điểm này bằng nguyên tắc ISTQB.

**Trả lời gợi ý gốc:**

Phản biện: nguyên tắc ”exhaustive testing impossible” và ”testing shows presence of defects” áp dụng bất kể độ đơn giản – code đơn giản vẫn có thể có edge case bị bỏ sót.

#### C1-1.3-thuc_te-07 · Câu gốc 7

Một tổ chức áp dụng test case CŨ suốt 3 năm không cập nhật. Phân tích hiện tượng ”Pesticide Paradox” trong tình huống này.

**Trả lời gợi ý gốc:**

Đây chính là Pesticide Paradox – test case cũ không còn phát hiện được lỗi mới phát sinh; cần làm mới/bổ sung test case định kỳ.

#### C1-1.3-thuc_te-08 · Câu gốc 8

Một startup phát hiện 80% lỗi nghiêm trọng đều nằm trong module thanh toán. Đề xuất chiến lược phân bổ nguồn lực QA dựa trên Defect Clustering.

**Trả lời gợi ý gốc:**

Chiến lược: tập trung 60-70% nguồn lực QA vào module thanh toán (theo Defect Clustering), phần còn lại phân bổ đều các module khác. 17

#### C1-1.3-thuc_te-09 · Câu gốc 9

Một hệ thống y tế yêu cầu chứng minh test coverage đầy đủ cho cơ quan quản lý. Đề xuất loại coverage phù hợp và giới hạn của nó.

**Trả lời gợi ý gốc:**

Đề xuất branch/statement coverage kèm giải thích rõ giới hạn (không đảm bảo hết lỗi phụ thuộc giá trị cụ thể, cần bổ sung Security Testing).

#### C1-1.3-thuc_te-10 · Câu gốc 10

Một công ty phát hiện lỗi bảo mật nghiêm trọng dù test suite có Branch Coverage 100%. Giải thích vì sao điều này có thể xảy ra.

**Trả lời gợi ý gốc:**

Có thể do lỗi phụ thuộc GIÁ TRỊ cụ thể của input (VD: chia cho 0, integer overflow) mà Branch Coverage không đo được – coverage chỉ đo đường đi, không đo giá trị.

#### C1-1.3-thuc_te-11 · Câu gốc 11

Một sản phẩm bị khách hàng từ chối dù ”tuân thủ đúng 100% đặc tả kỹ thuật”. Phân tích khoảng cách giữa Verification và Validation trong trường hợp này.

**Trả lời gợi ý gốc:**

Khoảng cách giữa Verification (đúng đặc tả) và Validation (đúng nhu cầu) – đặc tả có thể đã sai/lỗi thời so với nhu cầu thị trường thực tế.

#### C1-1.3-thuc_te-12 · Câu gốc 12

Một đội DevOps muốn tự động hóa Regression Testing cho mọi lần deploy. Đề xuất chiến lược chọn test case để tối ưu thời gian CI/CD.

**Trả lời gợi ý gốc:**

Chiến lược: ưu tiên test case có LỊCH SỬ phát hiện lỗi cao nhất, test case liên quan trực tiếp thay đổi code, giới hạn thời gian chạy CI bằng cách chọn lọc thông minh (risk-based selection).

#### C1-1.3-thuc_te-13 · Câu gốc 13

Một tổ chức phát hiện tester và developer thường xuyên tranh cãi về việc ”đây có phải là lỗi hay không”. Đề xuất quy trình Defect Lifecycle rõ ràng để giảm xung đột.

**Trả lời gợi ý gốc:**

Đề xuất: định nghĩa RÕ tiêu chí ”lỗi” (severity/priority matrix) và quy trình escalation khi có bất đồng giữa dev/tester.

#### C1-1.3-thuc_te-14 · Câu gốc 14

Một hệ thống thương mại điện tử bị lỗi tính sai giá chỉ khi khách hàng nhập số lượng âm. Phân tích thiếu sót trong Boundary Value Analysis.

**Trả lời gợi ý gốc:**

Thiếu sót trong Boundary Value Analysis – có thể chỉ test số dương, bỏ sót trường hợp số âm cho ”số lượng”.

#### C1-1.3-thuc_te-15 · Câu gốc 15

Một công ty game phát hành bản beta test với người dùng thật thay vì chỉ QA nội bộ. Bàn luận ưu/nhược điểm cách tiếp cận này so với testing truyền thống.

**Trả lời gợi ý gốc:**

Ưu: phát hiện lỗi thực tế đa dạng từ người dùng thật; Nhược: thiếu kiểm soát, khó tái tạo lỗi, trải nghiệm người dùng có thể bị ảnh hưởng xấu.

## Mục 1.4: Kiểm thử và kiểm chứng phần mềm II

### Trắc nghiệm (8 câu)

#### C1-1.4-trac_nghiem-01 · Câu gốc 1

Formal Verification khác Testing thông thường ở điểm cốt lõi nào?

**A.** Formal Verification chứng minh toán học thay vì chỉ thử một số trường hợp

**B.** Formal Verification luôn nhanh hơn Testing

**C.** Không có khác biệt thực sự

**D.** Formal Verification chỉ áp dụng cho phần cứng

**Đáp án gốc:** A

**Giải thích gốc:**

Formal Verification chứng minh toán học, không chỉ thử một số trường hợp.

#### C1-1.4-trac_nghiem-02 · Câu gốc 2

Hai hướng tiếp cận chính của Formal Verification là gì?

**A.** Unit Testing và Integration Testing

**B.** Model Checking và Theorem Proving

**C.** Black-box và White-box Testing

**D.** Static và Dynamic Testing

**Đáp án gốc:** B

**Giải thích gốc:**

Model Checking và Theorem Proving.

#### C1-1.4-trac_nghiem-03 · Câu gốc 3

Model Checking hoạt động theo nguyên lý nào?

**A.** Kiểm tra tự động, vét cạn không gian trạng thái

**B.** Chỉ thử một input ngẫu nhiên

**C.** Yêu cầu con người chứng minh từng bước

**D.** Không cần mô hình hệ thống

**Đáp án gốc:** A

**Giải thích gốc:**

Model Checking: kiểm tra tự động, vét cạn không gian trạng thái.

#### C1-1.4-trac_nghiem-04 · Câu gốc 4

Theorem Proving có ưu điểm gì so với Model Checking?

**A.** Luôn nhanh hơn

**B.** Xử lý được hệ thống vô hạn trạng thái

**C.** Không cần chuyên gia

**D.** Hoàn toàn tự động không cần con người

**Đáp án gốc:** B

**Giải thích gốc:**

Theorem Proving xử lý được hệ thống vô hạn trạng thái.

#### C1-1.4-trac_nghiem-05 · Câu gốc 5

Công cụ nào sau đây là Theorem Prover?

**A.** NuSMV

**B.** SPIN

**C.** Coq

**D.** CBMC

**Đáp án gốc:** C

**Giải thích gốc:**

Coq là Theorem Prover.

#### C1-1.4-trac_nghiem-06 · Câu gốc 6

”Sound” trong ngữ cảnh kỹ thuật QA có nghĩa là gì?

**A.** Không báo sai (không bỏ sót lỗi thật)

**B.** Tìm được mọi lỗi

**C.** Chạy nhanh

**D.** Không cần con người can thiệp

**Đáp án gốc:** A

**Giải thích gốc:**

Sound: không báo sai, không bỏ sót lỗi thật.

#### C1-1.4-trac_nghiem-07 · Câu gốc 7

”Complete” trong ngữ cảnh kỹ thuật QA có nghĩa là gì?

**A.** Tìm được mọi lỗi tồn tại (không có false positive che khuất)

**B.** Không bao giờ sai

**C.** Chỉ áp dụng cho phần cứng

**D.** Luôn chạy trong thời gian hữu hạn

**Đáp án gốc:** A

**Giải thích gốc:**

Complete: tìm được mọi lỗi tồn tại.

#### C1-1.4-trac_nghiem-08 · Câu gốc 8

Trong bảng so sánh kỹ thuật, Model Checking có đặc điểm nào về Sound và Complete?

**A.** Không sound, không complete

**B.** Sound và Complete (trong không gian trạng thái hữu hạn)

**C.** Chỉ complete, không sound

**D.** Chỉ sound, không complete

**Đáp án gốc:** B

**Giải thích gốc:**

Model Checking: Sound và Complete trong không gian hữu hạn.

### Lý thuyết (15 câu)

#### C1-1.4-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa Formal Verification và phân biệt với Testing thông thường.

**Trả lời gợi ý gốc:**

Formal Verification dùng phương pháp toán học CHỨNG MINH tính đúng đắn đối với đặc tả hình thức, khác Testing chỉ thử một số trường hợp cụ thể không đầy đủ.

#### C1-1.4-ly_thuyet-02 · Câu gốc 2

Mô tả hai hướng tiếp cận chính của Formal Verification: Model Checking và Theorem Proving.

**Trả lời gợi ý gốc:**

Model Checking: tự động, vét cạn không gian trạng thái (hữu hạn/rút gọn); Theorem Proving: xây dựng chứng minh toán học, có thể cần tương tác con người.

#### C1-1.4-ly_thuyet-03 · Câu gốc 3

Giải thích ý tưởng cốt lõi của Model Checking, liên hệ với Kripke Structure đã học ở Mục 1.5.

**Trả lời gợi ý gốc:**

Model Checking hoạt động trên mô hình Kripke Structure K = (S, S0 , R, L), kiểm tra công thức CTL/LTL bằng cách duyệt/phân tích không gian trạng thái để xác nhận đúng hoặc tìm counterexample.

#### C1-1.4-ly_thuyet-04 · Câu gốc 4

Trình bày ưu và nhược điểm của Theorem Proving so với Model Checking.

**Trả lời gợi ý gốc:**

Ưu Theorem Proving: xử lý hệ vô hạn trạng thái; Nhược: cần chuyên gia, tốn công sức, khó tự động hóa hoàn toàn so với Model Checking.

#### C1-1.4-ly_thuyet-05 · Câu gốc 5

Giải thích khái niệm Sound và Complete, cho ví dụ minh họa mỗi khái niệm.

**Trả lời gợi ý gốc:**

Sound: không có false negative (khi nói an toàn là chắc chắn đúng). VD: một type checker sound không bao giờ chấp nhận chương trình có lỗi kiểu dữ liệu.

#### C1-1.4-ly_thuyet-06 · Câu gốc 6

Bàn luận: tại sao không có kỹ thuật QA nào vừa Sound, vừa Complete, vừa hoàn toàn tự động cho MỌI chương trình?

**Trả lời gợi ý gốc:**

Không thể vì theo hệ quả Định lý Rice, hầu hết thuộc tính ngữ nghĩa không tầm thường là undecidable – luôn phải đánh đổi ít nhất một trong ba tính chất.

#### C1-1.4-ly_thuyet-07 · Câu gốc 7

Trình bày bảng so sánh Testing, Fuzzing, Static Analysis, Model Checking, Theorem Proving theo các tiêu chí: automation, sound, complete, chi phí.

**Trả lời gợi ý gốc:**

Bảng: Testing(cao,không,không,thấp); Fuzzing(cao,không,không,thấp-TB); Static Analysis(TB,thường có,thường không,TB); Model Checking(TB-cao,có,có trong bound,TB- cao); Theorem Proving(thấp,có,có,rất cao).

#### C1-1.4-ly_thuyet-08 · Câu gốc 8

Giải thích Penetration Testing và vai trò của nó trong bức tranh tổng thể Security Testing.

**Trả lời gợi ý gốc:**

Penetration Testing mô phỏng tấn công THỰC TẾ trên hệ thống ĐANG CHẠY bởi chuyên gia (ethical hacker), bổ sung cho phân tích tĩnh bằng góc nhìn kẻ tấn công thực sự.

#### C1-1.4-ly_thuyet-09 · Câu gốc 9

Mô tả Red Team/Blue Team exercise và giá trị của diễn tập này đối với tổ chức.

**Trả lời gợi ý gốc:**

Red Team tấn công, Blue Team phòng thủ trong một kịch bản mô phỏng thực tế – giúp tổ chức đánh giá khả năng phát hiện/ứng phó sự cố thực sự, không chỉ lý thuyết.

#### C1-1.4-ly_thuyet-10 · Câu gốc 10

Trình bày Common Criteria (ISO 15408) và ý nghĩa của các mức EAL1– EAL7.

**Trả lời gợi ý gốc:**

Common Criteria (ISO 15408): 7 mức EAL1(thấp nhất)-EAL7(cao nhất), mức càng cao yêu cầu bằng chứng đảm bảo an toàn càng nghiêm ngặt, tới EAL6-7 cần formal verification.

#### C1-1.4-ly_thuyet-11 · Câu gốc 11

Giải thích tại sao DO-178C (hàng không) Level A yêu cầu formal methods chặt chẽ hơn phần mềm thông thường.

**Trả lời gợi ý gốc:**

DO-178C Level A (mức nghiêm trọng cao nhất) áp dụng cho phần mềm mà lỗi có thể gây tai nạn thảm khốc – yêu cầu formal methods để đạt độ tin cậy tối đa.

#### C1-1.4-ly_thuyet-12 · Câu gốc 12

Bàn luận về vai trò của ISO/IEC 27001 trong quản lý an toàn thông tin tổ chức.

**Trả lời gợi ý gốc:**

ISO/IEC 27001 cung cấp khung quản lý an toàn thông tin toàn diện (chính sách, quy trình, kiểm soát) cho tổ chức, không chỉ kỹ thuật mà cả quản trị.

#### C1-1.4-ly_thuyet-13 · Câu gốc 13

Trình bày các yếu tố cần cân nhắc khi lựa chọn kỹ thuật QA phù hợp cho một dự án cụ thể.

**Trả lời gợi ý gốc:**

Các yếu tố: mức độ tới hạn module, kích thước codebase, kỹ năng đội ngũ, deadline dự án – không có công thức cố định, cần đánh giá tổng hợp.

#### C1-1.4-ly_thuyet-14 · Câu gốc 14

Giải thích tại sao thành phần bảo mật lõi (crypto, authentication) thường được ưu tiên áp dụng Formal Verification.

**Trả lời gợi ý gốc:**

Vì lỗi trong thành phần bảo mật lõi (crypto, auth) có tác động LAN RỘNG (ảnh hưởng mọi chức năng phụ thuộc) và khó phát hiện bằng testing thông thường do tính chất toán học phức tạp.

#### C1-1.4-ly_thuyet-15 · Câu gốc 15

Mô tả Security Code Review và phân biệt với cả Static Analysis tự động lẫn Penetration Testing.

**Trả lời gợi ý gốc:**

````text
Security Code Review: con người rà soát mã nguồn tĩnh; Static Analysis: công cụ tự động; Penetration Testing: tấn công hệ thống chạy thực tế – ba góc nhìn bổ sung nhau. 20

```
MỤC 1.4 – KIỂM THỬ VÀ KIỂM CHỨNG PHẦN MỀM II
```
````

### Thực hành (15 câu)

#### C1-1.4-thuc_hanh-01 · Câu gốc 1

Viết một bảng so sánh (Markdown) 5 kỹ thuật QA đã học theo 4 tiêu chí: automation, sound, complete, chi phí.

**Trả lời gợi ý gốc:**

````text
Bảng: Testing(Auto:cao,Sound:không,Complete:không,Chi phí:thấp); tương tự cho

```
kỹ thuật còn lại theo lý thuyết đã học.
```
````

#### C1-1.4-thuc_hanh-02 · Câu gốc 2

Cho một thư viện mã hóa ngân hàng, đề xuất tổ hợp kỹ thuật QA cụ thể (liệt kê từng kỹ thuật và lý do).

**Trả lời gợi ý gốc:**

````text
Đề xuất: Unit test (functional) + Static Analysis Cppcheck (nhanh) + CBMC (module core mã hóa) + Penetration test (trước release). 21

```
MỤC 1.4 – KIỂM THỬ VÀ KIỂM CHỨNG PHẦN MỀM II
```
````

#### C1-1.4-thuc_hanh-03 · Câu gốc 3

Viết một checklist (5 mục) đánh giá xem một module có ”đủ tới hạn” để cần Formal Verification hay không.

**Trả lời gợi ý gốc:**

Checklist: (1) Ảnh hưởng tài chính/an toàn tính mạng?, (2) Lỗi khó phát hiện bằng testing?, (3) Yêu cầu compliance?, (4) Chi phí lỗi cao?, (5) Có chuyên gia formal method?

#### C1-1.4-thuc_hanh-04 · Câu gốc 4

Thiết kế một quy trình (flowchart) lựa chọn kỹ thuật QA dựa trên: mức độ tới hạn, deadline, kỹ năng đội ngũ.

**Trả lời gợi ý gốc:**

Flowchart: Module mới → [Tới hạn cao?] –Yes–> Formal Verification; –No–> [Deadline gấp?] –Yes–> Testing nhanh; –No–> Static Analysis.

#### C1-1.4-thuc_hanh-05 · Câu gốc 5

Với module xử lý input mạng phức tạp, đề xuất thứ tự áp dụng: Testing → Fuzzing → Static Analysis → Formal Verification.

**Trả lời gợi ý gốc:**

Thứ tự: Testing cơ bản (baseline) → Fuzzing (tìm crash) → Static Analysis (Cppcheck+CBMC) → Formal Verification (nếu cần chứng minh tuyệt đối).

#### C1-1.4-thuc_hanh-06 · Câu gốc 6

Viết một bảng ánh xạ Common Criteria EAL level → mức độ formal method cần áp dụng.

**Trả lời gợi ý gốc:**

Bảng: EAL1-2→Testing cơ bản; EAL3-4→Static Analysis; EAL5-6→Model Checking; EAL7→Theorem Proving đầy đủ.

#### C1-1.4-thuc_hanh-07 · Câu gốc 7

Cho một tình huống dự án hàng không (DO-178C Level A), liệt kê các hoạt động QA cụ thể cần thực hiện.

**Trả lời gợi ý gốc:**

Hoạt động: formal spec mọi yêu cầu, code review 100%, static analysis bắt buộc, model checking module điều khiển, test coverage 100% MC/DC.

#### C1-1.4-thuc_hanh-08 · Câu gốc 8

Thiết kế một bảng phân loại 10 module giả định của một hệ thống theo mức độ tới hạn (Low/Medium/High/Critical).

**Trả lời gợi ý gốc:**

Bảng 10 module: Auth(Critical), Logging(Low), Payment(Critical), UI(Low), Search(Medium)... phân loại theo impact.

#### C1-1.4-thuc_hanh-09 · Câu gốc 9

Viết kịch bản (scenario) đơn giản cho một buổi diễn tập Red Team/Blue Team trong một tổ chức nhỏ.

**Trả lời gợi ý gốc:**

Kịch bản: Red Team cố gắng truy cập hệ thống HR trong 3 ngày; Blue Team giám sát/phản ứng; debrief cuối cùng rút kinh nghiệm.

#### C1-1.4-thuc_hanh-10 · Câu gốc 10

Cho một danh sách 5 thành phần hệ thống, đề xuất kỹ thuật QA phù hợp nhất cho từng thành phần kèm lý do.

**Trả lời gợi ý gốc:**

VD: Auth module→Model Checking(tới hạn cao); Logging module→Testing thông thường(tới hạn thấp); Payment→Formal Verification+Pentest.

#### C1-1.4-thuc_hanh-11 · Câu gốc 11

````text
Viết một đoạn văn (200 từ) so sánh cách tiếp cận ”kiểm thử truyền thống” và ”kiểm chứng hình thức” cho một hàm xử lý thanh toán. 23

```
MỤC 1.4 – KIỂM THỬ VÀ KIỂM CHỨNG PHẦN MỀM II
```
````

**Trả lời gợi ý gốc:**

Đoạn văn: kiểm thử truyền thống thử một số trường hợp cụ thể (nhanh, không đảm bảo đầy đủ); kiểm chứng hình thức chứng minh cho MỌI trường hợp có thể trong mô hình (chậm hơn, đảm bảo cao hơn) – với hàm thanh toán, formal verification đáng giá do rủi ro tài chính cao.

#### C1-1.4-thuc_hanh-12 · Câu gốc 12

Thiết kế bảng phân bổ ngân sách QA (giả định 100 triệu VNĐ) cho 4 kỹ thuật khác nhau dựa trên mức độ ưu tiên.

**Trả lời gợi ý gốc:**

Ngân sách: Testing(20tr), Static Analysis(30tr), Model Checking module core(40tr), Pentest(10tr) = 100tr, ưu tiên theo mức tới hạn.

#### C1-1.4-thuc_hanh-13 · Câu gốc 13

Cho một startup fintech mới thành lập, đề xuất lộ trình áp dụng dần các kỹ thuật QA theo thời gian (6 tháng, 1 năm, 2 năm).

**Trả lời gợi ý gốc:**

Lộ trình: Tháng 1-6 chỉ Testing; Năm 1 thêm Static Analysis (Cppcheck/SonarQube); Năm 2 thêm Model Checking cho module lõi khi đã ổn định.

#### C1-1.4-thuc_hanh-14 · Câu gốc 14

Viết một bảng liệt kê 3 công cụ Model Checking và 3 công cụ Theorem Proving phổ biến, kèm ngôn ngữ/nền tảng hỗ trợ.

**Trả lời gợi ý gốc:**

Bảng: NuSMV(symbolic,C-like input), SPIN(Promela,concurrent system); Coq(Gallina,general), Isabelle/HOL(ML-like,mathematics), Lean(dependent types,math+software).

#### C1-1.4-thuc_hanh-15 · Câu gốc 15

Thiết kế một ma trận quyết định (decision matrix) với trọng số cho việc chọn giữa Testing, Static Analysis, Formal Verification.

**Trả lời gợi ý gốc:**

Ma trận: tiêu chí(tới hạn,chi phí,thời gian) x trọng số x điểm mỗi kỹ thuật, tổng điểm cao nhất là lựa chọn.

### Tình huống thực tế (15 câu)

#### C1-1.4-thuc_te-01 · Câu gốc 1

````text
Một hãng hàng không phát hiện phần mềm điều khiển động cơ chỉ qua Unit Test, chưa qua formal verification. Phân tích rủi ro và đề xuất theo DO-178C. 24

```
MỤC 1.4 – KIỂM THỬ VÀ KIỂM CHỨNG PHẦN MỀM II
```
````

**Trả lời gợi ý gốc:**

Rủi ro nghiêm trọng (an toàn tính mạng); DO-178C Level A yêu cầu formal verification bắt buộc, không thể chỉ dựa Unit Test.

#### C1-1.4-thuc_te-02 · Câu gốc 2

Một ngân hàng quyết định KHÔNG đầu tư Formal Verification cho module core vì ”quá tốn kém”. Phân tích rủi ro dài hạn của quyết định này.

**Trả lời gợi ý gốc:**

Rủi ro dài hạn: lỗ hổng logic tinh vi có thể tồn tại nhiều năm không phát hiện, dẫn tới thiệt hại tài chính lớn hơn nhiều chi phí formal verification ban đầu.

#### C1-1.4-thuc_te-03 · Câu gốc 3

Một công ty đạt chứng chỉ Common Criteria EAL4 nhưng vẫn bị tấn công qua lỗ hổng logic. Phân tích giới hạn của chứng chỉ này.

**Trả lời gợi ý gốc:**

Chứng chỉ chỉ đảm bảo mức kiểm chứng NHẤT ĐỊNH tại thời điểm đánh giá, không đảm bảo an toàn TUYỆT ĐỐI, đặc biệt với lỗi logic ngoài phạm vi threat model đã xét.

#### C1-1.4-thuc_te-04 · Câu gốc 4

Một tổ chức tài chính thuê Red Team bên ngoài, phát hiện lỗ hổng nghiêm trọng chưa từng biết. Bàn luận giá trị của diễn tập Red Team so với chỉ dựa vào audit nội bộ.

**Trả lời gợi ý gốc:**

Red Team bên ngoài mang góc nhìn ”kẻ tấn công thực sự” không bị giới hạn bởi giả định nội bộ – audit nội bộ dễ bỏ sót vì ”quen thuộc” với hệ thống.

#### C1-1.4-thuc_te-05 · Câu gốc 5

Một startup công nghệ y tế cần tuân thủ ISO 27001 để ký hợp đồng với bệnh viện lớn. Đề xuất lộ trình đạt chứng chỉ này.

**Trả lời gợi ý gốc:**

Lộ trình: đánh giá gap hiện tại → xây dựng policy/quy trình → triển khai kiểm soát kỹ thuật → audit thử → đăng ký chứng nhận chính thức.

#### C1-1.4-thuc_te-06 · Câu gốc 6

Một dự án chính phủ yêu cầu Theorem Proving cho module bỏ phiếu điện tử nhưng đội ngũ thiếu chuyên gia. Đề xuất giải pháp (đào tạo, thuê ngoài, hoặc thay đổi kỹ thuật).

**Trả lời gợi ý gốc:**

Giải pháp: đào tạo nội bộ 1 người chuyên sâu, hoặc thuê tư vấn ngắn hạn kết hợp, hoặc cân nhắc Model Checking (ít cần chuyên gia hơn Theorem Proving) nếu đủ đáp ứng yêu cầu.

#### C1-1.4-thuc_te-07 · Câu gốc 7

Một công ty ô tô tự lái phát hiện lỗi logic hiếm gặp chỉ xảy ra trong 1/10 triệu tình huống. Phân tích vì sao Testing thông thường khó phát hiện và đề xuất Model Checking.

**Trả lời gợi ý gốc:**

Testing khó phát hiện vì tần suất quá thấp (1/10 triệu); Model Checking vét cạn KHÔNG GIAN TRẠNG THÁI thay vì thử ngẫu nhiên, có khả năng phát hiện các trường hợp hiếm này.

#### C1-1.4-thuc_te-08 · Câu gốc 8

Một tổ chức bị kiểm toán phát hiện không có bất kỳ Security Code Review nào trong 2 năm. Phân tích rủi ro tích lũy và đề xuất khắc phục.

**Trả lời gợi ý gốc:**

Rủi ro tích lũy: lỗ hổng không phát hiện chồng chất theo thời gian; khắc phục: thiết lập lịch Security Code Review định kỳ (VD mỗi quý) bắt buộc.

#### C1-1.4-thuc_te-09 · Câu gốc 9

Một dự án quốc phòng yêu cầu EAL7 (mức cao nhất). Phân tích chi phí và thời gian ước tính so với dự án thương mại thông thường.

**Trả lời gợi ý gốc:**

````text
EAL7 đòi hỏi formal verification cho TOÀN BỘ thiết kế, thời gian có thể gấp 5-10 lần dự án thương mại thông thường (nhiều năm so với vài tháng). 23

```
MỤC 1.4 – KIỂM THỬ VÀ KIỂM CHỨNG PHẦN MỀM II
```
````

#### C1-1.4-thuc_te-10 · Câu gốc 10

Một công ty bảo hiểm bị khách hàng khởi kiện do lỗi tính toán sai trong hợp đồng tự động. Đề xuất kỹ thuật QA lẽ ra nên áp dụng để ngăn lỗi này.

**Trả lời gợi ý gốc:**

Kỹ thuật lẽ ra nên áp dụng: Model Checking hoặc Theorem Proving cho công thức tính phí (thuộc tính tới hạn tài chính), không chỉ testing thông thường.

#### C1-1.4-thuc_te-11 · Câu gốc 11

Một tổ chức y tế mua phần mềm từ nhà cung cấp không rõ quy trình QA. Đề xuất các câu hỏi cần đặt ra trước khi ký hợp đồng.

**Trả lời gợi ý gốc:**

Câu hỏi: Quy trình QA của nhà cung cấp là gì? Có chứng chỉ ISO 27001/Common Criteria không? Có SBOM không? Có lịch sử CVE và cách xử lý ra sao?

#### C1-1.4-thuc_te-12 · Câu gốc 12

Một dự án blockchain phát hiện lỗ hổng smart contract gây thiệt hại hàng triệu đô sau khi triển khai. Phân tích vì sao formal verification ngày càng quan trọng trong lĩnh vực này.

**Trả lời gợi ý gốc:**

Ngày càng quan trọng vì smart contract không thể ”vá” sau triển khai (immutable) và xử lý tài sản giá trị lớn – formal verification là cách duy nhất đảm bảo TRƯỚC khi không thể sửa.

#### C1-1.4-thuc_te-13 · Câu gốc 13

Một công ty phần mềm nha khoa nhỏ hỏi có cần Common Criteria không. Tư vấn dựa trên mức độ rủi ro thực tế của sản phẩm.

**Trả lời gợi ý gốc:**

Tư vấn: mức rủi ro thấp (dữ liệu không quá nhạy cảm), có thể không cần Common Criteria chính thức, nhưng nên áp dụng static analysis cơ bản.

#### C1-1.4-thuc_te-14 · Câu gốc 14

Một tổ chức phát hiện Red Team và Blue Team của họ không bao giờ thực sự ”đối đầu” (đã biết trước kịch bản). Phân tích vấn đề và đề xuất cải thiện tính thực tế.

**Trả lời gợi ý gốc:**

Vấn đề: kịch bản biết trước làm mất tính ”thực tế” của diễn tập; cải thiện: Red Team độc lập, Blue Team không biết trước thời điểm/phương thức tấn công.

#### C1-1.4-thuc_te-15 · Câu gốc 15

Một dự án hàng không vũ trụ yêu cầu chứng minh formal cho MỌI dòng code. Bàn luận tính khả thi và đề xuất ưu tiên theo mức độ tới hạn.

**Trả lời gợi ý gốc:**

Không khả thi 100%; đề xuất: ưu tiên formal verification cho module điều khiển bay/an toàn tính mạng trực tiếp, dùng testing/static analysis cho phần còn lại.

## Mục 1.5: Cấu trúc Kripke (Kripke Structure)

### Trắc nghiệm (9 câu)

#### C1-1.5-trac_nghiem-01 · Câu gốc 1

Một Kripke Structure được định nghĩa là bộ 4 thành phần nào?

**A.** (S, S0 , R, L)

**B.** (V, E, W, D)

**C.** (A, B, C, D)

**D.** (P, Q, R, S)

**Đáp án gốc:** A

**Giải thích gốc:**

K = (S, S0 , R, L).

#### C1-1.5-trac_nghiem-02 · Câu gốc 2

Trong Kripke Structure, S đại diện cho:

**A.** Tập hữu hạn các trạng thái

**B.** Tập trạng thái khởi tạo

**C.** Quan hệ chuyển tiếp

**D.** Hàm gán nhãn

**Đáp án gốc:** A

**Giải thích gốc:**

S: tập hữu hạn các trạng thái.

#### C1-1.5-trac_nghiem-03 · Câu gốc 3

S0 trong Kripke Structure là:

**A.** Tập con của S, đại diện trạng thái khởi tạo

**B.** Tập tất cả các cạnh

**C.** Hàm gán nhãn

**D.** Số lượng trạng thái

**Đáp án gốc:** A

**Giải thích gốc:**

S0 : tập con của S, trạng thái khởi tạo.

#### C1-1.5-trac_nghiem-04 · Câu gốc 4

Quan hệ chuyển tiếp R trong Kripke Structure phải thỏa mãn tính chất gì?

**A.** Đối xứng

**B.** Total (mọi trạng thái có ít nhất một trạng thái kế tiếp)

**C.** Bắc cầu

**D.** Phản xạ

**Đáp án gốc:** B

**Giải thích gốc:**

R phải total: mọi trạng thái có ít nhất một trạng thái kế tiếp.

#### C1-1.5-trac_nghiem-05 · Câu gốc 5

Nếu một trạng thái không có transition đi ra, ta nên xử lý thế nào để thỏa mãn tính ”total”?

**A.** Xóa trạng thái đó

**B.** Thêm self-loop

**C.** Bỏ qua yêu cầu total

**D.** Không cần xử lý gì

**Đáp án gốc:** B

**Giải thích gốc:**

Thêm self-loop để đảm bảo total.

#### C1-1.5-trac_nghiem-06 · Câu gốc 6

Hàm gán nhãn L trong Kripke Structure có kiểu dữ liệu nào?

**A.** L : S → 2AP

**B.** L : S → S

**C.** L : AP → S

**D.** L : R → S

**Đáp án gốc:** A

**Giải thích gốc:**

L : S → 2AP .

#### C1-1.5-trac_nghiem-07 · Câu gốc 7

AP trong định nghĩa Kripke Structure là viết tắt của:

**A.** Atomic Propositions (mệnh đề nguyên tử)

**B.** Algorithm Process

**C.** Abstract Pointer

**D.** Access Permission

**Đáp án gốc:** A

**Giải thích gốc:**

AP = Atomic Propositions.

#### C1-1.5-trac_nghiem-08 · Câu gốc 8

Một ”path” trong Kripke Structure là:

**A.** Một dãy hữu hạn các trạng thái

**B.** Một dãy vô hạn s0 , s1 , s2 , . . . thỏa quan hệ R

**C.** Chỉ một trạng thái duy nhất

**D.** Tập hợp tất cả các trạng thái

**Đáp án gốc:** B

**Giải thích gốc:**

Path: dãy vô hạn s0 , s1 , . . . thỏa R.

#### C1-1.5-trac_nghiem-09 · Câu gốc 9

”Trace” của một path là:

**A.** Dãy các tập nhãn L(s0 ), L(s1 ), . . . tương ứng

**B.** Số lượng trạng thái trong path

**C.** Thời gian thực thi

**D.** Tên của Kripke Structure

**Đáp án gốc:** A

**Giải thích gốc:**

Trace: dãy nhãn L(s0 ), L(s1 ), . . ..

### Lý thuyết (15 câu)

#### C1-1.5-ly_thuyet-01 · Câu gốc 1

Trình bày định nghĩa hình thức của Kripke Structure K = (S, S0 , R, L) và giải thích ý nghĩa từng thành phần.

**Trả lời gợi ý gốc:**

K = (S, S0 , R, L): S tập trạng thái, S0 ⊆ S trạng thái khởi tạo, R ⊆ S × S quan hệ chuyển tiếp (total), L : S → 2AP hàm gán nhãn.

#### C1-1.5-ly_thuyet-02 · Câu gốc 2

Giải thích tại sao quan hệ chuyển tiếp R trong Kripke Structure phải có tính chất ”total”.

**Trả lời gợi ý gốc:**

R phải total để đảm bảo MỌI path đều vô hạn (không bị ”kẹt”) – cần thiết cho định nghĩa toán học nhất quán của path trong model checking.

#### C1-1.5-ly_thuyet-03 · Câu gốc 3

Mô tả khái niệm path và trace, phân biệt hai khái niệm này.

**Trả lời gợi ý gốc:**

Path: dãy vô hạn trạng thái s0 , s1 , . . . theo R; Trace: dãy các NHÃN tương ứng L(s0 ), L(s1 ), . . . – trace là những gì quan sát được từ bên ngoài, path là chuỗi trạng thái nội tại.

#### C1-1.5-ly_thuyet-04 · Câu gốc 4

Trình bày công thức CTL AG(ϕ) và EF (ϕ), cho ví dụ minh họa mỗi công thức.

**Trả lời gợi ý gốc:**

AG(ϕ): trên MỌI path, ϕ đúng ở MỌI trạng thái (invariant, VD ”không bao giờ unsafe”). EF (ϕ): TỒN TẠI path mà ϕ đúng tại một điểm (reachability, VD ”có thể đạt admin”).

#### C1-1.5-ly_thuyet-05 · Câu gốc 5

Giải thích mối liên hệ giữa hàm check_invariant() trong kripke.py và công thức CTL AG(¬unsaf e).

**Trả lời gợi ý gốc:**

check_invariant(unsafe) dùng BFS tìm xem có trạng thái nào mang nhãn unsafe REACHABLE từ S0 hay không – nếu có, AG(¬unsaf e) SAI (counterexample); nếu không, AG(¬unsaf e) ĐÚNG.

#### C1-1.5-ly_thuyet-06 · Câu gốc 6

Giải thích mối liên hệ giữa hàm check_reachability() và công thức CTL EF (goal).

**Trả lời gợi ý gốc:**

check_reachability(goal) tìm tập TOÀN BỘ trạng thái reachable rồi lọc những trạng thái có nhãn goal – nếu tập khác rỗng, EF (goal) ĐÚNG.

#### C1-1.5-ly_thuyet-07 · Câu gốc 7

Mô tả thuật toán BFS được dùng trong check_invariant() để tìm counterexample.

**Trả lời gợi ý gốc:**

BFS duyệt theo tầng từ S0 , lưu parent để tái tạo đường đi ngắn nhất tới trạng thái vi phạm khi tìm thấy, làm counterexample dễ hiểu nhất.

#### C1-1.5-ly_thuyet-08 · Câu gốc 8

Trình bày vấn đề State Explosion và giải thích tại sao nó là thách thức cốt lõi của Model Checking.

**Trả lời gợi ý gốc:**

State Explosion: không gian trạng thái tăng theo HÀM MŨ với số biến độc lập (2n ), khiến việc liệt kê/lưu trữ tường minh trở nên bất khả thi với hệ thống thực tế lớn.

#### C1-1.5-ly_thuyet-09 · Câu gốc 9

Giải thích ba hướng giải quyết State Explosion: Bounded Model Checking, Symbolic Model Checking, SAT/SMT solving.

**Trả lời gợi ý gốc:**

BMC: giới hạn số bước unroll k để giảm kích thước bài toán; Symbolic MC: biểu diễn TẬP trạng thái bằng BDD thay vì liệt kê từng cái; SAT/SMT: quy bài toán về công thức logic cho solver giải.

#### C1-1.5-ly_thuyet-10 · Câu gốc 10

Bàn luận: vì sao Bounded Model Checking chỉ ”sound có điều kiện” (trong giới hạn bound đã chọn)?

**Trả lời gợi ý gốc:**

BMC chỉ ”sound trong bound k” vì nếu lỗi thực sự nằm ở bước thứ k + 1 trở đi, BMC sẽ KHÔNG phát hiện được – cần unwinding-assertions để biết bound đã đủ hay chưa (học ở Ch.3.5).

#### C1-1.5-ly_thuyet-11 · Câu gốc 11

Trình bày công cụ Model Checking thực tế: NuSMV, SPIN, CBMC, Z3 – mỗi công cụ phù hợp với loại bài toán nào.

**Trả lời gợi ý gốc:**

NuSMV/nuXmv: symbolic MC hệ hữu hạn trạng thái; SPIN: verify hệ concurrent (Promela); CBMC: BMC trực tiếp trên mã C; Z3: SMT solver nền tảng cho nhiều công cụ trên.

#### C1-1.5-ly_thuyet-12 · Câu gốc 12

Giải thích tại sao CBMC được coi là bước tiến so với NuSMV/SPIN trong việc kiểm chứng mã nguồn thực tế.

**Trả lời gợi ý gốc:**

CBMC không cần xây mô hình trừu tượng THỦ CÔNG – nó TỰ ĐỘNG sinh mô hình từ chính mã nguồn C, giảm sai sót do mô hình hóa tay và phản ánh chính xác hành vi thực tế.

#### C1-1.5-ly_thuyet-13 · Câu gốc 13

Mô tả ví dụ mô hình đăng nhập (login) trong bài giảng, chỉ ra lỗ hổng bypass xác thực bằng Kripke Structure.

**Trả lời gợi ý gốc:**

Mô hình login: s0(init) → s1(waiting) → s2(auth) → s3(admin_hop_le); đường tắt s1 → s4(admin_bypass) là lỗ hổng – AG(¬unsaf e_no_auth) SAI với counterexample s0 → s1 → s4.

#### C1-1.5-ly_thuyet-14 · Câu gốc 14

Trình bày ví dụ đèn giao thông như một Kripke Structure đơn giản, xác định đầy đủ S, S0 , R, L.

**Trả lời gợi ý gốc:**

Đèn giao thông: S = {, xanh, vng}, S0 = {}, R = {(, xanh), (xanh, vng), (vng, )}, L() = {stop},...

#### C1-1.5-ly_thuyet-15 · Câu gốc 15

Giải thích sự khác biệt giữa LTL và CTL về sức biểu đạt (expressiveness).

**Trả lời gợi ý gốc:**

LTL biểu diễn thuộc tính trên MỘT dãy thi hành tuyến tính; CTL phân nhánh trên CÂY các path có thể – hai loại có sức biểu đạt không so sánh được (mỗi loại biểu diễn được thuộc tính mà loại kia không biểu diễn tự nhiên). 26

### Thực hành (15 câu)

#### C1-1.5-thuc_hanh-01 · Câu gốc 1

Chạy python3 atpm/ch1_concepts/kripke.py và ghi lại kết quả check_invariant() cho mô hình đăng nhập mẫu.

**Trả lời gợi ý gốc:**

Kết quả: holds=False, counterexample = s0 → s1 → s4 (đường bypass xác thực). 27

#### C1-1.5-thuc_hanh-02 · Câu gốc 2

Sửa mô hình build_login_example(): loại bỏ đường tắt s1 → s4, chạy lại và xác nhận AG(¬unsaf e) đúng.

**Trả lời gợi ý gốc:**

Sau khi xóa add_transition("s1_cho_dang_nhap", "s4_admin_bypass"), chạy lại check_invariant trả về holds=True.

#### C1-1.5-thuc_hanh-03 · Câu gốc 3

Mở rộng mô hình đăng nhập: thêm trạng thái s5_khoa_tai_khoan sau 3 lần đăng nhập sai, kiểm tra EF (locked).

**Trả lời gợi ý gốc:**

Thêm k.add_state("s5_khoa", labels=["locked"]) và transition từ trạng thái sai 3 lần; check_reachability("locked") trả về True nếu có đường tới s5.

#### C1-1.5-thuc_hanh-04 · Câu gốc 4

Xuất mô hình bằng to_dot() và render bằng Graphviz (dot -Tpng model.dot -o model.png).

**Trả lời gợi ý gốc:**

Lệnh: model.to_dot() in ra DOT source; sau đó dot -Tpng model.dot -o model.png sinh ảnh trực quan.

#### C1-1.5-thuc_hanh-05 · Câu gốc 5

Viết một Kripke Structure mới bằng Python mô hình hóa đèn giao thông có thêm trạng thái ”nhấp nháy khẩn cấp”.

**Trả lời gợi ý gốc:**

Kripke: S = {, xanh, vng, nhp_nhy}, thêm transition từ mọi trạng thái tới nhấp_nháy khi có tín hiệu khẩn cấp.

#### C1-1.5-thuc_hanh-06 · Câu gốc 6

Viết test pytest xác nhận AG(¬bypass) đúng cho mô hình đã sửa (loại bỏ đường tắt).

**Trả lời gợi ý gốc:**

def test_no_bypass(): model = build_login_example_fixed(); result = model.check_invarian assert result["holds"] == True.

#### C1-1.5-thuc_hanh-07 · Câu gốc 7

Cài đặt hàm check_eventually(self, goal_label) kiểm tra công thức AF (goal) (khác với EF đã có).

**Trả lời gợi ý gốc:**

def check_eventually(self, goal): reachable = self.reachable_from(); return all(goal in self.labels_of(s) for s in leaf nodes) (cần xử lý thêm cho path vô hạn).

#### C1-1.5-thuc_hanh-08 · Câu gốc 8

Viết một Kripke Structure mô hình hóa hệ thống file access control (no_access → read_only → read_write) với 1 lỗ hổng privilege escalation.

**Trả lời gợi ý gốc:**

States: no_access→read_only→read_write(hợp lệ), thêm cạnh tắt no_access→read_write(lỗ hổng privilege escalation).

#### C1-1.5-thuc_hanh-09 · Câu gốc 9

Chạy check_reachability("admin") trên mô hình đăng nhập gốc, giải thích witness_states trả về.

**Trả lời gợi ý gốc:**

witness_states chứa cả s3_admin_hop_le và s4_admin_bypass – cho thấy ”admin” đạt được qua CẢ đường hợp lệ lẫn đường lỗ hổng.

#### C1-1.5-thuc_hanh-10 · Câu gốc 10

Viết hàm Python tính số lượng trạng thái reachable từ S0 bằng cách gọi reachable_from().

**Trả lời gợi ý gốc:**

def count_reachable(k): return len(k.reachable_from()).

#### C1-1.5-thuc_hanh-11 · Câu gốc 11

Thiết kế một Kripke Structure có ít nhất 2 lỗ hổng bypass khác nhau và viết test phát hiện cả hai bằng check_invariant.

**Trả lời gợi ý gốc:**

Model với 2 unsafe labels khác nhau (VD ”bypass_auth” và ”privilege_leak”), gọi check_invariant riêng cho từng label.

#### C1-1.5-thuc_hanh-12 · Câu gốc 12

Sửa to_dot() để thêm màu sắc khác nhau cho trạng thái ”unsafe” khi xuất ra Graphviz. 29

**Trả lời gợi ý gốc:**

Sửa to_dot(): fillcolor = "red" if "unsafe" in label else "white" thêm vào node attributes.

#### C1-1.5-thuc_hanh-13 · Câu gốc 13

Viết một kịch bản Python tạo ngẫu nhiên một Kripke Structure với 10 trạng thái và kiểm tra tính total.

**Trả lời gợi ý gốc:**

import random; states = [f"s{i}" for i in range(10)]; ... sinh transitions ngẫu nhiên rồi gọi validate_total().

#### C1-1.5-thuc_hanh-14 · Câu gốc 14

Cài đặt hàm count_unsafe_states(self, unsafe_label) đếm số trạng thái có nhãn unsafe trong mô hình.

**Trả lời gợi ý gốc:**

def count_unsafe_states(self, label): return sum(1 for s in self.states if label in self.labels_of(s)).

#### C1-1.5-thuc_hanh-15 · Câu gốc 15

Với ví dụ file access control, viết test pytest xác nhận AG(¬priv_esc) SAI (có bypass) trước khi sửa.

**Trả lời gợi ý gốc:**

result = model.check_invariant("priv_esc"); assert result["holds"] == False – xác nhận lỗ hổng tồn tại trước khi sửa.

### Tình huống thực tế (15 câu)

#### C1-1.5-thuc_te-01 · Câu gốc 1

Một hệ thống điều khiển thang máy cần đảm bảo ”không bao giờ cửa mở khi thang đang di chuyển”. Mô hình hóa bằng Kripke Structure và xác định thuộc tính CTL cần kiểm tra. 30

**Trả lời gợi ý gốc:**

Mô hình: states=moving,door_open,door_closed; unsafe label khi (moving ∧ door_open) đồng thời; kiểm tra AG(¬(moving ∧ door_open)).

#### C1-1.5-thuc_te-02 · Câu gốc 2

Một công ty fintech phát hiện lỗi logic trong quy trình xử lý giao dịch qua nhiều trạng thái (pending, processing, completed, failed). Đề xuất cách mô hình hóa bằng Kripke Structure để tìm lỗi.

**Trả lời gợi ý gốc:**

Mô hình hóa transaction states (pending,processing,completed,failed) bằng Kripke Structure, kiểm tra AG(¬(completed ∧ failed)) (không đồng thời hai trạng thái cuối mâu thuẫn).

#### C1-1.5-thuc_te-03 · Câu gốc 3

Một hệ thống kiểm soát ra vào tòa nhà bằng thẻ từ gặp sự cố cho phép vào dù thẻ đã bị vô hiệu hóa. Mô hình hóa tình huống này và xác định trạng thái ”unsafe”.

**Trả lời gợi ý gốc:**

Trạng thái unsafe: ”access_granted ∧ card_disabled”; mô hình hóa transition kiểm tra thẻ, tìm counterexample nếu có đường bỏ qua kiểm tra trạng thái thẻ.

#### C1-1.5-thuc_te-04 · Câu gốc 4

Một đội phát triển game online cần đảm bảo ”người chơi không bao giờ có điểm âm”. Đề xuất mô hình Kripke và thuộc tính CTL kiểm tra.

**Trả lời gợi ý gốc:**

Mô hình: score là biến trong label (VD score_negative); AG(¬score_negative) là thuộc tính cần kiểm tra qua mọi trạng thái game.

#### C1-1.5-thuc_te-05 · Câu gốc 5

Một hệ thống quản lý kho hàng phát hiện lỗi cho phép xuất kho khi số lượng tồn = 0. Mô hình hóa và xác định counterexample tương ứng.

**Trả lời gợi ý gốc:**

Mô hình states kho hàng (in_stock, out_of_stock); unsafe = ”export ∧ out_of_stock”; counterexample chỉ ra transition thiếu kiểm tra tồn kho.

#### C1-1.5-thuc_te-06 · Câu gốc 6

Một ngân hàng cần kiểm chứng ”tài khoản không bao giờ có số dư âm sau giao dịch”. Đề xuất cách mô hình hóa bằng Kripke Structure.

**Trả lời gợi ý gốc:**

Mô hình: balance là một phần label; kiểm tra AG(balance ≥ 0) qua toàn bộ transitions giao dịch (nạp, rút, chuyển khoản).

#### C1-1.5-thuc_te-07 · Câu gốc 7

Một hệ thống đèn giao thông thông minh (smart traffic light) cần đảm bảo không bao giờ 2 hướng cùng có đèn xanh. Mô hình hóa và kiểm tra bằng CTL.

**Trả lời gợi ý gốc:**

Mô hình 2 hướng đèn (A,B) với AP={A_green, B_green}; kiểm tra AG(¬(A_green ∧ B_green)).

#### C1-1.5-thuc_te-08 · Câu gốc 8

Một ứng dụng đặt phòng khách sạn phát hiện lỗi cho phép đặt trùng phòng trong cùng khung giờ. Đề xuất mô hình hóa trạng thái phòng và kiểm tra.

**Trả lời gợi ý gốc:**

Mô hình trạng thái phòng (available, booked) theo khung giờ; unsafe = 2 booking chồng chéo cùng phòng cùng giờ.

#### C1-1.5-thuc_te-09 · Câu gốc 9

Một hệ thống quản lý quyền truy cập tài liệu (document access) cần đảm bảo ”người dùng không có quyền không bao giờ đọc được tài liệu mật”. Mô hình hóa bằng Kripke Structure.

**Trả lời gợi ý gốc:**

AP gồm quyền của user và trạng thái tài liệu; kiểm tra AG(¬(no_permission ∧ document_read)).

#### C1-1.5-thuc_te-10 · Câu gốc 10

Một dây chuyền sản xuất tự động cần đảm bảo ”robot không bao giờ hoạt động khi cửa an toàn đang mở”. Đề xuất mô hình và thuộc tính an toàn (safety-critical).

**Trả lời gợi ý gốc:**

Safety-critical: AG(¬(robot_active ∧ door_open)) – đây là thuộc tính an toàn TÍNH MẠNG, cần verify nghiêm ngặt (formal, không chỉ testing).

#### C1-1.5-thuc_te-11 · Câu gốc 11

Một hệ thống bỏ phiếu điện tử cần chứng minh ”một người chỉ bỏ phiếu được đúng một lần”. Mô hình hóa bằng Kripke Structure và xác định AP cần thiết.

**Trả lời gợi ý gốc:**

AP: đã bỏ phiếu (đã_vote); kiểm tra AG(so_lan_vote ≤ 1) cho mỗi cử tri qua toàn bộ transitions hệ thống.

#### C1-1.5-thuc_te-12 · Câu gốc 12

Một công ty logistics phát hiện lỗi cho phép đơn hàng chuyển trạng thái ”delivered” mà chưa từng ”shipped”. Mô hình hóa và tìm counterexample.

**Trả lời gợi ý gốc:**

Mô hình order status; unsafe = ”delivered ∧¬shipped_before”; cần theo dõi THỨ TỰ trạng thái đã qua (có thể cần mở rộng AP lưu lịch sử).

#### C1-1.5-thuc_te-13 · Câu gốc 13

Một hệ thống điều khiển lò phản ứng (giả định, mô phỏng) cần đảm bảo ”nhiệt độ không bao giờ vượt ngưỡng khi van làm mát đóng”. Đề xuất mô hình hóa an toàn.

**Trả lời gợi ý gốc:**

An toàn tới hạn (safety-critical): AG(¬(nhiet_do_cao ∧ van_dong)) – cần formal verification nghiêm ngặt tương tự ngành hạt nhân thực tế. 29

#### C1-1.5-thuc_te-14 · Câu gốc 14

Một ứng dụng chia sẻ file cần đảm bảo ”file đã xóa không bao giờ truy cập lại được” (liên hệ Use-After-Free ở Ch.2). Mô hình hóa bằng Kripke Structure.

**Trả lời gợi ý gốc:**

Liên hệ UAF (Ch.2): trạng thái ”deleted” không nên có transition quay lại ”accessible”; AG(deleted ⇒ AG(¬accessible)) (thuộc tính lồng nhau, cần LTL/CTL* mở rộng).

#### C1-1.5-thuc_te-15 · Câu gốc 15

Một hệ thống quản lý phiên đăng nhập (session) cần đảm bảo ”phiên hết hạn không bao giờ được dùng lại”. Đề xuất mô hình hóa và kiểm tra.

**Trả lời gợi ý gốc:**

AP: session_expired, session_used; kiểm tra AG(¬(session_expired∧session_used)).
