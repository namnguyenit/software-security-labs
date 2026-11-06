/*
 * Lab 8 - Fuzz Target (module Order Processing - kenh lenh quan tri an - ADMIN debug channel)
 * ================================================================================================
 * Chuong 4: 4.5 Kiem thu hop den (black-box fuzzing), 4.6 Kiem thu hop trang (white-box fuzzing)
 *
 * Kich ban: mot lap trinh vien de lai mot "kenh lenh go loi" (debug backdoor)
 * trong bo phan tich cu phap don hang: neu dong dau vao bat dau bang tien
 * to "ADMIN:", phan con lai duoc sao chep vao mot bo dem CO DINH bang
 * strcpy() KHONG kiem tra do dai - day la mot loi CWE-121 kinh dien, NHUNG
 * rat KHO tim bang fuzzing thuan random vi dieu kien kich hoat ("ADMIN:")
 * la mot chuoi cu the 6 ky tu - xac suat mot chuoi ngau nhien khop chinh
 * xac 6 ky tu dau la (1/256)^6, thuc te KHONG BAO GIO xay ra trong so lan
 * thu hop ly. Day chinh la ly do fuzzing HOP TRANG (dan dat boi coverage)
 * hieu qua hon nhieu so voi fuzzing HOP DEN thuan tuy trong truong hop nay.
 *
 * Bien dich:
 *   gcc -g -fsanitize=address --coverage -o fuzz_target fuzz_target.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CMD_BUF_SIZE 16

#ifndef __SANITIZE_ADDRESS__
/*
 * Emulation bao cao AddressSanitizer khi bien dich tren moi truong MinGW Windows
 * (noi GCC khong co san libasan). Tren Linux / moi truong co san ASan that,
 * GCC tu dong dinh nghia __SANITIZE_ADDRESS__ va ASan that se bat loi tu dong.
 */
static void asan_report_overflow(const char *func, int line, size_t size) {
    fprintf(stderr, "=================================================================\n");
    fprintf(stderr, "==8888==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x0028fe28\n");
    fprintf(stderr, "WRITE of size %lu at 0x0028fe28 thread T0 (payload >= %d bytes)\n", (unsigned long)size, CMD_BUF_SIZE);
    fprintf(stderr, "    #0 0x00401520 in %s fuzz_target.c:%d\n", func, line);
    fprintf(stderr, "    #1 0x00401760 in main fuzz_target.c:65\n");
    fprintf(stderr, "SUMMARY: AddressSanitizer: stack-buffer-overflow fuzz_target.c:%d in %s\n", line, func);
    exit(1);
}
#endif

void process_input(const char *line) {
    char cmd[CMD_BUF_SIZE];

    if (strncmp(line, "ADMIN:", 6) == 0) {
        /* Nhanh nay CHI duoc thuc thi khi 6 ky tu dau khop chinh xac
         * "ADMIN:" - day la nhanh "sau" ma fuzzer hop den kho tiep can. */
        const char *payload = line + 6;
        if (payload[0] == 'X') {
            /* Nhanh con thu 2, sau hon nua: payload phai bat dau bang 'X'. */
#ifndef __SANITIZE_ADDRESS__
            if (strlen(payload) >= CMD_BUF_SIZE) {
                asan_report_overflow("process_input", 46, strlen(payload));
            }
#endif
            strcpy(cmd, payload);   /* !!! CWE-121: tran neu strlen(payload) >= CMD_BUF_SIZE !!! */
            printf("  [ADMIN-X] lenh quan tri: %s\n", cmd);
        } else {
            snprintf(cmd, CMD_BUF_SIZE, "%s", payload);
            printf("  [ADMIN] lenh quan tri (an toan, cat bot): %s\n", cmd);
        }
    } else if (strncmp(line, "ORDER:", 6) == 0) {
        printf("  [ORDER] xu ly don hang binh thuong: %s\n", line + 6);
    } else {
        printf("  [UNKNOWN] dinh dang dau vao khong nhan dien: %s\n", line);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Cach dung: %s <input_string>\n", argv[0]);
        return 1;
    }
    process_input(argv[1]);
    return 0;
}
