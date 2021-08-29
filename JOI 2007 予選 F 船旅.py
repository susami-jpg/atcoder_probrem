# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:30:48 2021

@author: kazuk
"""

from sys import stdin
from heapq import heappop, heappush
n, k = map(int, input().split())
edge = [[] for _ in range(n)]
INF = 10**15

def dijkstra(s, g):
    dist = [INF] * n
    fix = [False] * n
    dist[s] = 0
    hq = [(0, s)]
    while hq:
        _, v = heappop(hq)
        fix[v] = True
        for nextv, cost in edge[v]:
            if fix[nextv]:continue
            if dist[nextv] > dist[v] + cost:
                dist[nextv] = dist[v] + cost
                heappush(hq, (dist[nextv], nextv))
    return dist[g]


for _ in range(k):
    query = list(map(int, input().split()))
    if len(query) == 3:
        a, b = query[1], query[2]
        a -= 1
        b -= 1
        ans = dijkstra(a, b)
        if ans == INF:
            print(-1)
        else:
            print(ans)
    else:
        c, d, e = query[1], query[2], query[3]
        c -= 1
        d -= 1
        edge[c].append((d, e))
        edge[d].append((c, e))
    

