# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:07:12 2021

@author: kazuk
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = 0
for i in range(n):
    d += abs(a[i] - b[i])

if k >= d and (k - d) % 2 == 0:
    print('Yes')
else:
    print('No')
    