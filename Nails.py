# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 00:02:00 2021

@author: kazuk
"""

from itertools import accumulate
n, m = map(int, input().split())
tri = [[0] * i for i in range(1, n + 5)]
for _ in range(m):
    a, b, x = map(int, input().split())
    a += 1
    tri[a][b] += 1
    tri[a][b + 1] -= 1
    tri[a + x + 1][b] -= 1
    tri[a + x + 2][b + 1] += 1
    tri[a + x + 1][b + x + 2] += 1
    tri[a + x + 2][b + x + 2] -= 1

tri = [list(accumulate(i)) for i in tri]
tri_2 = []
for i in range(n + 4):
    t = []
    for j in range(i + 1):
        t.append(tri[n + 3 - j][i - j])
    t = list(accumulate(t))
    tri_2.append(t)
ans = 0
for i in range(n + 4):
    t = []
    for j in range(i + 1):
        t.append(tri_2[n + 3 - j][i - j])
    t = list(accumulate(t))
    for k in t:
        if k != 0:
            ans += 1
print(ans)
            

        
        
        
        

