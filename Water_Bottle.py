# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 02:28:26 2021

@author: kazuk
"""

from math import atan, degrees
a, b, x = map(int, input().split())
harfvol = a * a * b / 2
if harfvol * 2 == x:
    print(0)
elif harfvol < x:
    ans = degrees(atan(a**3 / (2 * (a**2*b - x))))
    print(90 - ans)
else:
    ans = degrees(atan(2*x / (b**2 * a)))
    print(90 - ans)

