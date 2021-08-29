# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:56:17 2021

@author: kazuk
"""

n, m = map(int, input().split())
INF = 10 ** 15
dist = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = t
    dist[b][a] = t
for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = INF
for i in range(n):
    cnd = 0
    for j in range(n):
        cnd = max(cnd, dist[i][j])
    ans = min(ans, cnd)
print(ans)


