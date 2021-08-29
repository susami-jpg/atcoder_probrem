# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:43:14 2021

@author: kazuk
"""

w, h = map(int, input().split())
mod = 100000

#dp[i][j][d][p]: マス(i, j)にいて、d方向を向いていて前のマスで方向転換したか(p)の状態数
#d == 0なら南方向、d == 1なら東方向
#p == 0なら前のマスで方向転換していない、p == 1なら前のマスで方向転換した
dp = [[[[0] * 2 for _ in range(2)] for _ in range(w)] for _ in range(h)]

dx = [0, 1]
dy = [1, 0]

def valid(y, x):
    return 0 <= y <= h-1 and 0 <= x <= w-1

dp[1][0][0][0] = dp[0][1][1][0] = 1
for i in range(h):
    for j in range(w):
        for d in range(2):
            for p in range(2):
                if i == j == 0:continue
                c = dp[i][j][d][p]
                #前のマスで方向転換した場合
                if p:
                    #現在向いている方向と同じ方向にしか進めない
                    nexti, nextj = i+dy[d], j+dx[d]
                    if not valid(nexti, nextj):continue
                    dp[nexti][nextj][d][0] += c
                    dp[nexti][nextj][d][0] %= mod
                    
                #前のマスで方向転換していない場合
                else:
                    #同じ方向に進む場合
                    nexti, nextj = i+dy[d], j+dx[d]
                    if valid(nexti, nextj):
                        dp[nexti][nextj][d][0] += c
                        dp[nexti][nextj][d][0] %= mod
                    
                    #方向転換する場合
                    nexti, nextj = i+dy[1-d], j+dx[1-d]
                    if valid(nexti, nextj):
                        dp[nexti][nextj][1-d][1] += c
                        dp[nexti][nextj][1-d][1] %= mod

ans = 0
for d in range(2):
    for p in range(2):
        ans += dp[h-1][w-1][d][p]

print(ans%mod)

                    
                