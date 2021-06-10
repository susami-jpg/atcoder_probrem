# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:35:10 2021

@author: kazuk
"""

from itertools import permutations
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
m = int(input())
xy = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    xy[x - 1].append(y - 1)
    xy[y - 1].append(x - 1)
    
inf = 10 ** 10
ans = inf
for perm in permutations(range(n)):
    perm = list(perm)
    cnd = 0
    for j in range(n - 1):
        now = perm[j]
        next = perm[j + 1]
        if next in xy[now]:
            break
        cnd += a[now][j]
    else:
        cnd += a[perm[-1]][-1]
        ans = min(ans, cnd)
        

if ans == inf:
    ans = -1
print(ans)
        
        
    
    

