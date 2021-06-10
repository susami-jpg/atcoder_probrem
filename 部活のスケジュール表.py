# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:13:47 2021

@author: kazuk
"""

n = int(input())
joi = {'J': 0, 'O': 1, 'I': 2}
yotei = list(input())
dp = [[0] * (1 << 3) for _ in range(n)]
for j in range(1 << 3):
    if (j >> (joi[yotei[0]])) & 1 and (j >> 0) & 1:
        dp[0][j] = 1

for i in range(1, n):
    for j in range(1 << 3):
        #責任者が出席していない場合
        a = joi[yotei[i]]
        b = (a + 1) % 3
        c = (a + 2) % 3
        if (j >> a) & 1 == 0:
            continue
        #全員出席している場合
        if j == (1 << 3) - 1:
            dp[i][j] = sum(dp[i - 1])
            dp[i][j] = dp[i][j] % 10007
        #責任者とほかの誰かが出席している場合
        elif (j >> b) & 1:
            for k in range(1 << 3):
                if (k >> a) & 1 or (k >> b) & 1:
                    dp[i][j] += dp[i - 1][k]
            dp[i][j] = dp[i][j] % 10007
        elif (j >> c) & 1:
            for k in range(1 << 3):
                if (k >> a) & 1 or (k >> c) & 1:
                    dp[i][j] += dp[i - 1][k]
            dp[i][j] = dp[i][j] % 10007
        #責任者のみが出席している場合
        else:
            for k in range(1 << 3):
                if (k >> a) & 1:
                    dp[i][j] += dp[i - 1][k]
            dp[i][j] = dp[i][j] % 10007
print(sum(dp[-1]) % 10007)
                    
            
            