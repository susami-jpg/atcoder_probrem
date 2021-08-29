# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:36:20 2021

@author: kazuk
"""

h, w, k = map(int, input().split())
maze = [list(input()) for _ in range(h)]
ans = 0
for i in range(1 << h):
    row = []
    for a in range(h):
        if (i >> a) & 1:
            row.append(a)
    for j in range(1 << w):
        col = []
        for b in range(w):
            if (j >> b) & 1:
                col.append(b)
    
        cnt = 0
        for r in range(h):
            for c in range(w):
                if r in row or c in col:
                    continue
                if maze[r][c] == "#":
                    cnt += 1
        
        if cnt == k:
            ans += 1

print(ans)

        
                    