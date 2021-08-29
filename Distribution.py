# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 20:49:19 2021

@author: kazuk
"""

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

#dp[i]: i番目の人が宝石をもらう最短時間
#答えはdp[i+n] ~ dp[2n-1]
#dp[i+1] = min(dp[i] + s[i], dp[i+1])
#dp[i]はt[i]で初期化
dp = t * 2

for i in range(1, 2*n):
    dp[i] = min(dp[i-1] + s[(i-1)%n], dp[i])

print(*dp[n:])
