# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:23:04 2021

@author: kazuk
"""

from itertools import accumulate
from sys import exit
n, w = map(int, input().split())
lim = 2 * 10 ** 5 + 1
acc = [0] * lim

for _ in range(n):
    s, t, p = map(int, input().split())
    acc[s] += p
    acc[t] -= p

if acc[0] > w:
    print("No")
    exit()

for i in range(1, lim):
    acc[i] += acc[i-1]
    if acc[i] > w:
        print("No")
        break
else:
    print("Yes")
    
    