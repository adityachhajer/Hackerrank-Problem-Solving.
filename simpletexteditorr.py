ans=[]
s=""
p=[""]
t=int(input())
for i in range(0,t):
    l=list(input().split())
    k=int(l[0])
    if(k==1):
        s=s+l[1]
        p.append(s)
        print(s)
        print(p)

    if(k==2):
        s=s[:-int(l[1])]
        p.append(s)
        print(s)
        print(p)

    if(k==3):
        print(s[int(l[1])-1])

    if(k==4):
        p.pop()
        s=p[-1]


print(s,p)
