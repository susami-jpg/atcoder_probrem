# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:18:32 2021

@author: kazuk
"""

n = int(input())
light = list(map(int, input().split()))
row = [0, 0]
part = 1
prev = light[0]
for i in range(1, n):
    now = light[i]
    if prev == now:
        row.append(part)
        part = 1
    else:
        part += 1
    prev = now
row.append(part)

for _ in range(2):
    row.append(0)

ans = 0
for i in range(len(row) - 2):
    cnd = row[i] + row[i + 1] + row[i + 2]
    if ans < cnd:
        ans = cnd

print(ans)
    
        
    
    