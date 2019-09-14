#include <iostream>
#include <typeinfo>
#include <exception>
using namespace std;

class CBase { virtual void f(){} };
class CDerived : public CBase {};

int main () {
   try{
      CBase* a = new CBase;
      CBase* b = new CDerived;
      int c = 300;
      cout << "a is: " << typeid(a).name() << '\n';
      cout << "b is: " << typeid(b).name() << '\n';
      cout << "*a is: " << typeid(*a).name() << '\n';
      cout << "*b is: " << typeid(*b).name() << '\n';
      cout << "c is: " << typeid(c).name() << '\n';
   }catch (exception& e){
      cout << "Exception: " << e.what() << endl;
   }

   return 0; 
}