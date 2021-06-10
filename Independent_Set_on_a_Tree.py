# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:15:17 2021

@author: kazuk
"""

from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10**7)
n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

set1 = []
set2 = []
seen = [0] * n

def bfs(v, flg):
    deq = deque()
    deq.append((v, flg))
    while deq:
        v, flg = deq.popleft()
        if seen[v] == 1:
            continue
        seen[v] = 1
        if flg:
            set2.append(v + 1)
            flg = 0
        else:
            set1.append(v + 1)
            flg = 1
        for nextv in adj[v]:
            deq.append((nextv, flg))
    return

def dfs(v, flg):
    seen[v] = 1
    if flg:
        set2.append(v + 1)
        flg = 0
    else:
        set1.append(v + 1)
        flg = 1
    for nextv in adj[v]:
        if seen[nextv]:
            continue
        dfs(nextv, flg)
    return

for i in range(n):
    if seen[i] == 0:
        dfs(i, 0)
if len(set(set1)) >= len(set(set2)):
    ans = list(set(set1))
else:
    ans = list(set(set2))
print(*ans[:n//2])







    
    
    