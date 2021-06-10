# -*- coding: utf-8 -*-
"""
Created on Wed May 26 14:50:17 2021

@author: kazuk
"""

n, k = map(int, input().split())

def g1(x):
    x = list(map(int, list(str(x))))
    x.sort(reverse=True)
    x = list(map(str, x))
    return int("".join(x))

def g2(x):
    x = list(map(int, list(str(x))))
    x.sort()
    x = list(map(str, x))
    return int("".join(x))

def f(g1, g2):
    return g1 - g2

ans = n
for _ in range(k):
    ans = f(g1(ans), g2(ans))
print(ans)


    