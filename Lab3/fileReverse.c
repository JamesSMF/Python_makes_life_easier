#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char *stringReverse(char *str){ /* A char pointer refered to a strng */
    char temp, *front, *back;

   /* Make sure *str != '\0' and str is not null. */
   if(!str || !*str)
      return str;

   /* Swap the front and the back   (namely reverse) */
   for(front=str,back=str+strlen(str)-1;front < back;front++,back--){
      temp = *front;        /* Here * is used for dereference */
      *front = *back;
      *back = temp;
   }
    return str;
}

int main(int argc, char* argv[]){
   FILE* in;  /* file handle for input */  
   FILE* out; /* file handle for output */
   char word[256]; /* char array to store words from input file */

   /* check command line for correct number of arguments */
   if( argc != 3 ){
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
   if( out==NULL ){
      printf("Unable to write to file %s\n", argv[2]);
      exit(EXIT_FAILURE);
   }

   /* read words from input file, print on separate lines to output file*/
   while( fscanf(in, " %s", word) != EOF ){
      stringReverse(word);
      fprintf(out, "%s\n", word);
   }

   /* close input and output files */
   fclose(in);
   fclose(out);

   return(EXIT_SUCCESS);
}



