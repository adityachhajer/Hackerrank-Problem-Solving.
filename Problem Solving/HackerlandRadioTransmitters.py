n=list(map(int,input().split()))[:2]
l=list(map(int,input().split()))[:n[0]]
l.sort()
t=0
k=n[1]
i=1
while(i<n[0]):
    if(l[i]-l[i-1]<=k):
        light = True
        t = t + 1
        a = 0
        for j in range(i + 1, len(l)):
            while (l[j] - l[i] <= k):
                a = a + 1
            if(a==0):
                break
            else:
                i = i + a + 1
    else:
        t=t+1
print(t)









