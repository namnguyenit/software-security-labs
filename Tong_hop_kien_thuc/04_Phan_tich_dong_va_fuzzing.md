# Chương 4. Phân tích động, coverage và fuzzing

## 4.1 Tư duy kiểm thử bảo mật

Functional testing thường hỏi “input hợp lệ có cho chức năng đúng không?”. Security testing còn hỏi “input hoặc thứ tự thao tác bất thường có phá thuộc tính bảo mật không?”. Cùng một hàm parser cần kiểm tra payload hợp lệ, payload cắt ngắn, trường length mâu thuẫn, byte đặc biệt, độ sâu lớn và lỗi tài nguyên.

Fuzzing tự động sinh hoặc biến đổi nhiều input rồi chạy target để tìm hành vi bất thường. Nó hiệu quả khi có target chạy đủ nhanh và oracle phát hiện vấn đề. Fuzzer không phải công cụ tự hiểu mọi logic nghiệp vụ.

| Oracle | Phát hiện được | Cần chú ý |
| --- | --- | --- |
| Crash/exception | Một số lỗi runtime | Exception dự kiến hoặc input bị từ chối chưa chắc là bug |
| Hang/timeout | Một số liveness/DoS | Có thể do môi trường chậm; cần ngưỡng và replay |
| ASan/UBSan | Một số lỗi bộ nhớ và UB | Chỉ trên đường thực thi và loại kiểm tra được hỗ trợ |
| Assertion/invariant | Vi phạm điều kiện nội bộ | Invariant phải đúng và chưa bị disable |
| Differential oracle | Hai implementation cho kết quả khác nhau | Cần đặc tả chung, chuẩn hóa kết quả |
| Metamorphic oracle | Vi phạm quan hệ giữa các lần chạy | Quan hệ phải có cơ sở |

Không crash không đồng nghĩa bảo mật. Một hàm trả dữ liệu của người khác có thể vi phạm authorization mà không crash; cần oracle về quyền hoặc dữ liệu.

## 4.2 Harness và chiến dịch fuzzing

Harness chuyển input fuzzer thành lời gọi target, thiết lập trạng thái, thu kết quả và dọn tài nguyên. Một harness tốt giới hạn kích thước khi cần, xử lý input ngắn, tránh phụ thuộc không cần thiết vào mạng/thời gian và reset trạng thái giữa các lần chạy.

Ví dụ hình thức harness libFuzzer:

```c
#include <stddef.h>
#include <stdint.h>

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    parse_packet(data, size);
    return 0;
}
```

`parse_packet` cần là API nhận buffer/size hợp lệ. Không biến `data` thành C string bằng strlen nếu chưa đảm bảo NUL. Đưa code chạy hàng triệu lần vào một tiến trình còn đòi dọn allocation và trạng thái toàn cục đúng.

Theo [tài liệu LLVM](https://llvm.org/docs/LibFuzzer.html), libFuzzer dùng coverage để hướng dẫn biến đổi corpus và gọi target trong tiến trình. Điều này khác fuzzer Python của lab gọi subprocess rồi chạy gcov cho từng input, vốn là minh họa chậm hơn.

Quy trình chiến dịch:

1. Chọn API/định dạng và threat model.
2. Viết harness; xác nhận seed hợp lệ vào được code mục tiêu.
3. Build với instrumentation và sanitizer cần thiết.
4. Chọn corpus, dictionary, mutation và resource budget.
5. Chạy, theo dõi coverage, exec/s, unique crashes, hang và tài nguyên.
6. Replay, deduplicate và minimize input gây lỗi.
7. Sửa nguyên nhân; giữ input thành regression test.

Ghi phiên bản, flags, corpus ban đầu, seed ngẫu nhiên, số lần thử, thời gian và giới hạn input. Nếu chỉ ghi “chạy 1.000 lần” mà target chạy không đúng/harness chặn input trước parser, kết quả ít giá trị.

## 4.3 Coverage và feedback

Fuzzer hướng coverage giữ input tạo ra thông tin thực thi mới:

```text
corpus = seeds
seen = coverage(seeds)
repeat theo budget:
    parent = chọn một seed
    candidate = mutate(parent)
    result, covered = chạy target(candidate)
    nếu có lỗi: lưu bằng chứng/input
    nếu covered có mục chưa thuộc seen:
        thêm candidate vào corpus
        seen = seen union covered
```

**Line/statement coverage** cho biết vùng code đã chạy; **edge coverage** phân biệt transition trong CFG; bitmap/hit count giúp lưu feedback gọn. Hash collision trong bitmap có thể làm mất phân biệt giữa các mục. Công cụ và instrumentation khác nhau cho độ đo khác nhau; không so phần trăm nếu mẫu số không cùng phạm vi.

Một corpus nhỏ bao phủ nhiều vùng quan trọng thường tốt hơn nhiều file trùng đường. **Corpus minimization** chọn tập input giữ coverage mong muốn; **crash minimization** rút gọn input mà vẫn gây cùng lỗi. Hai công việc có mục tiêu khác nhau.

Coverage plateau gợi ý cần xem seed, dictionary, parser depth, checksum, magic constant, hạn chế harness, instrumentation hoặc chiến lược. Plateau không chứng minh đã hết bug. Có thể target chặn input quá sớm hoặc coverage còn thiếu do error handling chưa được tiếp cận.

Gcov của Lab 2/7 chủ yếu đang đếm **dòng**, dù một helper có tên `compute_branch_coverage`. Muốn đo branch đúng cần thu branch records bằng tùy chọn phù hợp, phân biệt nhánh compiler-generated và phạm vi hàm. Line coverage cao không được viết thành branch coverage cao.

## 4.4 Theo dõi thực thi và taint

| Kỹ thuật | Dữ liệu thu được | Chi phí/giới hạn |
| --- | --- | --- |
| Logging/assertion | Event/invariant do người viết chọn | Có thể thiếu đường cần xem; log có ảnh hưởng thời gian |
| Instrumentation | Block, edge, comparison hoặc memory access | Chi phí phụ thuộc mức chi tiết |
| System-call tracing | Tương tác với OS, file, process | Không thấy mọi logic giữa các syscall |
| Call/stack tracing | Chuỗi lời gọi và độ sâu | Chi tiết phụ thuộc cách thu thập |
| Intel PT | Thông tin luồng điều khiển phần cứng | Cần phần cứng và giải mã hỗ trợ |
| Record/replay | Tái hiện execution đã ghi | Có giới hạn về hệ thống, thread và môi trường |
| Dynamic taint | Dòng chảy dữ liệu trên đường thực thi | Không bao phủ đường chưa chạy; cần propagation policy |
| eBPF/ftrace | Sự kiện kernel/userspace theo cơ chế hỗ trợ | Khả năng và quyền triển khai phụ thuộc hệ thống |

**Comparison tracing** giúp nhận ra input đang bị so với constant. CmpLog và tách phép so sánh dài có thể giúp fuzzer vượt magic value mà không cần symbolic execution đầy đủ. Đây là các kỹ thuật được giới thiệu trong nguồn; không được ghi là đã bật trong fuzzer lab nếu code chỉ đọc gcov.

Timing/side-channel testing đo khác biệt có thể lộ thông tin, nhưng cần kiểm soát noise và giả thiết quan sát của attacker. Chỉ thấy một lần chạy chậm hơn chưa đủ kết luận có side channel khai thác được.

**Executions per second** phản ánh tốc độ thử; instrumentation, fork/subprocess, solver và IO đều có chi phí. Persistent mode giảm khởi tạo lặp lại nhưng phải reset trạng thái; nếu state còn sót, testcase không còn độc lập và crash khó tái hiện.

## 4.5 Phân loại fuzzer trên các trục riêng

| Trục | Nhóm | Ý nghĩa |
| --- | --- | --- |
| Thông tin chương trình | Black-box | Không dùng cấu trúc code hoặc coverage để hướng dẫn |
| Thông tin chương trình | Grey-box | Dùng feedback nhẹ như coverage/comparison |
| Thông tin chương trình | White-box | Dùng mô hình ngữ nghĩa, symbolic/concolic và constraint solving |
| Tạo input | Mutation-based | Đột biến từ seed |
| Tạo input | Generation-based | Sinh từ grammar/schema/model |
| Chiến lược | Directed | Ưu tiên mục tiêu cụ thể |
| Kết hợp | Hybrid | Ghép mutation/coverage với giải ràng buộc khi cần |

Các trục không loại trừ nhau. Một generation-based fuzzer có thể dùng coverage; dictionary không tự biến black-box thành white-box; có mã nguồn không nghĩa thuật toán đang làm symbolic execution.

Trong slide và Lab 8, thuật ngữ “white-box” đôi khi dùng rộng để chỉ có coverage feedback. Để học chính xác, `lab8/python/whitebox_fuzzer.py` và fuzzer coverage trong `atpm_project` nên được hiểu là **coverage-guided/grey-box minh họa**. Toolkit `04_concolic_execution.py` mới có bước lấy path condition và gọi Z3 để phủ định nhánh.

## 4.6 Mutation, grammar và dictionary

Mutation operators thường gồm bit flip, byte replacement, insert/delete, arithmetic ±1 ở field số, block duplication, token insertion và splicing giữa hai seed. **Havoc** ghép nhiều đột biến ngẫu nhiên; stage deterministic thử những biến đổi có hệ thống trước hoặc bên cạnh havoc.

Với format `[magic4][length4][payload]`:

- Giữ magic đúng để tiếp cận parser sâu; vẫn có test riêng cho magic sai/ngắn.
- Thử length bằng 0, thực tế, thực tế±1 và giá trị biên kiểu.
- Có chiến dịch giữ length/checksum hợp lệ để vào logic payload.
- Có chiến dịch cố ý phá consistency để kiểm tra validation.
- Mutate nội dung payload, cấu trúc lồng nhau và các field nhạy cảm.

Grammar-based fuzzing sinh cấu trúc hợp lệ hoặc có chủ đích gần hợp lệ. Nếu tất cả input đều hoàn hảo theo grammar, vẫn có thể thiếu coverage của error handling. Một generator cần cân bằng valid và invalid cases.

**Dictionary** chứa token định dạng, magic header hoặc keyword. Nó giúp vượt một số guard với chi phí thấp, nhưng hiệu quả phụ thuộc vị trí chèn, stage mutation và các điều kiện phía sau.

### Xác suất magic value

Với `m` byte độc lập, đều trong 256 giá trị tại vị trí cố định:

\[
p=256^{-m},\quad E[tries]=1/p,\quad P(ít\ nhất\ 1\ lần\ trúng)=1-(1-p)^n
\]

`BEGIN` gồm 5 byte: `p=2^-40 ≈ 9,094947×10^-13`, số lần thử kỳ vọng khoảng `1,0995×10^12`. Trong 2.000.000 lần thử, số lần trúng kỳ vọng chỉ khoảng `1,819×10^-6`. Một số số mũ trong slide/chuỗi print của toolkit lệch; dùng công thức này để tính lại.

Kỳ vọng không phải cam kết “đến lần đó chắc chắn trúng”. Khi thêm dictionary, không lấy một hệ số tăng tốc cố định cho mọi chiến dịch; xác suất chọn token chỉ là một phần của quá trình vào được nhánh.

## 4.7 Symbolic và concolic execution

**Symbolic execution** thực thi mô hình với input tượng trưng, tích lũy path condition. **Concolic** chạy input cụ thể đồng thời ghi ràng buộc tượng trưng của những quyết định đã đi qua, rồi đổi một quyết định để sinh input mới.

Ví dụ:

```python
def classify(x, y):
    if x > 0:
        if y > 0:
            return 1
        return 2
    return 3
```

Chạy `(5,5)` tạo path `x>0 && y>0`. Muốn vào return2: giữ `x>0`, phủ định `y>0`, giải `x>0 && y<=0`. Muốn return3: phủ định điều kiện đầu, giải `x<=0`; **không giữ mọi điều kiện phía sau** vốn chỉ được đánh giá nếu x>0. Toolkit minh họa đúng nguyên tắc prefix tới nhánh bị phủ định.

Nếu solver trả UNSAT, không có input theo các ràng buộc mô hình đó. Nếu path condition được lấy thiếu hoặc sai ngữ nghĩa, kết luận feasibility cũng sai. Lời gọi thư viện, file, thời gian và concurrency cần environment modeling; dùng concrete fallback giúp chạy được nhưng có thể bỏ lỡ các biến thể tượng trưng.

### Path explosion và search strategy

- `n` quyết định Boolean độc lập liên tiếp, mỗi tổ hợp khả thi: có thể tới `2^n` đường hoàn chỉnh.
- Một chuỗi `if/else if` có n điều kiện thường có tối đa `n+1` nhánh lá của cấu trúc đó.
- Một chuỗi chỉ lồng trong nhánh true không nhất thiết có `2^n` lá; cây phân nhánh đầy đủ theo n mức mới có thể đạt số đó.
- Đạt branch coverage có thể cần ít test hơn nhiều so với mọi tổ hợp path.

DFS đi sâu nhanh; BFS ưu tiên đường ngắn nhưng dùng nhiều bộ nhớ; coverage-guided chọn input tạo thông tin mới; directed search ưu tiên một vùng mục tiêu. Không thể kết luận một chiến lược luôn tốt nhất mà không xét hình dạng CFG và budget.

**State/path merging** gộp trạng thái hội tụ bằng biểu thức điều kiện, có thể giảm số state nhưng tăng độ khó constraint. **Constraint caching**, pruning và bound là các cách quản lý tài nguyên; mọi giới hạn cần ghi trong kết luận.

## 4.8 White-box, hybrid và môi trường

White-box có thể giải `code==0x1337` trực tiếp thay vì chờ random input. Nhưng solver gặp arithmetic phi tuyến, path dài, alias hoặc thư viện phức tạp có thể rất tốn thời gian. KLEE là ví dụ với chương trình/LLVM representation; angr là ví dụ phân tích binary; SAGE là case study concolic trong tài liệu. Việc mô tả các công cụ không có nghĩa chúng đang được cài hoặc đã chạy trong thư mục.

Hybrid thường dùng mutation/coverage khám phá rộng; khi gặp guard khó thì symbolic/concolic tạo seed mới; quay lại mutation với seed đó. Cần đo thêm overhead solver và hiệu quả seed, không chỉ số crash.

Fuzzing đồng thời hoặc giao thức nhiều bước cần mô hình trạng thái/session; chỉ mutate một message độc lập có thể không vào được logic cần thiết. Syzkaller và OSS-Fuzz trong giáo trình minh họa mở rộng tới syscall và fuzzing liên tục; nội dung học tập ở đây tập trung nguyên lý, không sử dụng số liệu triển khai chưa được xác minh.

## 4.9 Crash triage, sanitizer và regression

Một campaign có thể có nhiều input cùng gây một lỗi. Triage nên dựa trên loại sanitizer finding, frame liên quan, vị trí nguyên nhân và tái hiện, không chỉ hash toàn bộ stderr vì địa chỉ/timing khác nhau.

Các bước: replay bằng build thích hợp → xác nhận tính ổn định → rút gọn input → tìm nguyên nhân gốc → sửa → chạy lại input cũ, test biên và corpus liên quan. Với hang, phân biệt logic vòng lặp với sự chậm do IO hoặc tiến trình bị nghẽn.

ASan phát hiện một số lỗi vùng nhớ/lifetime; UBSan phát hiện những nhóm UB được hỗ trợ và bật; MSan theo dõi một số đọc dữ liệu chưa khởi tạo và cần môi trường build thích hợp. LeakSanitizer còn phụ thuộc platform/cấu hình. Không có sanitizer nào tự kiểm tra mọi quyền nghiệp vụ.

**Differential fuzzing** so hai implementation với cùng input, chẳng hạn parser/serializer hoặc compiler. Cần chuẩn hóa phần kết quả không đáng so như timestamp/thứ tự không có nghĩa, và xác định implementation nào sai qua đặc tả. **Metamorphic fuzzing** kiểm tra quan hệ giữa input/output khi khó có oracle tuyệt đối.

## 4.10 Những giới hạn cụ thể trong fuzzer của thư mục

- Fuzzer Lab 8 chạy subprocess và đọc line coverage bằng gcov; không có SMT hay symbolic path collection.
- Hai fuzzer Lab 8 dùng mutation operators, seed ngẫu nhiên và budget khác nhau. Test dùng white-box 500 lần, black-box 1.000 lần, dù tên có nhắc “same budget”. Kết quả minh họa không phải so sánh thực nghiệm đã kiểm soát mọi biến.
- Black-box Lab 8 thêm candidate vào corpus với xác suất 5%, không theo coverage. White-box giữ candidate có dòng mới và bỏ đường crash khỏi feedback thông thường.
- Fuzzer `atpm_project` nhận return code âm như crash và mã âm cho timeout; phải phân biệt hang với crash và xét cách Windows mã hóa lỗi tiến trình.
- Gcov counter phải reset đúng tên để so campaign độc lập; line coverage có thể chịu ảnh hưởng driver CLI ngoài hàm mục tiêu.
- Kết quả `fuzzing_comparison_results.json` là dữ liệu có sẵn, không phải số liệu đã tái chạy trong lần tổng hợp này.

**Tự kiểm tra:** viết được harness nhận length; chọn oracle; phân biệt grey-box và concolic; tính xác suất; giải thích plateau; rút gọn crash; thiết kế so sánh hai chiến dịch công bằng.

## 4.11 Nguồn theo trang

- `Chuong4_Phan1_ATPM.pdf`: trang 4-24 security testing; 26-48 coverage/corpus; 54-76 tracing, comparison và hiệu năng.
- `Chuong4_Phan2_ATPM.pdf`: trang 4-20 sinh đường; 21-44 mutation/generation/dictionary; 45-66 symbolic, hybrid, environment và path merging.
- Giáo trình: trang PDF 67-80; sanitizer, minimization, structure-aware và differential fuzzing.
- Lab 7-8, `softsec-toolkit/ch4_dynafuzz`, `atpm/ch4_dynamic_analysis`.
