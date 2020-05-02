#include<iostream>
using namespace std;

int main()
{
    int y,i,j,k;
    cin>>y;
    for(k=0;k<y;k++)
    {
    
    int x;
    int m;
    cin>>m;
    int n;
    cin>>n;
    int arr[n];
    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    for(i=0;i<n-1;i++)
    {
        
        {
            for(j=i+1;j<n;j++)
        {
           x=arr[i]+arr[j];
           if(x==m)
           {cout<<i+1<<" "<<j+1<<endl;
           x=0;
           break;
           }
           else
               {
                   x=0;
            }
               
          }
        }
        
    }
    
    }
    return 0;
}

