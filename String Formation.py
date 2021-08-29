# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:46:43 2021

@author: kazuk
"""

from collections import deque
S = deque(list(input()))
Q = int(input())
flg = 0
for _ in range(Q):
    query = list(input().split())
    if len(query) == 1:
        flg = 1 - flg
    else:
        F = int(query[1])
        C = query[2]
        if flg:
            if F == 1:
                S.append(C)
            else:
                S.appendleft(C)
        else:
            if F == 1:
                S.appendleft(C)
            else:
                S.append(C)

S = list(S)
if flg:
    S = S[::-1]
print("".join(S))

        
        
