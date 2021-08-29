# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:52:30 2021

@author: kazuk
"""

n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x+y)
    Y.append(x-y)

X.sort()
Y.sort()

ans = max(abs(X[-1] - X[0]), abs(Y[-1] - Y[0]))
print(ans)

    