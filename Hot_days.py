# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:09:54 2021

@author: kazuk
"""

d, n = map(int, input().split())
day = [0] * d
for i in range(d):
    day[i] = int(input())
a = []
b = []
c = []
for _ in range(n):
    ai, bi, ci = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)

dp = [[-10 ** 10] * n for _ in range(d)]

#dp[i][j]はi日目までに選んだ服の価値の最大値を示す　jは当日に選んだ服を示す
for i in range(d):
    temp = day[i]
    for j in range(n):
        #変数jは前日にどの服を選んだかを示すインデックス
        if i == 0:
            if a[j] <= temp and temp <= b[j]:
                #初日に選べる服のインデックスを0とする(初日は点数が加算されない)
                dp[i][j] = 0
        else:
            for k in range(n):
                #変数kは当日にどの服を選ぶかを示すインデックス
                if a[k] <= temp and temp <= b[k]:
                    dp[i][k] = max(dp[i - 1][j] + abs(c[j] - c[k]), dp[i][k])
                        #最大値の更新
print(max(dp[-1]))
                    
                    
                
        
      
            
        
            
    