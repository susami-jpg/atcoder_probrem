# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:29:25 2021

@author: kazuk
"""

a, b, c = map(int, input().split())
right = pow(c, b)
if a < right:
    print('Yes')
else:
    print('No')