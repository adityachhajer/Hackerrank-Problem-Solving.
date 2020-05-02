n=int(input())
l=[]
c=n/2
d=[]
for i in range(0,n):
    x=list(input().split())[:2]
    if(int(x[0])<len(l)):
        if (i >= c):
            l[int(x[0])].append(x[1])
        else:
            l[int(x[0])].append('-')
    else:
        p=(int(x[0]))-len(l)
        for j in range(len(l),int(x[0])+1):
            l.append([0])
        if (int(x[0]) < len(l)):
            if (i > c):
                l[int(x[0])].append(x[1])
            else:
                l[int(x[0])].append('-')
for j in range(0,len(l)):
    for k in range(1,len(l[j])):
        print(l[j][k],end=" ")



