#include<iostream>
using namespace std;

int tellmeupdown(char arr[],int x)
{
    int i;
    int sum=0;
    int v=0;
    for(i=0;i<x;i++)
    {
        if(arr[i]=='D')
        {
            sum--;
        }
        else if(arr[i]=='U')
        {
            sum++;
            if(sum==0)
            {
                v=v+1;
            }
        }
        
    }return v;
}
int main()
{
    int y,i,x;
    char *arr;
  
    cin>>x;
    
    arr=new char[x];
    for(i=0;i<x;i++)
    {
        cin>>arr[i];
    }
    
    y=tellmeupdown(arr,x);
    cout<<y<<endl;
    return 0;
}

