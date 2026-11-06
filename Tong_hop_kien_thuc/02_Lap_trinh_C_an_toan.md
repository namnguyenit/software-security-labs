# Chương 2. Lập trình C an toàn và quản lý bộ nhớ

## 2.1 Rủi ro đặc thù của C

C cho phép thao tác gần phần cứng, kiểm soát dữ liệu và chi phí thực thi. Đổi lại, ngôn ngữ không tự động kiểm tra mọi bounds hoặc quản lý vòng đời object. Một hàm biên dịch thành công vẫn có thể chứa undefined behavior, đọc dữ liệu ngoài object hoặc làm sai trạng thái allocator.

Khi đánh giá chương trình C, theo dõi dữ liệu từ **source** tới **sink**: nguồn input mạng/file/argv → parsing → chuyển kiểu/tính kích thước → allocation/copy/index → output hoặc thao tác có quyền. Chọn điểm có nguy cơ bằng cách hỏi: ai điều khiển giá trị này; miền hợp lệ là gì; kiểm tra diễn ra trước hay sau khi sử dụng; nếu lỗi thì ai giải phóng tài nguyên?

Bề mặt tấn công gồm không chỉ input bình thường mà cả file lỗi, dữ liệu cắt ngắn, số âm, kích thước cực lớn, dữ liệu nhị phân có byte NUL và thứ tự gọi API sai. Giới hạn do giao diện người dùng đặt ra không thay thế kiểm tra tại hàm xử lý.

## 2.2 Mô hình bộ nhớ và vòng đời object

| Vùng thường gặp | Nội dung điển hình | Lỗi cần chú ý |
| --- | --- | --- |
| Text/code | Mã máy | Nhảy tới địa chỉ sai, thực thi dữ liệu nếu thiếu bảo vệ |
| Data/BSS | Biến tĩnh/toàn cục đã khởi tạo hoặc zero-init | Race, sai trạng thái dùng chung |
| Stack | Biến tự động, thông tin lời gọi trên nhiều ABI | Vượt mảng cục bộ, trả con trỏ tới biến đã hết vòng đời |
| Heap | Vùng cấp phát động | Leak, UAF, double free, overflow |

Đây là mô hình tiến trình điển hình, không phải layout bắt buộc bởi chuẩn C. Hướng tăng của stack/heap và vị trí từng vùng phụ thuộc hệ điều hành, ABI và cách cấp phát. `sizeof(pointer)` không nói kích thước allocation mà pointer trỏ tới.

Hai loại memory safety cần phân biệt:

- **Spatial safety:** truy cập đúng phạm vi object. Với mảng `N` phần tử, chỉ số hợp lệ `0 <= i < N`.
- **Temporal safety:** chỉ sử dụng object trong vòng đời hợp lệ. Pointer còn chứa địa chỉ sau `free` không có nghĩa object còn tồn tại.

Pointer một-past-the-end có thể dùng theo những quy tắc của C để biểu diễn ranh giới/so sánh thích hợp, nhưng không được dereference. `NULL` là một giá trị pointer, còn dangling pointer là pointer tới object đã hết vòng đời; hai khái niệm khác nhau.

## 2.3 malloc, calloc, realloc và ownership

### Nguyên tắc ownership

Mỗi allocation cần một bên chịu trách nhiệm giải phóng; các pointer mượn chỉ hợp lệ trong thời gian owner cho phép. API nên ghi rõ trả về owned pointer hay borrowed pointer, ai gọi destructor và hàm có giữ pointer sau khi trả về không.

```c
#include <stdint.h>
#include <stdlib.h>

int *allocate_items(size_t count) {
    if (count == 0 || count > SIZE_MAX / sizeof(int)) {
        return NULL;
    }
    int *items = malloc(count * sizeof *items);
    if (items == NULL) {
        return NULL;
    }
    return items; /* người gọi sở hữu và phải free */
}
```

Kiểm tra multiplication trước `malloc` là điều kiện cần để tránh cấp phát vùng nhỏ do wraparound. Sau `malloc`, vùng nhớ chưa được khởi tạo; `calloc` zero các byte nhưng không làm mất nhu cầu kiểm tra các điều kiện nghiệp vụ hoặc lỗi allocation.

`realloc` có thể di chuyển allocation. Với kích thước mới dương, dùng pointer tạm:

```c
void *candidate = realloc(buffer, new_size);
if (candidate == NULL) {
    /* buffer cũ còn hợp lệ; xử lý lỗi theo hợp đồng */
    return ERROR_ALLOCATION;
}
buffer = candidate;
```

Nếu gán thẳng `buffer = realloc(...)` rồi thất bại, mất pointer cũ và có thể leak. Pointer alias tới vùng cũ có thể không còn hợp lệ khi realloc thành công. Thiết kế rõ trường hợp size 0 và tránh dựa vào hành vi khác nhau giữa phiên bản chuẩn/implementation.

`free(NULL)` không làm gì; `free` chỉ nhận pointer hợp lệ tới đầu allocation tương ứng chưa bị giải phóng. Không free pointer stack, pointer tới giữa allocation hoặc cùng allocation hai lần. `p=NULL` sau free giúp tránh sử dụng lại qua **biến p**, nhưng không sửa các alias khác.

### Cleanup và đường lỗi

Một hàm cấp phát nhiều tài nguyên cần cleanup tương ứng trên mọi đường thoát: lỗi parsing, lỗi cấp phát thứ hai, lỗi file, return sớm. Có thể dùng một khối cleanup và trạng thái ownership rõ ràng. Không tự động gọi free với pointer chưa được khởi tạo.

**Leak** là allocation không được giải phóng khi hết thời gian sử dụng. Cần phân biệt “mất hoàn toàn pointer”, “còn reachable nhưng tồn tại quá lâu” và tài nguyên được thiết kế tồn tại tới cuối tiến trình. Không phải mọi allocation chưa free ở thời điểm đo đều cùng mức nghiêm trọng, nhưng leak tăng theo số request có thể gây DoS.

## 2.4 Cấu trúc dữ liệu động an toàn

### Linked list

Các invariant điển hình: `head` là NULL hoặc node hợp lệ; mỗi `next` là NULL hoặc node còn sống; node thuộc một danh sách có ownership rõ; danh sách không có chu trình nếu thuật toán đòi hỏi kết thúc tại NULL.

Khi giải phóng, phải giữ `next` trước `free`:

```c
void destroy_list(Node *head) {
    while (head != NULL) {
        Node *next = head->next;
        free(head);
        head = next;
    }
}
```

Mẫu `free(head); head=head->next;` là UAF. Khi xóa node giữa: sửa link của node trước hoặc cập nhật head → free node bị xóa → không tiếp tục đọc node đó. Với doubly linked list phải cập nhật cả `prev` và `next`, gồm trường hợp xóa đầu/cuối/node duy nhất.

Trong Lab 4, `list_remove_by_title` bản buggy unlink node nhưng không free; `list_count_UNSAFE` dùng `int count` chưa khởi tạo; `list_insert_front` dereference kết quả malloc trước khi kiểm tra. Bản fixed sửa ba cơ chế này, nhưng tên “fixed” không tự chứng minh mọi đầu vào và mọi lỗi đã được xử lý.

### Dynamic array, hash table, tree

- Dynamic array cần phân biệt `size` là số phần tử đang dùng và `capacity` là vùng đã cấp phát; tăng capacity phải kiểm tra phép nhân và cộng.
- Hash table phải quản lý bucket, node, key/value, resize và collision. Nếu key/value là borrowed pointer, destructor không được free chúng tùy ý.
- Tree thường giải phóng hậu tự: hủy subtree trước node. Độ sâu lớn có thể làm recursion tràn stack; cân nhắc duyệt lặp hoặc giới hạn cấu trúc.
- Chu trình hoặc chia sẻ node làm hợp đồng giải phóng phức tạp hơn; traversal tree đơn giản không an toàn với graph có shared ownership.

## 2.5 Chuỗi, buffer và parsing đầu vào

Chuỗi C cần byte kết thúc `\0`. Buffer `char name[16]` chứa tối đa **15 byte nội dung** nếu phải là C string. “16 ký tự” không bằng “16 byte” với UTF-8. Đối với dữ liệu nhị phân, truyền pointer và length rõ ràng thay vì dùng strlen.

| API/mẫu nguy hiểm | Vấn đề | Cách xử lý |
| --- | --- | --- |
| `gets` | Không có bounds, không dùng | `fgets` với kích thước và xử lý dòng bị cắt |
| `strcpy`, `strcat` | Không biết capacity đích | Kiểm tra length/capacity hoặc wrapper có hợp đồng rõ |
| `sprintf` | Không giới hạn output | `snprintf`, kiểm tra lỗi và truncation |
| `strncpy` | Có thể không đặt NUL | Hiểu đúng `n`, capacity đích và kết thúc chuỗi |
| `scanf("%s",buf)` | Không giới hạn độ dài | Width phù hợp và kiểm tra conversion; thường ưu tiên đọc dòng rồi parse |
| `printf(input)` | Input là format string | `printf("%s",input)` hoặc API ghi dữ liệu |
| `atoi` | Khó phân biệt lỗi, thiếu kiểm tra overflow | `strtol`/`strtoul`, end pointer, errno và bounds kiểu đích |

Ví dụ copy **từ chối quá dài**, không âm thầm truncation:

```c
/* src phải là C string hợp lệ; dst phải có cap byte ghi được. */
int copy_name(char *dst, size_t cap, const char *src) {
    if (dst == NULL || src == NULL || cap == 0) return -1;
    size_t length = strlen(src);
    if (length >= cap) return -1;
    memcpy(dst, src, length + 1);
    return 0;
}
```

Mẫu này đòi hỏi `src` có NUL trong object hợp lệ và các vùng không overlap. Không dùng nó trực tiếp cho dữ liệu mạng chưa có độ dài đáng tin. Với input `(src,len)`, kiểm tra `len < cap` và copy đúng `len` byte, rồi thêm NUL nếu đó là dữ liệu chuỗi.

Với `snprintf`, kết quả âm là lỗi; kết quả không âm `>= capacity` cho biết bị cắt. Dù không vượt buffer, truncation ID thiết bị hoặc token có thể tạo lỗi logic/xung đột định danh. Vì vậy “copy có bounds” và “đáp ứng đặc tả” là hai kiểm tra riêng.

Trong `atpm_project/c/ch2_memory/safe_string.c`, `ss_copy` trả length gốc; người gọi so với `dst_size` để nhận biết truncation. `ss_concat` dùng `strnlen` để kiểm tra chuỗi đích. `ss_alloc_checked` kiểm tra multiplication trước calloc. Các API vẫn có precondition về buffer hợp lệ, chuỗi nguồn có NUL và overlap; không phải wrapper giải quyết mọi lỗi con trỏ.

### Format string

Khi dữ liệu người dùng trở thành format, các conversion có thể đọc/ghi qua đối số mà code không cung cấp đúng; `%n` còn có ngữ nghĩa ghi số ký tự đã in vào vùng chỉ định. Phòng ngừa bằng format cố định và đúng kiểu đối số. Validation nội dung không thay thế việc giữ format là hằng do chương trình quyết định.

## 2.6 Số nguyên và undefined behavior

**Unsigned** có arithmetic modulo `2^w`; đây là hành vi được định nghĩa nhưng có thể vi phạm hợp đồng tính kích thước. **Signed overflow** trong C thông thường là undefined behavior; compiler được phép tối ưu dựa trên giả thiết nó không xảy ra.

Mẫu kiểm tra sau `a+b` đã overflow không sửa được UB. Kiểm tra trước:

```c
#include <limits.h>

int add_checked(int a, int b, int *result) {
    if (result == NULL) return -1;
    if ((b > 0 && a > INT_MAX - b) ||
        (b < 0 && a < INT_MIN - b)) {
        return -1;
    }
    *result = a + b;
    return 0;
}
```

Với `size_t`, cộng kiểm tra `a > SIZE_MAX-b`; nhân với `b>0` kiểm tra `a > SIZE_MAX/b`. Đổi số âm thành unsigned có thể biến một giá trị nhỏ thành số rất lớn. Với bounds array, nên xác minh miền signed trước khi cast.

UB còn gồm đọc biến chưa khởi tạo, dereference NULL/dangling pointer, truy cập ngoài object, vi phạm alignment hoặc quy tắc aliasing, chia số nguyên cho 0 và một số phép shift sai miền. Riêng `INT_MIN / -1` cũng cần xét khả năng overflow. Hành vi “chạy đúng” trong debug không loại trừ UB ở bản tối ưu.

`const` giúp biểu đạt một số quyền sửa qua một reference; không kéo dài lifetime, không bảo đảm thread safety và không xác nhận dữ liệu đáng tin. `assert` hữu ích cho invariant nội bộ nhưng có thể bị loại khi bật `NDEBUG`; input không tin cậy cần kiểm tra lỗi bình thường.

## 2.7 Alignment, padding và serialization

Alignment yêu cầu địa chỉ object phù hợp với kiểu truy cập. Với yêu cầu `a` byte, mô hình đơn giản là `address % a == 0`. `sizeof(struct)` có thể lớn hơn tổng size các field vì padding giữa field và ở cuối.

Ví dụ trên ABI phổ biến có `char=1`, `int=4`, alignment `int=4`:

```c
struct Example {
    char a;   /* offset 0 */
    int b;    /* offset 4: trước đó có padding */
    char c;   /* offset 8 */
};            /* thường sizeof=12, align=4 */
```

Đây là kết quả phụ thuộc ABI. Xác minh bằng `sizeof`, `_Alignof` và `offsetof`; không lấy con số 12 làm định luật cho mọi nền tảng. Sắp xếp field theo alignment có thể giảm padding, nhưng thay đổi layout có thể phá tương thích ABI, file hoặc giao thức.

**Rủi ro padding:** serialize nguyên struct có thể gửi cả byte không có ý nghĩa nghiệp vụ, gây rò rỉ; layout và endian cũng khác giữa máy. Nên encode từng field theo định dạng xác định. Không dùng `memcmp` nguyên struct để so sánh giá trị logic nếu padding chưa được kiểm soát.

`packed` giảm padding nhưng có thể tạo field misaligned; ép pointer tới dữ liệu mạng sang `int*` không an toàn chỉ vì máy hiện tại cho phép. Đọc byte vào biến đúng kiểu qua `memcpy`, rồi xử lý endian; đích vẫn cần alignment đúng và nguồn đủ byte.

| Chủ đề mở rộng | Điều cần nhớ |
| --- | --- |
| Endianness | Thứ tự byte của số nhiều byte, khác alignment |
| Union | Các field chia sẻ vùng nhớ; size/alignment theo implementation và các thành viên |
| Bit-field | Layout có đặc tính phụ thuộc implementation; không tự làm chuẩn giao thức |
| `_Alignas`, `_Alignof` | Yêu cầu/kiểm tra alignment theo chuẩn ngôn ngữ thích hợp |
| SIMD | Có instruction có yêu cầu alignment riêng |
| False sharing | Thread sửa dữ liệu khác nhau nhưng cùng cache line gây contention; chủ yếu là hiệu năng |

Không mọi hiện tượng cache hoặc misalignment đều là một lỗ hổng bảo mật; phải chỉ ra tác động cụ thể lên thuộc tính.

## 2.8 Allocator và cơ chế giảm nhẹ

Heap allocator có metadata và các cấu trúc quản lý chunk. Ghi vượt allocation hoặc free sai có thể làm sai cả dữ liệu ứng dụng lẫn trạng thái allocator. Layout glibc trong giáo trình là ví dụ của một implementation, không đại diện mọi allocator hay mọi phiên bản.

| Cơ chế | Tác dụng chính | Giới hạn |
| --- | --- | --- |
| Stack canary | Phát hiện một số ghi hỏng stack trước khi return | Không bảo vệ mọi object hoặc lỗi logic |
| ASLR | Làm địa chỉ khó đoán hơn | Không sửa UAF/overflow |
| NX/DEP | Hạn chế thực thi vùng dữ liệu | Không ngăn mọi cách điều khiển hành vi |
| PIE | Hỗ trợ ngẫu nhiên hóa địa chỉ executable | Cần môi trường phù hợp |
| RELRO | Bảo vệ một số vùng relocation | Không thay bounds checking |
| Fortified library checks | Thêm kiểm tra khi compiler có thông tin size | Không biết mọi size hoặc mọi lifetime |
| Hardened allocator | Kiểm tra metadata, phát hiện một số free sai | Không phải chứng minh absence of bugs |

Cơ chế giảm nhẹ làm việc khai thác khó hơn hoặc giúp phát hiện lỗi; vẫn phải sửa nguyên nhân gốc. Morris Worm là case study lịch sử trong giáo trình về input không được giới hạn và bài học loại bỏ API không có bounds; không suy ra mọi lỗi hiện đại đều là cùng cơ chế.

## 2.9 Công cụ và cách đọc bằng chứng

| Công cụ | Loại | Bằng chứng |
| --- | --- | --- |
| Compiler warnings | Tĩnh, chủ yếu dựa trên thông tin compiler | Vị trí và cảnh báo kiểu/control/data flow |
| cppcheck | Tĩnh | Finding có ID, severity, CWE và location |
| Clang Static Analyzer | Tĩnh | Đường phân tích dẫn tới lỗi |
| clang-tidy | Tĩnh | Check về bug, style, portability, hiệu năng tùy rule |
| Pattern scanner của toolkit | Tĩnh theo mẫu cú pháp | Dòng có hàm/mẫu đáng nghi |
| ASan | Động, instrumented | Overflow/UAF và stack trace ở đường đã chạy |
| UBSan | Động | Những UB được bật và instrument hỗ trợ |
| LeakSanitizer/Valgrind | Động | Allocation, leak và truy cập trong lần chạy |

Valgrind không phải static analyzer. Regex thấy `strcpy` chưa chứng minh allocation thực tế bị vượt; regex không thấy `strcpy` cũng chưa chứng minh không có overflow qua memcpy hoặc indexing.

Khi đọc ASan: xác định loại lỗi → lệnh đọc/ghi và số byte → stack trace của thao tác → allocation trace → free trace nếu có → offset so với object. Một overflow giữa hai field trong **cùng allocation** có thể không bị bộ kiểm tra bounds theo allocation phát hiện. Lab 3 cố ý có cả copy vào field struct và allocation heap riêng để minh họa khác biệt này.

Bản “secure” trong Lab 3 còn precondition chưa đầy đủ: helper heap không kiểm tra `title==NULL`; caller in `%s` với pointer malloc thất bại; hàm nhận `count` tổng quát chưa kiểm tra miền và multiplication. Trong main hiện tại `count=5` nên một số đường này chưa được kích hoạt. Hãy dùng chúng để luyện review, không xem tên file là chứng nhận an toàn toàn diện.

## 2.10 Quy trình sửa lỗi có kiểm chứng

1. Mô tả input và thuộc tính bị vi phạm.
2. Dựng một test tái hiện ngắn nhất có thể.
3. Xác định nguyên nhân: bounds, ownership, số học hay quyền.
4. Sửa tại nơi đảm bảo invariant; kiểm tra mọi caller liên quan.
5. Chạy lại test lỗi cũ và những biên lân cận.
6. Kiểm tra tác động phụ: truncation, thay đổi ownership, return code và cleanup.
7. Lưu input lỗi thành regression test và ghi giới hạn phương pháp.

Không sửa UAF bằng việc thêm delay, không sửa overflow chỉ bằng tăng buffer vô hạn và không sửa warning bằng suppress mà chưa hiểu nguyên nhân.

## 2.11 Nguồn theo trang

- `Chuong2_Phan1_ATPM.pdf`: trang 4-21 đánh giá rủi ro; 24-47 cấu trúc động; 51-76 secure coding và công cụ động.
- `Chuong2_Phan2_ATPM.pdf`: trang 4-27 alignment/layout; 32-58 static analysis; 70-71 demo.
- Giáo trình: trang PDF 31-51; phần mở rộng allocator, mitigation, format string, integer overflow, tree/hash và đọc ASan.
- Lab 3-4; `softsec-toolkit/ch2_memsafe`; `atpm_project/c/ch2_memory` và wrapper cppcheck.
