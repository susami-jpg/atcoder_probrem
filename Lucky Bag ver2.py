# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 18:47:52 2021

@author: kazuk
"""

n, s = map(int, input().split())
bag = [0] + [tuple(map(int, input().split())) for _ in range(n)]
#dp[i][j]:= i日目まで決めた時に総額がj円となるような福袋の買い方
dp = [[""] * (s+1) for _ in range(n+1)]
if bag[1][0] <= s:
    dp[1][bag[1][0]] = "A"
if bag[1][1] <= s:
    dp[1][bag[1][1]] = "B"
for i in range(1, n):
    for j in range(s+1):
        if len(dp[i][j]) != i:continue
        a, b = bag[i+1]
        if j+a <= s:
            dp[i+1][j+a] = dp[i][j] + "A"
        if j+b <= s:
            dp[i+1][j+b] = dp[i][j] + "B"

if dp[n][s]:
    print(dp[n][s])
else:
    print('Impossible')
    

#dp復元解法
n, s = map(int, input().split())
bag = [0] + [tuple(map(int, input().split())) for _ in range(n)]
#dp[i][j]:= i日目まで決めた時に総額がj円となるような福袋の買い方ができるか?(bool)
dp = [[False] * (s+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(1, n+1):
    a, b = bag[i]
    for j in range(s+1):
        if j-a >= 0 and dp[i-1][j-a]:
            dp[i][j] = True
        if j-b >= 0 and dp[i-1][j-b]:
            dp[i][j] = True

if not dp[n][s]:
    print('Impossible')
else:
    #復元パート
    ans = []
    i = n
    j = s
    while i >= 1:
        a, b = bag[i]
        if j-a >= 0 and dp[i-1][j-a]:
            ans.append("A")
            j -= a
        elif j-b >= 0 and dp[i-1][j-b]:
            ans.append("B")
            j -= b
        i -= 1

    print("".join(ans[::-1]))
