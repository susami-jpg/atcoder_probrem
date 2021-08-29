# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:25:27 2021

@author: kazuk
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [i-1 for i in A]
D = 60
dub = [A] + [[0] * N for _ in range(D)]
#dub[i][j]:= jからスタートして2のi乗先の町
for i in range(D):
    for j in range(N):
        dub[i+1][j] = dub[i][dub[i][j]]

now = 0
L = len(bin(K)[2:])-1
for i in range(L, -1, -1):
    if (K>>i)&1:
        now = dub[i][now]
print(now+1)

    