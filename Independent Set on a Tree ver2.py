# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:10:47 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10**7)
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

ans1 = []
ans2 = []
def dfs(v, par, c):
    if c:
        ans1.append(v+1)
    else:
        ans2.append(v+1)
    for nextv in edge[v]:
        if nextv == par:continue
        dfs(nextv, v, 1-c)
    return

dfs(0, -1, 1)
if len(ans1) > len(ans2):
    ans = ans1
else:
    ans = ans2
print(*ans[:n//2])

    