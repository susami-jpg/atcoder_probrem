# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:04:18 2021

@author: kazuk
"""

from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)
input = stdin.readline

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

#dfs(v, c)は頂点vをc色に塗った時に矛盾がないかを判定する
#n個の頂点の色を初期化。0:未着色、1:黒、-1:白
color = [0] * n
def dfs(v, c):
    color[v] = c
    for nextv in edge[v]:
        #隣接頂点が同じ色なら矛盾
        if color[nextv] == c:
            return False
        #隣接頂点を違う色に塗った場合の評価がFalseなら矛盾
        if color[nextv] == 0 and not dfs(nextv, -c):
            return False
    #矛盾がなければTrue
    return True

def is_bipartite():
    return dfs(0, 1) #頂点0を黒(1)に塗ってdfs開始

#二部グラフの場合
#ひとつのグループからもう一つのグループに移動するのに奇数長のパスが存在する
#つまり二つのグループからひとつづつ頂点を選んで距離1のパスを引けば距離3のパスを引ける回数を出せる
if is_bipartite():
    black = color.count(1)
    white = color.count(-1)
    ans = black * white - m
    print(ans)

#二部グラフでない場合
#奇数長のサイクルが存在する
# -> 任意の二点について必ず偶数でも奇数でも行けるパスが存在する
#この中からすでに距離1でつながっている二点の組み合わせ(m種類)を引けばよい
else:
    ans = n * (n-1) // 2 - m
    print(ans)
    
    