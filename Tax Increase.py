# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:01:52 2021

@author: kazuk
"""

a, b = map(int, input().split())
for x in range(1, 2000):
    c1 = (x*8)//100
    c2 = x//10
    if c1 == a and c2 == b:
        print(x)
        break
else:
    print(-1)
    