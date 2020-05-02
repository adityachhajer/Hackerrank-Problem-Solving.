x=str(input())
y=str(input())
c=len(x)+len(y)
d=0
l3=[]
l=[]
for i in x:
    l3.append(i)
l2=[]
for j in y:
    l2.append(j)
for i in l3:
    if i in l2:
        d=d+1
        l.append(i)
        l2.remove(i)

k=len(l)*2
f=c-k
print(f)