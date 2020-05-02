#include <iostream>
using namespace std;
int staircase(int n) 
{
    int i;
    int space;
    int star;
    for(i=1;i<=n;i++)
    {
        for(space=n-1;space>=i;space--)
        {
            cout<<" ";
            
        }
        for(star=0;star<i;star++)
        {
            cout<<"#";
            
        }
           cout << "\n";
    }
    return 0;
}
int main()
{
    int n;
    cin>>n;
    staircase(n);
    return 0;    
}

