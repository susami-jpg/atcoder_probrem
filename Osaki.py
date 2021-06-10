# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 02:29:50 2021

@author: kazuk
"""

from itertools import accumulate
while True:
    n = int(input())
    if n == 0:
        break
    train = [0] * (24 * 60 ** 2 + 2)
    for _ in range(n):
        s, l = str(input()).split()
        stime = int(s[0] + s[1]) * 60 ** 2 + int(s[3] + s[4]) * 60 + int(s[6] + s[7])
        ltime = int(l[0] + l[1]) * 60 ** 2 + int(l[3] + l[4]) * 60 + int(l[6] + l[7])
        train[stime] += 1
        train[ltime] -= 1
    train = list(accumulate(train))
    print(max(train))

        