# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:29:05 2021

@author: kazuk
"""

n, m = map(int, input().split())
c = []
for _ in range(m):
    c.append(int(input()))
x = [0]
for _ in range(n):
    x.append(int(input()))

dp = [[10 ** 15] * 256 for _ in range(n + 1)]
dp[0][128] = 0

for i in range(1, n + 1):
    #iは行を指し、xの値を指定する
    for j in range(256):
        #jは行を指定し、yの値を指定する
        for c_cnd in c:
            nexty = j + c_cnd
            if nexty < 0:
                nexty = 0
            if 255 < nexty:
                nexty = 255
            dp[i][nexty] = min(dp[i][nexty],(x[i] - nexty) ** 2 + dp[i - 1][j])  

print(min(dp[-1]))