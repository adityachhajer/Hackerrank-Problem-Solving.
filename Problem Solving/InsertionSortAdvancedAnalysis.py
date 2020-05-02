t=int(input())
w=0
for d in range(0,t):
    n=int(input())
    l=list(map(int,input().split()))[:n]
    for i in range(1,len(l)):
        j=i-1
        key=l[i]
        while(j>=0 and l[j]>key):
            l[j+1]=l[j]
            j=j-1
            w=w+1
        l[j+1]=key
    print(w)
    w=0

