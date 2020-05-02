# ans=[]
s=[]
t=int(input())
c=0
for i in range(0,t):
    c=0
    l=list(input())
    for i in l:
        if ((i == '(') or (i == '{') or (i == '[')) :
            s.append(i)
            c=0
        else:
            if(len(s)==0):
                c=0
                # ans.append("NO")

                # print("NO")
                break
            else:
                if (i == ')' and s[-1] == '('):
                    s.pop()

                    c = 1

                elif (i == ']' and s[-1] == '['):
                    s.pop()
                    c = 1

                elif (i == '}' and s[-1] == '{'):
                    s.pop()
                    c = 1
                else:
                    # print("NO")
                    # ans.append("NO")
                    c = 0
                    break

    if(c==1):
        # ans.append("YES")
        print("YES")
    else:
        print("NO")
# print(ans)

