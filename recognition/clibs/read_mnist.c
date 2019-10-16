/* C function library used by python program. */
#include "read_mnist.h"

uint8_t* test (FILE *f){
    uint8_t *b;
    int i, j;
    fseek (f , 0 , SEEK_END);
    long fSize = ftell (f);
    rewind (f);

    printf("%ld", fSize);
   
    b = (uint8_t*) malloc (sizeof(uint8_t) * fSize);
    fread(b, 1, fSize, f);
    return b;
}
/* Functoton to read training and testing images from binary file .*/
uint8_t* img_data(FILE *f){
    uint8_t * buffer;
    
    fseek (f , 0 , SEEK_END);
    long fSize = ftell (f);
    rewind (f);
   
    buffer = (uint8_t*) malloc (sizeof(uint8_t)*fSize);
    fread (buffer,1,fSize,f);
    uint32_t items  = (buffer[4] << 24) + (buffer[5] << 16) + (buffer[6] << 8) + buffer[7];
    
    return buffer;
}
/*  Read training and testing labels file. */
uint8_t * label_data(FILE *f){
    uint8_t * buffer;
   
    fseek (f , 0 , SEEK_END);
    long fSize = ftell (f);
    rewind (f);
   
    buffer = (uint8_t*) malloc (sizeof(uint8_t)*fSize);
    fread (buffer,1,fSize,f);
   
    return buffer;
}

/* Process byte arrays of raw data and return array of 2d arrays for each image. */
uint8_t* process_bytes(uint8_t bytes[], int magic_number, long item_count ){
    int i,j , k = 0;
    int pos = 16;
    uint8_t (*matrix)[784] = malloc(sizeof(uint8_t[784]) * item_count);
    
    for(i = 0; i < item_count; i++){
        for(j = 0; j < 28*28; j++){
            matrix[i][j] = bytes[pos];
            pos++;
        }
    }
    return &matrix[0][0];
}