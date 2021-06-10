# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:45:46 2021

@author: kazuk
"""

n = int(input())
s = set()
for i in range(2, n):
    if i ** 2 > n:
        break
    cnt = 2
    while True:
        cnd = pow(i, cnt)
        if cnd <= n:
            s.add(cnd)
            cnt += 1
        else:
            break
 
print(n - len(s))
