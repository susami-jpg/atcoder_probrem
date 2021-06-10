# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 01:03:44 2021

@author: kazuk
"""

from heapq import heappop, heappush
v, e = map(int, input().split())
st = [[] for _ in range(v)]
for _ in range(e):
    s, t, w = map(int, input().split())
    st[s].append((t, w))
    st[t].append((s, w))

visited = [False] * v
hq = []
heappush(hq, (0, 0))
ans = 0
while hq:
    w, now = heappop(hq)
    if visited[now] == True:
        continue
    ans += w
    visited[now] = True
    for nextv, w in st[now]:
        heappush(hq, (w, nextv))
print(ans)
    
    

