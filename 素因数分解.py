# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:02:09 2021

@author: kazuk
"""
from math import sqrt
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
        
print(f'{n}:', *ans)
