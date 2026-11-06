CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -O2
TARGET = c/access_simulator

.PHONY: all clean run-safe run-buggy run-fixed verify-python verify-all test pdf logs

all: $(TARGET)

$(TARGET): c/access_simulator.c
	$(CC) $(CFLAGS) -o $(TARGET) c/access_simulator.c

run-safe: $(TARGET)
	./$(TARGET) dataset/access_safe_states.csv dataset/access_safe_transitions.csv dataset/access_safe_init.txt insert_card auth_success door_closed_timeout

run-buggy: $(TARGET)
	./$(TARGET) dataset/access_buggy_states.csv dataset/access_buggy_transitions.csv dataset/access_buggy_init.txt insert_card timeout_glitch

run-fixed: $(TARGET)
	./$(TARGET) dataset/access_fixed_states.csv dataset/access_fixed_transitions.csv dataset/access_fixed_init.txt insert_card auth_success door_closed_timeout tamper_sensor operator_reset

verify-python:
	python python/kripke_model.py dataset/access_system_model.json
	python python/kripke_model.py dataset/access_system_model_BUGGY.json

verify-all:
	python python/kripke_model.py dataset/access_system_model.json
	python python/kripke_model.py dataset/access_system_model_BUGGY.json
	python python/kripke_model.py dataset/access_system_model_FIXED.json

test: $(TARGET)
	python tests/test_kripke.py

pdf:
	python generate_pdf.py

clean:
	rm -f $(TARGET) $(TARGET).exe BAO_CAO_LAB1.html
