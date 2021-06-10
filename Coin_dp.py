# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:39:33 2021

@author: kazuk
"""

n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(m)]
for i, yen in enumerate(c):
    if i == 0:
        for j in range(n + 1):
            dp[i][j] = j
    else:
        for j in range(n + 1):
            if j - yen >= 0:
                dp[i][j] = min(dp[i][j - yen] + 1, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
print(dp[m - 1][n])
