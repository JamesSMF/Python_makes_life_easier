#include <stdio.h>

int main()
{
    int foo, bar;
    char c; 

    int *ptr_foo, *ptr_bar;
    char *ptr_c;
    void *ptr_gen;

    foo = 42;
    bar = 7;
    c = 'a';

    ptr_foo = &foo;
    ptr_bar = &bar;
    ptr_c = c;

    ptr_gen = &foo;

    printf("ptr_foo = %u\n",ptr_foo);
    printf("ptr_gen = %u\n",ptr_gen);
    printf("ptr_bar = %u\n",ptr_bar);
    printf("ptr_c = %u\n\n",ptr_c);

    printf("bar before = %d\n",bar);
    bar = *(int *) ptr_gen;

    printf("bar after = %d\n",bar);

    ptr_c = ptr_foo;

    printf("At ptr_foo: %d\n",*ptr_foo);
    printf("At ptr_bar: %d\n",*ptr_bar);
    printf("At ptr_c: %d\n",*ptr_c);
}

