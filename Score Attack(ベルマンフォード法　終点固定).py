# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:21:02 2021

@author: kazuk
"""

n, m = map(int, input().split())
edge = []
for _ in range(m):
    f, t, c = map(int, input().split())
    f -= 1
    t -= 1
    edge.append((f, t, -c))
    
def bellman_ford(s, edge, n):
    dist = [float('inf')]*n # 各頂点への最小コスト
    dist[s] = 0 # 自身への距離は0
    for i in range(n):
        for f, t, cost in edge:
            if dist[t] > dist[f] + cost:
                dist[t] = dist[f] + cost
        # 負閉路が存在(n回の更新)
        #(for分の内側なのでn回目の更新があればここまで来ない)
        #終点へのパスに負の経路が検出された場合にFalse
        #(終点へのdistのn回目の更新があった場合)
                if i == n-1 and t == n-1:
                    return False
    return dist

score = bellman_ford(0, edge, n)
if not score:
    print('inf')
else:
    print(-score[n-1])
    