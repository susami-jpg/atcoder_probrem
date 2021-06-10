# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 01:28:29 2021

@author: kazuk
"""


n, m, k = map(int, input().split())
hq = []
for _ in range(m):
    a, b, c = map(int, input().split())
    hq.append((c, a, b))
hq.sort()
    

par = [i for i in range(n + 1)]
rank = [0] * (n + 1)
#「閉路ができる」＝「既に2点が繋がっているところに辺を作る」なのでUnionFind木で確認する。
#union find木の定義
#findはxの親を返す関数
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) #圧縮(findによる再帰呼び出しで一番上にいる親を見つけてpar[x]を更新)
        return par[x]
    
#sameはxとyが同じグループに所属しているかどうかをbool値で返す
def same(x, y):
    return find(x) == find(y)

#uniteはxとyを同じグループに結合する関数
def unite(x, y):
    x = find(x)
    y = find(y)
    #親が同じ場合
    if x == y:
        return
    #親が違う場合
    #yの所属するグループの大きさのほうが大きいとき
    #木の最大深さ（ランク）を記録しておく
    #Union時、ランクの低い方のグループを、高い方のグループにつなぐ
    #互いのランクが等しい場合を除き、ランクが高くならずに済む（等しい場合のみ1増える）
    if rank[x] < rank[y]:
        par[x] = y #xをyのグループに統合
    #xの所属するグループの大きさのほうが大きいとき
    else:
        par[y] = x #yをxのグループに統合
        #二つのグループの大きさが同じだった場合
        if rank[x] == rank[y]:
            rank[x] += 1

ans = 0
count = 0
while count < n - k:
    c, a, b = hq.pop(0)
    #同じグループに属しているかどうかを確認(属している=閉路を作る)
    if same(a, b):
        continue
    ans += c
    count += 1
    unite(a, b)

print(ans)
    
    