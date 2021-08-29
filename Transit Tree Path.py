# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:08:37 2021

@author: kazuk
"""


from heapq import heappush, heappop
import sys # 入力高速化
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

def dijkstra(s, graph): # (始点, グラフのリスト)
    INF = 10 ** 18
    dist = [INF] * n # INF で初期化
    check = [False] * n # Bool
    dist[s] = 0
    q = [(0, s)] # （距離・ノード）
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue # すでに行っていたらcontinue
        check[v] = True # 訪問済み
        for i, j in graph[v]: # 先のノード・距離
            if check[i] != False: continue
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i)) # 必ず[0]が距離になるように（優先度付きキュー）
    return dist

q, k = map(int, input().split())
dist = dijkstra(k-1, graph)
for _ in range(q):
    x, y = map(int, input().split())
    print(dist[x-1] + dist[y-1])

