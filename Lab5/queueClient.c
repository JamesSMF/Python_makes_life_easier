#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "queue.h"

int main(int argc, char* argv[]){
   FILE* out;      // output file
   FILE* in;       // input file
   Link* head = NULL;     // the head of the list
   Link* tail = NULL;     // the tail of the list

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

   char ch;
   char numberArray[10];
   int i = 0;            // index of the number array
   int actualVal;        // the actual value to be pushed into the queue
   while(ch != EOF){       // traverse the whole input file
      ch = getc(in);       // get the next char
      switch(ch){
         case '0':
         case '1':
         case '2':
         case '3':
         case '4':
         case '5':
         case '6':
         case '7':
         case '8':
         case '9':
            numberArray[i++] = ch;        // push into the number array
            break;

         case 'p':       // if it is 'p'
            numberArray[0] = 'z';
            printLinkedList(out, head);
            break;

         case 'd':
            ;
            int deletedNum = -10000; // just in case, set it to -10000 instead of -1
            Link* tempLink = NULL;  // a null link used to store the new "first" link temporarily
            numberArray[0] = 'z';

            if(head == NULL || tail == NULL){
               fprintf(out, "empty\n");
               break;
            }

            tempLink = head -> next;       // store the next link
            deletedNum = head -> data;           // store the data to be deleted
            if(tempLink == NULL) tail = NULL;       // check for empty
            free(head);                      // free the current first pointer
            head = tempLink;                 // shift first to the next

            fprintf(out, "%d\n", deletedNum);
            break;

         case '\n':       // if it is a new line
            if(numberArray[0] != 'z'){         // if there is some number to be pushed in
               actualVal = atoi(numberArray);    // parse the string into actual number

            /* This is the insertion method. To avoid segfault, I wrote it directly here */
               Link* new_link = newLink(actualVal);                 // create a new link
               if(head == NULL){             // if empty
                  head = new_link;           // set first to the new link
               }
               else tail -> next = new_link;
               tail = new_link;
            /* To this point, the link has been inserted into the list.                  */

               fprintf(out, "enqueued %d\n", actualVal);   // print enqueue message
            }
            memset(numberArray, '\0', sizeof(numberArray));    // set the number array to null
            i = 0;                            // set to 0 to accept new input
            break;

         default:      // for white spaces or other chars, just pass to the next char
            memset(numberArray, '\0', sizeof(numberArray));    // set the number array to null
            i = 0;
            numberArray[0] = 'z';
            break;
      }
   }   // end while
   if(head != NULL)
      freeList(head);

   fclose(in);
   fclose(out);
}
