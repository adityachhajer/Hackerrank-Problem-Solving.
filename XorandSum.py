x=input()
y=input()
a=int(x,2)
b=int(y,2)
c=0
for i in range(0,314160):
    c=c+(a^(b<<i))
print(c%(10**9+7) )