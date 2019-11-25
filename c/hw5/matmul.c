#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>

#define SIZE 1024

volatile __uint64_t A[SIZE][SIZE];
volatile __uint64_t B[SIZE][SIZE];
volatile __uint64_t C[SIZE][SIZE];
volatile __uint64_t D[SIZE][SIZE];
volatile __uint64_t E[SIZE][SIZE];

void init(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]){
   int r, c;

   for (c = 0; c < SIZE; c++) {
      for (r = 0; r < SIZE; r++) {
         A[r][c] = rand();
         B[r][c] = rand();
      }
   }
}

int verify(volatile __uint64_t C[][SIZE], volatile __uint64_t D[][SIZE]){
   int r, c;

   for (c = 0; c < SIZE; c++) {
      for (r = 0; r < SIZE; r++) {
         if (C[r][c] != D [r][c]) {
            printf("error!\n");
            return -1;
         }
         
      }
   }
   return 0;
}

void matmul(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]){
   int rowA, colB, idx;

   for (rowA = 0; rowA < SIZE; rowA++) {
      for (colB = 0; colB < SIZE; colB++) {
         for (idx = 0; idx < SIZE; idx++) {
            C[rowA][colB] += A[rowA][idx] * B[idx][colB];
         }
      }
   }
}

void modified_matmul(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]){
   int rowA, colB, idx;

   for (rowA = 0; rowA < SIZE; rowA++) {
      for (colB = 0; colB < SIZE; colB++) {
         for (idx = 0; idx < SIZE; idx++) {
            E[rowA][colB] += A[rowA][idx] * B[colB][idx];
         }
      }
   }
}

void blocking_mult(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]
      , int block_size){
   int gi, gk, gj, k, j, i;
   __uint64_t sum=0;
   int number_block = SIZE / block_size;

   // gi, gk, gj traverses through the matrix according to blocks
   // i, k, j traverses each block and calculate those motherfucking shitty god damn values
   for(gi=0; gi<SIZE; gi+=block_size)
      for(gj=0; gj<SIZE; gj+=block_size)
         for(gk=0; gk<SIZE; gk+=block_size)
            for(i=0 ; i<block_size; ++i)
               for(j=0 ; j<block_size; ++j)
                  for(k=0; k<block_size; ++k)
                     D[gi+i][gj+j] += A[gi+i][gk+k] * B[gk+k][gj+j];

   // I'm fucked up after writing this seemingly O(n^6) shitty algorithm.
}

int main(int argc, char **argv){
   clock_t t;
   double time_taken;

   init(A, B);
   memset((__uint64_t**)C, 0, sizeof(__uint64_t) * SIZE * SIZE);
   memset((__uint64_t**)D, 0, sizeof(__uint64_t) * SIZE * SIZE);
   memset((__uint64_t**)E, 0, sizeof(__uint64_t) * SIZE * SIZE);
   
   t = clock();
   matmul(A, B);     // the result is in C
   t = clock() - t;
   time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
   
   printf("Matmul took %f seconds to execute \n", time_taken);

   // BLOCKING --------------------------------------------------------
   t = clock();
   // change the size for block (namely the last arg) to test different cases.
   blocking_mult(A, B, 16);     // the result is in D
   t = clock() - t;
   time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

   printf("Matmul_blocking took %f seconds to execute \n", time_taken);

   // transpose B
   for (int c = 0; c < SIZE; ++c) {
      for (int r = c; r < SIZE; ++r) {
         // Trust me. This is gonna work.
         if(r==c) continue;
         B[r][c] = B[r][c]^B[c][r];
         B[c][r] = B[r][c]^B[c][r];      // B[c][r] = (B[r][c]^B[c][r])^B[c][r] = B[r][c]^0 = B[r][c]
         B[r][c] = B[r][c]^B[c][r];      // B[r][c] = (B[r][c]^B[c][r])^B[r][c] = B[c][r]^0 = B[c][r]
      }
   }
   
   // TRANSPOSE -------------------------------------------------------
   t = clock();
   modified_matmul(A, B);       // the result is in E
   t = clock() - t;
   time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

   printf("Matmul_transpose took %f seconds to execute \n", time_taken);
}
