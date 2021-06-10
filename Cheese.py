# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:06:26 2021

@author: kazuk
"""
from collections import deque
h, w, n = map(int, input().split())
si = ['X'] * (w + 2)
chart = []
chart.append(si)
for i in range(h):
    row = ['X'] + list(input()) + ['X']
    if 'S' in row:
        sx = row.index('S')
        sy = i + 1
    chart.append(row)
chart.append(si)
dig = [(0,1),(1,0),(-1,0),(0,-1)]

#関数cheeseはスタートの座標とゴールのチーズ工場のチーズの硬さを受け取り、
#ゴール地点の座標とスタート地点からゴールまでの距離を返す
def cheese(sy, sx, goal):
     #visはいった場所を記録し、その場所のスタート地点からの距離を記録する
    vis = [[-1] * (w + 2) for _ in range(h + 2)]
    vis[sy][sx] = 0
    q = deque()
    q.append([sy, sx])
    while q:
        y, x = q.popleft()
        if chart[y][x] == goal:
            break
        for i, j in dig:
            nexty = y + i
            nextx = x + j
            if vis[nexty][nextx] == -1 and chart[nexty][nextx] != 'X':
                q.append([nexty, nextx])
                vis[nexty][nextx] = vis[y][x] + 1
    return y, x, vis[y][x]

ans = 0
for i in range(1, n + 1):
    sy, sx, d = cheese(sy, sx, str(i))
    ans += d
    
print(ans)


