di={}
s=[]
x=int(input())
for i in range(0,x):
    l=list(map(int,input().split()))[:2]
    if l[0]==1:
        if l[1] in di.keys():
            di[l[1]]+=1
        else:
            di[l[1]]=1
    elif(l[0]==2):
        if l[1] in di.keys():
            if di[l[1]]>0:
                di[l[1]]-=1
    elif(l[0]==3):
        if l[1] in di.values():
            s.append(1)
        else:
            s.append(0)

print(*s, sep = "\n")