# -*- coding: utf-8 -*-
"""
Created on Thu May 13 00:19:53 2021

@author: kazuk
"""

w, n = map(int, input().split())
dish = []
for _ in range(n):
    l, r, v = map(int, input().split())
    dish.append((l, r, v))
inf = -(10 ** 10)
dp = [[inf] * (w + 1) for _ in range(n)]
dp[0][0] = 0
for i in range(n):
    l, r, v = dish[i]
    for j in range(w + 1):
        if i == 0:
            if l <= j <= r:
                dp[i][j] = v
            elif j < l:
                dp[i][j] = 0
        else:
            if 0 <= j-l and j-r < 0:
                dp[i][j] = max(dp[i-1][j], max(dp[i-1][:j-l+1]) + v)
            elif 0 <= j-r:
                dp[i][j] = max(dp[i-1][j], max(dp[i-1][j-r:j-l+1]) + v)
            
    
ans = dp[-1][w]
if ans < 0:
    print(-1)
else:
    print(ans)
    
                
            
        
        