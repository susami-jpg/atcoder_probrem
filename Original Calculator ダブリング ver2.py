# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:26:51 2021

@author: kazuk
"""

N, K = map(int, input().split())
mod = 10**5
D = 60
def nxt(n):
    if n == 0:
        return 0
    cnt = 0
    for c in list(str(n)):
        cnt += int(c)
    return (n + cnt)%mod
dub = [[nxt(i) for i in range(mod)]] + [[0] * mod for _ in range(D)]
for i in range(D):
    for j in range(mod):
        dub[i+1][j] = dub[i][dub[i][j]]

L = len(bin(K)[2:])-1
now = N
for i in range(L, -1, -1):
    if (K>>i)&1:
        now = dub[i][now]

print(now)

        
