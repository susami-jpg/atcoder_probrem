# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 02:44:58 2021

@author: kazuk
"""

n, m, x = map(int, input().split())
price = [0] * n
A = []
for i in range(n):
    query = list(map(int, input().split()))
    price[i] = query[0]
    A.append(query[1:])

INF = 10**15
ans = INF
for i in range(1 << n):
    p = 0
    C = [0] * m
    for j in range(n):
        if (i >> j) & 1:
            p += price[j]
            for k in range(m):
                C[k] += A[j][k]
    for k in range(m):
        if C[k] < x:
            break
    else:
        ans = min(ans, p)
    
if ans == INF:
    print(-1)
else:
    print(ans)

            
    