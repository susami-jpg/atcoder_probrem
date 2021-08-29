# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:27:49 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))

maxi = a[0]
ans = 0
for i in range(1, n):
    if maxi > a[i]:
        ans += maxi - a[i]
    maxi = max(maxi, a[i])

print(ans)
