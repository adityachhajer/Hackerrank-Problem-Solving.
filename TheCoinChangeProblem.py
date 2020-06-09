k=list(map(int,input().split()))[:2]
l=list(map(int,input().split()))[:k[1]]
sum=k[0]
t=[[0 for _ in range(sum+1)]for _ in range(k[1]+1)]
for i in range(0,len(l)+1):
    t[i][0]=1
for i in range(1,k[1]+1):
    for j in range(1,sum+1):
        if l[i-1]>j:
            t[i][j]=t[i-1][j]
        else:
            t[i][j]=t[i][j-l[i-1]]+t[i-1][j]
print(t[len(l)][sum])

