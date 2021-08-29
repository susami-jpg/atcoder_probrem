# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:03:26 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
n, m, t = map(int, input().split())
A = list(map(int, input().split()))
edge = [[] for _ in range(n)]
edge_rev = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c))
    edge_rev[b].append((a, c))

INF = 10**15
def dijkstra(s, edge):
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
    return dist

dist_go = dijkstra(0, edge)
dist_back = dijkstra(0, edge_rev)
ans = 0
for i in range(n):
    time = t - (dist_go[i] + dist_back[i])
    if time >= 0:
        cnd = time * A[i]
        ans = max(ans, cnd)

print(ans)

        