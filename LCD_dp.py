# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 17:02:31 2021

@author: kazuk
"""

q = int(input())

def longestdp(x, y):
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]
ans = []
for _ in range(q):
    x = input()
    y = input()
    ans.append(longestdp(x, y))

for i in ans:
    print(i)
            
    
    
    