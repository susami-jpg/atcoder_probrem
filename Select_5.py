# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:15:33 2021

@author: kazuk
"""


n, p, q = map(int, input().split())
A = [i%p for i in list(map(int, input().split()))]
ans = 0

for a in range(n-4):
    for b in range(a+1, n-3):
        for c in range(b+1, n-2):
            for d in range(c+1, n-1):
                for e in range(d+1, n):
                    cnd = A[a]
                    for i in [b,c,d,e]:
                        cnd *= A[i]
                        cnd %= p
                    if cnd == q:
                        ans += 1
    

print(ans)
                    
        