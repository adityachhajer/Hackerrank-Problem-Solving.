s=str(input())
l=set(s)
t=[]
for i in l:
    y=s.count(i)
    t.append(y)

k=set(t)
if(len(k)<=2):

    ma = max(t)
    mi = min(t)
    if (ma == mi):
        print("YES")
    else:
        if (t.count(mi) > t.count(ma)):
            if (t.count(ma) == 1):
                ma = ma - 1
                if (ma == mi):
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            if (t.count(mi) == 1):
                mi = mi - 1
                if (mi == 0):
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")


else:
    print("NO")


