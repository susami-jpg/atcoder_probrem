# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:07:58 2021

@author: kazuk
"""

from sys import setrecursionlimit, exit
setrecursionlimit(10**7)
sea = [[0] * 12]
maze = [[0] + [1 if i == "o" else 0 for i in list(input())] + [0] for _ in range(10)]
maze = sea + maze + sea
seen = [[0] * 12 for _ in range(12)]
dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(y, x):
    if seen[y][x] or maze[y][x] == 0:
        return
    seen[y][x] = 1
    for a, b in dxdy:
        nexty = y + a
        nextx = x + b
        dfs(nexty, nextx)
    return


for i in range(1, 11):
    for j in range(1, 11):
        if maze[i][j]:
            continue
        maze[i][j] = 1
        seen = [[0] * 12 for _ in range(12)]
        dfs(i, j)
        if maze == seen:
            print("YES")
            exit()
        maze[i][j] = 0

else:
    print("NO")
    