if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a = str(input())
        b = str(input())
        n=len(a)
        m=len(b)
        t=[[0 for _ in range(m+1)]for _ in range(n+1)]
        for i in range(0,n+1):
            t[i][0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if a[i - 1] == b[j - 1]:
                    t[i][j]=t[i-1][j-1]
                elif a[i-1].upper()==b[j-1]:
                    t[i][j] = t[i - 1][j - 1] or t[i-1][j]
                else:
                    if a[i-1].isupper():
                        t[i][j]=0
                    else:
                        t[i][j]=t[i-1][j]
        if t[n][m]:
            print("YES")
        else:
            print("NO")




