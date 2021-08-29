# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:21:11 2021

@author: kazuk
"""

n = int(input())
t = [int(input()) for _ in range(n)]

ans = 100000000000
for i in range(1 << n):
    t1 = 0
    t2 = 0
    for j in range(n):
        if (i >> j) & 1:
            t1 += t[j]
        else:
            t2 += t[j]
    ans = min(ans, max(t1, t2))
print(ans)

max_t = 50 * n + 1
t = [0] + t
S = sum(t)
S_2 = S // 2

dp = [[False] * max_t for _ in range(n+1)]
dp[0][0] = True
for i in range(1, n+1):
    time = t[i]
    for j in range(max_t):
        dp[i][j] = dp[i-1][j]
        if j-time >= 0:
            dp[i][j] = (dp[i][j] or dp[i-1][j-time])

cnd = []
for ind, bool in enumerate(dp[-1]):
    if bool:
        cnd.append(ind)


from bisect import bisect_left, bisect_right

def LessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

_, mid = LessThan(S_2, cnd)

if mid == -1:
    ans = max(cnd[0], S-cnd[0])
elif mid == len(cnd)-1:
    ans = max(cnd[-1], S-cnd[-1])
else:
    diff1 = abs(S_2 - cnd[mid])
    diff2 = abs(S_2 - cnd[mid+1])
    if diff1 < diff2:
        ans = max(cnd[mid], S-cnd[mid])
    else:
        ans = max(cnd[mid+1], S-cnd[mid+1])

print(ans)

    
    