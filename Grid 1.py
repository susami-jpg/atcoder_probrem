# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:43:54 2021

@author: kazuk
"""

mod = 10**9+7
h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if maze[i][j] == "#":
            continue
        if i == j == 0:
            continue
        elif i == 0:
            dp[i][j] += dp[i][j-1]%mod
        elif j == 0:
            dp[i][j] += dp[i-1][j]%mod
        else:
            dp[i][j] += (dp[i-1][j] + dp[i][j-1])%mod
            
print(dp[-1][-1]%mod)


        
