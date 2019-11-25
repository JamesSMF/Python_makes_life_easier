#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <inttypes.h>
#include <stdlib.h>

#define SIZE 8

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

void modified_matmul(volatile __uint64_t A[][SIZE], volatile __uint64_t B[][SIZE]){
   int rowA, colB, idx;

   for (rowA = 0; rowA < SIZE; rowA++) {
      for (colB = 0; colB < SIZE; colB++) {
         for (idx = 0; idx < SIZE; idx++) {
            D[rowA][colB] += A[rowA][idx] * B[colB][idx];
         }
      }
   }
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

int main(int argc, char **argv){
   clock_t t;
   double time_taken;

   init(A, B);
   memset((__uint64_t**)C, 0, sizeof(__uint64_t) * SIZE * SIZE);
   memset((__uint64_t**)D, 0, sizeof(__uint64_t) * SIZE * SIZE);

   matmul(A,B);

   printf("non-trans B: (0,0) = %" PRIu64 "\n", B[0][0]);
   // transpose B
   for (int c = 0; c < SIZE; ++c) {
      for (int r = c; r < SIZE; ++r) {
         // Trust me. This is gonna work.
         printf("original B[%d][%d] = %" PRIu64 "\n", c,r,B[c][r]);
         __uint64_t temp = B[r][c];
         B[r][c]         = B[c][r];
         B[c][r]         = temp;
         printf("B[%d][%d] = %" PRIu64 "\n", c,r,B[c][r]);
         /* B[r][c] = B[r][c]^B[c][r]; */
         /* B[c][r] = B[r][c]^B[c][r];      // B[c][r] = (B[r][c]^B[c][r])^B[c][r] = B[r][c]^0 = B[r][c] */
         /* B[r][c] = B[r][c]^B[c][r];      // B[r][c] = (B[r][c]^B[c][r])^B[r][c] = B[c][r]^0 = B[c][r] */
      }
   }

   t = clock();
   modified_matmul(A, B);
   t = clock() - t;
   time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
   verify(C,D);
   
   printf("Matmul took %f seconds to execute \n", time_taken);
   printf("without trans: (0,0) = %" PRIu64 "\n", C[0][0]);
   printf("with trans: (0,0) = %" PRIu64 "\n", D[0][0]);
   printf("Trans B: (0,0) = %" PRIu64 "\n", B[0][0]);
}
