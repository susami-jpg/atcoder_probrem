# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 03:43:40 2021

@author: kazuk
"""

from sys import exit
x = int(input())

for a in range(-10**3, 10**3):
    for b in range(-10**3, 10**3):
        if a**5 - b**5 == x:
            print(a, b)
            exit()