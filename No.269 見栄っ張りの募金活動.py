# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:59:52 2021

@author: kazuk
"""
"""
n, s, k = map(int, input().split())
mod = 10**9+7
#dp[i][j]: i人目が支払う金額を決めた時の暫定合計金額の通り数
dp = [[0] * (s + 1) for _ in range(n)]
#0人目は何円支払っても良い
for j in range(s + 1):
    sn = j * n
    if sn > s:
        break
    dp[0][sn] = 1
for i in range(1, n):
    #i人目は最低でもk円増やす必要がある
    for j in range(k * (n-i), s+1):
        for l in range(j+1):
            if j-k*(n-i)-l < 0:break
            dp[i][j] += dp[i-1][j-k*(n-i)-l]
            dp[i][j] %= mod

print(dp[-1][s]%mod)
"""

#分割数による解法
from sys import exit
n, s, k = map(int, input().split())
#x[i]:= (i 人目の生徒の支払う金額) - i*K とすると、

#x[0] + x[1] + ⋯+x[N-1] = S−(K+2K+⋯+(N-1)K)
#0 <= x[0] <= x[1] <= ... <= x[N-1]
#を満たす (x[0], x[1], ..., x[N-1]) の組を数え上げる問題になるので、これは分割数 P(S−(K+2K+⋯+(N-1)K), N) です。
mod = 10**9 + 7
S = s - k*(n-1)*n//2

def part_num(n, k):
    if n == k == 0:
        return 1
    mod = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for j in range(1, k+1):
        dp[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i - j >= 0:
                dp[i][j] = (dp[i][j-1] + dp[i-j][j])%mod
            else:
                dp[i][j] = dp[i][j-1]
                
    return dp[n][k]

if S < 0:
    print(0)
    exit()
ans = part_num(S, n)
print(ans%mod)

