#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<assert.h>

/* ------------------------------------------ */
/* Link                                       */
/* Generate a link with an int value.         */

typedef struct Link{
   int data;
   struct Link* next;     // point to the next link
} Link;

Link* newLink(int dataitem){          // constructor
   Link* theLink = (Link*) malloc(sizeof(Link));    // request a piece of memory
   theLink -> data = dataitem;     // initialize
   theLink -> next = NULL;
   return theLink;              // return the Link
}

/* ------------------------------------------ */
/* First Last List                            */
/* Basically a linked list, used for          */
/* implementation of queue.                   */

typedef struct LinkedList{
   Link* first;
   Link* last;
} LinkedList;

LinkedList* newList(void){        // constructor
   LinkedList* AList = (LinkedList*)malloc(2*sizeof(Link));
   AList -> first = NULL;
   AList -> last = NULL;
   return AList;
}

void freeList(LinkedList* toBeFree){     // destructor
   if(toBeFree -> first != NULL){        // the list is non-empty
      Link* current = toBeFree -> first;
      Link* temp = toBeFree -> first;
      while(current != NULL){      // while there are still some links left
         temp = current -> next;   // After freeing, next would no longer exist. So temp stores next.
         free(current);            // free the link
         current = NULL;
         current = temp;           // go to the next unfreed link
      }
      free(toBeFree);              // free the list
      toBeFree = NULL;
   }
}

void insert(int number, LinkedList S){    // Insert from the last
   Link new_link = *newLink(number);
   if(S.first == NULL){
      printf("NM$L\n");
      S.first = &new_link;
      printf("%d\n", S.first -> data);
   }
   else S.last -> next = &new_link;
   S.last = &new_link;
   printf("%d\n", S.first -> data);
}

void printLinkedList(FILE* out, LinkedList S){
   Link* cursor = S.first;         // error line
   while(cursor != NULL){
      fprintf(out, "%d ", (*cursor).data);
      cursor = cursor -> next;
   }
}

Link find(int number, LinkedList S){
   Link null = *newLink(-2.718281829);
   Link current = *(S.first);
   while(current.data != number){
      if(current.next == NULL) return null;
      current = *current.next;
   }
   return current;
}

int delete(LinkedList S){       // delete the first
   int temp = S.first -> data;      // store the value to be deleted
   if(S.first -> next != NULL) S.last = NULL;       // check for empty
   S.first = S.first -> next;
   return temp;
}

int main(int argc, char* argv[]){
   FILE* out;      // output file
   FILE* in;       // input file
   LinkedList* theQueue = newList();     // declare an empty list

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
            printLinkedList(out, *theQueue);
            break;

         case '\n':       // if it is a new line
            actualVal = atoi(numberArray);    // parse the string into actual number
            insert(actualVal, *theQueue);     // insert into the queue
            if(numberArray[0] != 'z')         // if there is some number to be pushed in
               fprintf(out, "enqueued %d\n", actualVal);   // print enqueue message
            memset(numberArray, '\0', sizeof(numberArray));    // set the number array to null
            i = 0;                            // set to 0 to accept new input
            break;

         default:      // for white spaces or other chars, just pass to the next char
            break;
      }
   }   // end while






/*
 *
 *    char line[32];              // the input would not be too long, so 32 might be enough
 *       while(fgets(line, 32, in) != NULL){       // get the input from next line
 *             char userInput = getc(in);        // initialize the user input char
 *                   printf("%c\n", userInput);
 *                         char theNumber[16];              // parse the number into string first
 *                               int insertNum = 0;           // initialize the number to be inserted
 *
 *                                     switch(userInput){
 *                                              case 'e':
 *                                                          getc(in);
 *                                                                      int i = 0;       // index for theNumber
 *                                                                                  char ch;
 *                                                                                              while(ch != '\n'){    // until the line hits the end
 *                                                                                                             ch = getc(in);            // goes to the next digit of the number
 *                                                                                                                            theNumber[i++] = ch;    // store one digit into the array
 *                                                                                                                                        }
 *                                                                                                                                                    insertNum = atoi(theNumber);      // parse the string into an int
 *                                                                                                                                                                insert(insertNum, *theQueue);      // insert the number into the queue
 *                                                                                                                                                                            fprintf(out, "enqueued %d\n", insertNum);
 *                                                                                                                                                                                        break;
 *
 *                                                                                                                                                                                                 case 'd':
 *                                                                                                                                                                                                             ;     // declarition is not a statement, so this empty statement is necessary
 *                                                                                                                                                                                                                         int deleted;
 *                                                                                                                                                                                                                                     deleted = delete(*theQueue);    // store the value deleted
 *                                                                                                                                                                                                                                                 fprintf(out, "%d\n", deleted);     // print in out in out file
 *                                                                                                                                                                                                                                                             break;
 *
 *                                                                                                                                                                                                                                                                      case 'p':
 *                                                                                                                                                                                                                                                                                  printLinkedList(out, *theQueue);
 *                                                                                                                                                                                                                                                                                              break;
 *
 *                                                                                                                                                                                                                                                                                                       default:              // other invalid chars or \n char
 *                                                                                                                                                                                                                                                                                                                   break;             // do nothing and goes to the next one
 *                                                                                                                                                                                                                                                                                                                         }
 *                                                                                                                                                                                                                                                                                                                            }      */
   freeList(theQueue);

   fclose(in);
   fclose(out);
}



