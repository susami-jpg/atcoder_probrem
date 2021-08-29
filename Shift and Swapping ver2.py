# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:23:04 2021

@author: kazuk
"""

n, q = map(int, input().split())
a = list(map(int, input().split()))
shift = 0
for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        x -= 1
        y -= 1
        x = (x-shift)%n
        y = (y-shift)%n
        a[x], a[y] = a[y], a[x]
    if t == 2:
        shift += 1
    if t == 3:
        x -= 1
        ind = (x-shift)%n
        print(a[ind])
