# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:09:41 2021

@author: kazuk
"""

from math import sqrt

def dist(v1, v2):
    x1, y1, z1, r1 = v1
    x2, y2, z2, r2 = v2
    return sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) - (r1 + r2)

def find(x):
    if par[x] == x:
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

while True:
    n = int(input())
    if n == 0:
        break
    par = [i for i in range(n)]
    rank = [0] * n
    V = []
    for _ in range(n):
        x, y, z, r = map(float, input().split())
        V.append((x, y, z, r))
    
    cell = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = max(dist(V[i], V[j]), 0)
            cell.append((d, i, j))
    cell.sort()
    ans = 0
    
    for v in cell:
        d, i, j = v
        if same(i, j):
            continue
        ans += d
        unite(i, j)
    print('{:.3f}'.format(ans))
            
    
    
    
            
            
            

    