# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 00:28:52 2021

@author: kazuk
"""

n, w = map(int, input().split())
goods = []
for _ in range(n):
    wi, vi = map(int, input().split())
    goods.append((wi, vi))
vmax = 10 ** 5
inf = 10 ** 12
dp = [[inf] * (vmax + 1) for _ in range(n)]
dp[0][0] = 0
wi, vi = goods[0]
for j in range(vmax + 1):
    if j - vi == 0:
        dp[0][j] = wi
for i in range(1, n):
    wi, vi = goods[i]
    for j in range(vmax + 1):
        if j - vi >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - vi] + wi)
                       
        else:
            dp[i][j] = dp[i - 1][j]
w_cnd = dp[-1][::-1]
for ans, wi in enumerate(w_cnd):
    if wi <= w:
        print(vmax - ans)
        break

            
        
