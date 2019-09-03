#include <iostream>
using namespace std;

template <class T> T GetMax (T a, T b) {
   return (a>b) ? a : b;;
}

int main () {
   cout << GetMax<int>(5,6) << endl;
   cout << GetMax<long>(10,5)<< endl;
   return 0;
}
