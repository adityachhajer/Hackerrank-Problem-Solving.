l=list(map(int,input().split()))[:3]
t1=l[0]
t2=l[1]
n=l[2]
c=n-2
t=[]
t.append(t1)
t.append(t2)
while(c>0):
    a=t[-2]+(t[-1]**2)
    t.append(a)
    c-=1
print(t[-1])