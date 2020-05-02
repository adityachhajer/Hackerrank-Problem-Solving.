#include<iostream>
using namespace std;

void QusoFu(int arr[],int n)
{
	int pivot=arr[0];
	int arr1[1];
	for(int h=0;h<1;h++)
	{
		arr1[h]=pivot;
	}
	int arr2[n];
	int k=0;
	int arr3[n];
	int t=0;
	
	for(int i=1;i<n;i++)
	{
		
		if(arr[i]>=pivot)
		{
			arr3[t]=arr[i];
			t=t+1;
		}
		else
		{
			arr2[k]=arr[i];
			k=k+1;
		}
	}
	for(int s=0;s<k;s++)
	{
		cout<<arr2[s]<<" ";
	}
	for(int f=0;f<1;f++)
	{
		cout<<arr1[f]<<" ";
	}
	for(int g=0;g<t;g++)
	{
		cout<<arr3[g];
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
	QusoFu(arr,n);
	return 0;
	
}
