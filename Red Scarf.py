# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:38:23 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))

S = a[0]
for i in range(1, n):
    S ^= a[i]

ans = []
for i in range(n):
    ans.append(S ^ a[i])
print(*ans)
