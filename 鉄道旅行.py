# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 03:25:19 2021

@author: kazuk
"""

from itertools import accumulate
n, m = map(int, input().split())
p = list(map(int, input().split()))
ride = [0] * (n + 1)
for i in range(m - 1):
    if p[i] < p[i + 1]:
        prev = p[i]
        next = p[i + 1]
    else:
        prev = p[i + 1]
        next = p[i]
    ride[prev] += 1
    ride[next] -= 1
ride = list(accumulate(ride))

fee = [(0, 0, 0)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    fee.append((a, b, c))
ans = 0
for train in range(1, n):
    k = ride[train]
    if k <= 0:
        continue
    fee1 = fee[train][0] * k
    fee2 = fee[train][1] * k + fee[train][2]
    if fee1 < fee2:
        ans += fee1
    else:
        ans += fee2
        
print(ans)
