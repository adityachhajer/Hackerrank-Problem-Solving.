n=list(map(int,input().split()))[:3]
l=[]
for rows in range(0,n[0]):
    l.append([0])
    for columns in range(0,n[1]-1):
        l[rows].append(0)
v=n[0]*n[1]
for i in range(0,n[2]):
    a=list(map(int,input().split()))[:3]
    t=a[0]-1
    for j in range(a[1]-1,a[2]):
        l[t][j]=1

print(sum(x == 0 for row in l for x in row))


