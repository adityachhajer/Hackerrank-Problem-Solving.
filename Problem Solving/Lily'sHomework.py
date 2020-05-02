def solution(l):
    di = {}
    for i in range(len(l)):
        di[l[i]]=i

    g=sorted(l)
    c=0

    for i in range(len(l)):
        if(l[i]!=g[i]):
            c=c+1
            temp=di[g[i]]
            di[l[i]]=di[g[i]]
            l[i],l[temp]=g[i],l[i]
    return c



n=int(input())
l=list(map(int,input().split()))[:n]

asc = solution(l[::])
desc =solution(l[::-1])
print(min(asc, desc))
