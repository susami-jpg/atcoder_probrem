# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:01:16 2021

@author: kazuk
"""

h, n = map(int, input().split())
mahou = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
INF = 10 ** 10
dp = [[INF] * (h + 1) for _ in range(n+1)]
dp[0][-1] = 0
acc_min = [INF] * (h + 1)
for i in range(1, n+1):
    for j in range(h, -1, -1):
        a, b = mahou[i]
        dp[i][j] = dp[i-1][j]
        if j+a <= h:
            dp[i][j] = min(dp[i][j], dp[i][j+a] + b)
        if j == 0:
            dp[i][j] = min(dp[i][j], min(dp[i][:a+1]) + b)
print(dp[-1][0])

            
