# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:54:47 2021

@author: kazuk
"""

from sys import exit
n, m = map(int, input().split())
mod = 10**9 + 7

if m == 1:
    print(1)
    exit()
    
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

def combination(n, k):
    nCk = under = top = 1
    mod = 10 ** 9 + 7

    # 分母
    for i in range(2, k + 1):
        under *= i
        under %= mod

    # 分子
    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

fact = factorization(m)
ans = 1
for _, num in fact:
    ans *= combination(n-1+num, num)
    ans %= mod

print(ans%mod)


