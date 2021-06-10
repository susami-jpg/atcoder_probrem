# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:06:40 2021

@author: kazuk
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = float('inf')
for i in range(1 << n):
    a_cnd = a[:]
    money = 0
    cnt = 1
    for j in range(n):
        if j == 0:
            continue
        if (i >> j) & 1:
            cnt += 1
            floor = max(a_cnd[:j])
            if floor >= a_cnd[j]:
                money += (floor - a_cnd[j]) + 1
                a_cnd[j] = floor + 1
    if cnt >= k:
        ans = min(ans, money)
print(ans)

            