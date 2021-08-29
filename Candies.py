# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:23:27 2021

@author: kazuk
"""

from itertools import accumulate
mod = 10 ** 9 + 7
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

#dp[i][j] : i人目までの子供でj個のキャンディーを分ける場合の数
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1

acc_prev = list(accumulate(dp[0]))
acc_now = [0] * (k + 1)
for i in range(1, n + 1):
    for j in range(k + 1):
        if j == 0:
            dp[i][j] = acc_now[j] = 1
            continue
        l = j - a[i]
        if l <= 0:
            cnd = acc_prev[j]
        else:
            cnd = acc_prev[j] - acc_prev[l-1]
        dp[i][j] = cnd%mod
        acc_now[j] = acc_now[j-1] + dp[i][j]
    acc_prev = acc_now
    acc_now = [0] * (k + 1)

print(dp[-1][-1]%mod)

        