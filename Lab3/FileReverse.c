#include<stdio.h>
#include<stdlib.h>

char theStack[30];
int top = -1;

int main(int argc, char* argv[]){
	FILE* in;
	FILE* out;

   if( argc != 3 ){         /* check the number of input files */
      printf("Usage: %s <input file> <output file>\n", argv[0]);
      exit(EXIT_FAILURE);
   }

   /* open input file for reading */
   in = fopen(argv[1], "r");
   if( in==NULL ){
      printf("Unable to read from file %s\n", argv[1]);
      exit(EXIT_FAILURE);
   }

   /* open output file for writing */
   out = fopen(argv[2], "w");
   if( out==NULL )
      printf("Unable to write to file %s\n", argv[2]);

   /* read words from input file, print on separate lines to output file */
   while( fscanf(in, " %s", theStack) != EOF ){
      fprintf(out, "%s\n", theStack);
   }

   fclose(in);
   fclose(out);

   return(EXIT_SUCCESS);
}

void push(char ch){
	top = top + 1;
	theStack[top] = ch;
}




