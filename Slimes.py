# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:47:45 2021

@author: kazuk
"""

from itertools import accumulate
n = int(input())
a = [0] + list(map(int, input().split()))
a_sum = list(accumulate(a))
inf = 10 ** 15
#dp[i][j]: 左端がa[i]、右端がa[j]のスライムの合成コストの最小値
dp = [[inf] * n for _ in range(n)]

#1ぴきの合成コストは0
for i in range(n):
    dp[i][i] = 0

for diff in range(1, n):
    for i in range(n-diff):
        j = i + diff
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]\
                #結局ij間のスライムの合計値がコストとして足される
                + a_sum[j+1] - a_sum[i])

print(dp[0][-1])



            