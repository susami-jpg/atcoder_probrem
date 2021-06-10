# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 07:47:43 2021

@author: kazuk
"""
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
n = int(input())
node = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)
    
depth = [-1] * n
def dfs(v, d):
    depth[v] = d
    for nextv in node[v]:
        if depth[nextv] == -1:
            dfs(nextv, d + 1)
    return

dfs(0, 0)
maxdepth = max(depth)
maxv = depth.index(maxdepth)
depth = [-1] * n
dfs(maxv, 0)
print(max(depth) + 1)


    
    
    
    
#この問題は木構造
#木構造は以下のような性質がある
#頂点uから頂点vに行く単純パスはただひとつ
#頂点uとvを双方向に結ぶ辺を1本追加するとき、閉路は一つだけ出現し、長さはuからvの単純パス+1

#よってこの問題は単純パスの長さの最大値E(木の直径と呼ばれる)を求める問題に帰着できる
#木の直径を求めるには最短距離計算を二回やる
#木の直径をO(N)で求めるアルゴリズムは以下の通りである
#頂点1から各頂点までの最短距離を求める
#もっとも最短距離の大きい点をuとしてuから各頂点への最短距離を計算すると、もっとも最短距離が大きいものがEとなっている


"""
dfsやbfsではTLE(n**2)

def dfs(v, d):
    visited[v] = 1
    global ans
    if ans < d:
        ans = d
    for nextv in node[v]:
        if visited[nextv] == 0:
            dfs(nextv, d + 1)
    visited[v] = 0
    return

for i, v in enumerate(node):
    if len(v) == 1:
        dfs(i, 1)

print(ans)
"""

