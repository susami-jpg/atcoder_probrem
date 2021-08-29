# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 00:13:49 2021

@author: kazuk
"""

n, m, l, x = map(int, input().split())
a = list(map(int, input().split()))
#dp[i][j]: i番目までの燃料のうちからいくつかを選んでj番目の休憩所に泊まることができる最小の周回回数
INF = 10**15
dp = [[INF] * m for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        dp[i+1][(j+a[i])%m] = min(dp[i+1][(j+a[i])%m], (dp[i][j]*m + j + a[i])//m)

if dp[-1][l] <= x:
    print("Yes")
else:
    print("No")
    