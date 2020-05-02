//brute force approach
#include<iostream>
using namespace std;
int main()
{
	int i,j,k,n;
	cin>>n;
	int arr[n];
	for(i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	int min=arr[0];
	for(j=0;j<n-1;j++)
	{
		for(k=j+1;k<n;k++)
		{
			int z=0;
			int x=arr[j];
			int y=arr[k];
			if(y<x)
			{
				z=x-y;
				if(z<min)
				{
			    	min=z;
				}
			}
		}
	}cout<<min;
	return 0;
}
