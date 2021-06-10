# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:19:51 2021

@author: kazuk
"""

n = int(input())
ukv = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]

stack = []
time = 0
d = [0] * (n + 1)
f = [0] * (n + 1)

#関数dfsは頂点uと現在時刻tを受け取り、uにつながっている頂点をすべて探索し終わった時の時刻を返す
#function 深さ優先探索(v)
    #v に訪問済みの印を付ける
    #v を処理する
    #for each v に接続している頂点 i do
     #   if i が未訪問 then
      #      深さ優先探索(i)
def dfs(u, t):
    t += 1 #頂点uを発見したのでtをインクリメント
    d[u] = t
    while ukv[u][1] > 0:
        for v in ukv[u][2:]:
            ukv[u][1] -= 1 #探索候補数のデクリメント
            if d[v] == 0: #vが未発見の場合
                t = dfs(v, t) #探索し終わった時刻の更新
    t += 1
    #探索し終わったらtをインクリメント
    f[u] = t
    return t

for i in range(1, n + 1):
    if d[i]==0: # 未発見なら
        time = dfs(i,time)
    print (i, d[i], f[i])
    
                
                
