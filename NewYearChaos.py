t=int(input())
for j in range(0,t):
    n=int(input())
    l=list(map(int,input().split()))[:n]
    di={}
    k=0
    for j in l:
        di[j]=k
        k=k+1
    h=[2]*n
    k=len(l)
    c=0
    for i in range(len(l)-1,-1,-1):
        if l[i] == k:
            k = k - 1
        else:
            a = di[k]
            di[k], di[l[i]] = di[l[i]], di[k]
            x = di[k]
            y = di[l[i]]
            h[x]-=1
            h[y]-=1
            l[i], l[a] = l[a], l[i]
            c = c + 1
            k = k - 1
            if(h[x]<0 or h[y]<0):
                print("Too chaotic")
                c = 0
                break

    if c!=0:
        print(c)



