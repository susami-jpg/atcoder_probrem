# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:23:46 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
h, w, n = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(h)]

#dp[i][j]: n-1回目までの散歩でマス(i, j)に何度訪れたか
dp = [[0] * w for _ in range(h)]

dp[0][0] = n-1
for i in range(h):
    for j in range(w):
        #北から南の移動
        if i-1 >= 0:
            c = dp[i-1][j]
            #2回に一回は必ず訪れる
            dp[i][j] += c//2
            #前のマスの訪問回数が奇数で初期盤面で自分のほうに向いていれば+1
            if c%2 and maze[i-1][j] == 0:
                dp[i][j] += 1
        
        #西から東への移動
        if j-1 >= 0:
            c = dp[i][j-1]
            dp[i][j] += c//2
            if c%2 and maze[i][j-1]:
                dp[i][j] += 1


#最終盤面の行先を実際に移動
i = j = 0
while i < h and j < w:
    if dp[i][j]%2:
        d = 1-maze[i][j]
    else:
        d = maze[i][j]
    if d:
        j += 1
    else:
        i += 1

print(i+1, j+1)
        
            
                
            