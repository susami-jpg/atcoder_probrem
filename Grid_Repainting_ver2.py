# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:49:16 2021

@author: kazuk
"""

from collections import deque
h, w = map(int, input().split())
hw = [['#'] * (w + 2)]
white = 0
for _ in range(h):
    inp = list(input())
    white += inp.count('.')
    hw.append(['#'] + inp + ['#'])
hw.append(['#'] * (w + 2))

dxdy = [(0,1),(1,0),(0,-1),(-1,0)]
q = deque()
q.append((1,1,1))
visited = [[0] * (w + 2) for _ in range(h + 2)]
while q:
    y, x, d = q.popleft()
    if y == h and x == w:
        print(white - d)
        break
    if visited[y][x] == 1:
        continue
    visited[y][x] = 1
    for a, b in dxdy:
        nexty = y + b
        nextx = x + a
        if hw[nexty][nextx] == '.':
            q.append((nexty, nextx, d + 1))
else:
    print(-1)

    