# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:12:10 2021

@author: kazuk
"""

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
row = [0] * h
column = [0] * w

def trans(A):
    new_A = [list(x) for x in zip(*A)]
    return new_A

for i in range(h):
    row[i] = sum(A[i])

new_A = trans(A)

for j in range(w):
    column[j] = sum(new_A[j])

B = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        B[i][j] = row[i] + column[j] - A[i][j]

for row in B:
    print(*row)
    
    