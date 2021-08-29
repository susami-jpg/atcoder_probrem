# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:22:43 2021

@author: kazuk
"""

h, w = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(h)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for i in range(h):
    for j in range(w):
        if A[i][j] == -1:
            continue
        ans += dist[A[i][j]][1]
print(ans)

            