# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:50:27 2021

@author: kazuk
"""

n, m = map(int, input().split())
dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    a, b, c, w = map(int, input().split())
    dp[a][b][c] = max(dp[a][b][c], w)

for i in range(101):
    for j in range(101):
        for k in range(101):
            if i == j == k == 0:continue
            dp[i][j][k] = max(dp[i][j][k], dp[max(i-1, 0)][j][k],\
                              dp[i][max(j-1, 0)][k],\
                                  dp[i][j][max(k-1, 0)])
            

for _ in range(m):
    x, y, z = map(int, input().split())
    print(dp[x][y][z])
                
            
            