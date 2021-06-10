# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:47:55 2021

@author: kazuk
"""

#pypyだとMLE
#pythonでAC
n = int(input())
row = []
prev = None
for i in range(1, n + 1):
    now = int(input())
    if i == 1:
        cnt = 1
    elif i % 2 == 1:
        if prev == now:
            cnt += 1
        else:
            row.append(cnt)
            cnt = 1    
    else:
        if prev == now:
            cnt += 1
        else:
            if row:
                cnt += row.pop()
            cnt += 1
    if i == n:
        last = now
    prev = now
row.append(cnt)
if len(row) % 2 == 1:
    row.insert(0, 0)
if last == 0:
    print(sum(row[::-2]))
else:
    print(sum(row[::2]))

    
        
        
    