#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<assert.h>

/* ------------------------------------------ */
/* Link                                       */
/* Generate a link with an int value and a    */
/* pointer to the next link                   */

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

void freeList(Link* first){     // destructor
   Link* toBeFree;

   while(toBeFree != NULL){      // while there are still some links left
      toBeFree = first -> next;   // After freeing, next would no longer exist. So temp stores next.
      first = toBeFree;           // go to the next unfreed link
      free(toBeFree);             // free the link
   }
}

void printLinkedList(FILE* out, Link* first){
   Link* cursor = first;
   while(cursor != NULL && cursor -> data != '\0'){
      fprintf(out, "%d ", cursor -> data);
      cursor = cursor -> next;
   }
   fprintf(out, "\n");
}


