# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 10:20:02 2021

@author: kazuk
"""

n = int(input())
k = int(input())
maze = [list(input()) for _ in range(n)]
seen = set()
red_painted = []
ans = 0

def valid(y, x):
    return 0 <= y <= n-1 and 0 <= x <= n-1

def dfs():
    global ans
    #banmenは現在の赤く塗られた盤面の状態を整数であらわす
    #赤く塗られた箇所をsortして二桁ごとに持つことで固有の盤面の状態を保存
    banmen = sum([val * 100**i for i, val in enumerate(sorted(red_painted))])
    #探索済みなら終了
    if banmen in seen:
        return 
    
    seen.add(banmen)
    
    #赤く塗られた箇所がk個であれば、ansに加算して探索終了
    red_num = len(red_painted)
    if red_num == k:
        ans += 1
        return
    
    dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for red_grid in red_painted:
        y = red_grid // n
        x = red_grid % n
        for a, b in dxdy:
            nexty, nextx  = y + a, x + b
            next_int = nexty * n + nextx
            if valid(nexty, nextx) and maze[nexty][nextx] == "." and next_int not in red_painted:
                red_painted.append(next_int)
                dfs()
                red_painted.pop()
    return


for i in range(n):
    for j in range(n):
        if maze[i][j] == ".":
            now = i*n + j
            red_painted = [now]
            dfs()
            red_painted.pop()

print(ans)


        
    
                  
    
    

