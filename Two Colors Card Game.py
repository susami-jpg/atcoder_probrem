# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:00:02 2021

@author: kazuk
"""

from collections import defaultdict
n = int(input())
b = []
r = []
blue = defaultdict(int)
for _ in range(n):
    s = input()
    blue[s] += 1
    b.append(s)
m = int(input())
red = defaultdict(int)
for _ in range(m):
    s = input()
    red[s] += 1

ans = 0
for s in set(b):
    cnd = blue[s] - red[s]
    ans = max(ans, cnd)
print(ans)

    