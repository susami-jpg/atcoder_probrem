# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:59:31 2021

@author: kazuk
"""

from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
cnt = defaultdict(int)
for i in range(N):
    cnt[A[i]] += 1

ans = 0
for i in range(N+1):
    if cnt[i] == 0:continue
    ans += cnt[i] * (cnt[i]-1) // 2

for k in range(N):
    print(ans - cnt[A[k]] + 1)
