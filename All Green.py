# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:37:10 2021

@author: kazuk
"""

d, g = map(int, input().split())
from math import ceil
prob = []
comp = []
for i in range(d):
    p, c = map(int, input().split())
    prob.append(p)
    comp.append(c)

ans = 10**15
for i in range(1 << d):
    cnt = 0
    point = 0
    used = [0] * d
    for j in range(d):
        if (i >> j) & 1:
            cnt += prob[j]
            point += (j + 1) * 100 * prob[j] + comp[j]
            used[j] = 1
    if point < g:
        for j in range(d-1, -1, -1):
            if used[j]:
                continue
            p_ceil = prob[j] - 1
            p_cnd = ceil((g-point)/(100*(j+1)))
            cnd = min(p_ceil, p_cnd)
            cnt += cnd
            point += cnd * 100 * (j + 1)
            if point >= g:
                break
    if point >= g:
        ans = min(ans, cnt)

print(ans)
