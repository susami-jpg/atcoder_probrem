# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:00:19 2021

@author: kazuk
"""

n, m = map(int, input().split())
node = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a == b:
        continue
    if a > b:
        a, b = b, a
    node[b] += 1

ans = 0
for i in node:
    if i == 1:
        ans += 1

print(ans)
