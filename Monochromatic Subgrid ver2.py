# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:43:23 2021

@author: kazuk
"""

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for k in range(1<<8):
    part = []
    for i in range(H):
        if (k>>i)&1:
            part.append(P[i])
    L = len(part)
    if L == 0:continue
    cnt = [0] * (H*W+1)
    for j in range(W):
        for l in range(L-1):
            if part[l][j] != part[l+1][j]:
                break
        else:
            cnt[part[0][j]] += L
    ans = max(ans, max(cnt))
            
print(ans)

                