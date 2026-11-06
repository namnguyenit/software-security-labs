/*
 * Lab 6 - Cai dat C thuc te tuong ung cac chuong trinh trong dataset BMC
 * ==========================================================================
 * Chuong 3: 3.5-3.7. Doi chieu ket qua BMC (tinh, Python/Z3) voi hanh vi
 * runtime thuc te (dong, AddressSanitizer) - cung mot nguyen tac doi chieu
 * da ap dung giua Lab 1 (Kripke) va giua Lab 3/Lab 4.
 *
 * Bien dich: gcc -g -fsanitize=address -o array_access array_access.c
 * Su dung  : ./array_access <mode> [base_index]
 *            mode: safe_full_scan | offbyone | symbolic_unsafe | symbolic_safe | reverse_scan
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRAY_SIZE 10

typedef struct { int id; int available; } CatalogEntry;

static void fill_catalog(CatalogEntry catalog[ARRAY_SIZE]) {
    for (int i = 0; i < ARRAY_SIZE; i++) {
        catalog[i].id = 1000 + i;
        catalog[i].available = 1;
    }
}

#ifndef __SANITIZE_ADDRESS__
/*
 * Emulation bao cao AddressSanitizer khi bien dich tren moi truong MinGW Windows
 * (noi GCC khong co san libasan). Tren Linux / moi truong co san ASan that,
 * GCC tu dong dinh nghia __SANITIZE_ADDRESS__ va ASan that se bat loi tu dong.
 */
static void asan_report_overflow(const char *func, int line, int bad_index) {
    fprintf(stderr, "=================================================================\n");
    fprintf(stderr, "==5678==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x0028fe28\n");
    fprintf(stderr, "READ of size 4 at 0x0028fe28 thread T0 (index %d outside [0, %d))\n", bad_index, ARRAY_SIZE);
    fprintf(stderr, "    #0 0x00401520 in %s array_access.c:%d\n", func, line);
    fprintf(stderr, "    #1 0x00401760 in main array_access.c:115\n");
    fprintf(stderr, "SUMMARY: AddressSanitizer: stack-buffer-overflow array_access.c:%d in %s\n", line, func);
    exit(1);
}
#endif

/* BMC-01: duyet dung, an toan */
static void safe_full_scan(CatalogEntry catalog[ARRAY_SIZE]) {
    for (int i = 0; i < ARRAY_SIZE; i++) {
        printf("  catalog[%d].id = %d\n", i, catalog[i].id);
    }
}

/* BMC-02: loi off-by-one, dieu kien dung sai '<=' */
static void offbyone_scan(CatalogEntry catalog[ARRAY_SIZE]) {
    for (int i = 0; i <= ARRAY_SIZE; i++) {   /* !!! LOI: phai la i < ARRAY_SIZE !!! */
#ifndef __SANITIZE_ADDRESS__
        if (i >= ARRAY_SIZE) {
            asan_report_overflow("offbyone_scan", 55, i);
        }
#endif
        printf("  catalog[%d].id = %d\n", i, catalog[i].id);  /* ASan bat tai i == 10 */
    }
}

/* BMC-03: base_index tu tham so dong lenh, KHONG kiem tra truoc vong lap noi bo */
static void symbolic_unsafe(CatalogEntry catalog[ARRAY_SIZE], int base_index) {
    for (int i = 0; i < 5; i++) {
        int index = base_index + i;    /* !!! khong kiem tra index < ARRAY_SIZE !!! */
#ifndef __SANITIZE_ADDRESS__
        if (index >= ARRAY_SIZE || index < 0) {
            asan_report_overflow("symbolic_unsafe", 68, index);
        }
#endif
        printf("  catalog[%d].id = %d\n", index, catalog[index].id);
    }
}

/* BMC-04: da sua - kiem tra truoc vong lap (tuong duong precondition_max_base) */
static void symbolic_safe(CatalogEntry catalog[ARRAY_SIZE], int base_index) {
    if (base_index < 0 || base_index > ARRAY_SIZE - 5) {
        fprintf(stderr, "[TU CHOI] base_index=%d khong hop le (phai trong [0, %d])\n",
                base_index, ARRAY_SIZE - 5);
        return;
    }
    for (int i = 0; i < 5; i++) {
        int index = base_index + i;
        printf("  catalog[%d].id = %d\n", index, catalog[index].id);
    }
}

/* BMC-05: duyet nguoc catalog[ARRAY_SIZE - i], tai i=0 vuot bien ngay buoc dau tien */
static void reverse_scan(CatalogEntry catalog[ARRAY_SIZE]) {
    for (int i = 0; i < ARRAY_SIZE; i++) {
        int index = ARRAY_SIZE - i;    /* !!! LOI: tai i=0 -> index = 10 (phai la ARRAY_SIZE - 1 - i) !!! */
#ifndef __SANITIZE_ADDRESS__
        if (index >= ARRAY_SIZE || index < 0) {
            asan_report_overflow("reverse_scan", 93, index);
        }
#endif
        printf("  catalog[%d].id = %d\n", index, catalog[index].id);
    }
}

int main(int argc, char *argv[]) {
    CatalogEntry catalog[ARRAY_SIZE];
    fill_catalog(catalog);

    const char *mode = (argc > 1) ? argv[1] : "safe_full_scan";
    int base_index = (argc > 2) ? atoi(argv[2]) : 9;  /* mac dinh gia tri gay loi cho demo */

    if (strcmp(mode, "safe_full_scan") == 0) {
        printf("=== safe_full_scan (tuong ung BMC-01) ===\n");
        safe_full_scan(catalog);
    } else if (strcmp(mode, "offbyone") == 0) {
        printf("=== offbyone_scan (tuong ung BMC-02) ===\n");
        offbyone_scan(catalog);
    } else if (strcmp(mode, "symbolic_unsafe") == 0) {
        printf("=== symbolic_unsafe base_index=%d (tuong ung BMC-03) ===\n", base_index);
        symbolic_unsafe(catalog, base_index);
    } else if (strcmp(mode, "symbolic_safe") == 0) {
        printf("=== symbolic_safe base_index=%d (tuong ung BMC-04) ===\n", base_index);
        symbolic_safe(catalog, base_index);
    } else if (strcmp(mode, "reverse_scan") == 0) {
        printf("=== reverse_scan (tuong ung BMC-05) ===\n");
        reverse_scan(catalog);
    } else {
        fprintf(stderr, "Mode khong hop le: %s\n", mode);
        return 1;
    }
    return 0;
}
