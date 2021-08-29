# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:58:00 2021

@author: kazuk
"""

from collections import defaultdict
N = int(input())
S = input()
ans = 0
rec = defaultdict(int)
col = ["R", "G", "B"]
for k in range(N):
    now = S[k]
    prod = 1
    for c in col:
        if c == now:continue
        prod *= rec[c]
    j = k-1
    i = k-2
    while i >= 0:
        if set([S[i], S[j], S[k]]) == set(col):
            prod -= 1
        i -= 2
        j -= 1
    ans += prod
    rec[now] += 1
print(ans)

    