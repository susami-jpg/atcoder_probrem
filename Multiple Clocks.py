# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 12:20:01 2021

@author: kazuk
"""

from sys import exit
from math import gcd

# 2数を受け取って最小公倍数を返す関数
def lcm(a, b):
    y = a*b // gcd(a, b)
    return int(y)

# 可変引数を受け取って最小公倍数を返す関数
import functools

def lcm_2(*vals):
    return functools.reduce(lcm, vals)

n = int(input())
T = [int(input()) for _ in range(n)]
if n == 1:
    print(T[0])
    exit()
ans = lcm_2(*T)
print(ans)
