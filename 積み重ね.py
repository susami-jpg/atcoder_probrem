# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:48:23 2021

@author: kazuk
"""

from bisect import bisect_left
n = int(input())
max_w = 10**6 + 1
box = []
for _ in range(n):
    w = int(input())
    ind = bisect_left(box, w)
    if ind == len(box):
        box.append(w)
    else:
        box[ind] = w
print(len(box))
