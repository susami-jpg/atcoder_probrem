# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:56:04 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
n = int(input())
sset = set()
for i in range(1, n + 1):
    s = str(input())
    if s not in sset:
        print(i)
        sset.add(s)
        