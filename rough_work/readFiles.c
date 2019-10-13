 #include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/* C program to read MNIST byte files */

int main()
{
  FILE *pFile;
  long lSize;
  uint8_t *buffer;
  
  pFile = fopen("t10k-images.idx3-ubyte", "rb");
  // Get file size
  fseek(pFile, 0, SEEK_END);
  lSize = ftell(pFile);
  rewind(pFile);

  buffer = (uint8_t *)malloc(sizeof(uint8_t) * lSize);

  fread(buffer, 1, lSize, pFile);
  
  printf("Header\n");
  
  // convert first 8 bytes to magic number and items count
  // big endian
  uint32_t magicNumber = (buffer[0] << 24) + (buffer[1] << 16) + (buffer[2] << 8) + buffer[3];
  uint32_t numberOfItems = (buffer[4] << 24) + (buffer[5] << 16) + (buffer[6] << 8) + buffer[7];
  
  printf("%d  %d", magicNumber, numberOfItems);

  fclose(pFile);
  free(buffer);
  return 0;
}
