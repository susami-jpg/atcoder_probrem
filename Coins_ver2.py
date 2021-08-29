# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:50:21 2021

@author: kazuk
"""

n = int(input())
p = [0] + list(map(float, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

#dp[i][j]: i枚目までのコインを投げた時、j枚のコインが表である確率
#j枚目が表: dp[i][j] += dp[i-1][j-1] * pi
#j枚目が裏: dp[i][j] += dp[i-1][j] * (1-pi)

for i in range(1, n + 1):
    for j in range(n + 1):
        if j == 0:
            dp[i][j] = dp[i-1][j] * (1-p[i])
        else:
            dp[i][j] += dp[i-1][j-1] * p[i]
            dp[i][j] += dp[i-1][j] * (1-p[i])

ans = 1 - sum(dp[-1][:n//2 + 1])
print(ans)

