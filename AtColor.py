# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 02:08:42 2021

@author: kazuk
"""

from itertools import accumulate
n = int(input())
color = [0] * (10 ** 6 + 2)
for _ in range(n):
    a, b = map(int, input().split())
    color[a] += 1
    color[b + 1] -= 1

color = list(accumulate(color))
print(max(color[:10 ** 6 + 1]))
