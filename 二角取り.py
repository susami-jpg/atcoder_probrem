# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 23:15:42 2021

@author: kazuk
"""

from collections import deque
h, w, n = map(int, input().split())
dx = [(0,1),(0,-1)]
dy = [(1,0),(-1,0)]
card = [[46] * (w + 2)]
for _ in range(h):
    c = list(map(ord, input().split()))
    card.append([46] + [int(i) for i in c] + [46])
card.append([46] * (w + 2))

def bfs(a1, b1, A1, B1):
    start = card[a1][b1]
    goal = card[A1][B1]
    if start != goal:
        return False
    deq = deque()
    deq.append((a1, b1, 2, 0))
    visited = [[3] * (w + 2) for _ in range(h + 2)]
    while deq:
        y, x, turn, cnt = deq.popleft()
        if cnt >= 3:
            continue
        if y == A1 and x == B1:
            return True
        if visited[y][x] <= cnt:
            continue
        visited[y][x] = cnt
        for a, b in dx:
            nextx = x + b
            nexty = y + a
            if 0 <= nextx <= w + 1 and 0 <= nexty <= h + 1:
                if card[nexty][nextx] == 46 or (nexty == A1 and nextx == B1):
                    if turn == 1:
                        deq.append((nexty, nextx, 0, cnt + 1))
                    else:
                        deq.append((nexty, nextx, 0, cnt))
        for a, b in dy:
            nextx = x + b
            nexty = y + a
            if 0 <= nextx <= w + 1 and 0 <= nexty <= h + 1:
                if card[nexty][nextx] == 46 or (nexty == A1 and nextx == B1):
                    if turn == 0:
                        deq.append((nexty, nextx, 1, cnt + 1))
                    else:
                        deq.append((nexty, nextx, 1, cnt))
    else:
        return False
                
            
for _ in range(n):
    a1, b1, A1, B1 = map(int, input().split())
    if bfs(a1, b1, A1, B1):
        print('yes')
    else:
        print('no')

    