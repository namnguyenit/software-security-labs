#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pin_validator.c"

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <pin> <failed_attempts> OR %s --batch <pin1> <failed1> ...\n", argv[0], argv[0]);
        return 99;
    }

    if (strcmp(argv[1], "--batch") == 0) {
        for (int i = 2; i + 1 < argc; i += 2) {
            const char *pin = (strcmp(argv[i], "NULL") == 0) ? NULL :
                              (strcmp(argv[i], "EMPTYSTR") == 0) ? "" : argv[i];
            int failed = atoi(argv[i + 1]);
            PinResult r = validate_pin(pin, failed);
            printf("%d\n", (int)r);
        }
        return 0;
    }

    const char *pin = (strcmp(argv[1], "NULL") == 0) ? NULL :
                      (strcmp(argv[1], "EMPTYSTR") == 0) ? "" : argv[1];
    int failed = atoi(argv[2]);
    PinResult r = validate_pin(pin, failed);
    printf("%d\n", (int)r);
    return 0;
}
