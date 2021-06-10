# -*- coding: utf-8 -*-
"""
Created on Wed May 19 21:50:00 2021

@author: kazuk
"""

h, w = map(int, input().split())
a = [[1 if i == "+" else -1 for i in list(str(input()))] for _ in range(h)]
dp = [[0] * w for _ in range(h)]

#dp[i][j]: マス(i, j)から始めた時に自分がとれる最高のcost(cost = 自分-相手)
for i in range(h-1, -1, -1):
    for j in range(w-1, -1, -1):
        if i == h-1 and j == w-1:
            continue
        #p = 1を高橋、p = 0を青木のターンとする
        if (i + j) % 2:
            p = 1
        else:
            p = 0
        #行く先が+か-かのチェック
        if i == h-1:
            dp[i][j] = -dp[i][j+1] + a[i][j+1]
        elif j == w-1:
            dp[i][j] = -dp[i+1][j] + a[i+1][j]
        else:
            dp[i][j] = max(-dp[i][j+1]+a[i][j+1], -dp[i+1][j]+a[i+1][j])

ans = dp[0][0]
if ans > 0:
    print("Takahashi")
elif ans < 0:
    print("Aoki")
else:
    print("Draw")
    
           