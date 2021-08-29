# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 01:11:22 2021

@author: kazuk
"""

from sys import setrecursionlimit, stdin
setrecursionlimit(10**7)
input = stdin.readline
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

#dp[v]: vを根とする部分木を構成する頂点数
dp = [-1] * n

def dfs(v, par):
    if dp[v] != -1:
        return dp[v]
    cnt = 1
    for nextv in edge[v]:
        if nextv == par:continue
        cnt += dfs(nextv, v)
    dp[v] = cnt
    return cnt

dfs(0, -1)
ans = 0
for v in range(n):
    ans += dp[v] * (n - dp[v])
print(ans)
