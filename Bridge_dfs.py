# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:50:55 2021

@author: kazuk
"""

# input
N, M = map(int, input().split())
edge_lst = [list(map(int, input().split())) for i in range(M)]

adj_matrix = {} # グラフを辺列挙 -> 隣接行列に変換

# 頂点の数がN, 辺の数がM,
for i in range(1, N + 1):
    adj_lst = []
    for j in range(M):
        if edge_lst[j][0] == i:
            adj_lst.append(edge_lst[j][1])
        if edge_lst[j][1] == i:
            adj_lst.append(edge_lst[j][0])
    adj_matrix[i] = adj_lst

# root: 葉を探索中の根
# next: 次に探索される葉
# count: 探索回数
# order[1,...,N]: 頂点iが探索された順番
# low[1,...,N]: 頂点iから訪問可能な頂点のうち、最も上にある頂点の探索順

def dfs_bridge(graph, root, next, count, low, order, bridges): # graphは隣接行列表示
    count += 1
    order[next] = count
    low[next] = order[next]

    for w in graph[next]: # vと隣接している頂点
        if order[w] == -1: # wは未訪問
            dfs_bridge(graph, next, w, count, low, order, bridges)

            low[next] = min(low[next], low[w])
            if low[w] == order[w]: # 頂点w以降から頂点v以前に戻れない
                bridges.append((next, w))
        elif w != root: # 一つ前の頂点（自明に戻れる頂点）より前に戻れる場合
            low[next] = min(low[next], order[w])

def get_bridges(graph):
    bridges = []
    count = 0
    low = {n: -1 for n in graph.keys()}
    order = low.copy()

    for n in graph.keys():
        dfs_bridge(graph, n, n, count, low, order, bridges)
    
    return(bridges) # 橋 = (node, node)のタプルのリスト
            
ans = get_bridges(adj_matrix)
print(len(ans))
    

  