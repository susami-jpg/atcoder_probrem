# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:55:05 2021

@author: kazuk
"""

from itertools import permutations
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

perm = permutations(range(1, n))

ans = 0
for p in perm:
    p = [0] + list(p)
    for i in range(1, n):
        if p[i] not in adj[p[i-1]]:
            break
    else:
        ans += 1

print(ans)



        
            
            
