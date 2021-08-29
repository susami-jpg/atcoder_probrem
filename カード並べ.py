# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:22:10 2021

@author: kazuk
"""

from collections import defaultdict
from itertools import permutations
n = int(input())
k = int(input())
card = [input() for _ in range(n)]
data = defaultdict(int)

ans = 0
for perm in permutations(card, k):
    cnd = int("".join(perm))
    if data[cnd] == 1:continue
    ans += 1
    data[cnd] += 1

print(ans)
