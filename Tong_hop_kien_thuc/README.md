# Bộ kiến thức An toàn phần mềm — tổng hợp toàn thư mục

**Nguồn:** thư mục `Safe Application`, kiểm kê ngày 09/10/2026. Đã đọc/phân loại 222 file gốc, trích xuất 25 PDF với 1.095 trang, phân tích 84 file mã C/Python/header, dữ liệu JSON/CSV, hai Word, mẫu Excel 10 sheet và 13 ZIP. Hai EXE được kiểm tra metadata/hash; chưa có source để kiểm toán nội bộ.

**Bắt đầu đọc:** [Bản phân tích toàn diện học phần](BAN_PHAN_TICH_TOAN_DIEN_ATPM.md) hoặc [Bản tổng hợp liền mạch chi tiết](TOAN_BO_KIEN_THUC.md). Bản này chứa toàn bộ hệ thống hóa lý thuyết 4 chương, giải phẫu 8 bài lab, phân tích spec/mô hình và cẩm nang bài tập có lời giải. Toàn bộ 1.257 câu hỏi nằm trong 4 file riêng để tài liệu chính dễ học và tra cứu.

## Mục lục theo chương

| Phần | Tài liệu | Nội dung |
| --- | --- | --- |
| 0 | [Chương 0. Tổng quan học phần và cách sử dụng tài liệu](00_Tong_quan_va_cach_hoc.md) | Phạm vi, cấu trúc học phần, cách học và bằng chứng xác minh. |
| 1 | [Chương 1. Nền tảng an toàn phần mềm](01_Nen_tang_an_toan_phan_mem.md) | CIA/AAA, threat/risk, kiểm soát truy cập, kiểm thử, coverage, Kripke và CTL/LTL. |
| 2 | [Chương 2. Lập trình C an toàn và quản lý bộ nhớ](02_Lap_trinh_C_an_toan.md) | Lifetime, ownership, chuỗi, số học, cấu trúc động, alignment/padding và sanitizer. |
| 3 | [Chương 3. Phân tích tĩnh, SAT/SMT và kiểm chứng hình thức](03_Phan_tich_tinh_va_kiem_chung.md) | Phân tích tĩnh, xấp xỉ, SAT/SMT, Z3, BMC, induction và memory model. |
| 4 | [Chương 4. Phân tích động, coverage và fuzzing](04_Phan_tich_dong_va_fuzzing.md) | Harness, oracle, coverage, tracing, mutation, concolic, fuzzing và triage. |
| 5 | [Chương 5. Phân tích và hướng dẫn hiểu 8 bài lab](05_Phan_tich_8_bai_lab.md) | Phân tích từng lab 1-8, code, dataset, kết quả và giới hạn. |
| 6 | [Chương 6. Đặc tả, mô hình JSON/Excel và bài tập lớn](06_Dac_ta_mo_hinh_va_du_an.md) | 10 sheet Excel, 7 spec JSON, 15 mô hình, IoT gateway, BTL và báo cáo. |
| 7 | [Chương 7. Hệ thống ôn tập, bài tập có lời giải và thuật ngữ](07_On_tap_va_bai_tap_co_loi_giai.md) | 18 bài có lời giải, công thức, bảng so sánh, cách ôn và thuật ngữ Anh-Việt. |
| 8 | [Chương 8. Đính chính, khác biệt giữa nguồn và giới hạn kết luận](08_Dinh_chinh_va_gioi_han.md) | Những điểm sai/thiếu điều kiện trong nguồn; phạm vi kết luận và test đã chạy. |
| 9 | [Chương 9. Bản đồ toàn bộ mã nguồn và dữ liệu liên quan](09_Ban_do_ma_nguon.md) | Từng 84 file source, API/dòng, dữ liệu và 22 mô hình chính/29 flow. |
| 10 | [Chương 10. Danh mục toàn bộ nguồn và khả năng truy vết](10_Danh_muc_nguon.md) | Từng 222 file, SHA-256, PDF, trùng nội dung, EXE và 186 thành viên ZIP. |
| 11 | [Chương 11. Ngân hàng câu hỏi gốc theo từng chương](11_Ngan_hang_cau_hoi.md) | Mục lục và cách sử dụng toàn bộ 1.257 câu hỏi gốc. |

## Ngân hàng câu hỏi

| File | Số câu |
| --- | ---: |
| [Chương1](cau_hoi/Chuong_1.md) | 267 |
| [Chương2](cau_hoi/Chuong_2.md) | 270 |
| [Chương3](cau_hoi/Chuong_3.md) | 360 |
| [Chương4](cau_hoi/Chuong_4.md) | 360 |
| **Tổng** | **1.257** |

Các câu hỏi, phương án, đáp án/giải thích và tóm tắt được bảo toàn theo dữ liệu HTML. Đáp án được ghi là đáp án gốc; chưa thẩm định từng câu riêng biệt. Phần đính chính giúp nhận ra các lỗi hoặc giả thiết thiếu quan trọng.

## Tra cứu PDF gốc

[Chỉ mục toàn bộ trang PDF](CHI_MUC_PDF_THEO_TRANG.md) ghi thứ tự trang và nội dung đầu trang. Danh mục nguồn có liên kết trở về từng file gốc. Các đường dẫn tương đối hoạt động khi giữ bộ tài liệu trong thư mục này; nếu chuyển sang máy khác, giữ cấu trúc thư mục nguồn để liên kết vẫn có nghĩa.

## Mức xác minh

Đã chạy có chọn lọc các ví dụ Python/Z3 và test có sẵn: 19 đạt, 5 skip do thiếu CBMC, 7 test gọi C loại khỏi lượt Python. Có đối chiếu mô hình bằng duyệt đồ thị và kiểm tra ảnh PDF đại diện. Kết quả ASan/cppcheck/CBMC/fuzzing C lưu sẵn được ghi rõ là kết quả nguồn; chưa chạy lại toàn bộ.

Không sửa 222 file ban đầu. Những điểm cần đính chính được nêu trong tài liệu mới, có căn cứ code/công thức và nguồn chính thức khi cần.

Bộ tài liệu dùng tiếng Việt, giữ thuật ngữ và API gốc để bạn đối chiếu khi thực hành. Bốn chương1-4 là mạch lý thuyết của học phần; các phần 5-11 là thực hành và phụ lục học tập, không làm thay đổi cấu trúc môn học.
