# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:36:39 2021

@author: kazuk
"""

a, b, k = map(int, input().split())
if k <= a:
    print(a - k, b)
else:
    print(0, max(0, b - (k - a)))
