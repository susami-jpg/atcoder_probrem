# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:11:28 2021

@author: kazuk
"""

n = 10**5 + 2
dp = [1] * n
dp[0] = dp[1] = 0
for i in range(2, n):
    if dp[i] == 0:continue
    now = i+i
    while now < n:
        dp[now] = 0
        now += i

like_2017 = [0] * n
for i in range(3, n, 2):
    if dp[i] and dp[(i+1)//2]:
        like_2017[i] = 1

for i in range(1, n):
    like_2017[i] += like_2017[i-1]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    ans = like_2017[r] - like_2017[l-1]
    print(ans)
    