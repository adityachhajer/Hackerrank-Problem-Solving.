# efficient approach
x=int(input())
l=list(map(int,input().split()))[:x]
nums=list(l)
nums.sort()
# print(nums)
loss=10**10
for i in range(1,x):
    if((nums[i]-nums[i-1]<loss) and (l.index(nums[i])<l.index(nums[i-1]))):
        loss=nums[i]-nums[i-1]
print(loss)
