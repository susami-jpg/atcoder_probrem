# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:34:45 2021

@author: kazuk
"""

from bisect import bisect_left, bisect_right
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
C.sort()

ans = 0
for i in range(n):
    prod = bisect_left(A, B[i]) * (n-bisect_right(C, B[i]))
    ans += prod
print(ans)
