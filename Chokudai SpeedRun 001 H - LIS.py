# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:55:01 2021

@author: kazuk
"""

from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
#dp[i]: 長さiの増加部分列を作るときの最終要素の最小値
INF = 10 ** 10
dp = [INF] * n
for i in range(n):
    #更新箇所の取得
    ind = bisect_left(dp, a[i])
    dp[ind] = a[i]

for i in range(n-1, -1, -1):
    if dp[i] != INF:
        print(i+1)
        break

    