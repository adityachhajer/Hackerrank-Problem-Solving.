#include<iostream>
using namespace std;

void insertSort(int arr[],int n)
{
    int i;
    int j=0;
    int key;
    for(i=1;i<n;i++)
    {
        key=arr[i];
        j=i-1;
        while(j>=0 && arr[j]>key)
        {
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=key;
        for(int k=0;k<n;k++)
        {
            cout<<arr[k]<<" ";
        }
        cout<<endl;
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

