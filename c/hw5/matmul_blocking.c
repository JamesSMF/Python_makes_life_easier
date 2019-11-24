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
            printf("crash on entry %d, %d\n", r, c);
            return -1;
         }
         
      }
   }
   return 0;
}

void matmul(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]){
   int rowA, colB, idx;

   for (rowA = 0; rowA < SIZE; ++rowA) {
      for (colB = 0; colB < SIZE; ++colB) {
         for (idx = 0; idx < SIZE; ++idx) {
            C[rowA][colB] += A[rowA][idx] * B[idx][colB];
         }
      }
   }
}


// TODO: the result is not correct.

void blocking_mult(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]
      ,volatile __uint64_t C[][SIZE], int block_size){
   int gk=0, gj=0, k, j, i=0;
   __uint64_t sum=0;
   int number_block = SIZE / block_size;
   /* int number_block = block_size * (SIZE / block_size); */

   // gk, gj traverses through the matrix according to blocks
   // k, j traverses each block and calculate those motherfucking shitty god damn values
   // k stands for rows num in A and col num in B
   for(;gk<number_block; gk+=block_size){
      for(;gj<number_block; gj+=block_size){
         for(;i<SIZE; ++i){
            for(j=gj; j<gj+block_size; ++j){
               sum = C[i][j];
               for (k=gk; k<gk+block_size; ++k)
                  sum += A[i][k] * B[k][j];
               C[i][j] = sum;
            }
         }
      }
   }

   // I'm fucked up after writing this seemingly O(n^5) shitty algorithm.
}

int main(int argc, char **argv){
   clock_t t;
   double time_taken;

   init(A, B);
   memset((__uint64_t**)C, 0, sizeof(__uint64_t) * SIZE * SIZE);
   memset((__uint64_t**)D, 0, sizeof(__uint64_t) * SIZE * SIZE);
   
   t = clock();

   // change the size for block (namely the last arg) to test different cases.
   blocking_mult(A, B, D, 1024);
   t = clock() - t;
   time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

   matmul(A,B);
   verify(C,D);
   
   printf("Matmul took %f seconds to execute \n", time_taken);
}
