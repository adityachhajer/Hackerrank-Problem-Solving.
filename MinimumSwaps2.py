n=int(input())
swaps=0
l=list(map(int,input().split()))[:n]
di={}
k=0
for i in l:
    di[i]=k
    k=k+1
k=1
c=0
for i in range(0,len(l)):
    if l[i]==k:
        k=k+1
    else:
        a=di[k]
        di[k], di[l[i]] = di[l[i]], di[k]
        l[i],l[a]=l[a],l[i]
        c=c+1
        k=k+1
print(c)


# brute force approach method1
# for i in range(0,n-1):
#     a=i
#     for j in range(i+1,n):
#         if(l[j]<l[i]):
#             temp=j
#             j=i
#             i=temp
#
#     if(a!=i):
#         temp=l[a]
#         l[a]=l[i]
#         l[i]=temp
#         swaps+=1
#
# print(swaps)

# method2
# a=1
# for i in range(0,n-1):
#     if a==l[i]:
#         a=a+1
#     else:
#         for j in range(i+1,n):
#             if(l[j]==a):
#                 temp=l[i]
#                 l[i]=l[j]
#                 l[j]=temp
#                 a=a+1
#                 swaps=swaps+1
#                 break
# print(swaps)


