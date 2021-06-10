# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:54:51 2021

@author: kazuk
"""

import functools
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def gcd(nums):
    return functools.reduce(euclid, nums)


a, b, c = map(int, input().split())
r = gcd([a, b, c])
ans = (a // r - 1) + (b // r - 1) + (c // r - 1)
print(ans)
