# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:33:47 2021

@author: kazuk
"""

from collections import deque
m, n = map(int, input().split())
maze = [["1"] * (m + 2)]
for i in range(n):
    inp = list(str(input()).replace(" ", ""))
    if "s" in inp:
        sy = i + 1
        sx = inp.index("s") + 1
    if "g" in inp:
        gy = i + 1
        gx = inp.index("g") + 1
    maze.append(["1"] + inp + ["1"])
maze.append(["1"] * (m + 2))

deq = deque()
deq.append((sy, sx, 0))
ans = 10 ** 10
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
seen = [[0] * (m + 2) for _ in range(n + 2)]
while deq:
    y, x, d = deq.popleft()
    if y == gy and x == gx:
        ans = min(ans, d)
    if seen[y][x]:
        continue
    seen[y][x] = 1
    for a, b in dxdy:
        nextx = x + a
        nexty = y + b
        if maze[nexty][nextx] == "0" or maze[nexty][nextx] == "g":
            deq.append((nexty, nextx, d + 1))
if ans == 10 ** 10:
    print("Fail")
else:
    print(ans)
    
        
    
