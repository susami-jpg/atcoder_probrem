# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 22:23:00 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

ans = pow(sum(a), 2)
for i in a:
    ans -= pow(i, 2)

print((ans // 2)%mod)