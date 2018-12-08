#include <stdio.h>

struct Student
{
    int id;
    char major;
    int year;
};


int main()
{
    struct Student roster[4];

    roster[0].id = 100;
    roster[0].major = 'a';
    roster[0].year = 2000;

    roster[1].id = 101;
    roster[1].major = 'b';
    roster[1].year = 2001;

    roster[2].id = 102;
    roster[2].major = 'c';
    roster[2].year = 2002;

    printf("Value of roster: %u\n",roster);
    printf("Value of roster+2: %u\n",roster+2);
    printf("Value of roster+2: %u\n",(int *)(roster+2));
    printf("Value of roster+2: %u\n",(char *)(roster+2));
    printf("Value of roster+2+1 after char: %u\n",(char *)(roster+2)+1);

    printf("Int at roster+1: %d\n",*((int *)(roster+1)));
    printf("roster+2: %u\n",*(roster+2));
    printf("Char at crazy location: %c\n",*(char *)((long *)(roster+2)+1));
    printf("Char at crazy location: %c\n",*(char *)((long *)(roster+2)+1));

}

