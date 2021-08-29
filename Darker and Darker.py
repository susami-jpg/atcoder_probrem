# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:50:44 2021

@author: kazuk
"""


from collections import deque
h, w = map(int, input().split())

maze = [list(input()) for _ in range(h)]
dist = [[-1] * w for _ in range(h)]
deq = deque()
for i in range(h):
    for j in range(w):
        if maze[i][j] == "#":
            deq.append((i, j))
            dist[i][j] = 0

dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


while deq:
    y, x = deq.popleft()
    for a, b in dxdy:
        nexty = y + a
        nextx = x + b
        if 0 <= nexty <= h-1 and 0 <= nextx <= w-1:
            if maze[nexty][nextx] == "." and dist[nexty][nextx] == -1:
                dist[nexty][nextx] = dist[y][x] + 1
                deq.append((nexty, nextx))
                
    
ans = 0
for row in dist:
    ans = max(ans, max(row))
 
print(ans)




    
        
    
