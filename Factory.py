# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:34:30 2021

@author: kazuk
"""

from heapq import heappop, heappush
n, k = map(int, input().split())
hq = []
for i in range(n):
    a, b = map(int, input().split())
    heappush(hq, (a, b))
ans = 0
for _ in range(k):
    a, b, = heappop(hq)
    ans += a
    heappush(hq, (a + b, b))
print(ans)
