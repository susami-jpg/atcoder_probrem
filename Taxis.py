# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:43:48 2021

@author: kazuk
"""
from collections import deque
from heapq import heappop, heappush
inf = 10 ** 10
n, k = map(int, input().split())
taxi = [[]]
for _ in range(n):
    c, r = map(int, input().split())
    taxi.append((c, r))
adj = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(i, r):
    q = deque()
    cnd = set()
    dist = 0
    q.append((i, dist))
    while q:
        v, dist = q.popleft()
        if dist > r:
            break
        if v != 0:
            cnd.add(v)
        for nextv in adj[v]:
            q.append((nextv, dist + 1))        
    return list(cnd)

taxiadj = [[]]
for i, t in enumerate(taxi):
    if i == 0:
        continue
    c, r = t
    taxiadj.append(bfs(i, r))

def dijkstra(s, g):
    dist = [inf] * (n + 1)
    dist[s] = 0
    fix = [False] * (n + 1)
    hq = [(0, s)]
    while hq:
        v = heappop(hq)[1]
        fix[v] == True
        c = taxi[v][0]
        for nextv in taxiadj[v]:
            if fix[nextv] == False and dist[v] + c < dist[nextv]:
                dist[nextv] = dist[v] + c
                heappush(hq, (dist[nextv], nextv))
    return dist[g]

print(dijkstra(1, n))


    

    
    
