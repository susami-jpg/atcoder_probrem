# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:34:07 2021

@author: kazuk
"""

from collections import deque
h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
deq = deque()
dist = [[-1] * w for _ in range(h)]

def valid(y, x):
    return 0<=y<=h-1 and 0<=x<=w-1

dist[0][0] = 0
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
out = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
deq.append((0, 0))
while deq:
    y, x = deq.popleft()
    for a, b in dxdy:
        nexty, nextx = y + a, x + b
        if valid(nexty, nextx):
            cost = dist[y][x]
            if maze[nexty][nextx] == "." and (dist[nexty][nextx] == -1 or dist[nexty][nextx] > cost):
                dist[nexty][nextx] = cost
                deq.appendleft((nexty, nextx))
    for a in range(-2, 3):
        for b in range(-2, 3):
            if (a, b) in out:continue
            nexty, nextx = y + a, x + b
            if valid(nexty, nextx):
                if (dist[nexty][nextx] == -1 or dist[nexty][nextx] > cost + 1):
                    dist[nexty][nextx] = cost + 1
                    deq.append((nexty, nextx))

ans = dist[-1][-1]
print(ans)

    