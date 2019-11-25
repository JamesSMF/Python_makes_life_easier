#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
   int x = 3;
   int y = 4;

   // ^ means bitwise XOR
   x = x^y;
   y = x^y;      // y = (x^y)^y = x^0 = x
   x = x^y;      // x = (x^y)^x = y^0 = y

   printf("x = %d, y = %d\n", x, y);
}
