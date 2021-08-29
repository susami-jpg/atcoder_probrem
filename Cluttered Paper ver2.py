# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:26:47 2021

@author: kazuk
"""

from collections import defaultdict
n = int(input())
sheet = [[0] * 1002 for _ in range(1002)]
for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    sheet[ly][lx] += 1
    sheet[ly][rx] -= 1
    sheet[ry][lx] -= 1
    sheet[ry][rx] += 1

for i in range(1002):
    for j in range(1, 1002):
        sheet[i][j] += sheet[i][j-1]

for j in range(1002):
    for i in range(1, 1002):
        sheet[i][j] += sheet[i-1][j]

rec = defaultdict(int)
for i in range(1002):
    for j in range(1002):
        rec[sheet[i][j]] += 1

for k in range(1, n+1):
    print(rec[k])
    
    