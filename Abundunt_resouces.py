# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:56:20 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
acopy = a[:]
for i in range(n - 1):
    a[i + 1] += a[i]
ans = []
for k in range(1, n):
    cnd = [a[i + k] - a[i] for i in range(n - k)]
    cnd.append(a[k - 1])
    ans.append(max(cnd))
ans.append(sum(acopy))

for i in ans:
    print(i)
    