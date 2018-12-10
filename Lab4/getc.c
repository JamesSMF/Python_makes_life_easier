#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
   FILE* in;  /* file handle for input */
   FILE* out; /* file handle for output */

   in = fopen(argv[1], "r");
   out = fopen(argv[2], "w");
   char ch;

   while(ch != '\n'){
      ch = getc(in);
      putc(ch, out);
   }
}


