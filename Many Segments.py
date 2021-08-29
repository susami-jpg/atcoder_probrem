# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:46:13 2021

@author: kazuk
"""
"""
inf = 10 ** 15
mod = 10 ** 9 + 7
from sys import stdin, exit, setrecursionlimit
from math import floor, ceil
from collections import deque
from bisect import bisect_left, bisect_right
from itertools import accumulate

n = int(input())
n, k = map(int, input().split())
a, b, c = map(int, input().split())
s = input()
s = list(input())
a = list(map(int, input().split()))
"""
n = int(input())

kukan = []
for _ in range(n):
    t, l, r = map(int, input().split())
    kukan.append((t, l, r))

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        t1, l1, r1 = kukan[i]
        t2, l2, r2 = kukan[j]
        if r1 >= r2:
            tr, right = t2, r2
        else:
            tr, right = t1, r1
        if l1 >= l2:
            tl, left = t1, l1
        else:
            tl, left = t2, l2
        if left < right:
            ans += 1
        elif left == right:
            if (tl == 1 or tl == 2) and (tr == 1 or tr == 3):
                ans += 1
        
print(ans)



