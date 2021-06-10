# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 00:42:42 2021

@author: kazuk
"""

n, q = map(int, input().split())
par = [i for i in range(n)]
rank = [0] * n
def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        unite(x, y)
    else:
        if same(x, y):
            print(1)
        else:
            print(0)