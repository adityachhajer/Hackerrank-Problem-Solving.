#include <iostream>
#include <algorithm> 
using namespace std;

int main()
{
    int i,n,t,j;
    int c=0;
    cin>>n>>t;
    int arr[n];
    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    sort(arr, arr+n);
   
    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n && (arr[j]-arr[i]<=t);j++)
        {
            if(arr[j]-arr[i]==t)
            {
                
            c++;

            }
        }
    }cout<<c;
    return 0;    
}

