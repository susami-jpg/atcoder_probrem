# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:12:26 2021

@author: kazuk
"""

d = int(input())
N = int(input())
n = [0] + list(map(int, list(str(N))))
mod = 10**9+7

dp = [[[0] * d for _ in range(2)] for _ in range(len(n))]

dp[0][0][0] = 1
for i in range(len(n)-1):
    for j in range(2):
        for k in range(d):
            if j == 0:
                ceil = n[i+1]
                for c in range(ceil+1):
                    if c == ceil:
                        dp[i+1][0][(k+c)%d] += dp[i][j][k]%mod
                    else:
                        dp[i+1][1][(k+c)%d] += dp[i][j][k]%mod
            else:
                for c in range(10):
                    dp[i+1][1][(k+c)%d] += dp[i][j][k]%mod

ans = dp[-1][0][0] + dp[-1][1][0] - 1

print(ans%mod)

            
            