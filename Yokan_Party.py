# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:23:37 2021

@author: kazuk
"""

n, L = map(int, input().split())
k = int(input())
A = [0] + list(map(int, input().split())) + [L]
a = []
for i in range(len(A) - 1):
    a.append(A[i + 1] - A[i])
def check(m):
    piece = 0
    ps = []
    for i in a:
        piece += i
        if piece >= m:
            ps.append(piece)
            piece = 0
    ps[-1] += piece
    if len(ps) >= k + 1:
        return True
    else:
        return False

l = 0
r = L
while l + 1 < r:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid - 1
if check(r):
    print(r)
else:
    if check(mid):
        print(mid)
    else:
        print(l)
    