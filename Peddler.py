# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:15:29 2021

@author: kazuk
"""

from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
gold = [(cost, i) for i, cost in enumerate(a)]
gold.sort()
adj = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x-1].append(y-1)

seen = [0] * n

def bfs(v, s):
    deq = deque()
    deq.append((v, s))
    p = -10**10
    while deq:
        x, g = deq.popleft()
        if seen[x]:
            continue
        if x != v:
            p = max(p, g-s)
        seen[x] = 1
        for nextv in adj[x]:
            deq.append((nextv, a[nextv]))
    return p

ans = -10**10
for s, v in gold:
    if seen[v] == 0 and adj[v]:
        ans = max(ans, bfs(v, s))

print(ans)
    

        
        