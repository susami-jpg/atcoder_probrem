# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:55:45 2021

@author: kazuk
"""

n = int(input())
c = list(input())
rlen = c.count("R")
wlen = n - rlen
ans = c[:rlen].count("W")
print(ans)
