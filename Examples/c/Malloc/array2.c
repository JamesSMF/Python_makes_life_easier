#include <stdio.h>

struct Student
{
    int id;
    char major;
    int year;
};


int main()
{
    int foo[4];

    foo[0] = 42;
    foo[1] = 7;
    foo[2] = 10;
    foo[3] = 1;

    printf("Value of foo: %u\n",foo);
    printf("Value of foo+1: %u\n",foo+1);
    printf("Location of foo: %u\n",&foo);

    printf("What's at foo? %d\n",*foo);
    printf("What's at foo+1? %d\n",*(foo+1));
    printf("What's at foo+2? %d\n",*(foo+2));
    printf("What's at foo+3? %d\n\n",*(foo+3));

    if (foo+2 == &(foo[2]))
        printf("They're the same!\n");

}

