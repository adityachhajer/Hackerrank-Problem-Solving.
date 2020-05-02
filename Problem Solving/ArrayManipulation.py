l=[]
x=list(map(int,input().split()))[:2]
for i in range(0,x[0]):
    l.append(0)
for i in range(0,x[1]):
    t=list(map(int,input().split()))[:3]
    l[t[0]-1]=l[t[0]-1]+t[2]
    if((t[1])!=len(l)):
        l[t[1]] = l[t[1] ] - t[2]

for i in range(1,len(l)):
    l[i]=l[i]+l[i-1]
print(max(l))

