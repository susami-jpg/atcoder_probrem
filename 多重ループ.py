# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 23:54:12 2021

@author: kazuk
"""

mod = 10 ** 9 + 7
n = int(input())
k = int(input())
mx = 2 * 10 ** 5
fact = [1] * (mx + 1)
for i in range(mx):
    fact[i + 1] = fact[i] * (i + 1) % mod
def inv(n):
    return pow(n, mod - 2, mod)
ans = fact[n + k - 1] * inv(fact[k]) * inv(fact[n - 1]) % mod
print(ans)
