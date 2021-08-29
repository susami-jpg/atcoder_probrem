# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 14:06:50 2021

@author: kazuk
"""

a, b = input().split()
a = int(a)
b = int(b[0] + b[2] + b[3])
ans = a*b//100
print(int(ans))

