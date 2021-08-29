# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 00:36:00 2021

@author: kazuk
"""

from sys import exit
n = int(input())
if n%2:
    exit()

for i in range(1 << n):
    cnd = []
    stack = []
    for j in reversed(range(n)):
        if (i>>j) & 1:
            if not stack:
                break
            stack.pop()
            cnd.append(")")
        else:
            stack.append(1)
            cnd.append("(")
    if not stack and len(cnd) == n:
        print("".join(cnd))
