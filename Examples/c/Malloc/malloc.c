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
    int len;

    len = 10;
    
    printf("Value of foo: %u\n",foo);

    foo = NULL;
    printf("Value of foo: %u\n",foo);
    
    foo = (int *) malloc(len*sizeof(int));

    printf("Value of foo: %u\n",foo);
}

