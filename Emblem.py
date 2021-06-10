# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 01:47:52 2021

@author: kazuk
"""

from math import sqrt
n, m = map(int, input().split())
cent = []
for _ in range(n):
    x, y, r = map(int, input().split())
    cent.append((x, y, r))
rcent = len(cent) - 1
for _ in range(m):
    x, y = map(int, input().split())
    cent.append((x, y))

inf = 10 ** 10
ans = []
for i in range(len(cent) - 1):
    for j in range(i + 1, len(cent)):
        r1 = inf
        r2 = inf
        if i <= rcent:
            x1, y1, r1 = cent[i]
        else:
            x1, y1 = cent[i]
        if j <= rcent:
            x2, y2, r2 = cent[j]
        else:
            x2, y2 = cent[j]
        d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if r1 != inf and r2 != inf:
            ans.append(min(r1, r2))
        elif r1 != inf:
            ans.append(d - r1)
        elif r2 != inf:
            ans.append(d - r2)
        else:
            ans.append(d / 2)
print(min(ans))

            
            