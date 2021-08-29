# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:53:21 2021

@author: kazuk
"""

n, m = map(int, input().split())
c = [0] + list(map(int, input().split()))
inf = 10000000
dp = [[inf] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 0
for i in range(1, m + 1):
    for j in range(n + 1):
        dp[i][j] = dp[i-1][j]
        if j - c[i] >= 0:
            dp[i][j] = min(dp[i][j] ,dp[i-1][j-c[i]] + 1, dp[i][j-c[i]] + 1)

print(dp[-1][-1])
