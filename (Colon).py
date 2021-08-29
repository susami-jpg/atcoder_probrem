# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:05:35 2021

@author: kazuk
"""

from math import sqrt, cos, radians
a, b, h, m = map(int, input().split())
t = 60*h + m
C = abs(0.5*t%360 - 6*t%360)
c = sqrt(a**2 + b**2 - 2*a*b*cos(radians(C)))
print(c)
