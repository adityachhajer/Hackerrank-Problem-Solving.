#include<iostream>
using namespace std;

void insertSort(int arr[],int n)
{
    int x=arr[n-1];
    int t=n-2;
    for(int i=t;i>=0;i--)
    {
        if(arr[i]>x)
        {
            arr[i+1]=arr[i];
            for(int j=0;j<n;j++)
            {   
                cout<<arr[j]<<" ";
            }
            cout<<endl;
        }    
        else{
                arr[i+1]=x;
                break;
            }
        
    arr[i]=x;    
    }
    
    for(int k=0;k<n;k++)
    {
        cout<<arr[k]<<" ";
    }
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    insertSort(arr,n);
}

