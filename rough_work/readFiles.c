#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "read_mnist.h"
/* C program to read MNIST byte files */

int main()
{

  uint8_t *m = img_data("train-images.idx3-ubyte");
  for(int i = 0; i < 30000; i++){
    printf("%d", m[i]);
  }
  // FILE *pFile;
  // long lSize;
  // uint8_t *buffer;
  
  // pFile = fopen("train-images.idx3-ubyte", "rb");
  // //pFile = fopen("t10k-labels.idx1-ubyte", "rb");
  
  // // Get file size in bytes
  // fseek(pFile, 0, SEEK_END);
  // lSize = ftell(pFile);
  // rewind(pFile);

  // buffer = (uint8_t *)malloc(sizeof(uint8_t) * lSize);
  // // read the whole file to buffer for later processing
  // fread(buffer, 1, lSize, pFile);
  
  // printf("Header\n");
  
  // // convert first 8 bytes to magic number and items count
  // // big endian
  // uint32_t magicNumber = (buffer[0] << 24) + (buffer[1] << 16) + (buffer[2] << 8) + buffer[3];
  // uint32_t num_images  = (buffer[4] << 24) + (buffer[5] << 16) + (buffer[6] << 8) + buffer[7];
  
  // // declare arrays for images and labels
  // uint8_t img_arr[num_images][28][28];
  // uint8_t img_labels[num_images];
  
  // // if label
  // if(magicNumber == 2049){
  //   int pos = 8;
  //   for(int i = 0; i < num_images; i++){
  //       img_labels[pos] = buffer[pos];     
  //       printf("%d ", img_labels[pos]);
  //       pos++;
  //   }
  // }
  // //if image 
  // if(magicNumber == 2051){
  //   int pos = 16;
  //   for(int i = 0;i < num_images; i++){
  //     for(int j = 0; j < 28; j++){
  //       for(int k = 0; k < 28; k++){
  //         img_arr[i][j][k] = buffer[pos];
  //         printf("%s", img_arr[i][j][k] > 128 ? "0" : "~");
  //         pos++;
  //       }
  //       printf("\n");
  //     }
  //   }
  // }

  // fclose(pFile);
  // free(buffer);
  return 0;
}
