
#!/bin/python3

import math
import os
import random
import re
import sys

def checkMagazine(a, b):
    di={}
    for i in range(0,len(a)):
        if a[i] not in di.keys():
            di[a[i]]=1
        else:
            di[a[i]]+=1
    for i in range(0,len(b)):
        if b[i] not in di.keys():
            return False
        else:
            if di[b[i]]!=0:
                di[b[i]]-=1
            else:
                return False
    return True




if __name__ == '__main__':
    x = list(map(int, input().split()))[:2]
    a = list(map(str, input().split()))[:x[0]]
    b = list(map(str, input().split()))[:x[1]]
    y=checkMagazine(a, b)
    if y==True:
        print("Yes")
    else:
        print("No")



