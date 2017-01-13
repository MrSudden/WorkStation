#include <iostream>

using namespace std;

const int i=10;

int main(){
  int a, b, c=0, d;
  cout<<"Enter value for a: ";
  cin>>a;
  cout<<"Enter value for b: ";
  cin>>b;
  c=a+b;
u:  
  if(c<31){
    cout<<"Enter another value: ";
    cin>>d;
    c+=d;
  }
  if(c<31){
    goto u;
  }
  cout<<"Sum is equal to: "<<c;
  return 0;
}
