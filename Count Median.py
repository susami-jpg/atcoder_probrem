# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:43:44 2021

@author: kazuk
"""

n = int(input())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if n%2:
    L = A[n//2]
    R = B[n//2]
    print(R-L+1)
else:
    L = (A[n//2] + A[n//2 - 1]) / 2
    R = (B[n//2] + B[n//2 - 1]) / 2
    print(int((R-L+1)*2-1))
    