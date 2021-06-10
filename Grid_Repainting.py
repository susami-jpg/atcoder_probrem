# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:49:39 2021

@author: kazuk
"""
from collections import deque
h, w = map(int, input().split())
maze = []
kabe = ['?'] * (w + 2)
kuro = 0
maze.append(kabe)
for _ in range(h):
    ma = ['?'] + list(input()) + ['?']
    kuro += ma.count('#')
    maze.append(ma)
maze.append(kabe)
visited = [[0] * (w + 2) for _ in range(h + 2)]
visited[1][1] = 1
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque()
q.append([1, 1, 1])
while q:
    y, x, d = q.popleft()
    if y == h and x == w:
        kuro += d
        print(h * w - kuro)
        break
    for i, j in dxdy:
        nexty = y + i
        nextx = x + j
        if visited[nexty][nextx] == 0 and maze[nexty][nextx] == '.':
            q.append([nexty, nextx, d + 1])
            visited[nexty][nextx] = 1
else:
    print(-1)
    
    
    


