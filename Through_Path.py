# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 22:41:06 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10**7)
n = int(input())
adj = [[] for _ in range(n)]
a = []
b = []
for _ in range(n-1):
    ai, bi = map(int, input().split())
    a.append(ai-1)
    b.append(bi-1)
    adj[ai-1].append(bi-1)
    adj[bi-1].append(ai-1)

depth = [-1] * n
depth[0] = 0

def dfs(v, d):
    d += 1
    for nextv in adj[v]:
        if depth[nextv] != -1:
            continue
        depth[nextv] = d
        dfs(nextv, d)
    return

dfs(0, 0)

acc = [0] * n
q = int(input())
for _ in range(q):
    t, e, x = map(int, input().split())
    A, B = a[e-1], b[e-1]
    if t == 1:
        if depth[A] < depth[B]:
            acc[0] += x
            acc[B] -= x
        else:
            acc[A] += x
    else:
        if depth[A] < depth[B]:
            acc[B] += x
        else:
            acc[0] += x
            acc[A] -= x

seen = [1] * n
def accdfs(v):
    seen[v] = 0
    for nextv in adj[v]:
        if seen[nextv] and depth[nextv] > depth[v]:
            acc[nextv] += acc[v]
            accdfs(nextv)
    return

accdfs(0)

for v in acc:
    print(v)



    