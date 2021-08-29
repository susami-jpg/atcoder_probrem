# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 17:14:38 2021

@author: kazuk
"""

n, m = map(int, input().split())
rel = []
for _ in range(m):
    a, b = map(int, input().split())
    rel.append((b, a))

rel.sort()
r = rel[0][0]
ans = 1
for i in range(1, m):
    if r <= rel[i][1]:
        ans += 1
        r = rel[i][0]

print(ans)

    
