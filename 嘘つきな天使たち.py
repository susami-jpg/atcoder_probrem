# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 00:32:29 2021

@author: kazuk
"""

from sys import setrecursionlimit, stdin, exit
setrecursionlimit(10**7)
input = stdin.readline
n = int(input())
edge = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    a -= 1
    edge[i].append(a)
    edge[a].append(i)

color = [0] * n
def dfs(v, c):
    color[v] = c
    for nextv in edge[v]:
        if color[nextv] == c:
            return False
        if color[nextv] == 0 and not dfs(nextv, -c):
            return False
    return True

def is_partite(i):
    return dfs(i, 1)


for i in range(n):
    if color[i] == 0:
        judge = is_partite(i)
        if not judge:
            print(-1)
            exit()

black = color.count(1)
ans = max(black, n-black)
print(ans)


