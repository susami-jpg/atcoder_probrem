# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:07:16 2021

@author: kazuk
"""

from heapq import heappop, heappush
inf = 10 ** 10
n, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]

def dijkstra(s, t):
    dis = [inf] * (n + 1)
    dis[s] = 0
    fix = [False] * (n + 1)
    hq = [(0, s)]
    while hq:
        now = heappop(hq)[1]
        fix[now] = True
        for nextv, w in adj[now]:
            if fix[nextv] == False and dis[now] + w < dis[nextv]:
                dis[nextv] = dis[now] + w
                heappush(hq, (dis[nextv], nextv))
    return dis[t]

for _ in range(k):
    inp = list(map(int, input().split()))
    if len(inp) == 4:
        _, c, d, e = inp
        adj[c].append((d, e))
        adj[d].append((c, e))
    else:
        _, a, b = inp
        i = dijkstra(a, b)
        if i == inf:
            print(-1)
        else:
            print(i)

        
        
        
    