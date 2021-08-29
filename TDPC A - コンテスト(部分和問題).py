# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 11:59:08 2021

@author: kazuk
"""

n = int(input())
p = [0] + list(map(int, input().split()))
max_p = 10**4 + 1
dp = [[False] * max_p for _ in range(n + 1)]
dp[0][0] = True
for i in range(1, n+1):
    for j in range(max_p):
        dp[i][j] = dp[i-1][j]
        if j-p[i] >= 0:
            dp[i][j] |= dp[i-1][j-p[i]]

ans = dp[-1].count(True)
print(ans)

        