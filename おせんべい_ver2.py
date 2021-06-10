# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:49:01 2021

@author: kazuk
"""

r, c = map(int, input().split())
rc = []
for _ in range(r):
    rc.append(list(map(int, input().split())))
ans = 0
for i in range(1 << r):
    rc_cnd = rc[:]
    for j in range(r):
        if (i >> j) & 1:
            rc_cnd[j] = [0 if i == 1 else 1 for i in rc_cnd[j]]
    rc_cnd_t = [list(x) for x in zip(*rc_cnd)]
    cnt = 0
    for col in rc_cnd_t:
        t = col.count(0)
        cnt += max(t, r - t)
    ans = max(ans, cnt)
print(ans)
        
        