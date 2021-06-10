# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:51:20 2021

@author: kazuk
"""


n = int(input())
a = list(map(int, input().split()))
q = int(input())
mlist = list(map(int, input().split()))
s = [0] * (4 * 10 ** 4 + 1)
for i in range(1 << n):
    cnd = 0
    for j in range(n):
        if (i >> j) & 1:
            cnd += a[j]
    s[cnd] = 1

for m in mlist:
    if s[m]:
        print('yes')
    else:
        print('no')