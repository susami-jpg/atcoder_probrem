# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 18:26:13 2021

@author: kazuk
"""

n = int(input())
ans = 1
mod = 10**9+7
for _ in range(n):
    ans *= sum(list(map(int, input().split())))
    ans %= mod
print(ans)
