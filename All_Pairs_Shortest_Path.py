# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:14:20 2021

@author: kazuk
"""

n, e = map(int, input().split())
inf = float('inf')
#隣接行列の作製
st = [[inf] * n for _ in range(n)]
for _ in range(e):
    s, t, d = map(int, input().split())
    st[s][t] = d
for i in range(n):
    st[i][i] = 0
    
#ワーシャルフロイド
for k in range(n): #中継点
    for i in range(n): #始点
        for j in range(n): #終点
            st[i][j] = min(st[i][j], st[i][k] + st[k][j])

#負の閉路がないかを確認
for i in range(n):
    if st[i][i] < 0:
        print ('NEGATIVE CYCLE')
        break
else:
    for i in st:
        i = [str(c).replace('inf', 'INF') for c in i]
        print(' '.join(i))
        
            
            