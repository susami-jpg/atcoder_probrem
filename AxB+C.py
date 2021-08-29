# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:26:11 2021

@author: kazuk
"""

from math import floor, sqrt
n = int(input())

ans = 0
for a in range(1, floor(sqrt(n)) + 1):
    if floor((n-1) / a) - a >= 0:
        ans += (floor((n-1) / a) - a) * 2 + 1
print(ans)
    
    
        