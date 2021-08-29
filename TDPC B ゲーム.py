# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 22:23:16 2021

@author: kazuk
"""

from itertools import accumulate
A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [0] + a[::-1]
b = [0] + b[::-1]
acc_a = list(accumulate(a))
acc_b = list(accumulate(b))

#dp[i][j]: 山Aにi個のものがあり、山Bにj個のものがある状態から先手が
#得られる最大の価値
dp = [[0] * (B + 1) for _ in range(A + 1)]
for i in range(A + 1):
    for j in range(B + 1):
        if i == j == 0:continue
        elif i == 0:
            dp[i][j] = acc_b[j-1] - dp[i][j-1] + b[j]
        elif j == 0:
            dp[i][j] = acc_a[i-1] - dp[i-1][j] + a[i]
        else:
            dp[i][j] = max(acc_b[j-1] + acc_a[i] - dp[i][j-1] + b[j],\
                           acc_a[i-1] + acc_b[j] - dp[i-1][j] + a[i])
print(dp[A][B])


        