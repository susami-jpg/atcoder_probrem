# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 04:20:44 2021

@author: kazuk
"""

n = int(input())
seta = set()
setb = set()
for _ in range(n):
    s = str(input())
    if s[0] == "!":
        setb.add(s[1:])
    else:
        seta.add(s)

ans = list(seta & setb)
if len(ans) == 0:
    print("satisfiable")
else:
    print(ans[0])