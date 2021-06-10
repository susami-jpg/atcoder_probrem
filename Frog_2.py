# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:18:12 2021

@author: kazuk
"""

#infの値には注意
inf = 10 ** 12
n, k = map(int, input().split())
h = [0] + list(map(int, input().split()))
dp = [inf] * (n + 1)
dp[0] = dp[1] = 0
for i in range(2, n + 1):
    for j in range(i - 1, i - 1 - k, -1):
        if j == 0:
            break
        dp[i] = min(dp[i], dp[j] + abs(h[j] - h[i]))

print(dp[n])

    
    
