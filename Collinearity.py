# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 00:36:41 2021

@author: kazuk
"""

from sys import exit
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if y3*(x2 - x1) == (y2 - y1)*x3 + (y1*(x2 - x1) - (y2 - y1)*x1):
                print("Yes")
                exit()
else:
    print("No")
    
