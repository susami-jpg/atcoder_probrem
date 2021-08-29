# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:58:46 2021

@author: kazuk
"""

from statistics import median
n = int(input())
plotsX = []
plotsY = []
plots = []

for _ in range(n):
    x, y = map(int, input().split())
    plots.append((x, y))
    plotsX.append(x)
    plotsY.append(y)

Xm = median(plotsX)
Ym = median(plotsY)

cost = 0
for (x, y) in plots:
    cost += abs(Xm-x) + abs(Ym-y)

print(int(cost))


