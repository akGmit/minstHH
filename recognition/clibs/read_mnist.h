#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

uint8_t * img_data(FILE* f);
uint8_t * label_data(FILE* f);
uint8_t* process_bytes(uint8_t bytes[], int magic_number, long item_count);