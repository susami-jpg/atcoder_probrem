# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:02:27 2021

@author: kazuk
"""

#TLE
from heapq import heappop, heappush
n, m = map(int, input().split())
inf = 10 ** 10
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a - 1].append((b - 1, c))
    adj[b - 1].append((a - 1, c))

def chmin(a, b):
    if a > b:
        return b
    else:
        return a
    
def dijkstra(s):
    dis = [inf] * n
    dis[s] = 0
    fix = [False] * n
    hq = [(0, s)]
    while hq:
        now = heappop(hq)[1]
        fix[now] = True
        for nextv, w in adj[now]:
            if not fix[nextv]:
                dis[nextv] = chmin(dis[nextv], dis[now] + w)
                heappush(hq, (dis[nextv], nextv))
    return dis

ans = [0] * n
sg = dijkstra(0)
gs = dijkstra(n-1)
for i in range(n):
    print(sg[i] + gs[i])
    

    
    




    
