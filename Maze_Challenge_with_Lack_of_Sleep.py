# -*- coding: utf-8 -*-
"""
Created on Thu May 20 11:14:41 2021

@author: kazuk
"""
from collections import deque
h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [["#"] + list(str(input())) + ["#"] for _ in range(h)]
maze.insert(0, ["#"] * (w+2))
maze.append(["#"] * (w+2))
 
inf = 10 ** 10
#seen = [[0] * (w+2) for _ in range(h + 2)]
dist = [[[inf] * 4 for _ in range(w+2)] for _ in range(h + 2)]
deq = deque()
deq.append((sy, sx))
for i in range(4):
    dist[sy][sx][i] = 0
 
while deq:
    y, x = deq.popleft()
    #if seen[y][x]:
        #continue
    #seen[y][x] = 1
    for i in range(4):
        if i == 0:
            nextx = x-1
            nexty = y
        elif i == 1:
            nextx = x+1
            nexty = y
        elif i == 2:
            nextx = x
            nexty = y-1
        else:
            nextx = x
            nexty = y+1
        if maze[nexty][nextx] == "#":
            continue
        flg = 0
        for j in range(4):
            #進む方向と同じであれば前回のマスでその向きに向いている状態のdistを返す
            if i == j:
                if dist[y][x][i] < dist[nexty][nextx][j]:
                    dist[nexty][nextx][j] = dist[y][x][i]
                    flg = 1
            #上記の進行方向からそのほかの方向に向くにはコストが1加算される
            else:
                dist[nexty][nextx][j] = min(dist[y][x][i] + 1, dist[nexty][nextx][j])
        #前のマスから今のマスに移動するのにコストがかかったかどうか(方向転換したか判定)
        cost = min(dist[y][x]) - min(dist[nexty][nextx])
        
        #最小distの更新flgがあった場合deqに追加
        if flg:
            #コスト1ならdeqの後ろにつける
            if cost:
                deq.append((nexty, nextx))
            #コスト0ならdeqの前につける
            else:
                deq.appendleft((nexty, nextx))
 
print(min(dist[gy][gx]))
        
                
        
    
