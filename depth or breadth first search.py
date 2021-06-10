# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:12:56 2021

@author: kazuk
"""
#両端キュー(deque)を使えるようにする。popで後ろから、popleftで前から要素を取り出す。
#from collections import deque

#D = deque() 

#深さ優先探索(スタック)：一つの節点を探索した後は、その子以下の節点を探索し終わるまで隣りの節点には移らない。
#2分木Tに一つの接点に対して、その節点を格納できるスタックSを用いた以下のアルゴリズムを考える。
#1 Tの根をSにプッシュする。
#2 Sが空でないなら以下3~6を繰り返す。
#3   Sからポップしたデータをaと呼ぶ。
#4   aの値と「,」を出力する。
#5   aに左の子があれば、その節点をSにプッシュする。
#6   aに右の子があれば、その節点をSにプッシュする。

#幅優先探索(キュー)
#2分木Tに一つの接点に対して、その節点を格納できるキューQを用いた以下のアルゴリズムを考える。
#1 Tの根をQにエンキューする。
#2 Qが空でないなら以下3~6を繰り返す。
#3   Qからデキューしたデータをaと呼ぶ。
#4   aの値と「,」を出力する。
#5   aに左の子があれば、その節点をQにエンキューする。
#6   aに右の子があれば、その節点をQにエンキューする。

from collections import deque

#深さ優先探索
def depth_first_search(T):
    S = deque()
    if len(T) > 0:
        S.append(T)#;show(D)
    while len(S) > 0:
        L, a, R = S.pop()
        print(a, end = ',')#;show(D)
        if len(L) > 0:
            S.append(L)#;show(D)
        if len(R) > 0:
            S.append(R)#;show(D)  
    print()

#タイムスタンプあり参考
N = int(input())
adj = [[] for i in range(N)]
for n in range(N):
    V = list(map(int, input().split()))
    for v in V[2:]: # u,k,v1,v2,...
        adj[n].append(v-1)
d = [0] * N # 発見時刻
f = [0] * N # 完了時刻

def dfs(v, t):
    t+=1 # 発見したらインクリメント
    d[v] = t
    for next in adj[v]:
        if d[next] == 0: # 未発見なら
            t = dfs(next, t)
    t+=1 # 完了してもインクリメント
    f[v] = t
    return t

t = 0
for n in range(N):
    if d[n]==0: # 未発見なら
        t = dfs(n,t)
    print (n+1,d[n],f[n])
    
#自分の子のノードを数える(自分も含む)参考
dp = [0] * n
seen = [1] * n

def dfs(v, t):
    seen[v] = 0
    t += 1
    for nextv in adj[v]:
        if seen[nextv]:
            t += dfs(nextv, 0)
    dp[v] = t
    return t

for v in range(n):
    if seen[v]:
        dfs(v, 0)
        

    
#幅優先探索
def breadth_first_search(T):
    Q = deque()
    if len(T) > 0:
        Q.append(T)#;show(D)
    while len(Q) > 0:
        L, a, R = Q.popleft()
        print(a, end = ',')#;show(D)
        if len(L) > 0:
            Q.append(L)#;show(D)
        if len(R) > 0:
            Q.append(R)#;show(D)
    print()
    
def show(D):
    print('[', end = '') #空白をあけない、改行しない。
    for (L, a, R) in D:
        print(a, end = '<-')
    print(']')
    
    
        