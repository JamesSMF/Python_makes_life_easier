#include <stdio.h>

int main()
{
    int foo, bar;
    char c; 

    int *ptr_foo, *ptr_bar;
    char *ptr_c;

    foo = 42;
    bar = 7;
    c = 'a';
    
    ptr_foo = &foo;
    ptr_bar = &bar;
    ptr_c = &c;

    printf("ptr_foo = %u\n",ptr_foo);
    printf("ptr_bar = %u\n",ptr_bar);
    printf("ptr_c = %u\n\n",ptr_c);

    printf("At ptr_foo: %c\n",*ptr_foo);
    printf("At ptr_bar: %d\n",*ptr_bar);
    printf("At ptr_c: %c\n\n",*ptr_c);

    *ptr_foo = 100;
    printf("At ptr_foo: %d\n",*ptr_foo);

    printf("What is foo? %d\n",foo);

}

