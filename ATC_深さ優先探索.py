# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:52:00 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10**7)
h, w = map(int, input().split())
block = [["#"] * (w + 2)]
maze = [["#"] + list(input()) + ["#"] for _ in range(h)]
maze = block + maze + block

dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(1, h+1):
    for j in range(1, w+1):
        if maze[i][j] == "s":
            sy, sx = i, j
        if maze[i][j] == "g":
            gy, gx = i, j
            
seen = [[0] * (w + 2) for _ in range(h + 2)]
ans = "No"
def dfs(y, x):
    if seen[y][x] or maze[y][x] == "#":
        return
    if y == gy and x == gx:
        global ans
        ans = "Yes"
        return
    seen[y][x] = 1
    for a, b in dxdy:
        nexty = y + a
        nextx = x + b
        dfs(nexty, nextx)
    return

dfs(sy, sx)
print(ans)

        