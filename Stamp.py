# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 02:27:58 2021

@author: kazuk
"""

from math import ceil
from sys import exit
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if m == 0:
    print(1)
    exit()
    
cnd = []
prev = 0
for i in a:
    w = i-prev-1
    if w != 0:
        cnd.append(w)
    prev = i
if n - i != 0:
    cnd.append(n-i)
if len(cnd) == 0:
    print(0)
    exit()
    
k = min(cnd)
ans = 0
for c in cnd:
    ans += ceil(c / k)
print(ans)
