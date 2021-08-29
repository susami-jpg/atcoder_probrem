# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 00:40:07 2021

@author: kazuk
"""

n = int(input())
mod = 10 ** 9 + 7
ans = pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)
print(ans%mod)

