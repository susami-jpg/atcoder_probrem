# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:22:58 2021

@author: kazuk
"""

n = int(input())
#これまでの最小値を記録
minv = 10 ** 10
#これまでの最大"差異"を記録
maxdiff = -10 ** 10
for _ in range(n):
    r = int(input())
    maxdiff = max(maxdiff, r - minv)
    minv = min(minv, r)
    
print(maxdiff)


    