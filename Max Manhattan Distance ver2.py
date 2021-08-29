# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:59:10 2021

@author: kazuk
"""

n, Q = map(int, input().split())
X = []
Y = []
XY = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x+y)
    Y.append(x-y)
    XY.append((x+y, x-y))
    
X_min = min(X)
X_max = max(X)
Y_min = min(Y)
Y_max = max(Y)
for _ in range(Q):
    q = int(input()) - 1
    x, y = XY[q]
    print(max(abs(x-X_min), abs(x-X_max),\
              abs(y-Y_min), abs(y-Y_max)))

