# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:54:37 2021

@author: kazuk
"""

n = int(input())
alist = list(map(int, input().split()))
k = alist.pop()
m = 20
#dp[i][j] はi + 1個の数字(A[0:i])を足し算または引き算することによってその和をjにするのが何通りあるかを示す
dp = [[0] * (m + 1) for _ in range(len(alist))]
for i, a in enumerate(alist):
    if i == 0:
        dp[i][a] = 1
        #if文でA[0]をよけておくのには以下の理由がある
        #A[0] = 0だった場合dp[0][0]は0もしくは2として加算されてしまうためよける
    else:
        for j in range(m + 1):
            if a <= j:
                dp[i][j] += dp[i - 1][j - a]
            if j + a <= m:
                dp[i][j] += dp[i - 1][j + a]
print(dp[-1][k])



    
    
                
                
            
            
    
