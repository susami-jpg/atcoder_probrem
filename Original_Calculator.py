# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:05:38 2021

@author: kazuk
"""

from sys import exit
n, k = map(int, input().split())
mod = 10 ** 5

vis = [-1] * mod
x = n
cycle = 0
while 1:
    if vis[x] != -1:
        break
    vis[x] = cycle
    x = (x + sum(list(map(int, list(str(x)))))) % mod
    cycle += 1

cycle -= vis[x]
if k - vis[x] <= 0:
    ans = n
    for _ in range(k):
        ans = (ans + sum(list(map(int, list(str(ans)))))) % mod
    print(ans)
    exit()
    
k -= vis[x]
k %= cycle

ans = x
for _ in range(k):
    ans = (ans + sum(list(map(int, list(str(ans)))))) % mod
    
print(ans)
