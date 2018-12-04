#include <stdio.h>

struct Student
{
    char major;
    int id;
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
    printf("Address of c: %u\n\n",&c);

    printf("Address of Student s: %u\n",&s);
    printf("Address of Student s.id: %u\n",&(s.id));
    printf("Address of Student s.major: %u\n",&(s.major));
    printf("Address of Student s.year: %u\n",&(s.year));
}

