# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:50:53 2021

@author: kazuk
"""

#pypyならAC
n = int(input())
p = list(map(float, input().split()))
#dp[i][j]:i枚目までのコインを投げた時にj枚のコインが表である確率
dp = [[0] * (n + 1) for _ in range(n)]
dp[0][0] = 1 - p[0]
dp[0][1] = p[0]
for i in range(1, n):
    dp[i][0] = (1 - p[i]) * dp[i - 1][0]
dp[0][1] = p[0]
for i in range(1, n):
    for j in range(1, i + 3):
        if j > n:
            continue
        dp[i][j] = dp[i - 1][j] * (1 - p[i]) + dp[i - 1][j - 1] * p[i]
        
print(sum(dp[-1][(n + 1) // 2:]))