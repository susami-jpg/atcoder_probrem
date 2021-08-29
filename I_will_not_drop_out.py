# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:15:21 2021

@author: kazuk
"""

n, k = map(int, input().split())
score = []
for _ in range(n):
    a, b = map(int, input().split())
    a -= b
    score.append(a)
    score.append(b)

score.sort(reverse=True)
print(sum(score[:k]))

    