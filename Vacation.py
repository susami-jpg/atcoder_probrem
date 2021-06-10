# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 23:50:17 2021

@author: kazuk
"""

n = int(input())
abc = []
for _ in range(n):
    a, b, c = map(int, input().split())
    abc.append((a, b, c))
dp = [[0] * 3 for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = abc[0][0], abc[0][1], abc[0][2]
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + abc[i][0]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + abc[i][1]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + abc[i][2]
print(max(dp[-1]))

