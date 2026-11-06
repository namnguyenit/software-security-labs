# Chương 3. Phân tích tĩnh, SAT/SMT và kiểm chứng hình thức

## 3.1 Bài toán kiểm chứng

Một kết luận kiểm chứng có ý nghĩa khi xác định đủ **mô hình**, **thuộc tính** và **giả thiết môi trường**:

\[
M \models P \quad\text{dưới các giả thiết } A
\]

Ví dụ “truy cập mảng an toàn” phải nêu kích thước allocation, miền index, kiểu số, lifetime object và các kiểm tra trước truy cập. Nếu chỉ giả sử `0<=index<N`, chứng minh index không vượt bounds là đúng nhưng không chứng minh code thực tế đã kiểm tra giả thiết đó.

Một chuỗi thực hiện hợp lý: chọn thuộc tính → biểu diễn code/mô hình → khai báo miền input và môi trường → tạo công thức vi phạm → giải → diễn giải kết quả → replay phản ví dụ → sửa và kiểm tra lại.

**Hoare triple** `{P} C {Q}` nói rằng nếu precondition P đúng thì khi C kết thúc, postcondition Q đúng trong cách hiểu partial correctness. Muốn total correctness còn phải chứng minh kết thúc. Ví dụ swap hai biến cần giả thiết các phép gán có ngữ nghĩa phù hợp; phép đổi chỗ dùng cộng/trừ có thể overflow nếu dùng kiểu giới hạn.

## 3.2 Soundness, completeness và quy ước diễn đạt

Thuật ngữ “sound” phải gắn với **kết luận nào**. Với một bộ chứng minh tính an toàn, soundness nghĩa là không kết luận “an toàn” cho chương trình thật sự vi phạm thuộc tính trong ngữ nghĩa đã chọn.

Trong tài liệu học phần, khi nói về **bug finding**, thường dùng quy ước:

- **Không bỏ sót lỗi:** mọi hành vi lỗi thật trong phạm vi đều nằm trong kết quả phân tích; over-approximation phục vụ mục tiêu này.
- **Không báo động giả:** mọi lỗi được báo đều có thể xảy ra thật trong phạm vi; under-approximation/replay thường hỗ trợ mục tiêu này.

Giáo trình gọi tương ứng “sound = no false negatives”, “complete = no false positives”. Một số tài liệu logic hoặc công cụ dùng định nghĩa theo kết luận khác và cách gọi có thể đổi. Khi viết báo cáo, nên ghi trực tiếp **có thể bỏ sót không, có thể báo giả không, dựa trên giả thiết gì**, rồi mới gắn thuật ngữ.

Gọi `B` là tập hành vi lỗi thật và `A` là tập hành vi được phân tích là lỗi:

| Quan hệ | Điều suy ra | Không suy ra |
| --- | --- | --- |
| `B ⊆ A` | Không bỏ sót lỗi trong phạm vi | Mọi warning đều thực sự xảy ra |
| `A ⊆ B` | Lỗi được báo là thật theo mô hình | Không còn lỗi khác |
| `A = B` | Chính xác trong ngữ nghĩa và phạm vi đã định | Chính xác với môi trường chưa mô hình hóa |

False positive là báo lỗi khi tình huống thật không vi phạm; false negative là bỏ qua lỗi có thật. **Precision** thường liên quan mức xấp xỉ hoặc tỉ lệ báo đúng; nó không đồng nghĩa mọi khái niệm completeness. Một công cụ chạy nhanh nhưng bỏ nhiều đường không tự trở thành đầy đủ vì các warning còn lại dễ hiểu.

Định lý Rice và bài toán dừng cho thấy không thể có thuật toán luôn kết thúc và quyết định chính xác mọi thuộc tính ngữ nghĩa không tầm thường của mọi chương trình tổng quát theo các mô hình tính toán thông thường. Điều này không cấm kiểm chứng chính xác một mô hình hữu hạn, một miền hạn chế hoặc một chương trình cụ thể.

## 3.3 Các mức phân tích tĩnh

### Cú pháp, dữ liệu và đường thực thi

- **Syntax/pattern analysis:** tìm API hoặc mẫu code đáng nghi. Nhanh, dễ mở rộng nhưng ít hiểu ngữ nghĩa.
- **Control-flow analysis:** xây CFG, xác định reachability và nhánh.
- **Data-flow analysis:** theo dõi định nghĩa/sử dụng, biến chưa khởi tạo, giá trị có thể tới một điểm.
- **Taint analysis:** source không tin cậy → biến đổi/propagation → sanitizer phù hợp → sink nhạy cảm.
- **Points-to analysis:** pointer có thể trỏ tới object nào; hỗ trợ phát hiện alias và lỗi lifetime.
- **Path-sensitive analysis:** giữ điều kiện theo từng đường để tránh ghép các trạng thái không cùng xảy ra.
- **Context-sensitive analysis:** phân biệt những ngữ cảnh gọi hàm thay vì gom tất cả caller thành một.

Một sanitizer cho SQL không tự bảo vệ command shell; một bounds check trước allocation không nhất thiết còn đúng sau realloc. Cần theo dõi cả miền giá trị và trạng thái tài nguyên.

### Abstract interpretation

Thay các giá trị cụ thể bằng miền trừu tượng. Ví dụ `x∈[0,10]`, `y∈[2,3]` thì mô hình interval cho `x+y∈[2,13]`. Để kiểm tra mảng 12 phần tử, interval này chưa đủ chứng minh an toàn.

Khi hai nhánh có quan hệ `x=y` và `x=y+1`, interval tách từng biến có thể mất quan hệ. Miền relational có thể chính xác hơn nhưng tốn tài nguyên. **Join** gộp các đường; **widening** giúp hội tụ trên vòng lặp, có thể làm mất precision; **narrowing** có thể cải thiện một số bounds sau đó. Không được coi interval dự đoán chính là tập mọi giá trị đạt được nếu đã xấp xỉ.

### Phân tích tĩnh, mô phỏng và debugging

Phân tích tĩnh tìm vấn đề từ code/mô hình; simulation/testing quan sát hành vi của input cụ thể; debugging tìm cơ chế và nguyên nhân gốc. Cùng một UAF có thể được báo ở path của analyzer, xuất hiện trong ASan khi chạy, rồi được giải thích bằng breakpoint/trace. Các bằng chứng có vai trò bổ sung nhau.

## 3.4 SAT và cách tìm phản ví dụ

SAT hỏi: **có cách gán biến Boolean làm công thức đúng không?** Literal là biến hoặc phủ định của biến. Clause là OR của các literal. CNF là AND của các clause.

\[
\Phi=(a\lor b)\land(\neg a\lor c)\land(\neg b\lor c)\land\neg c
\]

Unit clause `!c` buộc `c=False`; hai clause sau buộc `a=False`, `b=False`; clause `(a∨b)` trở thành rỗng, nên UNSAT. Không cần liệt kê đủ 8 tổ hợp.

**DPLL** gồm đơn giản hóa công thức theo assignment, unit propagation, có thể pure-literal elimination, chọn biến và thử hai giá trị với backtracking. Quy tắc kết thúc quan trọng:

- Không còn clause: các ràng buộc còn lại đã thỏa, SAT.
- Có clause rỗng: nhánh hiện tại mâu thuẫn.
- Không có mâu thuẫn nhưng chưa xong: branch tiếp.

**CDCL** bổ sung học clause từ conflict, conflict analysis, non-chronological backjumping và các heuristic/restart. Clause học phải là hệ quả của ràng buộc để không xóa nghiệm hợp lệ. Solver nhanh trên nhiều bài toán thực tế không làm SAT tổng quát hết độ khó NP-complete.

Chuyển `(a && b) || c` thành CNF bằng phân phối cho `(a || c) && (b || c)`. Với công thức lớn, Tseitin encoding dùng biến phụ để tránh bùng nổ kích thước; thường bảo toàn tính thỏa với phép chiếu biến, không đòi tất cả biến phụ là biến ban đầu.

### Tương đương hai điều kiện

Muốn kiểm tra `P` và `Q` tương đương trên miền `D`, tìm:

\[
D\land(P\oplus Q)
\]

- SAT: có đầu vào khiến hai điều kiện khác nhau.
- UNSAT: không có đầu vào khác nhau trong miền đã mã hóa.
- UNKNOWN: chưa có kết luận.

Đây là nguyên lý Lab 5. `failed_attempts>=3` và `failed_attempts>3` khác nhau tại 3; thêm đường `is_admin && bypass_flag` vào điều kiện authenticated tạo ra phản ví dụ chưa xác thực nhưng được cấp quyền.

Tương đương biểu thức Boolean thuần túy không cho phép đổi thứ tự gọi hàm có side effect. Ví dụ `p!=NULL && p->field==1` không được hoán đổi hai điều kiện trong C chỉ vì AND giao hoán trong logic.

## 3.5 SMT, kiểu dữ liệu và Z3

SMT bổ sung lý thuyết vào logic Boolean. Những miền thường gặp: integer/real arithmetic, bit-vector, array, uninterpreted function. DPLL(T) kết hợp lớp tìm kiếm Boolean với solver của các lý thuyết.

| Kiểu/mô hình | Dùng cho | Bẫy thường gặp |
| --- | --- | --- |
| `Bool` | Điều kiện, flags | Nhầm logic solver với Boolean của Python |
| `Int` | Số nguyên toán học | Không tự có bounds int 32 hoặc wraparound |
| `Real` | Số thực toán học | Không tự mô hình IEEE floating-point |
| `BitVec(w)` | Phép toán bit và kiểu `w` bit | Cần chọn đúng signed/unsigned comparison |
| `Array` | Select/store và bộ nhớ trừu tượng | Không tự có bounds/lifetime như mảng C |
| Uninterpreted function | Quan hệ chưa mô tả implementation | Kết quả chỉ dựa trên axiom đã đưa vào |

Ví dụ Z3 tìm phản ví dụ cho truy cập mảng:

```python
from z3 import Int, Solver, Or

index = Int("index")
solver = Solver()
solver.add(index >= 0, index <= 12)  # giả thiết môi trường
solver.add(Or(index < 0, index >= 10))  # phủ định điều kiện an toàn
print(solver.check())
```

SAT vì 10,11,12 đều là phản ví dụ. Thay giả thiết bằng `0<=index<10` sẽ UNSAT; kết luận phụ thuộc giả thiết đó.

Với unsigned 8-bit, `250+10` ra 4 theo modulo 256. `Int` trả 260. Với bit-vector, các phép `<,>` trong Z3 Python thường có ngữ nghĩa signed; dùng `ULT`, `ULE`, `UGT`, `UGE` cho unsigned. Một path `unsigned x>100 && x<0` là infeasible theo unsigned comparison, nhưng có thể bị mô hình hóa sai nếu dùng comparison signed.

Kiểm tra overflow bằng integer toán học: giới hạn **từng input** vào miền int 32, tính biểu thức trên Int và tìm kết quả ngoài `[-2^31,2^31-1]`. Hoặc dùng bit-vector và predicate overflow/biểu thức đối chiếu thích hợp. Bit-vector wrap không tự biểu diễn việc signed overflow trong C là UB; cần thêm yêu cầu phát hiện UB hoặc dùng ngữ nghĩa phù hợp.

Khi có model: lấy giá trị với sort đúng, hỗ trợ model completion nếu biến không cần được gán, và đưa input đó chạy lại target. Khi `unknown`, giữ trạng thái chưa kết luận cùng lý do/timeout. Một vài helper trong thư mục dùng “không SAT” như “an toàn”; đó là giới hạn code, không phải quy tắc chuẩn.

`eval` trong Lab 5 được dùng cho dataset nội bộ; `{"__builtins__":{}}` không biến nó thành sandbox tổng quát. Khi biến đặc tả thành sản phẩm nhận input ngoài, cần parser và whitelist AST/grammar rõ ràng thay vì cho biểu thức Python tùy ý.

## 3.6 Bounded Model Checking

BMC tìm phản ví dụ có độ dài hữu hạn. Với invariant `P`, mô hình total và giới hạn `k` bước chuyển:

\[
BMC_k=I(s_0)\land\bigwedge_{i=0}^{k-1}T(s_i,s_{i+1})\land\bigvee_{i=0}^{k}\neg P(s_i)
\]

`I` mô tả initial, `T` mô tả transition, phần OR yêu cầu ít nhất một state vi phạm. Công thức trên mở rộng được prefix ngắn tới k nếu ngữ nghĩa/totalization cho phép; với mô hình kết thúc hữu hạn cần mã hóa termination hoặc xét riêng từng độ dài, không vô tình bỏ mất phản ví dụ ngắn.

- **SAT:** có trace vi phạm trong bound và mô hình đã mã hóa.
- **UNSAT:** không có trace vi phạm trong bound và giả thiết đó.
- **UNKNOWN/timeout:** chưa quyết định.

`k` bước chuyển có `k+1` state. “Unwind 10 lần” của vòng lặp không tự bằng “10 lần chuyển trạng thái” của một mô hình khác. Trong Lab 6, `range(unwind_bound)` kiểm tra `i=0..bound-1`; để thấy truy cập `i=10` cần `unwind_bound>=11`.

### Unroll và SSA

Vòng lặp được trải phẳng tới bound; mỗi phiên bản biến có tên riêng:

```text
i0 = 0
guard0 = i0 < N
index0 = base + i0
i1 = i0 + 1
guard1 = i1 < N
index1 = base + i1
...
```

Vi phạm bounds ở bước i chỉ có ý nghĩa nếu các guard dẫn tới bước đó đều đúng. Không được bỏ điều kiện điều khiển rồi kết luận code thật có đường lỗi mà code không thể thực thi.

Engine Lab 6 là mô hình riêng cho `index=base+i`, không phải parser tự động mã C. Nó tạo solver riêng cho mỗi i và không mô hình toàn bộ CFG, số học máy hay mọi con trỏ. Giá trị `SAFE` của engine cần đọc cùng phần giải thích “SAFE-UP-TO-BOUND”.

### Completeness threshold và unwinding assertion

Với một mô hình hữu hạn, có thể xác định bound đủ theo loại thuộc tính và cấu trúc đồ thị. Không lấy tùy ý “số state” làm ngưỡng cho mọi công thức liveness hoặc mọi chương trình có biến dữ liệu.

Unwinding assertion kiểm tra vòng lặp không còn tiếp tục ngoài bound đã chọn. Nó thất bại có thể vì bound chưa đủ, không nhất thiết vì assertion nghiệp vụ đã sai. Cần phân biệt **thiếu bao phủ vòng lặp** và **phản ví dụ vi phạm thuộc tính**.

Ví dụ lệnh cho một môi trường có CBMC:

```text
cbmc array_access.c --function symbolic_safe --bounds-check \
  --pointer-check --signed-overflow-check --unwind 6 \
  --unwinding-assertions --trace
```

Hàm, harness, nondeterministic input và bounds cần được thiết kế theo chương trình thật; lệnh đơn lẻ không tự hoàn thành phần đó. Cờ kiểm tra và mặc định phụ thuộc phiên bản; đối chiếu [manual CBMC](https://diffblue.github.io/cbmc/man/cbmc.html) và lưu phiên bản vào báo cáo.

## 3.7 K-induction và kiểm chứng không giới hạn

K-induction gồm:

1. **Base case:** thuộc tính đúng trên những prefix ban đầu cần thiết tới k.
2. **Inductive step:** nếu P đúng trên k state liên tiếp của một đoạn chuyển hợp lệ thì nó đúng ở state tiếp theo.

Nếu cả hai được chứng minh theo định nghĩa phù hợp, có thể suy ra invariant không giới hạn. Step case xét cả state chưa chắc reachable, nên có thể thất bại dù invariant đúng từ initial. Cần thêm invariant phụ hoặc tăng k, không vội kết luận có bug thật.

Đây là khác biệt giữa “đã thử đến k” và “đã chứng minh bước quy nạp”. Nhiều test hoặc nhiều lần tăng bound mà chưa có completeness/induction vẫn là kiểm tra hữu hạn.

## 3.8 Mô hình bộ nhớ hình thức

Một pointer có thể được mô hình bằng **object identity + offset**. Mỗi allocation có size, trạng thái alive, quyền truy cập và dữ liệu. Với truy cập `n` byte từ offset `o`:

\[
alive(object)\land 0\le o\land n\le size(object)-o
\]

Phải đồng thời bảo đảm các phép tính biểu diễn không overflow. Mô hình object-based giúp phân biệt truy cập sai object dù địa chỉ nằm trong một vùng phẳng lớn.

| Hành động | Cập nhật/điều kiện |
| --- | --- |
| malloc | Tạo object mới, size hợp lệ; có nhánh allocation failure nếu giả thiết cho phép |
| read/write | Object alive, offset/size đúng, dữ liệu khởi tạo và quyền phù hợp |
| free | Pointer tới allocation hợp lệ chưa free; đánh dấu hết lifetime |
| free lần hai | Vi phạm điều kiện alive/ownership |
| UAF | Read/write sau khi lifetime kết thúc |
| alias | Hai pointer cùng object; free qua một alias ảnh hưởng alias còn lại |

Một mảng Boolean `allocated[address]` minh họa double free nhưng chưa biểu diễn đầy đủ C: address có thể tái sử dụng, interior pointer, offset, kích thước, alias và identity qua nhiều lifetime. `Select/Store` của array SMT không tự kiểm tra bounds; cần ràng buộc riêng.

**Separation logic** dùng `P * Q` để diễn đạt các phần heap tách biệt, hỗ trợ suy luận cục bộ về ownership. Dấu `*` ở đây là separating conjunction, không phải multiplication hoặc phép AND thông thường. Redzone/shadow memory của sanitizer là cơ chế phát hiện động, khác với một chứng minh hình thức mọi truy cập hợp lệ.

### Aligned memory model

Thêm ràng buộc `address % alignment == 0`. Với mảng struct:

\[
address(field_i)=base+i\times sizeof(struct)+offset(field)
\]

Nếu base phù hợp, size struct là bội của alignment yêu cầu và field offset phù hợp, có thể chứng minh mọi phần tử đúng alignment. Còn phải kiểm tra index, bounds, lifetime và kiểu truy cập. Alignment đúng một mình không chứng minh memory safety.

## 3.9 BDD, abstraction và đồng thời

BDD biểu diễn hàm Boolean bằng đồ thị quyết định, chia sẻ những subgraph tương đương. Reduced ordered BDD có tính chuẩn tắc với **thứ tự biến cố định**; kích thước có thể rất khác khi đổi thứ tự. Symbolic model checking dùng tập state/transition dưới dạng biểu thức thay vì liệt kê mọi state, nhưng vẫn có trường hợp bùng nổ.

Với concurrency, cần nêu interleaving, scheduler, atomic operation và memory consistency model. Kiểm chứng dưới sequential consistency không tự bao phủ mọi hành vi do reorder của hệ máy có memory model yếu. Mô hình trong các JSON của thư mục chủ yếu là đồ thị hữu hạn mức khái niệm, không phải kiểm chứng implementation mutex của một hệ điều hành thực.

Case study seL4 trong giáo trình minh họa formal verification quy mô hệ thống. Điều cần rút ra là tính chất chứng minh luôn có phạm vi, phiên bản, cấu hình và giả thiết; không suy diễn “đã có formal proof” thành “mọi thành phần, mọi hardware và mọi thuộc tính bảo mật đều không có lỗi”.

## 3.10 Áp dụng vào các file hiện có

- Lab 5: 6 cặp điều kiện; XOR tìm phản ví dụ; brute-force C kiểm tra chéo các trường hợp Boolean.
- Lab 6: 4 mô hình index, gồm full scan, off-by-one, offset symbolic và precondition đã sửa.
- `atpm/ch3_static_analysis/smt_checks.py`: bounds, overflow multiplication, chia cho 0 và wrapper CBMC.
- Toolkit `ch3_verify`: SAT bằng liệt kê, ví dụ Z3, BMC nhỏ, double-free model, alignment và C harness cho CBMC.
- Phụ lục A giáo trình: DPLL solver, memory trace, layout và bounded checker minh họa; không mặc định những file này đã tồn tại trong toolkit trên ổ đĩa.

**Tự kiểm tra:** giải được CNF nhỏ bằng propagation; chọn Int hay BitVec đúng; viết công thức tìm vi phạm; đọc SAT/UNSAT/UNKNOWN; nêu rõ bound và assumptions; giải thích vì sao phản ví dụ của mô hình cần replay trên target.

## 3.11 Nguồn theo trang

- `Chuong3_Phan1_ATPM.pdf`: trang 4-17 V&V; 19-35 soundness/approximation; 38-54 tĩnh/động/debug; 56-78 SAT/SMT.
- `Chuong3_Phan2_ATPM.pdf`: trang 4-28 BMC; 30-43 memory model; 47-64 alignment và kết hợp kiểm chứng.
- Giáo trình: trang PDF 52-66; mở rộng BDD, abstract interpretation, k-induction, seL4 và DPLL trace.
- Lab 5-6, `softsec-toolkit/ch3_verify`, `atpm/ch3_static_analysis`.
