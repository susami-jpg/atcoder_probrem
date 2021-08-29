# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:21:23 2021

@author: kazuk
"""

from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
move = list(accumulate(a))
now = [0] * n
now[0] = a[0]
for i in range(1, n):
    now[i] = now[i-1] + move[i]
ans = 0
maxmove = 0
for i in range(n-1):
    maxmove = max(maxmove, move[i])
    ans = max(ans, now[i] + maxmove)
  
ans = max(ans, now[-1])
print(ans)
    