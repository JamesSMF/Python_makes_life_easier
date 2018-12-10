#include <stdio.h>

struct Student
{
    int id;
    char major;
    int year;
};


int main()
{
    int foo, bar;
    char c; 
    struct Student s;

    foo = 42;
    bar = 7;
    c = 'a';

    printf("Address of foo: %u\n",&foo);
    printf("Address of bar: %u\n",&bar);
    printf("Address of c: %u\n",&c);
    printf("Address of Student s: %u\n",&s);
}

