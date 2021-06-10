# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 01:15:35 2021

@author: kazuk
"""

n, w = map(int, input().split())
vw = [[0] * (w + 1) for _ in range(n)]

def dp(i, vi, wi):
    if i == 0:
        for wn, vn in enumerate(vw[i]):
            if wi <= wn:
                vw[i][wn] += vi
    else:
        for wn, vn in enumerate(vw[i]):
            if wi <= wn:
                vw[i][wn] = max(vw[i][wn - wi] + vi, vw[i - 1][wn])
            else:
                vw[i][wn] = vw[i - 1][wn]

for i in range(n):
    vi, wi = map(int, input().split())
    dp(i, vi, wi)

print(vw[n - 1][w])
