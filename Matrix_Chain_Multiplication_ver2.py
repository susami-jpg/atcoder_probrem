# -*- coding: utf-8 -*-
"""
Created on Tue May 18 20:17:41 2021

@author: kazuk
"""

n = int(input())
M = []
#左側だけをメモしておく(1番最後の行列は右側も覚えておく)
#こうすることであるi番目の行列の左側の値はM[i]で、右側の値はM[i+1]で取得できる。
for _ in range(n):
    r, c = map(int, input().split())
    M.append(r)
M.append(c)
inf = 10 ** 10
dp = [[inf] * n for _ in range(n)]
#行列の対角成分すなわち、行列積Miを計算するコストは0である
for i in range(n):
    dp[i][i] = 0
    
for l in range(1, n):
    for i in range(n - l):
        j = i + l
        for k in range(i, j):
            #cost(左側行列積) + cost(右側行列積) + 行列計算のコスト
            # 初回はR[0]*R[1]*R[2]
            #iは一番左側にかけてある行列、jは一番右側にかけてある行列、kはその間の行列
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + M[i] * M[k+1] * M[j+1])
            
print(dp[0][-1])

        
    