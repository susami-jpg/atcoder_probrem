# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:52:21 2021

@author: kazuk
"""

from sys import exit
a, b = map(int, input().split())
maze = [[1] * a for _ in range(b)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    maze[y][x] = 0

if maze[0][0] == 0:
    print(0)
    exit()
    
dp = [[0] * a for _ in range(b)]
dp[0][0] = 1
for i in range(b):
    for j in range(a):
        if i == j == 0:continue
        if maze[i][j] == 0:continue
        if i-1 >= 0:
            dp[i][j] += dp[i-1][j]
        if j-1 >= 0:
            dp[i][j] += dp[i][j-1]

print(dp[-1][-1])
