# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:20:31 2021

@author: kazuk
"""

from sys import exit
mod = 10**9 + 7
L, R = map(int, input().split())
l = len(str(L))
r = len(str(R))
ans = 0

def Sn(a, n):
    return n*(2*a + (n-1)) // 2

if l == r:
    ans += Sn(L, R-L+1) * l
    ans %= mod
    print(ans)
    exit()

ans += Sn(L, pow(10, l)-L) * l
ans %= mod 
ans += Sn(pow(10, r-1), R - pow(10, r-1) + 1) * r
ans %= mod

for i in range(l+1, r):
    ans += Sn(pow(10, i-1), pow(10, i) - pow(10, i-1)) * i
    ans %= mod

print(ans%mod)
    

