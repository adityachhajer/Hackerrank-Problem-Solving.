#include<iostream>
using namespace std;
void inSerSort(int arr[],int n)
{
	int i;
    int j=0;
    int value;
    int x=0;
    
    
	for(i=1;i<n;i++)
	{
		value=arr[i];
		j=i-1;
		while(j>=0 && arr[j]>value)
		{
			arr[j+1]=arr[j];
			j=j-1;
			x=x+1;
		}
		arr[j+1]=value;
		
		
	}
	cout<<x;
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
	
	inSerSort(arr,n);
	
}

