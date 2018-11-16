#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char* argv[]){
   char ch;
   int i, j, count;

   if( argc>1 )
   {
      for(i=1; i<argc; i++){
         ch = argv[i][0];
         count = j = 0;  
         while( ch!='\0' ){
            if( isalnum((int)ch) ) 
               count++;
            ch = argv[i][++j];
         }
         printf("%s contains %d alphanumeric and ", argv[i], count);
         printf("%d non-alphanumeric characters\n", strlen(argv[i])-count);
      }
   }   
   return EXIT_SUCCESS;
}
