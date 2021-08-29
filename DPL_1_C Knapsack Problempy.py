# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:50:42 2021

@author: kazuk
"""

N, W = map(int, input().split())
np = [(0,0)] + [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W + 1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(W + 1):
        v, w = np[i]
        dp[i][j] = dp[i-1][j]
        if j-w >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j-w] + v)

print(dp[-1][W])
