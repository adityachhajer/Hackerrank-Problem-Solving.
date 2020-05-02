#include<iostream>
using namespace std;

int tellmeupdown(int arr[],int x)
{

    int i,j;
    int t=-1;
    int sum=1;
    int v=0;
    for(i=0;i<x;i++,t++)
    {
        if(i<x-2 && arr[i+2]==0)
        {
            i++;

        }
        
    }return t;
}
int main()
{
    int y,i,x;
    int *arr;
    
    cin>>x;
    
    arr=new int[x];
    for(i=0;i<x;i++)
    {
        cin>>arr[i];
    }
    
    y=tellmeupdown(arr,x);
    cout<<y<<endl;
    return 0;
}

