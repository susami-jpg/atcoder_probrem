# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:42:43 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
maze = [list("#" + input() + "#") for _ in range(h)]
maze.insert(0, ["#"] * (w + 2))
maze.append(["#"] * (w + 2))
seen = [[0] * (w + 2) for _ in range(h + 2)]
dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#dfsは現在地点maze[y][x]と今まで動いた距離cntを記録し、スタート地点maze[sy][sx]に戻った時に今まで動いた距離の中で最も長い距離を返す関数
def dfs(y, x, sy, sx, cnt):
    #新たな地点に入ったらフラグをたてる
    seen[y][x] = 1
    #もしスタート地点に戻ってきているなら、その深さを返す
    #dfs(2, 3, 2, 3, 7)などはスタート地点に戻ってきたことを示す。この時cntを返し、たてたフラグも解除しておく。
    if y == sy and x == sx:
        seen[y][x] = 0
        return cnt
    
    #今まで動いた距離の最大値の更新
    num = -1
    for a, b in dxdy:
        nexty = y + a
        nextx = x + b
        if seen[nexty][nextx] or maze[nexty][nextx] == "#":
            continue
        num = max(num, dfs(nexty, nextx, sy, sx, cnt+1))
    seen[y][x] = 0
    
    return num
    
    
ans = 0
for sy in range(1, h + 1):
    for sx in range(1, w + 1):
        if maze[sy][sx] == "#":
            continue
        for a, b in dxdy:
            nexty = sy + a
            nextx = sx + b
            if maze[nexty][nextx] == "#":
                continue
            cnd = dfs(nexty, nextx, sy, sx, 1)
            ans = max(cnd, ans)

if ans <= 3:
    print(-1)
else:
    print(ans)
    