# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:05:25 2021

@author: kazuk
"""

h, w = map(int, input().split())
if h == 1 or w == 1:
    print(h * w)
else:
    hi = (h + 1) // 2
    wi = (w + 1) // 2
    print(hi * wi)