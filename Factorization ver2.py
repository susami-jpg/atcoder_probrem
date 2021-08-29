# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:55:19 2021

@author: kazuk
"""

from sys import exit
n, m = map(int, input().split())

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

fact = factorization(m)
MOD = 10**9+7

if m == 1:
    print(1)
    exit()
# nCk.pyよりも高速かな？（powを外に出した）
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

ans = 1
for p, c in fact:
    ans *= combination(n-1+c, n-1)
    ans %= MOD
print(ans)

