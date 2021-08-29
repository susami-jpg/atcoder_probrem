# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:58:33 2021

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
mod = 10**9 + 7
rec = [1] * (n+1)
ans = 1
for i in range(2, n+1):
    cnd = factorization(i)
    for p, cnt in cnd:
        rec[p] += cnt

for i in range(2, n+1):
    ans *= rec[i]
    ans %= mod
print(ans)
