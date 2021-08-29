# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 13:45:24 2021

@author: kazuk
"""

N, K = map(int, input().split())
mod = 10**9+7
ans = 0
def S(l, r):
    n = r-l+1
    return n*(2*l+n-1)//2

for k in range(K, N+2):
    l = S(0, k-1)
    r = S(N-k+1, N)
    ans += (r-l+1)
    ans %= mod
    
print(ans)
