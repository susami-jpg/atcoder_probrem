# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:11:09 2021

@author: kazuk
"""

from bisect import bisect_left
n = int(input())
inf = 10 ** 15
ball = [[] for _ in range(n)]
for _ in range(n):
    x, c = map(int, input().split())
    c -= 1
    ind = bisect_left(ball[c], x)
    ball[c].insert(ind, x)

#dp[i][j] :色がiのボールをj(左側もしくは右側)で取り終えた時の最小のtime
dp = [[inf] * 2 for _ in range(n)]

for i in range(n):
    if len(ball[i]) == 0:
        continue
    left = ball[i][0]
    right = ball[i][-1]
    dp[i][0] = abs(right) + abs(right-left)
    dp[i][1] = abs(left) + abs(right-left)
    sc = i
    break

prevc = sc
for i in range(sc + 1, n):
    col = ball[i]
    if len(col) == 0:
        continue
    for j in range(2):
        #最後にとるボールが左端の場合
        if j == 0:
            dp[i][j] = min(dp[prevc][0] + abs(ball[prevc][0] - ball[i][-1]),
                           dp[prevc][1] + abs(ball[prevc][-1] - ball[i][-1])) + abs(ball[i][-1] - ball[i][0])
        #右端の場合
        else:
            dp[i][j] = min(dp[prevc][0] + abs(ball[prevc][0] - ball[i][0]),
                           dp[prevc][1] + abs(ball[prevc][-1] - ball[i][0])) + abs(ball[i][-1] - ball[i][0])
        
    prevc = i

ans = min(dp[prevc][0] + abs(ball[prevc][0]), dp[prevc][1] + abs(ball[prevc][-1]))
print(ans)

    
