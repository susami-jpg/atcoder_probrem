# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:55:21 2021

@author: kazuk
"""

#行列計算
def matrix_prod(A, B):
    mod = 10**9+7
    h = len(A)
    w = len(B[0])
    K = len(A[0])
    if K != len(B):
        return 
    res = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(K):
                res[i][j] += A[i][k] * B[k][j]
                res[i][j] %= mod
    
    return res

n = int(input())
E = [[0] * n for _ in range(n)]
for i in range(n):
    E[i][i] = 1
    
#行列繰り返し二乗法
def matrix_power(A, K):
    if K == 0:
        return E
    res = matrix_power(A, K//2)
    res = matrix_prod(res, res)
    #奇数ならあと一回かける
    if K & 1:
        res = matrix_prod(res, A)
    return res
 