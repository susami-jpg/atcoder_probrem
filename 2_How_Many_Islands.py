# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:13:38 2021

@author: kazuk
"""

import sys
sys.setrecursionlimit(10**6)
while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    chart = [[0] * (w + 2)]
    for _ in range(h):
        c = list(map(int, input().split()))
        chart.append([0] + c + [0])
    chart.append([0] * (w + 2))
    
    dxdy = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    def dfs(x, y):
        visited[x][y] = 1
        for (a, b) in dxdy:
            #x+=..とするとxの値が更新されてしまうので注意
            nextx = x + a
            nexty = y + b
            if chart[nextx][nexty] != 0 and visited[nextx][nexty] == 0:
                dfs(nextx, nexty)
        return 1
    
    ans = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if chart[i][j] == 1 and visited[i][j] == 0:
                ans += dfs(i, j)
    print(ans)
            

        