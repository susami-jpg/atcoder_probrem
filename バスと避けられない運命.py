# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:09:30 2021

@author: kazuk
"""

inf = 10 ** 10
n, m = map(int, input().split())
bus = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    bus[a-1][b-1] = t
    bus[b-1][a-1] = t

#ワーシャルフロイドによって各バス停から各バス停に行くときの最短距離を求めておく
for i in range(n):
    bus[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

#各バス停に引っ越した時の最も遠い地点(最悪の場合の距離)を求める
cnd = []
for c in bus:
    cnd.append(max(c))
print(min(cnd))