# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 13:20:19 2021

@author: kazuk
"""
"""
s = input()
s = list(input())
n = int(input())
n, k = map(int, input().split())
a = list(map(int, input().split()))
"""

from collections import defaultdict
h, w = map(int, input().split())
grid = []

for _ in range(h):
    hl = list(map(int, input().split()))
    grid.append(hl)
    
ans = 1

for i in range(1, 1 << h):
    hs = 0
    cnd = []
    data = defaultdict(int)
    for j in range(h):
        if (i >> j) & 1:
            hs += 1
            cnd.append(grid[j])
    for j in range(w):
        for k in range(1, hs):
            if cnd[k-1][j] == cnd[k][j]:
                continue
            break
        else:
            data[cnd[0][j]] += hs
    data = dict(data)
    if len(data.values()):
        ans = max(ans, max(data.values()))
            
print(ans)

                
    
        
    
