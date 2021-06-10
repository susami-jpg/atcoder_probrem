# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:17:58 2021

@author: kazuk
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
minm = 1000000000000000

for i in range(2 ** N):
    money = 0
    A_copy = A[:]
    for j in range(1, N):
        if (i >> j) & 1:
            if A_copy[j] <= max(A_copy[:j]):
                money += max(A_copy[:j]) - A[j] + 1
                A_copy[j] = max(A_copy[:j]) + 1
    count = 1
    for k in range(1, N):
        if max(A_copy[:k]) < A_copy[k]:
            count += 1
    if count >= K:
        minm = min(minm, money)
        
print(minm)

    
        
                