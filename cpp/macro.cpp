# include <iostream>
using namespace std;

# define getmax(a,b) ((a)>(b)?(a):(b))

int main(){
   int x=5, y;
   y = getmax(x,2+5*4);
   cout << y << endl;
   return 0;
}
