# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:11:55 2021

@author: kazuk
"""

n, q = map(int, input().split())
xy = []
xmax = xmin = ymax = ymin = None
x, y = map(int, input().split())
xy.append((x-y, x+y)) #45°回転
xmax = xmin = x-y
ymax = ymin = x+y
for _ in range(n - 1):
    x, y = map(int, input().split())
    xy.append((x-y, x+y))
    #それぞれの成分の最大値、最小値を記録
    xmax = max(xmax, x-y)
    xmin = min(xmin, x-y)
    ymax = max(ymax, x+y)
    ymin = min(ymin, x+y)

for _ in range(q):
    p = int(input()) - 1
    x, y = xy[p]
    #全ての点について考える必要はない
    #各成分のminとmaxが最大距離の候補となる
    print(max(abs(xmax-x), abs(xmin-x), abs(ymax-y), abs(ymin-y)))
    
    
    