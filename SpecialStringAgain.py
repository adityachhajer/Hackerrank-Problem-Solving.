s=str(input())
l=[]
k=""
for i in range(0,len(s)):
    for j in s[i:]:
        k=k+j
        if(len(k)==1):
            l.append(k)
        elif(len(k)==2):
            h=k[0:]
            y=k[::-1]
            if(h==y):
                l.append(k)
        else:
            o=len(k)
            g=int(o/2)
            h=k[0:g]
            y=k[:g:-1]
            if(h==y):
                l.append(k)
    k=""

print(len(l))