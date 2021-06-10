# -*- coding: utf-8 -*-
"""
Created on Thu May  6 00:47:52 2021

@author: kazuk
"""

import bisect
n, m = map(int, input().split())
p = [0]
for _ in range(n):
    p.append(int(input()))

p2 = []
for i in p:
    for j in p:
        p2.append(i + j)

p2.sort()
ans = 0
for i in p2:
    if m - i < 0:
        break
    mindex = bisect.bisect(p2, m - i) - 1
    ans = max(ans, i + p2[mindex])
print(ans)
