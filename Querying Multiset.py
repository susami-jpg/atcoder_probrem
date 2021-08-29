# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 01:47:53 2021

@author: kazuk
"""

from heapq import heappop, heappush
q = int(input())
hq = []
S = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        heappush(hq, x-S)
    elif query[0] == 2:
        x = query[1]
        S += x
    else:
        ans = heappop(hq) + S
        print(ans)

