# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:07:20 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
S = sum(a) / 10
a *= 2
piece = [a[0]]
s = a[0]
i = 1
while i < 2*n:
    if s == S:
        print("Yes")
        break
    elif s > S:
        s -= piece.pop(0)
    else:
        piece.append(a[i])
        s += a[i]
        i += 1

else:
    print("No")
    
    

