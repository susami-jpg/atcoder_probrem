# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:48:10 2021

@author: kazuk
"""

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def chmax(a, b):
    if a >= b:
        return a
    else:
        return b

#メモ化再帰
def memo():
    #頂点数n、辺数m
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    #0-indexedに変更
    for _ in range(m):
        x, y = map(int, input().split())
        edge[x - 1].append(y - 1)
        
    # dp[v] := ノードvを始点とした時の有向パスの長さの最大値
    # -1 未訪問で初期化。
    dp = [-1] * n
    
    #関数recはノードvを始点としたときの有向パスの長さの最大値を返す関数
    def rec(v):
        if dp[v] != -1:
            return dp[v]
        ans = 0
        for nextv in edge[v]:
            ans = chmax(ans, rec(nextv) + 1)
        dp[v] = ans
        return dp[v]
    
    #有効グラフ全体としての最長パスを見つける
    ans = 0
    for v in range(n):
        ans = chmax(ans, rec(v))   
    print(ans)

#トポロジカルソート
from collections import deque

def topological():
    n, m = map(int, input().split())
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
    
    while que:
        v = que.popleft()
        topo.append(v)
        for nextv in edge[v]:
            #辺(v, nextv)をグラフから削除する
            deg[nextv] -= 1
            if deg[nextv] == 0:
                que.append(nextv)
            #最初に入力辺を持たなかった点からの距離
            dp[nextv] = chmax(dp[nextv], dp[v] + 1)
    
    print(max(dp))
    print(topo)
    