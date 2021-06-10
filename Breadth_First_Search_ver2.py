# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:40:37 2021

@author: kazuk
"""

from collections import deque
n = int(input())
node = [[] for _ in range(n + 1)]
for _ in range(n):
    vinfo = list(map(int, input().split()))
    if len(vinfo) >= 3:
        v, k, nextv = vinfo[0], vinfo[1], vinfo[2:]
        node[v] += nextv

depth = [-1] * (n + 1)
q = deque()
q.append((1, 0))
while q:
    now, d = q.popleft()
    if depth[now] != -1:
        continue
    depth[now] = d
    for nextv in node[now]:
        q.append((nextv, d + 1))

for v, d in enumerate(depth):
    if v == 0:
        continue
    print(v, d)
        
    


    
    
    