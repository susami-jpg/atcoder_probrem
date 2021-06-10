# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 02:14:21 2021

@author: kazuk
"""

from itertools import accumulate

h, w, k, v = map(int, input().split())
tera = [[0] * (w + 1)]
for _ in range(h):
    te = [0] + list(map(int, input().split()))
    te = list(accumulate(te))
    tera.append(te)

tera_t = [list(x) for x in zip(*tera)]
for i in range(w + 1):
    tera_t[i] = list(accumulate(tera_t[i]))

tera = [list(x) for x in zip(*tera_t)]

ans = 0
for a in range(1, h + 1):
    for c in range(a, h + 1):
        for b in range(1, w + 1):
            for d in range(b, w + 1):
                s = (c - a + 1) * (d - b + 1)
                yosan = s * k + tera[c][d] - tera[c][b - 1] - tera[a - 1][d] + tera[a - 1][b - 1]
                if yosan <= v:
                    ans = max(ans, s)
    
print(ans)




        
        
    
    