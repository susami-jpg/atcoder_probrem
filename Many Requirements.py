# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 16:37:00 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10**7)
n, m, q = map(int, input().split())

A = []
def combination_rep(now, array):
    if len(array) == n:
        A.append(array)
        return
    for nxt in range(now, m+1):
        combination_rep(nxt, array + [nxt])
    return

combination_rep(1, [])
query = [list(map(int, input().split())) for _ in range(q)]

ans = 0
for cnd in A:
    cnd = [0] + cnd
    point = 0
    for a, b, c, d  in query:
        if cnd[b] - cnd[a] == c:
            point += d
    ans = max(ans, point)

print(ans)

from itertools import combinations_with_replacement
ans = 0
for cnd in combinations_with_replacement(range(1, m+1), n):
    point = 0
    for a, b, c, d  in query:
        if cnd[b-1] - cnd[a-1] == c:
            point += d
    ans = max(ans, point)

print(ans)
    