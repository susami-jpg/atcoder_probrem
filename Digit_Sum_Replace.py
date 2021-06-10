# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:59:19 2021

@author: kazuk
"""

m = int(input())
ds = 0 #各桁の和
cs = 0 #桁数
for _ in range(m):
    d, c = map(int, input().split())
    ds += d*c
    cs += c

print((cs - 1) + ((ds - 1) // 9))
    
#dsが27などの場合を考えるとds-1の意味が分かる

