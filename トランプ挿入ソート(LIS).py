# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:40:10 2021

@author: kazuk
"""
import bisect
inf = 10 ** 10
n = int(input())
c = []
for _ in range(n):
    c.append(int(input()))

dp = [inf] * n
while c:
    now = c.pop(0)
    i = bisect.bisect_left(dp, now)
    dp[i] = now

for i in range(n - 1, -1, -1):
    if dp[i] < inf:
        print(n - 1 - i)
        break
    

    