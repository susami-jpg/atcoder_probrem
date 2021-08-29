# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:04:52 2021

@author: kazuk
"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in range(1, N):
    B.append(A[i] - A[i-1])
#前の地点との標高差(B[i] = A[i] - A[i-1])
B = [0] + B
acc_sum = 0
for i in range(N):
    acc_sum += abs(B[i])
    
for _ in range(Q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    #更新される部分の標高差を先に引いておく
    if l > 0:
        acc_sum -= abs(B[l])
    if r+1 < N:
        acc_sum -= abs(B[r+1])
    #標高の更新
    if l > 0:
        B[l] += v
    if r+1 < N:
        B[r+1] -= v
    #更新した結果を不便さに反映
    if l > 0:
        acc_sum += abs(B[l])
    if r+1 < N:
        acc_sum += abs(B[r+1])
    print(acc_sum)
