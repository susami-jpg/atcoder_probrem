# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:04:54 2021

@author: kazuk
"""

from collections import deque
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1

maze = []
for _ in range(r):
    maze.append(list(input()))
dxdy = [(0,1),(1,0),(-1,0),(0,-1)]
q = deque()
visited = [[0] * c for _ in range(r)]
q.append((sy, sx, 0, visited))
while q:
    y, x, d, visited = q.popleft()
    if y == gy and x == gx:
        print(d)
        break
    if visited[y][x] == 1:
        continue
    visited[y][x] = 1
    for a, b in dxdy:
        nexty = y + b
        nextx = x + a
        if maze[nexty][nextx] == '.':
            q.append((nexty, nextx, d + 1, visited))


            
    
