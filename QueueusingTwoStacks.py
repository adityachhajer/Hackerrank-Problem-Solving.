qu=[]
q=int(input())
for i in range(0,q):
    l=list(map(int,input().split()))
    if(l[0]==1):
        qu.append(l[1])
    elif(l[0]==2):
        qu.pop(0)
    elif(l[0]==3):
        print(qu[0])

