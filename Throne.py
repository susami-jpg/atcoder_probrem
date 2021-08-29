# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 03:18:44 2021

@author: kazuk
"""

from math import gcd
t = int(input())

#逆元はPythonであれば k^{-1} = pow(k,−1,n) で簡単に得られる。
for _ in range(t):
    n, s, k = map(int, input().split())
    g = gcd(gcd(n, s), k)
    s //= g
    n //= g
    k //= g
    d = gcd(n, k)
    if d != 1:
        print(-1)
    else:
        print((pow(k, -1, n) * (-s) % n))

    
        
            