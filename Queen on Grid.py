# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:04:08 2021

@author: kazuk
"""

h, w = map(int, input().split())
mod =10**9 + 7
S = [["#"] + list(input()) + ["#"] for _ in range(h)]
S = [["#"] * (w + 2)] + S + [["#"] * (w + 2)]

dp = [[0] * (w + 2) for _ in range(h + 2)]
X = [[0] * (w + 2) for _ in range(h + 2)]
Y = [[0] * (w + 2) for _ in range(h + 2)]
Z = [[0] * (w + 2) for _ in range(h + 2)]
#X[i][j] = dp[i][j] + dp[i][j-1] + dp[i][j-2] + ...  X[i][j]:    横からS[i][j]までくる通り数
#Y[i][j] = dp[i-1][j] + dp[i-2][j] + ...  Y[i][j]:               上からS[i][j]までくる通り数
#Z[i][j] = dp[i][j] + dp[i-1][j-1] + dp[i-2][j-2] + ... Z[i][j]: 斜め上からS[i][j]までくる通り数
#dp[i][j] = X[i][j] + Y[i][j] + Z[i][j]

dp[1][1] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        #壁の場合はその場所には絶対いけないので0
        if S[i][j] == ".":
            dp[i][j] += (X[i][j-1] + Y[i-1][j] + Z[i-1][j-1])%mod
            X[i][j] += (X[i][j-1] + dp[i][j])%mod
            Y[i][j] += (Y[i-1][j] + dp[i][j])%mod
            Z[i][j] += (Z[i-1][j-1] + dp[i][j])%mod

print(dp[h][w])

        

