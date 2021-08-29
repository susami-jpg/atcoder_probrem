# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:30:49 2021

@author: kazuk
"""

k = int(input())
#+1したら通った
max_a = int(pow(k, 1/3)) + 1

ans = 0
for a in range(1, max_a + 1):
    #+1したら通った
    max_b = int(pow(k/a, 1/2)) + 1
    for b in range(a, max_b + 1):
        if k % (a* b) != 0:
            continue
        c = k // (a * b)
        if c < b:
            continue
        ans += 1
print(ans)

        