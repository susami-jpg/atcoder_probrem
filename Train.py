# -*- coding: utf-8 -*-
"""
Created on Wed May 26 22:27:02 2021

@author: kazuk
"""

from heapq import heappop, heappush
n, m, x, y = map(int, input().split())
town = [[] for _ in range(n)]
for _ in range(m):
    a, b, t, k = map(int, input().split())
    town[a-1].append((b-1, t, k))
    town[b-1].append((a-1, t, k))

seen = [0] * n
hq = []
hq.append((0, x-1))
while hq:
    time, v = heappop(hq)
    if v == y-1:
        print(time)
        break
    if seen[v]:
        continue
    seen[v] = 1
    for nextv, t, k in town[v]:
        if time % k == 0:
            tcnd = 0
        else:
            tcnd = k - (time%k)
        heappush(hq, (time + tcnd + t, nextv))

else:
    print(-1)
            

