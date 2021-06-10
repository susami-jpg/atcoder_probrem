# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:45:14 2021

@author: kazuk
"""

#TLE
while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    C = []
    for _ in range(m):
        C.append(int(input()))
    x = [0]
    for _ in range(n):
        x.append(int(input()))
    inf = 10 ** 5
    dp = [[inf] * 256 for _ in range(n + 1)]
    dp[0][128] = 0
    for i in range(1, n + 1):
        for j in range(256):
            for c in C:
                k = j + c
                if  k < 0:
                    k = 0
                if k > 255:
                    k = 255
                dp[i][k] = min(dp[i][k], dp[i-1][j] + (x[i] - k) ** 2)
    
    print(min(dp[-1]))

