# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 00:06:57 2021

@author: kazuk
"""

n, w = map(int, input().split())
goods = []
for _ in range(n):
    wi, vi = map(int, input().split())
    goods.append((wi, vi))

dp = [[0] * (w + 1) for _ in range(n)]
wi, vi = goods[0]
for j in range(w + 1):
    if j >= wi:
        dp[0][j] = vi
    
for i in range(1, n):
    wi, vi = goods[i]
    for j in range(w + 1):
        if wi > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wi] + vi)
print(dp[-1][-1])

        
        
    
    