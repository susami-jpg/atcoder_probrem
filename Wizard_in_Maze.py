# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 23:50:25 2021

@author: kazuk
"""

from collections import deque
inf = 10 ** 10
h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
maze = [["#"] + list(input()) + ["#"] for _ in range(h)]
maze.insert(0, ["#"] * (w+2))
maze.append(["#"] * (w+2))

dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs01(sy, sx, gy, gx):
    deq = deque()
    deq.append((0, sy, sx))
    weight = [[-1] * (w+2) for _ in range(h+2)]
    while deq:
        wi, y, x = deq.popleft()
        if y == gy and x == gx:
            return wi
        if weight[y][x] != -1:
            continue
        weight[y][x] = wi
        for a, b in dxdy:
            nexty = y + a
            nextx = x + b
            if maze[nexty][nextx] == ".":
                deq.appendleft((wi, nexty, nextx))
        
        for i in range(-2, 3):
            for j in range(-2, 3):
                if (i, j) in dxdy:
                    continue
                nexty = y + i
                nextx = x + j
                if 1 <= nexty <= h and 1 <= nextx <= w and maze[nexty][nextx] == ".":
                    deq.append((wi+1, nexty, nextx))
    return -1

print(bfs01(ch, cw, dh, dw))



