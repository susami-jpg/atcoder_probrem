# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:03:04 2021

@author: kazuk
"""

n = int(input())
ans = 0
for i in range(1, n):
    ans += n / (n-i)

print(ans)
