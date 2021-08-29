# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:42:24 2021

@author: kazuk
"""
q = int(input())
for _ in range(q):
    x = [""] + list(input())
    y = [""] + list(input())
    lx = len(x)
    ly = len(y)
    
    dp = [[0] * lx for _ in range(ly)]
    for i in range(1, ly):
        for j in range(1, lx):
            if y[i] == x[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    print(dp[-1][-1])
