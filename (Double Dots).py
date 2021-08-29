# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:16:05 2021

@author: kazuk
"""

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

#dp[v]: 頂点vから頂点0に帰るための一回目の移動先
dp = [-1]*n

from collections import deque
deq = deque()
deq.append((0, -1))
while deq:
    v, par = deq.popleft()
    if dp[v] != -1:continue
    dp[v] = par
    for nextv in edge[v]:
        if dp[nextv] != -1:continue
        deq.append((nextv, v))


ans = dp[1:]
if -1 in ans:
    print("No")
else:
    print("Yes")
    for a in ans:
        print(a+1)
        
    

