i = str(input())

s = []

for c in i:
    if not s:
        s.append(c)
    else:
        if s[-1] == c:
            s.pop()
        else:
            s.append(c)

if not s:
    print("Empty String")
else:
    print(''.join(s))
