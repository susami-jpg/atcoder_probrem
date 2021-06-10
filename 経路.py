# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:04:40 2021

@author: kazuk
"""

mod = 10 ** 9 + 7
w, h = map(int, input().split())
w -= 1
h -= 1
mx = 2*10**5
fact = [1] * (mx + 1)
for i in range(mx):
    fact[i + 1] = fact[i] * (i + 1) % mod

def inv(n):
    return pow(n, mod - 2, mod)

ans = fact[w + h] * inv(fact[w]) * inv(fact[h]) % mod
# comb(W+H,W) = (W+H)!/(W!H!)
print (ans)
