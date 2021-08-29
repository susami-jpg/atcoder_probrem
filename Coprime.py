# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:44:46 2021

@author: kazuk
"""

from sys import exit
n = int(input())
A = list(map(int, input().split()))
max_a = 10**6+1


#SmallestPrimeFactor
#自分の素因数の中で最小の素因数を記録
#前処理O(nloglogn)
def spf(n):
    SPF = [i for i in range(n + 1)]
    check = [False] * (n + 1)
    SPF[0] = 0
    SPF[1] = 1
    check[0] = check[1] = True
    for i in range(2, int(n**0.5) + 1):
        if check[i]: continue
        for j in range(i, n + 1, i):
            if check[j]:continue
            SPF[j] = i
            check[j] = True
    return SPF

spf = spf(max_a)

"""
primefactは素因数分解した結果を返す
ただしsetではない
ex: 9 -> 3, 3を返す
"""
#上のSPFによる前処理を終えた前提
#クエリごとにO(logn)で素因数分解した結果を返す
def primefact(n):
    fact = []
    while n != 1:
        fact.append(spf[n])
        n //= spf[n]
    return fact

prime_rec = [0] * max_a
flg = 0
for a in A:
    cnd = primefact(a)
    for p in set(cnd):
        prime_rec[p] += 1
        if prime_rec[p] > 1:
            flg = 1
        if prime_rec[p] >= n:
            print("not coprime")
            exit()

if flg:
    print("setwise coprime")
else:
    print("pairwise coprime")
    
    






        
        
            