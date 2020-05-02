ans=[]
g=int(input())
x=0
n=0
for i in range(0,g):
    l=list(map(int,input().split()))[:3]
    s1=list(map(int,input().split()))[:l[0]]
    s2=list(map(int,input().split()))[:l[1]]
    while(x<l[2]):
        if((len(s1)!=0) and (len(s2)!=0) ):
            if (s1[0] < s2[0]):
                x = x + s1[0]
                n = n + 1
                s1.pop(0)
            else:
                x = x + s2[0]
                n = n + 1
                s2.pop(0)
        else:
            if(len(s1)==0):
                x = x + s2[0]
                n = n + 1
                s2.pop(0)
            else:
                x = x + s1[0]
                n = n + 1
                s1.pop(0)

    print(n-1)
    # ans.append(n-1)
    x=0
    n=0

