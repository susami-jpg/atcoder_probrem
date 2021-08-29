# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:37:34 2021

@author: kazuk
"""

from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
INF = float('inf')
a.sort()
a = [-INF] + a + [INF]

q = int(input())
for _ in range(q):
    b = int(input())
    ind = bisect_left(a, b)
    cnd1 = a[ind-1]
    cnd2 = a[ind]
    ans = min(abs(b-cnd1), abs(b-cnd2))
    print(ans)
    