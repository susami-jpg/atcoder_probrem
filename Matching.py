# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:52:37 2021

@author: kazuk
"""

mod = 10**9+7
n = int(input())
pair = [list(map(int, input().split())) for _ in range(n)]

#dp[S] :ペアが決定している女性が集合Sで、その人数(i)までの男性が決まっているとき男性[i+1]のペアを決める通り数
dp = [0] * (1 << n)
dp[0] = 1

for S in range(1<<n):
    #iは男性のindex
    i = bin(S).count("1")
    for j in range(n):
        #決定済みの女性はスルー
        if (S >> j) & 1:
            continue
        #配るdp
        if pair[i][j]:
            dp[S|(1<<j)] += dp[S]%mod

print(dp[-1]%mod)

            