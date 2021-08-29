# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 22:43:23 2021

@author: kazuk
"""

from math import sqrt, ceil
from sys import exit
n = int(input())
ans = []
nroof = int(sqrt(n))
now = n
if n % 2 == 0:
    while now % 2 == 0:
        ans.append(2)
        now /= 2
for i in range(3, nroof + 1):
    if i % 2 == 0:
        continue
    while now % i == 0:
        ans.append(i)
        now /= i
if now != 1:
    ans.append(int(now))

if len(ans) == 1:
    print(0)
    exit()
        
for i in range(30):
    if pow(2, i) >= len(ans):
        print(i)
        break
    

