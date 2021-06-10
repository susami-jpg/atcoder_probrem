# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:42:39 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
n, s = map(int, input().split())
lb = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (s+1) for _ in range(n)]
if lb[0][0] <= s:
    dp[0][lb[0][0]] = "A"
if lb[0][1] <= s:
    dp[0][lb[0][1]] = "B"

for i in range(1, n):
    A = lb[i][0]
    B = lb[i][1]
    for j in range(s + 1):
        if j-A >= 0 and dp[i-1][j-A] != 0:
            dp[i][j] = dp[i-1][j-A] + "A"
        if j-B >= 0 and dp[i-1][j-B] != 0:
            dp[i][j] = dp[i-1][j-B] + "B"

if dp[-1][s]:
    print(dp[-1][s])
else:
    print("Impossible")