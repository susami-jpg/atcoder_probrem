# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:53:37 2021

@author: kazuk
"""

#素数判定　あんまり早くない
def PrimaryCheck(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
            break
    return True

n = int(input())
if PrimaryCheck(n):
    print("YES")
else:
    print("NO")
    