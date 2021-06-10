# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:19:40 2021

@author: kazuk
"""

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

road = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][j] > a[i][k] + a[k][j]:
                print(-1)
                break
        else:
            continue
        break
    else:
        continue
    break

else:
    s = set()
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(n):
                if (i, j) in s or i == k or j == k:
                    continue
                if a[i][j] != a[i][k] + a[k][j]:
                    road += a[i][j]
                s.add((i, j))
    print(road)
    
            
                
    