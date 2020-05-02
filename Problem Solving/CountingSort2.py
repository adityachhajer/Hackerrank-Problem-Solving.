n=int(input())
l=list(map(int,input().split()))[:n]
ma=max(l)
mi=min(l)
r=ma+1
output_arr=[0 for i in range(n)]
count_arr = [0 for j in range(r)]
for j in range(0,n):
    count_arr[l[j]]+=1

for i in range(1,r):
    count_arr[i]=count_arr[i]+count_arr[i-1]


for k in range(0,n):
    count_arr[l[k]]-=1
    output_arr[count_arr[l[k]]]=l[k]

for i in output_arr:
    print(i,end=" ")