# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:47:52 2021

@author: kazuk
"""

#試し割法の素因数分解(1は空のリストを返すので注意)
#O(sqrt(N))
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

"""
print(prime_factorize(1))
# []

print(prime_factorize(36))
# [2, 2, 3, 3]

print(prime_factorize(840))
# [2, 2, 2, 3, 5, 7]

素数とその個数を取得する場合
c = collections.Counter(prime_factorize(840))
print(c)
# Counter({2: 3, 3: 1, 5: 1, 7: 1})
"""

#前計算なしのオイラー関数
#1,2,…,N のうち、N と互いに素であるものの個数
#N = 12なら1,5,7,11の4個
#上のprime_factrizeを使う
def Euler_count(n):
    from collections import Counter
    fact = Counter(prime_factorize(n))
    cnt = n
    for key in fact.keys():
        cnt *= (1 - (1/key))
    return int(cnt)
    
n = int(input())
print(Euler_count(n))

