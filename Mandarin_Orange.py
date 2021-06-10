# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:25:35 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))

cnd = list(set(a))
ans = 0
for c in cnd:
    maxc = 0
    cnt = 0
    for i in a:
        if i >= c:
            cnt += 1
        else:
            maxc = max(maxc, cnt)
            cnt = 0
    maxc = max(maxc, cnt)
    ans = max(ans, maxc*c)
print(ans)
            
        