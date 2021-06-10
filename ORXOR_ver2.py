# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:36:31 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))

ans = 10 ** 15
for i in range(1 << (n - 1)):
    xor = []
    prev = 0
    for j in range(n - 1):
        if (i >> j) & 1:
            cnd = 0
            for c in a[prev:j + 1]:
                cnd |= c
            xor.append(cnd)
            prev = j + 1
    cnd = 0
    for c in a[prev:]:
        cnd |= c
    xor.append(cnd)
    cnd = None
    for c in xor:
        if cnd == None:
            cnd = c
        else:
            cnd ^= c
    ans = min(ans, cnd)
print(ans)
        
        