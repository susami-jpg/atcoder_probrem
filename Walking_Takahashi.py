# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 18:42:43 2021

@author: kazuk
"""

from math import floor
x, k, d = map(int, input().split())
if k%2 == 0:
    if x == 0:
        print(0)
    else:
        x = abs(x)
        y1 = floor(x/(2*d)) * 2
        y2 = y1 + 2
        cnd1 = abs(x - d * y1)
        cnd2 = abs(x - d * y2)
        if y1 > k:
            print(x - d * k)
        elif y2 > k:
            print(x - d * y1)
        else:
            print(min(cnd1, cnd2))
else:
    if x == 0:
        print(abs(x+d))
    else:
        x = abs(x)
        if x-d <= 0:
            print(abs(x-d))
        else:
            y1 = floor((x-d)/(2*d)) * 2 + 1
            y2 = y1 + 2
            cnd1 = abs(x - d * y1)
            cnd2 = abs(x - d * y2)
            if y1 > k:
                print(x - d * k)
            elif y2 > k:
                print(x - d * y1)
            else:
                print(min(cnd1, cnd2))
