# Chương 7. Hệ thống ôn tập, bài tập có lời giải và thuật ngữ

## 7.1 Các quan hệ phải hiểu, không chỉ học thuộc

| Khái niệm A | Khái niệm B | Quan hệ cần nắm |
| --- | --- | --- |
| Threat | Vulnerability | Mối đe dọa có thể khai thác điểm yếu; tồn tại điểm yếu chưa tự xác định mức rủi ro |
| Safety | Liveness | Cấm điều xấu xảy ra và đòi hỏi điều tốt cuối cùng xảy ra |
| Verification | Validation | Phù hợp đặc tả và phù hợp nhu cầu sử dụng |
| Testing | Formal verification | Quan sát những lần chạy và suy luận trên mô hình/miền được mã hóa |
| Reachability | Invariant | Có đường tới trạng thái và mọi trạng thái reachable đều thỏa điều kiện |
| `EF p` | `AF p` | Có một đường tới p và mọi đường cuối cùng tới p |
| SAT | SMT | Boolean và Boolean kết hợp lý thuyết như số học/mảng/bit-vector |
| `Int` | `BitVec(n)` | Số nguyên không giới hạn và mẫu bit hữu hạn |
| Static analysis | Dynamic analysis | Suy từ mã/mô hình và quan sát khi chạy |
| Soundness | Precision | Không bỏ sót theo định nghĩa thuộc tính và mức ít cảnh báo giả |
| Line coverage | Branch coverage | Dòng đã chạy và lựa chọn điều khiển đã được đi qua |
| Branch coverage | Path coverage | Phủ từng nhánh không có nghĩa phủ mọi tổ hợp đường |
| Black-box | Grey-box | Mutation không dùng phản hồi nội bộ và mutation có phản hồi coverage |
| Grey-box | White-box | Coverage feedback và phân tích ràng buộc/semantics để giải input |
| Deadlock | Livelock | Không có chuyển tiếp và vẫn chuyển tiếp nhưng không tiến triển |
| Warning | Exploitable vulnerability | Tín hiệu cần phân tích và điểm yếu có đường khai thác dưới giả thiết cụ thể |

## 7.2 Công thức và điều kiện sử dụng

| Công thức | Cần nói kèm |
| --- | --- |
| `Risk ≈ Likelihood × Impact` | Mô hình định tính/bán định lượng, không tự là CVSS |
| `SLE = AssetValue × ExposureFactor` | Đơn vị tiền cho một sự kiện |
| `ALE = SLE × ARO` | Tần suất ARO theo năm |
| `Coverage = Covered / Total × 100%` | Định nghĩa mẫu số, loại coverage, file/hàm được đo |
| `V(G) = E - N + 2P` | CFG được xác định; P là số thành phần liên thông theo quy ước áp dụng |
| `M = (S, S₀, R, L)` | Trạng thái, trạng thái đầu, quan hệ chuyển tiếp và nhãn; nêu quy ước total |
| `AG p ≡ ¬EF ¬p` | Trên ngữ nghĩa CTL phù hợp |
| `A ≡ B ⇔ UNSAT(A XOR B)` | Cùng miền biến và giả thiết; kết quả `unknown` không đủ |
| `I(s₀) ∧ ∧T(sᵢ,sᵢ₊₁) ∧ ∨¬P(sᵢ)` | Công thức BMC tới k; nêu bound và giả thiết |
| `0 ≤ index < size` | Size không âm; tính index không tràn |
| `count ≤ SIZE_MAX / element_size` | Chỉ chia khi `element_size > 0`; phòng tràn kích thước cấp phát |
| `payload_length + 1 ≤ capacity` | Với chuỗi C cần NUL; kiểm tra tránh tràn phép cộng |
| `p = 256⁻ᵐ` | m byte độc lập, phân bố đều và cần khớp đúng vị trí |
| `P(ít nhất một lần) = 1-(1-p)ⁿ` | n lần thử độc lập; `np` chỉ xấp xỉ khi np nhỏ |

## 7.3 Bài 1: tính rủi ro định lượng

**Đề:** tài sản 500 triệu đồng; một sự cố gây mất 20% giá trị; trung bình hai sự cố mỗi năm. Giải pháp giá 80 triệu/năm giảm tần suất còn 0,2 lần/năm. Đánh giá lợi ích theo mô hình ALE.

**Giải:** SLE = 500 × 0,2 = 100 triệu. ALE trước = 100 × 2 = 200 triệu/năm. ALE sau = 100 × 0,2 = 20 triệu/năm. Tổn thất kỳ vọng giảm 180 triệu, lợi ích ròng sau chi phí = 100 triệu/năm. Đây là tính toán theo giả thiết đầu vào; chưa tính bất định, tác động uy tín hoặc phân bố tổn thất đuôi dài.

## 7.4 Bài 2: statement và branch coverage

Xét:

```c
int f(int a, int b) {
    int result = 0;
    if (a > 0) {
        result = a;
        if (b > 0)
            return result + b;
        return result;
    }
    return 0;
}
```

**Đề:** coi năm câu lệnh thực thi là hai phép gán và ba return; hai decision mỗi cái có hai nhánh. Tính coverage với `(5,3)` rồi bổ sung test.

**Giải:** `(5,3)` chạy `result=0`, `result=a`, `return result+b`, nên statement = 3/5 = 60%. Hai nhánh true được chạy, hai nhánh false chưa được chạy, nên branch = 2/4 = 50%. Thêm `(5,-3)` phủ return trong nhánh `b<=0`; thêm `(-5,0)` phủ nhánh `a<=0`. Bộ ba đạt 100% theo mẫu số này.

Nếu công cụ tính dòng, dòng chứa `if` và cách format code có thể đổi mẫu số. Không dùng con số statement ở bài tính tay như số line của gcov. Ba test cũng không phủ mọi giá trị số nguyên hoặc các vấn đề tràn `result+b`.

## 7.5 Bài 3: MC/DC với hai điều kiện

**Đề:** decision `D = A && B`; chọn test cho thấy từng điều kiện độc lập làm đổi D.

**Giải:** `(A,B) = (T,T), (F,T), (T,F)`. Cặp đầu và thứ hai giữ B=T, thay A làm D đổi T→F. Cặp đầu và thứ ba giữ A=T, thay B làm D đổi T→F. Short-circuit có thể khiến B không được đánh giá khi A=F; cần phân biệt giá trị logic của test và giá trị điều kiện thực sự được công cụ quan sát.

## 7.6 Bài 4: phản ví dụ safety trong Kripke

**Đề:** mô hình BUGGY lab 1 có `S0 → S1 → S5`; S5 có `unlocked` nhưng không có `authenticated`. Kiểm tra `AG(unlocked → authenticated)`.

**Giải:** mệnh đề kéo theo sai tại S5. S5 reachable nên invariant sai. Phản ví dụ ngắn gồm trạng thái `[S0,S1,S5]`, sự kiện `[insert_card,timeout_glitch]`. Sửa đường timeout để không đưa tới trạng thái mở cửa thiếu xác thực, rồi kiểm lại toàn mô hình.

Với `AG(tamper → alarm)`, nếu mô hình bỏ nhãn tamper khỏi mọi trạng thái reachable, thuộc tính có thể đúng vì tiền đề luôn sai. Cần kiểm tra sự kiện tamper thật được ánh xạ sang trạng thái/nhãn thế nào. Đây là **vacuous truth**, không phải bằng chứng hệ thống xử lý tamper đúng.

## 7.7 Bài 5: EF khác AF

**Đề:** máy bán hàng có `idle → selected`; từ selected có thể trả về idle hoặc đi đến paid rồi dispensing. Có self-loop/chu trình phù hợp để xét đường vô hạn. Kiểm tra EF và AF của dispensing.

**Giải:** EF đúng vì có đường `idle → selected → paid → dispensing`. AF sai vì đường `idle → selected → idle → selected → ...` không bao giờ đến dispensing. Muốn kết luận “người đã thanh toán sẽ nhận hàng”, thuộc tính và mô hình cần xét trạng thái paid, điều kiện không hỏng máy, scheduler và fairness tương ứng; thuộc tính AF từ idle là yêu cầu mạnh khác.

## 7.8 Bài 6: điểm bất động để tìm EF

**Đề:** các cạnh `s0→s1`, `s1→s2`, `s1→s3`, `s2→s2`, `s3→s3`; p chỉ đúng tại s2. Tìm tập trạng thái thỏa `EF p`.

**Giải:** bắt đầu Z₀={s2}. Thêm các tiền nhiệm có ít nhất một cạnh vào Z: Z₁={s1,s2}. Lặp lại Z₂={s0,s1,s2}. Lần sau không đổi, dừng. s3 không thuộc tập. Đây là least fixed point của `Z = Sat(p) ∪ PreE(Z)`; dùng reverse edges để tính hiệu quả. `AG !p` đúng tại s3 và sai tại s0,s1,s2.

## 7.9 Bài 7: chứng minh hai điều kiện tương đương

**Đề:** `!( !a || !b ) && !alarm` và `a && b && !alarm` có tương đương không?

**Giải:** De Morgan cho `!(!a || !b) = a && b`, nên bằng nhau trong logic Boolean. SMT thêm XOR của hai biểu thức: UNSAT xác nhận không có phép gán Boolean làm khác nhau. Với biểu thức C có lời gọi hàm, side effect hoặc giá trị không chuẩn Boolean, phải xét semantics đánh giá; không được đổi thứ tự tùy ý chỉ từ đẳng thức logic.

**Biến thể:** `attempts >= 3` và `attempts > 3` khác nhau tại attempts=3. Đây là input regression cần giữ lại.

## 7.10 Bài 8: SAT bằng unit propagation

**Đề:** F = `(a ∨ b) ∧ (¬a ∨ c) ∧ (¬c) ∧ (¬b)`.

**Giải:** unit `¬c` buộc c=F. Clause `(¬a∨c)` còn `¬a`, buộc a=F. Unit `¬b` buộc b=F. Clause `(a∨b)` trở thành empty clause, nên UNSAT. Đây là một lượt propagation đủ quyết định; không cần branch. Với CNF khác, DPLL có thể phải thử literal rồi backtrack. Các script brute force trong toolkit chỉ liệt kê phép gán, không tự thực hiện CDCL.

## 7.11 Bài 9: Int và bit-vector

**Đề:** x là unsigned 8-bit, x=255. Tính x+1 và so sánh với mô hình Int.

**Giải:** ở modulo 256, kết quả bit-vector là 0. Với Int, kết quả là 256. Nếu muốn kiểm tra overflow unsigned, xét tổng được mở rộng 9-bit >255 hoặc điều kiện thích hợp trước cộng. Trong Z3, `<` trên BitVec thường mang nghĩa signed; dùng `ULT/ULE/UGT/UGE` khi cần unsigned.

**Đề phụ:** signed 32-bit x=2.147.483.647, C tính `x+1`.

**Giải:** signed overflow là undefined behavior theo mô hình C chuẩn; không được kết luận luôn wrap thành -2.147.483.648. Mô hình bit-vector wrap là một mô hình máy cụ thể, không tự đúng với mọi tối ưu hóa C.

## 7.12 Bài 10: BMC và off-by-one

**Đề:** `int a[10]; for(i=0;i<=10;i++) a[i]=0;`. Bound k=10 có phát hiện truy cập index10 không?

**Giải:** phải xác định k đếm lần lặp, bước chuyển hay chỉ số. Engine lab 6 dùng `i=0..k-1`, nên k=10 chỉ xét i=0..9; k=11 mới xét i=10 và tìm vi phạm. Kết quả “safe” ở k=10 chỉ là safe trong phạm vi mô hình đó. Với CBMC, số unwind có semantics riêng; dùng unwinding assertions và kiểm tra vòng lặp đã được bao phủ thay vì áp dụng máy móc k=n hoặc n+1.

**Biến thể:** quét năm phần tử `a[base+i]`, i=0..4. Điều kiện đủ là `0≤base≤5`. Nếu cho base≤9, input base=9,i=1 truy cập10 gây lỗi.

## 7.13 Bài 11: vòng đời bộ nhớ và alias

```c
Node *p = malloc(sizeof *p);
if (p == NULL) return;
Node *q = p;
free(p);
p = NULL;
/* q vẫn giữ địa chỉ cũ. */
```

**Đề:** p=NULL có làm truy cập qua q an toàn không?

**Giải:** không. p và q là hai alias; free kết thúc lifetime object mà cả hai cùng chỉ tới. q trở thành dangling pointer; đọc q->field là UAF. Quản lý ownership và phạm vi alias mới xử lý được nguyên nhân. Tương tự `free(q)` sau free(p) có thể là double free.

## 7.14 Bài 12: buffer và NUL

**Đề:** `char dst[16]`; đầu vào tối đa16 byte; dùng `strcpy`. Lỗi ở đâu?

**Giải:** đầu vào16 byte cần byte17 để ghi NUL. Tăng capacity hoặc giảm payload còn15. Với `snprintf`, kiểm tra kết quả: giá trị âm báo lỗi; giá trị trả về ≥capacity báo truncation. Truncation có thể an toàn bộ nhớ nhưng vẫn sai nghiệp vụ, ví dụ hai ID khác nhau bị cắt thành cùng một chuỗi.

## 7.15 Bài 13: alignment và padding

**Đề:** trên ABI giả định char alignment1, int size/alignment4, double size/alignment8, tính layout `struct { char c; int x; double y; };`.

**Giải:** c ở offset0; padding3 byte; x ở offset4..7; y ở offset8..15; kích thước16, alignment8. Đổi thứ tự `char c; double y; int x;` cho offset0,8,16 và tail padding lên24 byte trên ABI này. Không suy ra mọi compiler/ABI đều giống; kiểm tra `sizeof`, `_Alignof`, `offsetof`. Không gửi raw struct qua mạng như một định dạng ổn định.

## 7.16 Bài 14: xác suất magic value

**Đề:** random đều cần khớp 5 byte độc lập. Với hai triệu lần, xác suất gần đúng có ít nhất một lần khớp?

**Giải:** p=256⁻⁵=2⁻⁴⁰≈9,094947×10⁻¹³. np≈1,818989×10⁻⁶, nên xác suất gần bằng giá trị đó, khoảng 0,000181899%. Kỳ vọng số lần tới thành công là 1/p≈1,0995 nghìn tỷ. Nếu từng byte đúng mở thêm coverage và seed cải thiện được giữ, quá trình có thể giải từng bước; lợi thế này cần cấu trúc phản hồi, không áp dụng cho mọi checksum/hash.

## 7.17 Bài 15: đánh giá thực nghiệm fuzzing

**Đề:** kết quả nguồn lab 8: black-box chạy 1000 lần không crash; coverage-guided chạy 500 lần có 3 crash, first crash tại 402. Có thể kết luận coverage-guided luôn tốt hơn đúng2 lần không?

**Giải:** không. Budget khác nhau; thuật toán mutation/dictionary cũng khác; ba crash có thể cùng root cause; randomness cần nhiều seed và phân bố thời gian. Kết luận hợp lệ là trong **lượt nguồn được lưu**, cấu hình coverage-guided tìm được crash còn cấu hình black-box không tìm được. Để so sánh, cố định target/harness/sanitizer, ngân sách thời gian hoặc số execution, seed và mutation tương đương rồi lặp nhiều lượt.

## 7.18 Bài 16: oracle cũng có thể sai

**Đề:** C và Python reference cùng viết nhầm giảm giá membership15% thành10%. Test so sánh hai kết quả đều pass. Đã chứng minh đặc tả đúng chưa?

**Giải:** chưa. Hai implementation cùng lỗi sẽ đồng ý. Cần test từ yêu cầu độc lập, ví dụ bảng quyết định business, trường hợp biên có đáp án tính tay, metamorphic relation hợp lệ. Oracle không nên chỉ là bản dịch gần như nguyên xi code cần test.

## 7.19 Bài 17: NaN và kiểm tra giá

**Đề:** code chỉ từ chối khi `price <= 0`. Nếu price là NaN thì sao?

**Giải:** so sánh ordered với NaN cho false, nên NaN có thể qua guard này. Phép tính total lan truyền NaN; điều kiện `total > limit` cũng false. Kiểm tra `isfinite(price)` và miền giá hợp lệ nếu đặc tả yêu cầu giá hữu hạn dương. CSV parser cũng cần xác nhận chuyển đổi thành công và hết chuỗi, không chỉ gọi hàm chuyển đổi bỏ qua lỗi.

## 7.20 Bài 18: giả thiết có thể loại mất lỗi

**Đề:** muốn chứng minh parser xử lý mọi length không tin cậy, nhưng harness có `assume(length < capacity)`. Kết quả safe nghĩa là gì?

**Giải:** chỉ nghĩa là parser safe cho input đã thỏa length<capacity trong mô hình. Harness đã loại miền quá dài, đúng miền có thể chứa lỗi. Nếu guard là trách nhiệm parser, phải đưa nó vào code thay vì giả thiết. Nếu guard là trách nhiệm caller, cần chứng minh caller thực sự đảm bảo điều kiện đó và nêu contract.

## 7.21 Tự kiểm tra theo từng chương

**Chương 1:** giải thích CIA/AAA và asset; viết threat model; phân biệt CWE/CVE; tạo partition/boundary; tính coverage; dựng Kripke; viết một safety và một liveness; tìm phản ví dụ và nhận diện vacuity.

**Chương 2:** vẽ lifetime object; phân biệt stack/heap overflow; sửa UAF/leak/double free; kiểm tra allocation failure; tính capacity chuỗi; kiểm tra signed/unsigned overflow; giải thích alignment/endianness; đọc sanitizer trace và giới hạn của công cụ.

**Chương 3:** mô tả over-approximation; đọc CFG/data-flow; giải CNF nhỏ; viết bài tương đương bằng XOR; chọn đúng Int/BitVec/Array; phân biệt sat/unsat/unknown; mã hóa BMC và giải thích bound; kiểm tra memory model và giả thiết.

**Chương 4:** thiết kế harness/oracle; phân biệt black/grey/white; mutation và generation; giải thích coverage feedback; lập path constraint; tìm input concolic; giảm crash, phân nhóm root cause và tạo regression; đánh giá thực nghiệm có cùng budget.

## 7.22 Gợi ý trình tự tự học

| Chặng | Nội dung | Sản phẩm tự kiểm tra |
| --- | --- | --- |
| 1 | Chương 1 + lab 1-2 | Threat model, Kripke, test decision/boundary |
| 2 | Chương 2 + lab 3-4 | Một bảng lifetime, bug→patch→regression |
| 3 | Chương 3 + lab 5-6 | SMT phản ví dụ và BMC có bound rõ |
| 4 | Chương 4 + lab 7-8 | Coverage và chiến dịch fuzzing có oracle |
| 5 | Chương 6 | Đặc tả có truy vết, báo cáo trước/sau |
| 6 | Chương 8 + ngân hàng câu hỏi | Giải thích vì sao đáp án đúng và nhận ra giả thiết thiếu |

Mỗi chặng có thể lặp lại bằng một ví dụ mới. Ưu tiên tự dựng một phản ví dụ nhỏ trước khi học thuật toán tổng quát; sau đó thay đổi giả thiết để thấy kết luận thay đổi.

## 7.23 Thuật ngữ Anh-Việt

| Thuật ngữ | Nghĩa trong tài liệu |
| --- | --- |
| Asset | Tài sản cần bảo vệ |
| Threat | Mối đe dọa |
| Vulnerability | Điểm yếu/lỗ hổng |
| Exploit | Cách hoặc mã khai thác |
| Attack surface | Bề mặt tấn công |
| Trust boundary | Ranh giới tin cậy |
| Confidentiality | Tính bí mật |
| Integrity | Tính toàn vẹn |
| Availability | Tính sẵn sàng |
| Authentication | Xác thực danh tính |
| Authorization | Phân quyền truy cập |
| Accounting / audit | Ghi nhận và kiểm toán hoạt động |
| Least privilege | Đặc quyền tối thiểu |
| Fail-safe default | Mặc định từ chối khi chưa được cho phép |
| Safety property | Thuộc tính cấm hành vi xấu |
| Liveness property | Thuộc tính đòi hỏi tiến triển |
| Invariant | Bất biến tại các trạng thái xét |
| Counterexample | Phản ví dụ |
| Witness | Chứng cứ/đường đi chứng minh tồn tại |
| Reachability | Khả năng đạt được trạng thái |
| Vacuous truth | Đúng do tiền đề không xảy ra |
| Fairness | Điều kiện công bằng của hành vi/scheduling |
| Deadlock | Bế tắc chờ đợi/không có chuyển tiếp theo mô hình |
| Livelock | Chuyển tiếp mà không tiến triển |
| Starvation | Một bên chờ mãi không được phục vụ |
| Memory safety | An toàn truy cập và lifetime bộ nhớ |
| Spatial safety | An toàn phạm vi địa chỉ |
| Temporal safety | An toàn vòng đời đối tượng |
| Dangling pointer | Con trỏ tới đối tượng hết lifetime |
| Ownership | Quyền/trách nhiệm quản lý tài nguyên |
| Alias | Hai tham chiếu có thể trỏ cùng đối tượng |
| Undefined behavior | Hành vi tiêu chuẩn không đặt yêu cầu |
| Alignment / padding | Căn chỉnh địa chỉ / byte đệm |
| Static / dynamic analysis | Phân tích tĩnh / động |
| Abstract interpretation | Diễn giải trừu tượng |
| Soundness | Tính đúng theo hướng đảm bảo đã định nghĩa |
| False positive / negative | Cảnh báo giả / bỏ sót lỗi |
| SAT / SMT | Thỏa mãn Boolean / thỏa mãn theo lý thuyết |
| Bit-vector | Vector bit hữu hạn |
| Bounded model checking | Kiểm chứng mô hình có giới hạn |
| Unwinding assertion | Kiểm tra giới hạn mở vòng đã đủ |
| Harness | Mã bao gọi target trong thử nghiệm |
| Oracle | Tiêu chí quyết định lần chạy đúng/sai |
| Seed / corpus | Input khởi đầu / tập input được giữ |
| Mutation / generation | Biến đổi input / sinh input theo quy tắc |
| Coverage-guided | Được định hướng bởi phản hồi coverage |
| Symbolic execution | Thực thi trên biểu thức ký hiệu |
| Concolic execution | Kết hợp chạy cụ thể và ràng buộc ký hiệu |
| Path constraint | Ràng buộc của đường thực thi |
| Crash triage | Phân loại, rút gọn và xác định nguyên nhân crash |
| Regression test | Test ngăn lỗi đã sửa tái phát |

## 7.24 Ngân hàng câu hỏi gốc

Xem [1.257 câu hỏi được tách theo chương](11_Ngan_hang_cau_hoi.md). Nội dung đáp án gốc được giữ để đối chiếu, không coi toàn bộ là kết luận đã thẩm định. Các điểm sai/thiếu điều kiện quan trọng được hệ thống hóa tại [Chương 8](08_Dinh_chinh_va_gioi_han.md). Lời giải các bài ở chương này được biên soạn theo phân tích code và ngữ nghĩa đã giải thích, không chép nguyên đáp án HTML.
