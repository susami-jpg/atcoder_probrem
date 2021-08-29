# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:07:41 2021

@author: kazuk
"""

from math import floor
a, b, n = map(int, input().split())
x = min(n, b-1)
ans = floor((a*x)/b)
print(ans)
