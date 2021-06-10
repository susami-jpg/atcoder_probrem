# -*- coding: utf-8 -*-
"""
Created on Mon May 10 20:32:41 2021

@author: kazuk
"""

n, m = map(int, input().split())
d = []
for _ in range(n):
    d.append(int(input()))
w = []
for _ in range(m):
    w.append(int(input()))
inf = 10 ** 10
dp = [[inf] * (n + 1) for _ in range(m + 1)]
for i in range(m + 1):
    dp[i][0] = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + w[i - 1] * d[j - 1])

print(dp[-1][-1])
