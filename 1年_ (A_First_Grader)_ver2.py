# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:05:52 2021

@author: kazuk
"""

n = int(input())
s = list(map(int, input().split()))
ans = s[-1]
s = s[:-1]
dp = [[0] * 21 for _ in range(n-1)]
dp[0][s[0]] = 1
for i in range(1, n-1):
    inc = s[i]
    for j in range(21):
        if j - inc >= 0:
            dp[i][j] += dp[i - 1][j - inc]
        if j + inc <= 20:
            dp[i][j] += dp[i - 1][j + inc]
            
print(dp[-1][ans])
        
        