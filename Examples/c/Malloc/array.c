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
    printf("Address of foo[0]: %u\n",&(foo[0]));
}

