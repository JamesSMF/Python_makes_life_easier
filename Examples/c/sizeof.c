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

    struct Student *ptr_s;

    foo = 42;
    bar = 7;
    c = 'a';

    printf("Address of foo: %u\n",&foo);
    printf("Address of bar: %u\n",&bar);
    printf("Address of c: %u\n",&c);
//     printf("Address of Student s: %u\n\n",&s);

    printf("Size of int: %lu\n",sizeof(int));
    printf("Size of char: %lu\n",sizeof(char));
    printf("Size of Student: %lu\n\n",sizeof(struct Student));
    printf("Size of ptr: %lu\n",sizeof(s));
}
