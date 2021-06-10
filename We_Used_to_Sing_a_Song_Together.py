# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:30:44 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 0
for ai, bi in zip(a, b):
    ans += abs(ai - bi)
print(ans)