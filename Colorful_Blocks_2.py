# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:31:34 2021

@author: kazuk
"""

from sys import exit
n, k = map(int, input().split())
mod = 10**9 + 7
if n == 1:
    print(k%mod)
elif n == 2:
    print(k*(k-1)%mod)
else:
    ans = k * (k-1) % mod
    ans *= pow(k-2, n-2, mod)
    ans %= mod
    print(ans)
    