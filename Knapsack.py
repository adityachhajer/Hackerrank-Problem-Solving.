t=int(input())
for _ in range(0,t):
    s=list(map(int,input().split()))[:2]
    l=list(map(int,input().split()))[:s[0]]
    W=s[1]
    t=[[0 for _ in range(W+1)]for _ in range(s[0]+1)]
    for i in range(1,s[0]+1):
        for j in range(1,W+1):
            if l[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=max(t[i-1][j],l[i-1]+t[i][j-l[i-1]])
    print(t[s[0]][W])