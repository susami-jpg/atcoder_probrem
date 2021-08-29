# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 22:29:57 2021

@author: kazuk
"""

from bisect import bisect_left
n = int(input())
circle = []
for _ in range(n):
    x, r = map(int, input().split())
    circle.append((x-r, x+r))
#ある円がstrictにもう一つの円を包含している条件
#x1-r1 < x2-r2 and x2+r2 < x1+r2
circle.sort(key=lambda x:(-x[0],-x[1]))
#sortによってi < jについてxi - ri > xj - rjが成り立つ

INF = 10**15
dp = [INF] * n
#i < jについてxi + ri < xj + rjとなるような最長増加部分列を求める
for i in range(n):
    _, s = circle[i]
    ind = bisect_left(dp, s)
    dp[ind] = s

for i in range(n-1, -1, -1):
    if dp[i] != INF:
        print(i+1)
        break
