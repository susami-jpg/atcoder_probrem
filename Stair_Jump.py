# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:24:48 2021

@author: kazuk
"""

mod = 10 ** 9 + 7
n, l = map(int, input().split())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    if i - l >= 0:
        dp[i] = (dp[i - l] + dp[i - 1]) % mod
    else:
        dp[i] = dp[i - 1]

print(dp[n] % mod)
        