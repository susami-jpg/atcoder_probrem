# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:17:32 2021

@author: kazuk
"""
mod = 10 ** 5
from itertools import accumulate
n, m = map(int, input().split())
town = [0] * (n)
for i in range(1, n):
    town[i] = int(input())
town = list(accumulate(town))
now = 0
ans = 0
for i in range(m):
    day = int(input())
    nexttown = now + day
    if nexttown > now:
        ans += (town[nexttown] - town[now])
    else:
        ans += (town[now] - town[nexttown])
    now = nexttown
ans %= mod
print(ans)

    
    