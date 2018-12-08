/* --------------------------------------------------------------------------- */
/* IntegerLinkedList.c                                                         */
/* Header file for the IntegerLinkedList ADT                                   */
/* --------------------------------------------------------------------------- */

#ifndef _INTEGER_LINKEDLIST_H_INCLUDE_
#define _INTEGER_LINKEDLIST_H_INCLUDE_

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/* Link                     */
/* Exported reference type  */
typedef struct LinkObj* Link;

/* constructor for node */
Link* newLink(int dataitem);

/*  freeList()                        */
/* destructor for the LinkedList type */
void freeList(Link* first);

/* --------------------------------------------------------------------------- */
/* prototypes of ADT operations deleted to save space                          */
/* --------------------------------------------------------------------------- */

/* printLinkedList()                                                       */
/* prints a text representation of the list to the file pointed to by out  */
/* pre: none                                                               */
void printLinkedList(FILE* out, Link* first);

#endif