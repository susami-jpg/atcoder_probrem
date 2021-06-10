# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:49:22 2021

@author: kazuk
"""

from collections import deque
deq = deque()
q = int(input())
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        deq.appendleft(x)
    elif t == 2:
        deq.append(x)
    else:
        print(deq[x-1])
