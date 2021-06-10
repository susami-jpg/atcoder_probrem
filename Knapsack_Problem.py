# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:10:29 2021

@author: kazuk
"""
n, w = map(int, input().split())
vw = [[0] * (w + 1) for _ in range(n)]
bag = []
for i in range(n):
    v, wi = map(int, input().split())
    bag.append([i, v, wi])

for i, v, wi in bag:
    if i == 0:
        for j in range(w + 1):
            vw[i][j] = (j // wi) * v
    else:
        for j in range(w + 1):
            if j >= wi:
                vw[i][j] = max(vw[i][j - wi] + v, vw[i - 1][j])
            else:
                vw[i][j] = vw[i - 1][j]
print(vw[n - 1][w])

