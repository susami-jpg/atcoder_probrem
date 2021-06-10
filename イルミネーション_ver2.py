# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:39:37 2021

@author: kazuk
"""

from collections import deque
dxdy_odd = [(0, -1), (0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0)]
dxdy_even = [(0, -1), (0, 1), (1, -1), (1, 0), (-1, -1), (-1, 0)]
w, h = map(int, input().split())
ilmi = [[0] * (w + 2)]
for _ in range(h):
    ilmi.append([0] + list(map(int, input().split())) + [0])
ilmi.append([0] * (w + 2))
q = deque()
q.append([0, 0])
ans = 0
visited = [[1] * (w + 2) for _ in range(h + 2)]
while q:
    y, x = q.popleft()
    if visited[y][x] == 0:
        continue
    visited[y][x] = 0
    if y % 2 == 1:
        dxdy = dxdy_odd
    else:
        dxdy = dxdy_even
    for a, b in dxdy:
        nexty = y + a
        nextx = x + b
        if 0 <= nexty <= h + 1 and 0 <= nextx <= w + 1:
            if ilmi[nexty][nextx] == 1:
                ans += 1
            else:
                q.append((nexty, nextx))
print(ans)
