# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:45:15 2021

@author: kazuk
"""

from math import floor
n = int(input())
rest = 1000 - n
ans = 0
coin = [500, 100, 50, 10, 5, 1]
for c in coin:
    num = floor(rest/c)
    rest -= num * c
    ans += num
print(ans)
