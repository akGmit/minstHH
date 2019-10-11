/* fread example: read an entire file */
#include <stdio.h>
#include <stdlib.h>

int main () {
  FILE * pFile;
  long lSize;
  char * buffer;
  
  size_t result;

  pFile = fopen ( "train-images.idx3-ubyte" , "rb" );
  if (pFile==NULL) {fputs ("File error",stderr); exit (1);}

  // obtain file size:
  fseek (pFile , 0 , SEEK_END);
  lSize = ftell (pFile);
  rewind (pFile);

  // allocate memory to contain the whole file:
  buffer = (char*) malloc (sizeof(char)*lSize);
  if (buffer == NULL) {fputs ("Memory error",stderr); exit (2);}

  // copy the file into the buffer:
  result = fread (buffer,1,lSize,pFile);
  if (result != lSize) {fputs ("Reading error",stderr); exit (3);}
  
  /* the whole file is now loaded in the memory buffer. */
  char  * processedBuffer;
  processedBuffer = (char*)malloc(sizeof(char)*lSize/4);
  
  
  printf("Buffer %d", buffer[20]);
  
//   for(int i = 16; i < lSize - 1; i++){
//       unsigned int x = bufferp[]
//       //*(processedBuffer + i) = buffer[pos] + buffer[pos+1] + buffer[pos +2]  + buffer[pos + 3];
//       //printf("%d", x);
//       pos = pos + 4;
//   }
  printf("\n%ld", lSize);
  printf("\n%ld", result);
  
  // terminate
  fclose (pFile);
  free (buffer);
  return 0;
}