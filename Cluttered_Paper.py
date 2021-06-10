# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:10:55 2021

@author: kazuk
"""

from itertools import accumulate
n = int(input())
xy  = [[0] * (10**3 + 2) for _ in range(10**3 + 2)]
#いもす法は加算or減算　=1ではない!!
for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    xy[ly][lx] += 1
    xy[ly][rx] -= 1
    xy[ry][lx] -= 1
    xy[ry][rx] += 1

    
xy_t = [list(x) for x in zip(*xy)]
def accum(xy):
    new = []
    for col in xy:
        col = list(accumulate(col))
        new.append(col)
    return new

xy_t = accum(xy_t)
xy = [list(x) for x in zip(*xy_t)]
xy = accum(xy)

ans = [0] * n
for row in xy:
    for i in row:
        if i == 0:
            continue
        ans[i - 1] += 1

for a in ans:
    print(a)
    
