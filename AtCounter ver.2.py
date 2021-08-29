# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:50:49 2021

@author: kazuk
"""

n = int(input())
s = " " + input()
atc = " atcoder"
mod = 10**9 + 7

#dp[i][j]: i番目の文字まで見た時に文字列sのj番目まで完成している場合の数
dp = [[0] * len(atc) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    for j in range(len(atc)):
        dp[i][j] += dp[i-1][j]
        if j-1 >= 0 and s[i] == atc[j]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= mod

print(dp[n][-1])

