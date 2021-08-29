# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:28:33 2021

@author: kazuk
"""

#TLE
max_n = 10**7+1
dp = [1] * max_n
dp[0] = dp[1] = 0
for i in range(2, max_n):
    if dp[i] == 0:continue
    now = i+i
    while now < max_n:
        dp[now] = 0
        now += i

for i in range(1, max_n):
    dp[i] += dp[i-1]

while 1:
    n = input()
    if not n:
        break
    n = int(n)
    print(dp[n])


