# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:14:25 2021

@author: kazuk
"""

mod = 10**9 + 7
n = int(input())
ans = 1
for _ in range(n):
    ans *= sum(list(map(int, input().split())))
    ans %= mod
print(ans%mod)
    