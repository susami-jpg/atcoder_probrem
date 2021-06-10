# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:16:27 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10**7)
n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

dp = [0] * n
seen = [1] * n

def dfs(v, t):
    seen[v] = 0
    t += 1
    for nextv in adj[v]:
        if seen[nextv]:
            t += dfs(nextv, 0)
    dp[v] = t
    return t

for v in range(n):
    if seen[v]:
        dfs(v, 0)

ans = 0
for i in dp:
    ans += i * (n - i)
print(ans)
    
    