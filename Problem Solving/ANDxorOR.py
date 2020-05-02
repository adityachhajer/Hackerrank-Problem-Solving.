'''
& -and
or- |
(((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2)) = m1^m2
xor=^
'''
n=int(input())
l=list(map(int,input().split()))[:n]
st=[0]
for i in range(0,len(l)-1):
    m1=l[i]
    m2=l[i+1]
    s = (((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2))
    if(s>st[0]):
        st.pop()
        st.append(s)
print(st[0])




