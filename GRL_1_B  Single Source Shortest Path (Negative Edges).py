# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:06:54 2021

@author: kazuk
"""


# O(EV)
#edgeは(from, to, cost)の順で情報を持った辺のリスト
#nは頂点数
n, m, r = map(int, input().split())
edge = []
for _ in range(m):
    f, t, c = map(int, input().split())
    edge.append((f, t, c))
    
def bellman_ford(s, edge, n):
    dist = [float('inf')]*n # 各頂点への最小コスト
    dist[s] = 0 # 自身への距離は0
    for i in range(n):
        update = False # 更新が行われたか
        for f, t, cost in edge:
            if dist[t] > dist[f] + cost:
                dist[t] = dist[f] + cost
                update = True
        if not update:
            break
        # 負閉路が存在(n回の更新)
        #(for分の内側なのでn回目の更新があればここまで来ない)
        if i == n-1:
            return False
    return dist

dist = bellman_ford(r, edge, n)
if not dist:
    print("NEGATIVE CYCLE")
else:
    for v in range(n):
        if dist[v] == float('inf'):
            print("INF")
        else:
            print(dist[v])
            
    