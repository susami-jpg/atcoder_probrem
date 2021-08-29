# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 21:54:15 2021

@author: kazuk
"""

from bisect import bisect_left
n = int(input())
box = []
for _ in range(n):
    h, w = map(int, input().split())
    box.append((h, w))

#lambda x:(-x[0],x[1]) による方法
#sort(key=lambda x:(-x[0],x[1]))
#以下は、2次元配列の 第1要素で降順 & 第2要素で昇順 sort します。
box.sort(key=lambda x:(x[0],-x[1]))
INF = 10**10
dp = [INF] * n
for i in range(n):
    w = box[i][1]
    ind = bisect_left(dp, w)
    dp[ind] = w
  
ans = bisect_left(dp, INF)
print(ans)



        
    