# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:32:30 2021

@author: kazuk
"""

s1 = " " + input()
s2 = " " + input()
ls1 = len(s1)
ls2 = len(s2)
dp = [[0] * ls2 for _ in range(ls1)]
for i in range(1, ls1):
    dp[i][0] = i
for j in range(1, ls2):
    dp[0][j] = j

for i in range(1, ls1):
    for j in range(1, ls2):
        if s1[i] == s2[j]:
            diff = 0
        else:
            diff = 1
        dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + diff)

print(dp[-1][-1])

    