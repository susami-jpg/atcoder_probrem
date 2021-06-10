# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:41:23 2021

@author: kazuk
"""
from collections import deque
w, h = map(int, input().split())
soto = [0] * (w + 2)
ilmi = []
ilmi.append(soto)
for _ in range(h):
    il = [0] + list(map(int, input().split())) + [0]
    ilmi.append(il)
ilmi.append(soto)
visited = [[0] * (w + 2) for _ in range(h + 2)]

even = [(-1, 0), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 0)]
odd = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]

q = deque()
q.append([0, 0])
ans = 0
while q:
    y, x = q.popleft()
    if visited[y][x] == 1:
        continue
    else:
        visited[y][x] = 1 #探索し終えたらフラグを立てる
        if y % 2 == 1:
            dxdy = odd
        else:
            dxdy = even
            for i, j in dxdy:
                nexty = y + i
                nextx = x + j
                if 0 <= nextx and nextx <= w + 1 and 0 <= nexty and nexty <= h + 1:
                        if ilmi[nexty][nextx] == 0:
                            q.append([nexty, nextx])
                        if ilmi[nexty][nextx] == 1:
                            ans += 1 #必要イルミネーション数のインクリメント
print(ans)      
    

    