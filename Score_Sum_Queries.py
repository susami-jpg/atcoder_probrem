# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 00:43:42 2021

@author: kazuk
"""

from itertools import accumulate
n = int(input())
c1 = [0] * (n + 1)
c2 = [0] * (n + 1)
for i in range(1, n + 1):
    c, p = map(int, input().split())
    if c == 1:
        c1[i] = p
    else:
        c2[i] = p
c1 = list(accumulate(c1))
c2 = list(accumulate(c2))
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    print(c1[b] - c1[a - 1], c2[b] - c2[a - 1])
    

    