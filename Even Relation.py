# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 18:11:28 2021

@author: kazuk
"""

from sys import setrecursionlimit, stdin
input = stdin.readline
setrecursionlimit(10**7)

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    w %= 2
    adj[u].append((v, w))
    adj[v].append((u, w))

color = [-1] * n

def dfs(v, c):
    if color[v] != -1:
        return
    color[v] = c
    for nextv, w in adj[v]:
        if w:
            dfs(nextv, 1-c)
        else:
            dfs(nextv, c)
    return

dfs(0, 0)

for c in color:
    print(c)
    
