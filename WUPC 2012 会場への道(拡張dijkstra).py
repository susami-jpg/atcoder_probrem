# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:50:56 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    f, t, c = map(int, input().split())
    edge[f].append((t, c))
    edge[t].append((f, c))

INF = 10**15
def ext_dijkstra(s, g, mod):
    dist = [[INF] * mod for _ in range(n)]
    fix = [[False] * mod for _ in range(n)]
    hq = [(0, 0, 0)]
    dist[0][0] = 0
    while hq:
        _, v, m = heappop(hq)
        fix[v][m] = True
        for nextv, cost in edge[v]:
            nextm = (dist[v][m] + cost)%mod
            if fix[nextv][nextm]:continue
            if nextv == g and nextm != 0:continue
            if dist[nextv][nextm] > dist[v][m] + cost:
                dist[nextv][nextm] = dist[v][m] + cost
                heappush(hq, (dist[nextv][nextm], nextv, nextm))
    return dist[g][0]

ans = min(ext_dijkstra(0, n-1, 4), ext_dijkstra(0, n-1, 7))
print(ans)



    