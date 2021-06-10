# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:42:13 2021

@author: kazuk
"""

n = int(input())
matrix = []
for _ in range(n):
    r, c = map(int, input().split())
    matrix.append(r)
matrix.append(c)

dp = [[10 ** 15] * (n) for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for l in range(1, n):
    for i in range(0, n - l):
        j = i + l
        print(i, j)
       #左側からの結合か右側からの結合かで比較
        for k in range(i, j): #kはiとjの差を表す
            dp[i][j] = min(dp[i][j],
                        dp[i][k] + dp[k + 1][j] + matrix[i] * matrix[k + 1] * matrix[j + 1])
            
        
print(dp[0][-1])

            
                               
            
    