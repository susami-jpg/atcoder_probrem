# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:03:11 2021

@author: kazuk
"""

from bisect import bisect_left
d = int(input())
n = int(input())
m = int(input())
tempo = [0]
for _ in range(n - 1):
    tempo.append(int(input()))
tempo.append(d)
tempo.sort()
ans = 0
for _ in range(m):
    k = int(input())
    k_cnd = bisect_left(tempo, k)
    if k_cnd == 0:
        ans += abs(tempo[k_cnd] - k)
    elif k_cnd == len(tempo):
        ans += abs(tempo[k_cnd - 1] - k)
    else:
        c1 = abs(tempo[k_cnd] - k) 
        c2 = abs(tempo[k_cnd - 1] - k)
        ans += min(c1, c2)
print(ans)