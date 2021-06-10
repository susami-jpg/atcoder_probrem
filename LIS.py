# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:22:06 2021

@author: kazuk
"""
import bisect
inf = 10 ** 10
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

#dpはindexが実現可能な最長増加部分列を示す
#dp[i]がinfであればそれは実現不可能、inf未満ならそのindexの長さ+1の部分列は実現可能
dp = [inf] * (n)
while a:
    #リストaの前の要素から確認していく
    now = a.pop(0)
    #bisect_leftによってdpのどこにはいるかを確認
    i = bisect.bisect_left(dp, now)
    #dpの更新(小さければ最小値に更新されるし大きければLISが長くなるように更新される)
    dp[i] = now
for i in range(n - 1, -1, -1):
    if dp[i] < inf:
        print(i + 1)
        break
        
    
    
    
    