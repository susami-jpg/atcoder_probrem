# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 01:12:04 2021

@author: kazuk
"""
from collections import deque
n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n):
    v, k, *T = map(int, input().split())
    g[v] = T

q = deque()
d = [-1] * (n + 1)
t = 0
q.append((1, 0))

while q:
   now, time = q.popleft()
   if d[now] != -1:
       continue
   d[now] = time
   for i in g[now]:
       q.append((i, time + 1))
                
for i in range(1, n + 1):
    print(i, d[i])


        
        




