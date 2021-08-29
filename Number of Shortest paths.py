# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:38:12 2021

@author: kazuk
"""
"""
n = int(input())
n, k = map(int, input().split())
a, b, c = map(int, input().split())
s = input()
s = list(input())
a = list(map(int, input().split()))
"""


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a-1].append((b-1, 1))
    adj[b-1].append((a-1, 1))


from collections import deque

#nは頂点数、adjはコスト付きの隣接リスト
def bfs_num(n, adj):
    INF = 10**10
    mod = 10**9+7
    deq = deque()
    dist = [INF] * n
    num = [0] * n
    dist[0] = 0
    num[0] = 1
    deq.append((0, 0))
    
    while deq:
        v, w = deq.popleft()
        if dist[v] < w:continue
        for nextv, cost in adj[v]:
            if dist[nextv] > dist[v] + cost:
                dist[nextv] = dist[v] + cost
                num[nextv] = num[v]
                deq.append((nextv, dist[nextv]))
            elif dist[nextv] == dist[v] + cost:
                num[nextv] += num[v]
                num[nextv] %= mod
    return dist[-1], num[-1]%mod

_, ans = bfs_num(n, adj)
print(ans)



n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a-1].append((b-1, 1))
    adj[b-1].append((a-1, 1))

from heapq import heappop, heappush

def dijkstra_num(n, adj):
    INF = 10**10
    mod = 10**9+7
    dist = [INF] * n
    num = [0] * n
    hq = [(0, 0)]
    dist[0] = 0
    num[0] = 1
    
    while hq:
        w, v = heappop(hq)
        if dist[v] < w:continue
        for nextv, cost in adj[v]:
            if dist[nextv] > dist[v] + cost:
                dist[nextv] = dist[v] + cost
                num[nextv] = num[v]
                heappush(hq, (dist[nextv], nextv))
            elif dist[nextv] == dist[v] + cost:
                num[nextv] += num[v]
                num[nextv] %= mod
    return dist[-1], num[-1]%mod

_, ans = dijkstra_num(n, adj)
print(ans)
