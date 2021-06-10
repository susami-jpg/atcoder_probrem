# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:18:15 2021

@author: kazuk
"""
inf = 10 ** 10
V, e = map(int, input().split())
#costにグラフの重みを記録、行が始点、列が終点を示し、edge[s][t] = dで表される
#存在しない経路はinfでふさぐ
cost = [[inf] * V for _ in range(V)]

for _ in range(e):
    s, t, d = map(int, input().split())
    cost[s][t] = d

#dp[S][v]:集合Sに含まれる点を全て通り、現在頂点vにいるときの最短距離を表す
#未訪問、訪問の判断はフラグ-1でできる
#1 << v　は2**vと同じ
#dpは列が訪問状態(集合S)を表し、現在地点を行(v)で示す
#現在地点は当然0~v-1のどれかなので、v通り
#集合Sは各頂点を行った/行ってないのbitで表せるので2**v通り

dp = [[-1] * V for _ in range(1 << V)]

#dfs(S, v, dp)は、訪問済み集合Sと現在地点vと最短距離を記録するdpを受け取り、
#集合Sに含まれる頂点を訪問したうえで再び頂点vまでの最短距離を返す関数
def dfs(S, v, dp):
    #頂点vを訪問済みの場合
    #これは集合Sに含まれる点を全て通り、現在頂点vにいるときの最短距離がわかっているのでdp[S][v]を返す
    if dp[S][v] != -1:
        return dp[S][v]
    
    #全ての頂点を訪問してスタート地点(v = 0)に戻ってきた場合
    #S = 11111....1(v行)
    if S == (1 << V) - 1 and v == 0:
        return 0 #もう動く必要はない
    
    #訪問済みの頂点以外が訪問する頂点の候補となるので記録Sを解読し、未訪問の頂点uを得る
    res = inf
    for u in range(V):
        #頂点uが未訪問だった場合
        if (S >> u) & 1 == 0:
            res = min(res, dfs(S|1<<u, u, dp) + cost[v][u])
    #未訪問の頂点の候補をひとつづつ探索し、それぞれの距離を計算
    #最短距離resが求まるのでdpに記録
    dp[S][v] = res
    return res

# 頂点0からスタートする。ただし頂点0は未訪問とする
ans = dfs(0, 0, dp)
if ans == inf:
    print(-1)
else:
    print(ans)
    
    