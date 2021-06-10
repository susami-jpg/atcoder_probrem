# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 22:07:17 2021

@author: kazuk
"""

from itertools import permutations
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for v in permutations(range(1, n)):
    prev = 0
    cost = 0
    for i in v:
        cost += t[prev][i]
        prev = i
    cost += t[prev][0]
    if cost == k:
        ans += 1
print(ans)
        