# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:59:21 2021

@author: kazuk
"""

from collections import deque
def main():
    h, w = map(int, input().split())
    kabe = [["#"] * (w + 2)]
    maze = kabe + [["#"] + list(input()) + ["#"] for _ in range(h)] + kabe
    dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    teleport = [[] for _ in range(26)]
    
    for i in range(1, h+1):
        for j in range(1, w+1):
            if maze[i][j] == "S":
                sy, sx = i, j
            elif maze[i][j] == "G":
                gy, gx = i, j
            elif maze[i][j].islower():
                teleport[ord(maze[i][j]) - 97].append((i, j))
    
    deq = deque()
    deq.append((sy, sx))
    ans = -1
    dist = [[10**10] * (w + 2) for _ in range(h + 2)]
    dist[sy][sx] = 0
    #超頂点に来た時のコスト
    dist_t = [10**10] * 26
    
    while deq:
        y, x = deq.popleft()
        #超頂点からの移動(コスト0)
        if x == -1:
            cost = dist_t[y]
            for i, j in teleport[y]:
                if cost < dist[i][j]:
                    dist[i][j] = cost
                    deq.appendleft((i, j))
        #普通の移動(コスト1、超頂点への移動も含む)
        else:
            if maze[y][x] == "#":continue
            cost = dist[y][x] + 1
            for i, j in dxdy:
                nexty, nextx = y + i, x + j
                if cost < dist[nexty][nextx]:
                    dist[nexty][nextx] = cost
                    deq.append((nexty, nextx))
            #超頂点への移動が可能な場合(ワープできる場合)
            if maze[y][x].islower():
                if cost < dist_t[ord(maze[y][x]) - 97]:
                    dist_t[ord(maze[y][x]) - 97] = cost
                    deq.append((ord(maze[y][x]) -97, -1))
    
    ans = dist[gy][gx]
    if ans >= 10**10:
        ans = -1
    print(ans)

if __name__ == "__main__":
    main()
    
   