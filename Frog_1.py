# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:35:44 2021

@author: kazuk
"""

n = int(input())
h = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[2] = abs(h[2] - h[1])
for i in range(n + 1):
    if i < 3:
        continue
    dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                dp[i - 2] + abs(h[i] - h[i - 2]))
print(dp[n])