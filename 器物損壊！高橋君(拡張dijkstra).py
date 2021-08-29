# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:20:44 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
h, w = map(int, input().split())
maze = []
for i in range(h):
    row = list(input())
    if "s" in row:
        sy, sx = i, row.index("s")
    if "g" in row:
        gy, gx = i, row.index("g")
        row[gx] = "."
    maze.append(row)

INF = 10 ** 15
def valid(y, x):
    return 0 <= y <= h-1 and 0 <= x <= w-1

def ext_dijkstra(sy, sx, gy, gx):
    dist = [[INF] * w for _ in range(h)]
    fix = [[False] * w for _ in range(h)]
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dist[sy][sx] = 0
    hq = [(0, sy, sx)]
    while hq:
        _, y, x = heappop(hq)
        fix[y][x] = True
        for a, b in dxdy:
            nexty, nextx = y + a, x + b
            if not valid(nexty, nextx) or fix[nexty][nextx]:
                continue
            if maze[nexty][nextx] == ".":
                if dist[nexty][nextx] > dist[y][x]:
                    dist[nexty][nextx] = dist[y][x]
                    heappush(hq, (dist[nexty][nextx], nexty, nextx))
            if maze[nexty][nextx] == "#":
                if dist[nexty][nextx] > dist[y][x] + 1:
                    dist[nexty][nextx] = dist[y][x] + 1
                    heappush(hq, (dist[nexty][nextx], nexty, nextx))
    return dist[gy][gx]

ans = ext_dijkstra(sy, sx, gy, gx)
if ans <= 2:
    print("YES")
else:
    print("NO")
                    
    