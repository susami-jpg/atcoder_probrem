# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:36:54 2021

@author: kazuk
"""

from bisect import bisect_left
INF = 10**15
N = int(input())
A = list(map(int, input().split()))
Ar = A[::-1]
#left[i]:= 数列Aにおいて0-indexでiの時にできるLISの最大長
left = [0] * N
#right[i]:= 数列Arにおいて0-indexでiの時にできるLISの最大長
right = [0] * N

dp = [INF] * N
for i in range(N):
    #普通のLIS
    ind = bisect_left(dp, A[i])
    dp[ind] = A[i]
    #i番目を見てる時にできるLISの最大長を測る
    L = bisect_left(dp, INF)
    #記録
    left[i] = L

#右からも同様に
dp = [INF] * N
for i in range(N):
    ind = bisect_left(dp, Ar[i])
    dp[ind] = Ar[i]
    L = bisect_left(dp, INF)
    right[i] = L

ans = 0
for i in range(N):
    #最大長は真ん中をindex iとしたとき、
    #左端からiまででできるLISの最大長 + 右端からiまででできるLISの最大長 - 1
    ans = max(ans, left[i] + right[N-1-i] - 1)
print(ans)


    
    