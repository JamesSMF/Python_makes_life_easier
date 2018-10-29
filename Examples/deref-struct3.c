#include <stdio.h>

struct Student
{
    float id;
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

    s.id = -79;
    s.major = 'c';
    s.year = 2017;

    ptr_s = &s;

    ptr_c = &(s.major);

    printf("At ptr_c: %c\n\n",*ptr_c);

    printf("At ptr_s, id: %d\n",ptr_s->id);
    printf("At ptr_s, major: %c\n",ptr_s->major);
    printf("At ptr_s, year: %d\n",ptr_s->year);
}
