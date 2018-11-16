#include <stdio.h>

int main()
{
    int foo, bar;
    char c; 
    int qwe;

    foo = 42;
    bar = 7;
    c = 'a';
    qwe = 100;

    printf("Address of foo: %u\n",&foo);
    printf("Address of bar: %u\n",&bar);
    printf("Address of c: %u\n",&c);
    printf("Address of qwe: %u\n",&qwe);
}

