#include<iostream>
using namespace std;

int partition(int arr[],int s,int e)
{
	int pivot=arr[e];
	int pIndex=s;
	for(int i=s;i<e;i++)
	{
		if(arr[i]<pivot)
		{
			int temp=arr[pIndex];
			arr[pIndex]=arr[i];
			arr[i]=temp;
			pIndex++;
		}
	}
	int temp2=arr[pIndex];
	arr[pIndex]=arr[e];
	arr[e]=temp2;
	return pIndex;
}
void quickSort(int arr[],int s,int e)
{
	if(s<e)
	{
		int p=partition(arr,s,e);
		quickSort(arr,s,(p-1));
		quickSort(arr,(p+1),e);
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
	quickSort(arr,0,(n-1));
	for(int j=0;j<n;j++)
	{
		cout<<arr[j]<<" ";
	}
	return 0;
}
