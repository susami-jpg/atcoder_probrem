# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 13:55:22 2021

@author: kazuk
"""

#三重dp(dp[i][j][k]でMLE(PyPy3)/ Python3だとTLEしたので添え字iを削除)
W = int(input())
N, K = map(int, input().split())
p = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W + 1) for _ in range(K+1)]
dp_prev = [[0] * (W + 1) for _ in range(K+1)]

for i in range(N):
    w, v = p[i]
    dp = [[0] * (W + 1) for _ in range(K+1)]
    for j in range(K+1):
        for k in range(W+1):
            dp[j][k] = max(dp_prev[j][k], dp[j][k])
            if j + 1 <= K and k + w <= W:
                dp[j+1][k+w] = max(dp[j+1][k+w], dp_prev[j][k] + v)
    dp_prev = dp

ans = 0
for j in range(K+1):
    for k in range(W+1):
        ans = max(ans, dp_prev[j][k])
print(ans)
