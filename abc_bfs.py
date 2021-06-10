# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:49:28 2021

@author: kazuk
"""
from collections import deque
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
chart = []
dig = [(1,0),(0,1),(-1,0),(0,-1)]

for _ in range(r):
    chart.append(list(input()))
    
q = deque()
q.append([sy - 1, sx - 1, 0])
while q:
    y, x, d = q.popleft()
    if chart[y][x] == '#':
        continue
    if y == gy - 1 and x == gx - 1:
        print(d)
        break
    chart[y][x] = '#' #戻れないようにする
    for i, j in dig:
        nexty = y + i
        nextx = x + j
        q.append([nexty, nextx, d + 1])
    