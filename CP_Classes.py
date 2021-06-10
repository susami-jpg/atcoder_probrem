# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:30:32 2021

@author: kazuk
"""

from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
a.sort()
q = int(input())
for _ in range(q):
    b = int(input())
    i = bisect_left(a, b)
    if i == 0:
        print(abs(b - a[i]))
    elif i == n:
        print(abs(b - a[i - 1]))
    else:
        cnd1 = abs(b - a[i - 1])
        cnd2 = abs(b - a[i])
        print(min(cnd1, cnd2))
    
    