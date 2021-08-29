# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:25:11 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10**7)
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

seen = [0] * n
def dfs(v, par=-1):
    if seen[v]:
        return False
    seen[v] = 1
    ans = True
    for nextv in adj[v]:
        if nextv == par:
            continue
        ans &= dfs(nextv, v)
    return ans

ans = 0
for v in range(n):
    if dfs(v):
        ans += 1
print(ans)


