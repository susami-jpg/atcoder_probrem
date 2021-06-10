# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:45:30 2021

@author: kazuk
"""

n = int(input())
S = [str(input()) for _ in range(n)]

dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = dp[0][1] = 1

for i in range(n):
    for j in range(2):
        if j == 0:
            if S[i] == "AND":
                dp[i+1][j] = dp[i][0] * 2 + dp[i][1]
            else:
                dp[i+1][j] = dp[i][0]
        else:
            if S[i] == "AND":
                dp[i+1][j] = dp[i][1]
            else:
                dp[i+1][j] = dp[i][0] + dp[i][1] * 2

print(dp[-1][1])

                
                