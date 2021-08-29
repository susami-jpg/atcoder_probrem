# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:19:35 2021

@author: kazuk
"""

a, b, c = map(int, input().split())
dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
for i in range(99, -1, -1):
    for j in range(99, -1, -1):
        for k in range(99, -1, -1):
            if i == j == k == 0:
                break
            n = i + j + k
            dp[i][j][k] = (i * (dp[i+1][j][k] + 1) + j * (dp[i][j + 1][k] + 1) + k * (dp[i][j][k + 1] + 1)) / n

print(dp[a][b][c])
