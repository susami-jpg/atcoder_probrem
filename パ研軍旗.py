# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:15:17 2021

@author: kazuk
"""

n = int(input())
flag = []
for _ in range(5):
    flag.append(list(input()))
flag = [list(x) for x in zip(*flag)]
color = ['R', 'B', 'W']
dp = [[0] * 3 for _ in range(n)]

for j in range(n):
    for c in range(3):
        counter = 0
        for i in flag[j]:
            if i != color[c]:
                counter += 1
        if j == 0:
            dp[j][c] = counter
        else:
            dp[j][c] = min(dp[j - 1][(c + 1) % 3] + counter, dp[j - 1][(c + 2) % 3] + counter)

print(min(dp[-1]))