# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:00:50 2021

@author: kazuk
"""

n, q = map(int, input().split())
a = list(map(int, input().split()))
shift = 0
for _ in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    xs = x-shift
    ys = y-shift
    if xs < 0:
        xs += n
    if ys < 0:
        ys += n
    if t == 1:
        a[xs], a[ys] = a[ys], a[xs]
    elif t == 2:
        shift += 1
    else:
        print(a[xs])


    