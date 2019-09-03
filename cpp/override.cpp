#include <iostream>
using namespace std;

class CVector{
   public:
      int x,y;
      CVector (){x=0; y=0;};
      CVector (int,int);
      CVector operator + (CVector);   // overloading function
};

CVector::CVector (int a, int b){
   x = a;
   y = b;
}

CVector CVector::operator+ (CVector param){
   CVector temp;
   temp.x = x + param.x;
   temp.y = y + param.y;
   return (temp);
}

int main () {
   CVector a (3,1);
   CVector b (1,2);
   CVector c;
   c = a + b;
   cout << c.x << "," << c.y << endl;
   return 0;
}
