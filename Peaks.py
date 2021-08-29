# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 03:18:12 2021

@author: kazuk
"""

n, m = map(int, input().split())
h = list(map(int, input().split()))
max_height = h[:]
flg = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if max_height[a] == h[b]:
        flg[a] = 1
    elif max_height[a] < h[b]:
        flg[a] = 0
        max_height[a] = h[b]
    if max_height[b] == h[a]:
        flg[b] = 1
    elif max_height[b] < h[a]:
        flg[b] = 0
        max_height[b] = h[a]
    
ans = 0
for v in range(n):
    if max_height[v] == h[v] and flg[v] == 0:
        ans += 1

print(ans)
