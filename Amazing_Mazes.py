# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:17:00 2021

@author: kazuk
"""
from collections import deque
w, h = map(int, input().split())
maze = []
for _ in range(2 * h - 1):
    ma = list(map(int, input().split()))
    maze.append(ma)
if w and h:
    gps = [[0] * w for _ in range(h)]
    gps[0][0] = 1
    q = deque()
    q.append([0, 0, 1])


    while q:
        y, x, d = q.popleft()
        if y == h - 1 and x == w - 1:
            print(d)
            break
        
        #左に移動する場合
        dx = -1
        nextx = x + dx
        nexty = y
        if 0 <= nextx and nextx <= w - 1 and gps[nexty][nextx] == 0:
            #xの稼働領域内かと未訪問かどうかの確認
            mx = x + dx    
            my = 2 * y
            if maze[my][mx] == 0:
                #障壁があるかどうかの確認
                q.append([nexty, nextx, d + 1])
                #訪問済みのフラグ
                gps[nexty][nextx] = 1
        
        #右に移動する場合
        dx = 1
        nextx = x + dx
        nexty = y
        if 0 <= nextx and nextx <= w - 1 and gps[nexty][nextx] == 0:
            #xの稼働領域内かと未訪問かどうかの確認
            mx = x    
            my = 2 * y
            if maze[my][mx] == 0:
                #障壁があるかどうかの確認
                q.append([nexty, nextx, d + 1])
                #訪問済みのフラグ
                gps[nexty][nextx] = 1
                
        #上に移動する場合
        dy = -1
        nextx = x 
        nexty = y + dy
        if 0 <= nexty and nexty <= h - 1 and gps[nexty][nextx] == 0:
            #yの稼働領域内かと未訪問かどうかの確認
            mx = x    
            my = 2 * y + dy
            if maze[my][mx] == 0:
                #障壁があるかどうかの確認
                q.append([nexty, nextx, d + 1])
                #訪問済みのフラグ
                gps[nexty][nextx] = 1
                
        #下に移動する場合
        dy = 1
        nextx = x 
        nexty = y + dy
        if 0 <= nexty and nexty <= h - 1 and gps[nexty][nextx] == 0:
            #yの稼働領域内かと未訪問かどうかの確認
            mx = x    
            my = 2 * y + dy
            if maze[my][mx] == 0:
                #障壁があるかどうかの確認
                q.append([nexty, nextx, d + 1])
                #訪問済みのフラグ
                gps[nexty][nextx] = 1
    
    else:
        print(0)
    
   
    
    
                
    
        