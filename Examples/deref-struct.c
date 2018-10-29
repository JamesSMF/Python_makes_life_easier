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

    int *ptr_foo, *ptr_bar;
    char *ptr_c;
    struct Student *ptr_s;

    foo = 42;
    bar = 7;
    c = 'a';

    s.id = 100;
    s.major = 'c';
    s.year = 2017;

    ptr_foo = &foo;
    ptr_bar = &bar;
    ptr_c = &c;
    ptr_s = &s;

    printf("At ptr_s, id: %d\n",(*ptr_s).id);
    printf("At ptr_s, major: %c\n",(*ptr_s).major);
    printf("At ptr_s, year: %d\n\n",(*ptr_s).year);

    printf("At ptr_s, id: %d\n",ptr_s->id);
    printf("At ptr_s, major: %c\n",ptr_s->major);
    printf("At ptr_s, year: %d\n",ptr_s->year);
}
