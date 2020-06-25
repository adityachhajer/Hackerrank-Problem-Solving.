if __name__ == '__main__':
    p=str(input())
    s=str(input())
    m=len(p)+1
    n=len(s)+1
    l=[[0]* (n) for j in range(m)]
    for i in range(1,len(p)+1):
        for j in range(1,len(s)+1):
            if p[i-1]==s[j-1]:
                l[i][j]=1+l[i-1][j-1]
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    print(l[-1][-1])
