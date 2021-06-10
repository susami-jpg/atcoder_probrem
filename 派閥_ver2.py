# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:35:44 2021

@author: kazuk
"""

n, m = map(int, input().split())
xy = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    xy[x - 1].append(y - 1)
    xy[y - 1].append(x - 1)

ans = 0
for i in range(1 << n):
    party = []
    for j in range(n):
        if (i >> j) & 1:
            party.append(j)
    for i in range(len(party) - 1):
        for j in range(i + 1, len(party)):
            if party[j] not in xy[party[i]]:
                break
        else:
            continue
        break
    else:
        ans = max(ans, len(party))
print(ans)
    
    