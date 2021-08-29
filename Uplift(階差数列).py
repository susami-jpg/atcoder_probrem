# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:07:21 2021

@author: kazuk
"""

n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (n + 1)
ans = 0
for i in range(1, n):
    ans += abs(a[i] - a[i-1])
    b[i] = a[i] - a[i-1]

for _ in range(q):
    l, r, v = map(int, input().split())
    mae = abs(b[l-1]) + abs(b[r])
    if l-1 >= 1:
        b[l-1] += v
    if r <= n - 1:
        b[r] -= v
    ato = abs(b[l-1]) + abs(b[r])
    ans += (ato - mae)
    print(ans)


    
    
