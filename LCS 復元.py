# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:49:48 2021

@author: kazuk
"""

s = " " + input()
t = " " + input()

ls = len(s)
lt = len(t)

#dp[i][j]: sをi文字目まで、tをj文字目まで見た時のLCS
dp = [[0] * lt for _ in range(ls)]

for i in range(1, ls):
    for j in range(1, lt):
        if s[i] == t[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ""
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    #sのi文字目とtのj文字目が一致している場合
    else:
        ans += s[i] #t[j]でもよい
        i -= 1
        j -= 1

print(ans[::-1])

        