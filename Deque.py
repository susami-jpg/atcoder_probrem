# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:30:19 2021

@author: kazuk
"""

inf = 10 ** 15
n = int(input())
a = list(map(int, input().split()))

#dp[l][r] : aの左端のindexがl、右端のindexがrの時、先手-後手の最大値
dp = [[inf] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = a[i]

for p in range(1, n):
    for l in range(n-p):
        r = l + p
        dp[l][r] = max(-dp[l+1][r] + a[l], -dp[l][r-1] + a[r])
        
print(dp[0][-1])
