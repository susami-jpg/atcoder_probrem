# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:34:07 2021

@author: kazuk
"""

from collections import deque
h, w = map(int, input().split())
block = [["#"] * (w + 2)]
maze = block + [["#"] + list(input()) + ["#"] for _ in range(h)] + block
deq = deque()
dist = [[-1] * (w + 2) for _ in range(h + 2)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if maze[i][j] == "s":
            sy, sx = i, j
            dist[sy][sx] = 0
            deq.append((i, j))
        if maze[i][j] == "g":
            gy, gx = i, j
            maze[i][j] = "."

dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while deq:
    y, x = deq.popleft()
    for a, b in dxdy:
        nexty, nextx = y + a, x + b
        if 0 <= nexty <= h + 1 and 0 <= nextx <= w + 1:
            if maze[nexty][nextx] == "." and dist[nexty][nextx] == -1:
                dist[nexty][nextx] = dist[y][x]
                deq.appendleft((nexty, nextx))
            elif maze[nexty][nextx] == "#" and dist[nexty][nextx] == -1:
                dist[nexty][nextx] = dist[y][x] + 1
                deq.append((nexty, nextx))
                    
ans = dist[gy][gx]
if ans == -1 or ans >= 3:
    print("NO")
else:
    print("YES")
    