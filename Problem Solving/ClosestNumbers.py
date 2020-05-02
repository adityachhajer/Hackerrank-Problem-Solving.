n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()
x=int(n/2)
print(l[x])

