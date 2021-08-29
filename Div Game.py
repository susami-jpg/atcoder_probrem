# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 16:01:48 2021

@author: kazuk
"""


"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

n = int(input())
from collections import defaultdict
rec = defaultdict(int)
ans = 0
while 1:
    div = factorization(n)
    for p, E in div:
        if p==1:continue
        for e in range(1, E+1):
            z = pow(p, e)
            if rec[z] == 0:
                rec[z] = 1
                n //= z
                ans += 1
                break
        else:
            continue
        break
    else:
        break

print(ans)

        