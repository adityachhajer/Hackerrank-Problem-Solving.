m=[]
t=0
c=0
p=[]
n=int(input())
for i in range(0,n):
    l=list(map(int,input().split()))
    if(l[0]==1):
        p.append(l[1])
        if(l[1]>t):
            c=1
            t=l[1]
            m.append(t)
    elif(l[0]==2):
        if(p[-1]==m[-1]):
            p.pop()
            m.pop()
            c=0
            t=0
            m=[]
        else:
            p.pop()
    elif(l[0]==3):
        if(c==0):
            print("answeer",max(p))
        else:
            print("answer",m[-1])

