d=list(map(int,input().split()))[:2]
l=list(map(int,input().split()))[:d[0]]
c=0
for i in range(0,len(l)):
    a=l[i:d[1]+i]

    if(len(a)==d[1]):
        ma = max(a)
        r = ma + 1
        output_arr = [0 for y in range(d[1])]
        count_arr = [0 for j in range(r)]
        for j in range(0, d[1]):
            count_arr[a[j]] += 1
        print(count_arr)
        for p in range(1, r):
            count_arr[p] = count_arr[p] + count_arr[p - 1]
        print(count_arr)
        for k in range(0, d[1]):
            count_arr[a[k]] -= 1
            output_arr[count_arr[a[k]]] = a[k]
        print(output_arr)

        x=int(d[1]/2)
        if(d[1]%2!=0):
            median=output_arr[x]*2
            j=i+d[1]
            if(j<d[0]):
                if(l[j]>=median):
                    c=c+1
                    break

            else:

                break

        else:
            median=output_arr[x]+output_arr[x-1]
            j=i+d[1]
            if (j < d[0]):
                if (l[j] >= median):
                    c = c + 1
            else:
                break


    else:
        break


print(c)


