# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:22:06 2021

@author: kazuk
"""

import bisect
INF = 10**10

N = int(input())
a = list(map(int, input().split()))
a_r = a[::-1]
dp = [INF] * N
dp_r = [INF] * N

for n in range(N):
    i = bisect.bisect_left(dp, a[n])
    dp[i] = a[n] # aがA[:n]中で最大なら、最も左のINFが更新される
    i = bisect.bisect_left(dp_r, a_r[n])
    dp_r[i] = a_r[n]

l = bisect.bisect_left(dp, INF)
r = bisect.bisect_left(dp_r, INF)

if dp[l-1] == dp[r-1]:
    print(l + r - 1)
elif l + r > n:
    print(N)
else:
    print(l + r)
    


    
    
    
    