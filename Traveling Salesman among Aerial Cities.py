# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:45:28 2021

@author: kazuk
"""

n = int(input())
town = [tuple(map(int, input().split())) for _ in range(n)]
inf = 10 ** 15
#dp[S][i]: 集合Sの街を訪問し、最後の街がiである時の最小コスト
dp = [[inf] * n for _ in range(1 << n)]

dp[0][0] = 0
for S in range(1 << n):
    for i in range(n):
        if (S >> i) & 1:
            #行先(町i)の座標
            p, q, r = town[i]
            for j in range(n):
                #出発点(町j)の座標
                a, b, c = town[j]
                dp[S][i] = min(dp[S][i], dp[S ^ (1<<i)][j] + \
                               abs(p-a) + abs(q-b) + max(0, r-c))

print(dp[-1][0])

