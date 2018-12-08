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

    s.id = 100;
    s.major = 'c';
    s.year = 2017;

    ptr_s = &s;
    ptr_foo = ptr_s;

    printf("BEFORE: At ptr_s, id: %d\n",ptr_s->id);

    *ptr_foo = 101;

    printf("ptr_s: %u\n",ptr_s);
    printf("location of s.id: %u\n\n",&(s.id));

    printf("At ptr_foo: %d\n\n",*ptr_foo);
    printf("AFTER: At ptr_s, id: %d\n",ptr_s->id);



    printf("At ptr_s, major: %c\n",(*ptr_s).major);
    printf("At ptr_s, year: %d\n\n",(*ptr_s).year);

//     printf("At ptr_s, id: %d\n",ptr_s->id);
//     printf("At ptr_s, major: %c\n",ptr_s->major);
//     printf("At ptr_s, year: %d\n",ptr_s->year);
}
