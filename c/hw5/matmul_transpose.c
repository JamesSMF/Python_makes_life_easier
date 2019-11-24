#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>

#define SIZE 1024

volatile __uint64_t A[SIZE][SIZE];
volatile __uint64_t B[SIZE][SIZE];
volatile __uint64_t C[SIZE][SIZE];

void init(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]){
   int r, c;

   for (c = 0; c < SIZE; ++c) {
      for (r = 0; r < SIZE; ++r) {
         A[r][c] = rand();
         B[r][c] = rand();
      }
   }
}

int verify(volatile __uint64_t C[][SIZE], volatile __uint64_t D[][SIZE]){
   int r, c;

   for (c = 0; c < SIZE; ++c) {
      for (r = 0; r < SIZE; ++r) {
         if (C[r][c] != D [r][c]) {
            printf("error!\n");
            return -1;
         }
         
      }
   }
   return 0;
}

////////////// Added /////////////////
//////////////////////////////////////

__uint64_t swap(__uint64_t a, __uint64_t b){
   return a;
}

void transpose(volatile __uint64_t A[][SIZE]){
   int r, c;

   for (c = 0; c < SIZE; ++c) {
      for (r = 0; r < SIZE; ++r) {
         // Trust me. This is gonna work.
         A[r][c] = swap(A[c][r], A[r][c]=A[c][r]);
      }
   }
}

////////////// Added /////////////////
//////////////////////////////////////

void modified_matmul(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]){
   int rowA, colB, idx;

   for (rowA = 0; rowA < SIZE; rowA++) {
      for (colB = 0; colB < SIZE; colB++) {
         for (idx = 0; idx < SIZE; idx++) {
            C[rowA][colB] += A[rowA][idx] * B[rowA][idx];
         }
      }
   }
}

int main(int argc, char **argv){
   clock_t t;
   double time_taken;

   init(A, B);
   memset((__uint64_t**)C, 0, sizeof(__uint64_t) * SIZE * SIZE);
   
   transpose(B);
   t = clock();
   modified_matmul(A, B);
   t = clock() - t;
   time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
   
   printf("Matmul took %f seconds to execute \n", time_taken);
}