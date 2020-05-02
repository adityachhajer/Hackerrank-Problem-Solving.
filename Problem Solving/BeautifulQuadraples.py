x=list(map(int,input().split()))[:4]
c=0
x.sort()
# for i in range(1,x[0]+1):
#     for j in range(i,x[1]+1):
#         for k in range(j,x[2]+1):
#             for s in range(k,x[3]+1):
#                 if((i^j^k^s)!=0):
#                     c=c+1

from itertools import combinations

comb = combinations([x[0],x[1],x[1],x[4]],2)

for i in list(comb):
    print(i)

print(c)