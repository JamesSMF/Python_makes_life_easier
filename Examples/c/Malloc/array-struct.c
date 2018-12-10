#include <stdio.h>

struct Student
{
    int id;
    int year;
    char major;
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
    printf("Value of roster+1: %u\n",roster+1);
}

