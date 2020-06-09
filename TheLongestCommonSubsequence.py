if __name__ == '__main__':
    s=list(map(int,input().split()))[:2]
    l1=list(map(int,input().split()))[:s[0]]
    l2=list(map(int,input().split()))[:s[1]]
    m=s[0]
    n=s[1]
    t=[[0 for _ in range(n+1)]for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if l1[i-1]==l2[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    l=[]
    i=m
    j=n
    while(i>0 and j>0):
        if l1[i-1]==l2[j-1]:
            l.append(l1[i-1])
            i-=1
            j-=1
        else:
            if t[i][j-1]>t[i-1][j]:
                j-=1
            else:
                i-=1
    print(*reversed(l))