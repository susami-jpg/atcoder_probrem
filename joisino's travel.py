# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:01:55 2021

@author: kazuk
"""

from itertools import permutations
n, m, r = map(int, input().split())
R = list(map(int, input().split()))
INF = 10 ** 15
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = INF
for perm in permutations(R):
    now = perm[0]-1
    cnd = 0
    for i in range(1, r):
        next = perm[i]-1
        cnd += dist[now][next]
        now = next
    ans = min(ans, cnd)

print(ans)

        