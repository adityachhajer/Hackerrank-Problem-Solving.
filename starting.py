f=int(input())
n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()
mid=int((n-1)/2)
if(f>l[mid]):
    for i in range(mid+1,n):
        if(l[i]==f):
            print(i)
elif(f<l[mid]):
    for j in range(0,mid):
        if (l[j] == f):
            print(j)

else:
    print(mid)