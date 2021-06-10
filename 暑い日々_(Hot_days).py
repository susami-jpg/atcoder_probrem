# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:09:15 2021

@author: kazuk
"""

inf = -10**7
d, n = map(int, input().split())
t = []
for _ in range(d):
    t.append(int(input()))
cloth = []
for _ in range(n):
    a, b, c = map(int, input().split())
    cloth.append((a, b, c))

dp = [[inf] * n for _ in range(d)]
temp = t[0]
for j in range(n):
    a, b, c = cloth[j]
    if a <= temp <= b:
        dp[0][j] = 0

for i in range(1, d):
    temp = t[i]
    for j in range(n):
        a, b, c = cloth[j]
        if a <= temp <= b:
            for k in range(n):
                if dp[i - 1][k] != inf:
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(cloth[j][2] - cloth[k][2]))

print(max(dp[-1]))

                    
            
            
        

    