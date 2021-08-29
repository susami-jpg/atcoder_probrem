# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 02:54:02 2021

@author: kazuk
"""

from sys import exit

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

loop = [1]
seen = [0] * (n + 1)
now = 1
seen[1] = 1
cnt = 0
while 1:
    cnt += 1
    now = a[now]
    if cnt == k:
        print(now)
        exit()
    if seen[now]:
        s_ind = loop.index(now)
        prev_loop = loop[:s_ind]
        loop = loop[s_ind:]
        L = len(loop)
        k -= len(prev_loop)
        k %= L
        print(loop[k])
        exit()
    seen[now] = 1
    loop.append(now)
