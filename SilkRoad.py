# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:04:34 2021

@author: kazuk
"""

n, m = map(int, input().split())
d = []
c = []
for _ in range(n):
    d.append(int(input()))
for _ in range(m):
    c.append(int(input()))

dp = [[10 ** 15] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 0

for i in range(1, m + 1):
    for j in range(n + 1):
        if j <= i:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + d[j - 1] * c[i - 1])
print(dp[-1][-1])

            