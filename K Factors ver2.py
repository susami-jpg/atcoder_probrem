# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 00:50:32 2021

@author: kazuk
"""

n, k = map(int, input().split())
dp = [0] * (n + 1)
for i in range(2, n+1):
    if dp[i] != 0:continue
    now = i
    while now < n+1:
        dp[now] += 1
        now += i

ans = 0
for i in range(n+1):
    if dp[i] >= k:
        ans += 1
print(ans)
