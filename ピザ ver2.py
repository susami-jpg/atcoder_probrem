# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:52:41 2021

@author: kazuk
"""

from bisect import bisect_left
D = int(input())
N = int(input())
m = int(input())
store = [int(input()) for _ in range(N-1)]
store.append(-10**15)
store.append(0)
store.append(D)
store.append(10**15)
L = len(store)
store.sort()
ans = 0
for _ in range(m):
    k = int(input())
    ind = bisect_left(store, k)
    ans += min(abs(store[ind]-k), abs(store[ind-1]-k))
print(ans)
 
