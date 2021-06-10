# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:33:15 2021

@author: kazuk
"""

#部分点解法
from sys import stdin
#input = stdin.readline
w, n = map(int, input().split())
comp = []
lr = []
ans = 0
for _ in range(n):
    l, r = map(int, input().split())
    lr.append((l, r))
    comp.append(l)
    comp.append(r)
comp = list(set(comp))
comp.sort()
acc = [0] * len(comp)
for l, r in lr:
    li = comp.index(l)
    ri = comp.index(r)
    update = max(acc[li:ri + 1]) + 1
    for i in range(li, ri + 1):
        acc[i] = update
    print(update)

    


    
        
    
    
        
    