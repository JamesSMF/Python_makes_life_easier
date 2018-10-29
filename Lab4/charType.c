#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
   FILE* in;  /* file handle for input */
   FILE* out; /* file handle for output */
   char ch;

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

   int alpha = 0;
   char al[256];
   int num = 0;
   char numeric[256];
   int punc = 0;
   char punctuation[256];
   int white = 0;
   char wh[256];

   int lineNum = 1;

   while(ch != EOF){
      if(ch != '\n'){    /* not newline */
         if(ch == 9 || ch == 32){
            wh[white ++] = ch;
         }else if(ch >= 48 && ch <= 57){
            numeric[num ++] = ch;
         }else if((ch >= 65 && ch <= 90) || (ch >= 97 && ch <= 122)){
            al[alpha ++] = ch;
         }else if((ch >= 33 && ch <= 47) || (ch >= 58 && ch <= 64) || (ch >= 91 && ch <= 96) ||
                  (ch >= 123 && ch <= 126)){
            punctuation[punc ++] = ch;
         }         /* end if-else */
      }else{           /* If newline */
         fprintf(out, "line %d contains:\n", lineNum++);

         if(alpha==1)
            fprintf(out, "%d alphabetic character: ", alpha);
         else
            fprintf(out, "%d alphabetic characters: ", alpha);
         for(int i=0; i<alpha; i++){
            fprintf(out, "%c", al[i]);
         }
         fprintf(out, "\n");

         if(num==1)
            fprintf(out, "%d numeric character: ", num);
         else
            fprintf(out, "%d numeric characters: ", num);
         for(int i=0; i<num; i++){
            fprintf(out, "%c", numeric[i]);
         }
         fprintf(out, "\n");

         if(punc==1)
            fprintf(out, "%d punctuation character: ", punc);
         else
            fprintf(out, "%d punctuation characters: ", punc);
         for(int i=0; i<punc; i++){
            fprintf(out, "%c", punctuation[i]);
         }
         fprintf(out, "\n");

         if(white==0)
            fprintf(out, "%d whitespace character: ", white+1);
         else
            fprintf(out, "%d whitespace characters: ", white+1);
         for(int i=0; i<white; i++){
            fprintf(out, "%c", wh[i]);
         }
         fprintf(out, "\n");
 
         /* initialize again to accept next line's input */
         alpha = 0;
         num = 0;
         punc = 0;
         white = 0;

         fprintf(out, "\n");
      }
      ch = getc(in);     /* get the next char */
   }

   /* close input and output files */
   fclose(in);
   fclose(out);
}



