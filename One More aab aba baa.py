# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 20:43:55 2021

@author: kazuk
"""

from sys import stdin, setrecursionlimit
from bisect import bisect_left, bisect_right


from itertools import permutations
from collections import defaultdict
setrecursionlimit(10**7)
s, k = input().split()
k = int(k)
S = len(s)
rec = defaultdict(int)

for i in s:
    rec[i] += 1
s = list(set(s))
s.sort()

cnd = []

def dfs(t, used):
    if len(t) == S+1:
        cnd.append(t[1:])
        return
    used[t[-1]] += 1
    for nxt in s:
        if used[nxt] == rec[nxt]:continue
        #ここでusedは更新される
        dfs(t+nxt, used)
    #更新されたusedを元に戻す
    used[t[-1]] -= 1


dfs(" ", defaultdict(int))
print(cnd[k-1])







    

