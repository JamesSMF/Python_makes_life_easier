#include <stdio.h>
#include <stdlib.h>

struct Student
{
    int id;
    char major;
    int year;
};


int main()
{
    int *foo;
    int i,len;

    len = 5;
    
    foo = (int *) malloc(len*sizeof(int));

    for (i=0;i<len;i++)
        *(foo+i) = i;

    for (i=0; i<len; i++)
        printf("%dth value in array foo: %d\n",i,foo[i]);

    free(foo);
    foo = NULL;
    foo = foo+1; 
    printf("Freed foo\n");


    //for (i=1; i<len; i++)
      //  printf("%dth value in array foo: %d\n",i,foo[i]);
}

