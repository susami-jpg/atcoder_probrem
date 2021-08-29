# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:49:22 2021

@author: kazuk
"""

def extgcd(a: int, b: int) -> int:
    "ax + by = gcd(a,b) = d となる (x, y, d) を返す"
    if b == 0:
        return (1, 0, a)

    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y

    return s, t, d # (qb + r)s + bt = dとなる s, t, d

a, b = map(int, input().split())
x, y, d = extgcd(a, b)
print(x, y)
