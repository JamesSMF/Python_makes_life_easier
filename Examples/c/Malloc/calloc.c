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
    
    printf("Value of foo: %u\n",foo);

    foo = NULL;                       // this only changes the address of foo
    printf("Value of foo: %u\n",foo);
    
    foo = (int *) calloc(len,sizeof(int));    // this also returns an adress

    printf("Value of foo: %u\n",foo);

    for (i=0; i<len; i++)              // this is the actual values of foo array
        printf("%dth value in array foo: %d\n",i,foo[i]);

    printf("\n\n");
    for (i=0; i<len; i++)              // this is also actual values of foo
        printf("%dth value in array foo: %d\n",i,*(foo+i));


}

