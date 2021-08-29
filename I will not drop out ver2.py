# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:27:50 2021

@author: kazuk
"""

n, k = map(int, input().split())
score = []
for _ in range(n):
    a, b = map(int, input().split())
    score.append(b)
    score.append(a-b)

score.sort(reverse=True)
ans = sum(score[:k])
print(ans)
