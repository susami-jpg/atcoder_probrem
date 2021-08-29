# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:51:46 2021

@author: kazuk
"""

d, n = map(int, input().split())
day = [int(input()) for _ in range(d)]
cloth = [tuple(map(int, input().split())) for _ in range(n)]
INF = 10**10
dp = [[-INF] * n for _ in range(d)]

for i in range(d):
    for j in range(n):
        for k in range(n):
            temp = day[i]
            a, b, c = cloth[j]
            prev_a, prev_b, prev_c = cloth[k]
            if a <= temp <= b:
                if i == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(c - prev_c))

print(max(dp[-1]))

            
            