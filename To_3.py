# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:06:41 2021

@author: kazuk
"""

n = int(input())
keta = list(map(int, list(str(n))))
mod = [0] * 3
k = len(keta)
for i in keta:
    mod[i%3] += 1

def modsum(mod):
    return (mod[0] * 0 + mod[1] * 1 + mod[2] * 2) % 3

for i in range(k):
    m = modsum(mod)
    if m == 0:
        print(i)
        break
    elif m == 1:
        if mod[1]:
            mod[1] -= 1
        elif mod[2]:
            mod[2] -= 1
        else:
            mod[0] -= 1
    else:
        if mod[2]:
            mod[2] -= 1
        elif mod[1]:
            mod[1] -= 1
        else:
            mod[0] -= 1
else:
    print(-1)
    

    