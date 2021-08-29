# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:40:51 2021

@author: kazuk
"""

n, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

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

E = [[0] * n for _ in range(n)]
for i in range(n):
    E[i][i] = 1
def matrix_power(A, K):
    if K == 0:
        return E
    res = matrix_power(A, K//2)
    res = matrix_prod(res, res)
    if K & 1:
        res = matrix_prod(res, A)
    return res
 
mod = 10**9+7
ans = 0   
res = matrix_power(A, K)
for i in range(n):
    for j in range(n):
        ans += res[i][j]
        ans %= mod
print(ans)
