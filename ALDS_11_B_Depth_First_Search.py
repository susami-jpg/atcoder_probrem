# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 17:39:11 2021

@author: kazuk
"""

import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
node = [[] for _ in range(n + 1)]
for _ in range(n):
    v, k, *nextv = map(int, input().split())
    node[v] += nextv

d = [-1] * (n + 1)
f = [-1] * (n + 1)
d[0] = 0
t = 0
def dfs(v, t):
    t += 1
    d[v] = t
    for nextv in node[v]:
        if d[nextv] == -1:
            t = dfs(nextv, t)
    t += 1
    f[v] = t
    return t

t = 0
for i in range(1, n + 1):
    if d[i] == -1:
        t = dfs(i, t)
    print(i, d[i], f[i])
    

    

    
    