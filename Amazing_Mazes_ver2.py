# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:04:29 2021

@author: kazuk
"""
while 1:
    from collections import deque
    w, h = map(int, input().split())
    if w == h == 0:
        break
    maze = []
    for _ in range(2 * h - 1):
        maze.append(list(map(int, input().split())))
    visited = [[0] * w for _ in range(h)]
    dxdy = [-1,1]
    q = deque()
    q.append((0,0,1))
    while q:
        y, x, d = q.popleft()
        if y == h - 1 and x == w - 1:
            print(d)
            break
        if visited[y][x] == 1:
            continue
        visited[y][x] = 1
        if 0 <= x + 1 <= w - 1:
            if maze[2 * y][x] == 0:
                q.append((y, x + 1, d + 1))
        if 0 <= x - 1 <= w - 1:
            if maze[2 * y][x - 1] == 0:
                q.append((y, x - 1, d + 1))
        if 0 <= y + 1 <= h - 1:
            if maze[2 * y + 1][x] == 0:
                q.append((y + 1, x, d + 1))
        if 0 <= y - 1 <= h - 1:
            if maze[2 * y - 1][x] == 0:
                q.append((y - 1, x, d + 1))
    else:
        print(0)
                

    