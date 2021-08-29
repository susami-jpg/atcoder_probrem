# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 12:41:53 2021

@author: kazuk
"""

K = int(input())
mod = 10**9+7

if K%9 != 0:
    print(0)
else:
    #dp[i]: 各桁の数字の和がiとなるような場合の数
    #dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-9]
    #先頭の桁の数を1~9のどれにするかを考えれば上記の遷移式になる
    dp = [0] * (K+1)
    for i in range(1, 10):
        dp[i] = 1
    for i in range(K+1):
        for j in range(1, 10):
            if i-j <= 0:break
            dp[i] += dp[i-j]
            dp[i] %= mod
    print(dp[K]%mod)
    
    