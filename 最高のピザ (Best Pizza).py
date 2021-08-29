# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:22:08 2021

@author: kazuk
"""

n = int(input())
a, b = map(int, input().split())
c = int(input())
D = [0] + [int(input()) for _ in range(n)]
#dp[i][j]: i番目までのトッピングのうちj個のトッピングを用いてできるピザの最大カロリー
dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = c
ans = 0
for i in range(1, n+1):
    for j in range(i+1):
        dp[i][j] = dp[i-1][j]
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + D[i])
        if i == n:
            dp[i][j] //= (a + j*b)
            ans = max(ans, dp[i][j])

print(ans)

            
        