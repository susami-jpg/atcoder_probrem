# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:39:44 2021

@author: kazuk
"""

mod = 10 ** 9 + 7
h, w = map(int, input().split())
hw = [['#'] * (w + 2)]
for _ in range(h):
    hw.append(['#'] + list(input()) + ['#'])
hw.append(['#'] * (w + 2))
dp = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if i == j == 1:
            dp[i][j] = 1
            continue
        if hw[i][j] == '#':
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[h][w] % mod)