# -*- coding: utf-8 -*-
"""
Created on Fri May 14 02:51:59 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10 ** 7)
n, m = map(int, input().split())
G = [[] for _ in range(n)]
Gr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    Gr[b-1].append(a-1)

seen = [1] * n
order = []
def dfs(v):
    seen[v] = 0
    for nextv in G[v]:
        if seen[nextv]:
            dfs(nextv)
    order.append(v)
    return

cnt = 0
def rdfs(v):
    seen[v] = 0
    global cnt
    cnt += 1
    for nextv in Gr[v]:
        if seen[nextv]:
            rdfs(nextv)
    return

for v in range(n):
    if seen[v]:
        dfs(v)

cnd = []
seen = [1] * n
for v in order[::-1]:
    cnt = 0
    if seen[v]:
        rdfs(v)
    cnd.append(cnt)

ans = 0
for i in cnd:
    ans += i*(i-1)//2

print(ans)
    
    
    
    
    