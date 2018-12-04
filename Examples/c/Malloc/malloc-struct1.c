#include <stdio.h>
#include <stdlib.h>

struct Student
{
    int id;
    char major;
    int year;
};


int main()
{
    int *foo;
    struct Student *ptr_s;
    int i,len;

    len = 3;
    
    ptr_s = (struct Student *) malloc(len*sizeof(struct Student));

    printf("Size of Student: %u\n",sizeof(struct Student));

    ptr_s->id = 42;
    ptr_s->major = 'a';
    ptr_s->year = 2001;

    (ptr_s+1)->id = 7;
    (ptr_s+1)->major = 'b';
    (ptr_s+1)->year = 2002;

    (ptr_s+2)->id = 100;
    (ptr_s+2)->major = 'c';
    (ptr_s+2)->year = 2003;

    foo = (int *) ptr_s;

    for (i=0; i < 12; i++)
        printf("Address %u: content %d\n",foo+i,*(foo+i));
}

