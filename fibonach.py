# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 01:36:53 2021

@author: kazuk
"""

def fib(n, a = 0, b = 1):
    if n < 1:
        return a
    return fib(n - 1, b, a + b)

print(fib(6))

