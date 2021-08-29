# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 18:22:19 2021

@author: kazuk
"""

import math
T = int(input())
L, X, Y = map(int, input().split())
q = int(input())


def dist(a, b, c, d, e, f):
    return math.sqrt((a-d)**2 + (b-e)**2 + (c-f)**2)

#sin -> 度
def asin_x(x):
    import math
    x = math.asin(x)
    return math.degrees(x)

for _ in range(q):
    e = int(input())
    rad = e*2*math.pi/T
    y = - (L/2) * math.sin(rad)
    z = (L/2) - (L/2) * math.cos(rad)
    d = dist(X, Y, 0, 0, y, z)
    ans = asin_x(z/d)
    print(ans)
    