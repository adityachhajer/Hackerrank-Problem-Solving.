#include<iostream>
using namespace std;
int main()
{
    int a1,a2,a3;
    int b1,b2,b3;
    cin>>a1>>a2>>a3;
    cin>>b1>>b2>>b3;
    int A=0;
    int B=0;
    if(a1>b1)
    {
        A=A+1;
    }
    else if(b1>a1)
    {
        B=B+1;
    }
    
    
    if(a2>b2)
    {
        A=A+1;
    }
    else if(b2>a2)
    {
        B=B+1;
    }
    
    if(a3>b3)
    {
        A=A+1;
    }
    else if(b3>a3)
    {
        B=B+1;
    }
    
cout<<A<<" "<<B;
    return 0;
    
}

