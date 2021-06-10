# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:04:21 2021

@author: kazuk
"""

from collections import deque
h, w, n = map(int, input().split())
maze = [['X'] * (w + 2)]
digit = [str(i) for i in range(1, 10)]

for i in range(h):
    t = list(input())
    for j in range(w):
        if t[j] == 'S':
            sx = j + 1
            sy = i + 1
    maze.append(['X'] + t + ['X'])
maze.append(['X'] * (w + 2))

dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(y, x, t, hp):
    q = deque()
    q.append((y, x, t))
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    while q:
        ny, nx, nt = q.popleft()
        if maze[ny][nx] == str(hp):
            return ny, nx, nt, hp + 1
        if visited[ny][nx] == 1:
            continue
        visited[ny][nx] = 1
        for a, b in dxdy:
            nexty = ny + b
            nextx = nx + a
            if maze[nexty][nextx] == 'X':
                continue
            q.append((nexty, nextx, nt + 1))

y = sy
x = sx
t = 0
hp = 1
while hp < n + 1:
    y, x, t, hp = bfs(y, x, t, hp)
print(t)
    
        
    
    

