# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 01:51:27 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))

a.sort()
acc_a = a[:]
for i in range(1, n):
    acc_a[i] += acc_a[i-1]

ans = 0
for i in range(1, n):
    ans += a[i] * i - acc_a[i-1]

print(ans)
