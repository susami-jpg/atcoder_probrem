# -*- coding: utf-8 -*-
"""
Created on Tue May 25 01:00:02 2021

@author: kazuk
"""

from sys import setrecursionlimit
from bisect import bisect_left, bisect_right
setrecursionlimit(10**7)
n = int(input())
adj = [[] for _ in range(n)]
p = list(map(int, input().split()))
for v, par in enumerate(p):
    adj[par - 1].append(v + 1)

#ある深さのノード(行きかけ順の番号で記録)のリスト
depth = [[] for _ in range(n)]
seen = [0] * n
#頂点vの部分木を行きかけ順番号の頂点のリストで記録
#頂点vの部分木: segment[v] = [left, right]
#行きかけ順でつけられた番号において、leftからrightの間にある番号の頂点が頂点vの部分木
segment = [[0, 0] for _ in range(n)]

def dfs(v, d, e):
    seen[v] = 1
    segment[v][0] = e
    depth[d].append(e)
    for nextv in adj[v]:
        if seen[nextv] == 0:
            e = dfs(nextv, d + 1, e + 1)
    segment[v][1] = e
    return e

dfs(0, 0, 0)

q = int(input())
for _ in range(q):
    u, d = map(int, input().split())
    cnd = depth[d]
    left = bisect_left(cnd, segment[u-1][0])
    right = bisect_right(cnd, segment[u-1][1])
    print(right - left)

    
    
            
    