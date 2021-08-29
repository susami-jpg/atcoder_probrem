# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:06:12 2021

@author: kazuk
"""

n = int(input())
max_n = 10**5 + 1
dp = [1] * max_n
dp[0] = dp[1] = 0
for i in range(2, max_n):
    if dp[i] == 0:continue
    now = i+i
    while now < max_n:
        dp[now] = 0
        now += i

ans = sum(dp[:n])
print(ans)

    