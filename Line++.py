# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 01:22:01 2021

@author: kazuk
"""

from collections import defaultdict
n, x, y = map(int, input().split())
edge = [[] for _ in range(n)]
edge[x-1].append((y-1, 1))
edge[y-1].append((x-1, 1))
for i in range(n-1):
    edge[i].append((i+1, 1))
    edge[i+1].append((i, 1))

def dijkstra(s, graph): # (始点, グラフのリスト)
    from heapq import heappop, heappush
    INF = 10 ** 18
    dist = [INF] * n # INF で初期化
    check = [False] * n # Bool
    dist[s] = 0
    q = [(0, s)] # （距離・ノード）
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue # すでに行っていたらcontinue
        check[v] = True # 訪問済み
        for nextv, cost in graph[v]: # 先のノード・距離
            if check[nextv] != False: continue
            if dist[nextv] <= dist[v] + cost: continue
            dist[nextv] = dist[v] + cost
            heappush(q, (dist[nextv], nextv)) # 必ず[0]が距離になるように（優先度付きキュー）
    return dist

ans = defaultdict(int)
for s in range(n):
    dist = dijkstra(s, edge)
    for g in range(n):
        ans[dist[g]] += 1

for k in range(1, n):
    print(ans[k]//2)
    