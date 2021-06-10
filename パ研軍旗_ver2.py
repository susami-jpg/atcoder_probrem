# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:26:02 2021

@author: kazuk
"""

n = int(input())
s = []
for _ in range(5):
    s.append(list(str(input())))

s = [list(x) for x in zip(*s)]
inf = 10 ** 10
dp = [[inf] * 3 for _ in range(n)]
col = ['R', 'B', 'W']
for c in range(3):
    cnt = s[0].count(col[c])
    dp[0][c] = 5 - cnt

for i in range(1, n):
    for j in range(3):
        cnt = s[i].count(col[j])
        dp[i][j] = 5 - cnt + min(dp[i - 1][(j + 1)%3], dp[i - 1][(j + 2)%3])
print(min(dp[-1]))

        
        