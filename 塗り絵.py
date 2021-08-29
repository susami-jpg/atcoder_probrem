# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:25:24 2021

@author: kazuk
"""

from sys import setrecursionlimit, stdin
input = stdin.readline
setrecursionlimit(10**7)
n = int(input())
mod = 10**9+7
adj = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

#dp[v][color]: vをcolor色で塗るときに(自分も含めた)部分木の塗り方の総数
dp = [[-1] * 2 for _ in range(n)]

def dfs(v, par, color):
    if dp[v][color] != -1:
        return dp[v][color]
    
    cnt = 1
    for child in adj[v]:
        if child == par:continue
        if color == 0:
            cnt *= (dfs(child, v, 0) + dfs(child, v, 1))
        else:
            cnt *= dfs(child, v, 0)
        cnt %= mod
    
    dp[v][color] = cnt
    return cnt

dfs(0, -1, 0)
dfs(0, -1, 1)
ans = dp[0][0] + dp[0][1]
ans %= mod
print(ans)
