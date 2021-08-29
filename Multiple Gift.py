# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:42:59 2021

@author: kazuk
"""

x, y = map(int, input().split())
ans = 0
now = x
while 1:
    if now <= y:
        ans += 1
    else:
        break
    now *= 2

print(ans)
