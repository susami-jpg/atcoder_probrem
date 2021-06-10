# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:31:48 2021

@author: kazuk
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1E+7))
n, q = map(int, input().split())
tree = [[] for _ in range(n + 1)] #リストのindexが頂点の番号を示し、リストの中身はその頂点につながる頂点を示す

for _ in range(n - 1):
    v, u = map(int, input().split())
    tree[v].append(u)
    tree[u].append(v)
    
counter = [0] * (n + 1)
checked = [False] * (n + 1)
            
action = []
for _ in range(q):
    p, x = map(int, input().split())
    action.append([p, x])
    counter[p] += x
    
#関数dfsは頂点pを受け取り頂点以下の部分木にその累積和を順に足していく
def dfs(parent):
    checked[parent] = True
    for child in tree[parent]:
        if checked[child]:
            continue
        counter[child] += counter[parent]
        dfs(child)

dfs(1)

for i in range(1, n + 1):
    print(counter[i])
    