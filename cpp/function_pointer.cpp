#include <iostream>
using namespace std;

int addition (int a, int b){ return (a+b); }
int subtraction (int a, int b){ return (a-b); }

int operation (int x, int y, int (*functocall)(int,int)){
   int g;
   g = (*functocall)(x,y);
   return (g);
}

int main (){
   int m,n;
   int (*minus)(int,int) = subtraction;  // A pointer called minus pointing to the function subtraction
   m = operation (7, 5, addition);
   n = operation (20, m, minus);
   // the same as:
   // n = operation (20, m, subtraction);

   cout << n << endl;
   return 0;
}
