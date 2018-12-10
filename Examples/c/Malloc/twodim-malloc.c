#include <stdio.h>

struct Student
{
    int id;
    char major;
    int year;
};


int main()
{
    struct Student **roster;
    int i,j;

    roster = (struct Student **) malloc(2*sizeof(struct Student *));
    for (i=0;i<2;i++)
        roster[i] = (struct Student *)malloc(3*sizeof(struct Student));


    roster[0][0].id = 100;
    roster[0][0].major = 'a';
    roster[0][0].year = 2000;

    roster[0][1].id = 101;
    roster[0][1].major = 'b';
    roster[0][1].year = 2001;

    roster[0][2].id = 102;
    roster[0][2].major = 'c';
    roster[0][2].year = 2002;

    roster[1][0].id = 103;
    roster[1][0].major = 'd';
    roster[1][0].year = 2003;

    roster[1][1].id = 104;
    roster[1][1].major = 'e';
    roster[1][1].year = 2004;

    roster[1][2].id = 105;
    roster[1][2].major = 'e';
    roster[1][2].year = 2005;

    for (i=0;i<2;i++)
        for (j=0;j<3;j++)
            printf("Location of roster[%d][%d]: %u\n",i,j,&(roster[i][j]));

    printf("\n");

    for (i=0;i<2;i++)
        printf("Value of roster[%d]: %u\n",i,roster[i]);

    printf("\n");

    printf("Value of roster: %u\n",roster);


}

