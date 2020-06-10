t=int(input())
for _ in range(t):
    x=int(input())
    l=list(map(int,input().split()))[:x]
    maxsum=l[0]
    totalsum=l[0]
    subseq=0
    if l[0]>0:
        subseq=l[0]
    for i in range(1,x):
        if l[i]>0:
            subseq+=l[i]
        maxsum=max(maxsum+l[i],l[i])
        totalsum=max(totalsum,maxsum)
    if subseq==0:
        print(totalsum,max(l))
    else:
        print(totalsum,subseq)


