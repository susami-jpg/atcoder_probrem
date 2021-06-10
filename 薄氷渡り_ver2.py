# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 06:47:53 2021

@author: kazuk
"""

import sys
sys.setrecursionlimit(10 ** 6)
m = int(input())
n = int(input())
chart = [[0] * (m + 2)]
for _ in range(n):
    chart.append([0] + list(map(int, input().split())) + [0])
chart.append([0] * (m + 2))
dxdy = [(0,1),(1,0),(-1,0),(0,-1)]
ans = 0
def dfs(x, y, d):
    #薄氷を割る
    chart[x][y] = 0
    global ans
    if ans < d:
        ans = d
    for a, b in dxdy:
        nextx = x + a
        nexty = y + b
        if chart[nextx][nexty] == 1:
            dfs(nextx, nexty, d + 1)
    #探索し終えたら薄氷復元
    chart[x][y] = 1
    return
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if chart[i][j] == 1:
            dfs(i, j, 1)
print(ans)
    


"""
以下のコードではWA
理由はある深さまで到達したときに戻ってほかの行き方を調べることができないから
再帰から抜けるときに、条件をもとに戻すことを忘れた。
再帰関数は以下のように実装したが、visited[i][j] = 0 が必要。

def dfs(x, y, cnt):
    visited[x][y] = 1
    global ans
    if cnt > ans:
        ans = cnt
    for a, b in dxdy:
        nextx = x + a
        nexty = y + b
        if visited[nextx][nexty] == 0 and chart[nextx][nexty] == 1:
            dfs(nextx, nexty, cnt + 1)
    return 

for i in range(1, n + 1):
    for j in range(1, m + 1):
        visited = [[0] * (m + 2) for _ in range(n + 2)]
        if chart[i][j] == 1:
            dfs(i, j, 1)
print(ans)
"""