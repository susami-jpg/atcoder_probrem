# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:13:04 2021

@author: kazuk
"""

n, m = map(int, input().split())
switch = []
for _ in range(m):
    k = list(map(int, input().split()))
    switch.append(k[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(1 << n):
    light = [0] * m
    for j in range(n):
        if (i >> j) & 1:
            for l in range(m):
                if (j + 1) in switch[l]:
                    light[l] += 1
    for r in range(m):
        if light[r] % 2 != p[r]:
            break
    else:
        ans += 1
print(ans)
            
                    
            
            
    
    