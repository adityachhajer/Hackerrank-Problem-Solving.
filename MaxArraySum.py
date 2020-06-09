if __name__ == '__main__':
    n=int(input())
    l=list(map(int,input().split()))[:n]
    t=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        t[i]=max(l[i-1]+t[i-2],t[i-1])
    print(t[n])
