# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:15:11 2021

@author: kazuk
"""

from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)
input = stdin.readline
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

#dfs1の最後に見た頂点を根としてもう一度dfs
dist = [-1] * n
def dfs(v, d):
    dist[v] = d
    for nextv in edge[v]:
        if dist[nextv] != -1:continue
        dfs(nextv, d+1)
    return

dfs(0, 0)
last_dist = max(dist)
last = dist.index(last_dist)
dist = [-1] * n
dfs(last, 0)

ans = max(dist) + 1
print(ans)


    
    