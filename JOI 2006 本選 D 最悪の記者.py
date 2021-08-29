# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:30:00 2021

@author: kazuk
"""

#トポロジカルソート
from collections import deque

def topological_sort():
    def chmax(a, b):
        if a >= b:
            return a
        else:
            return b
        
    n = int(input())
    m = int(input())
    
    edge = [[] for _ in range(n)]
    
    #各頂点の入力辺の本数を記録
    deg = [0] * n
    for _ in range(m):
        x, y = map(int, input().split())
        edge[x - 1].append(y - 1)
        deg[y - 1] += 1
    
    #入力辺を持たない頂点をqueueにいれる
    que = deque()
    for v in range(n):
        if deg[v] == 0:
            que.append(v)
    
    #各頂点の最初に入力辺を持たなかった点からの距離
    dp = [0] * n
    topo = []
    
    flg = 0
    while que:
        if len(que) > 1:
            flg = 1
        v = que.popleft()
        topo.append(v)
        for nextv in edge[v]:
            #辺(v, nextv)をグラフから削除する
            deg[nextv] -= 1
            if deg[nextv] == 0:
                que.append(nextv)
            #最初に入力辺を持たなかった点からの距離
            dp[nextv] = chmax(dp[nextv], dp[v] + 1)
    
    #閉路の場合-1を返す
    if len(topo) != n:
        return -1, -1
    else:
        return topo, flg

ans, flg = topological_sort()
if ans == -1:
    print(-1)
else:
    for i in ans:
        print(i+1)
    print(flg)
    
    
