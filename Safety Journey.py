# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 18:45:05 2021

@author: kazuk
"""

n, m, K = map(int, input().split())
mod = 998244353
 
edge = [[i] for i in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)

#dp[k][i]: k回の移動を行ったときに頂点iにいる場合の数
#dp[k][i] = Σdp[k-1][j] - Σdp[k-1][ban]
#jは全ての頂点、すなわちiによって第一項の値は変わらない -> prev_sum
#banは頂点iにむかって辺が伸びていない頂点

dp = [[0] * n for _ in range(K+1)]
dp[0][0] = 1

for k in range(1, K+1):
    prev_sum = sum(dp[k-1])
    for i in range(n):
        dp[k][i] = prev_sum
        for ban in edge[i]:
            dp[k][i] -= dp[k-1][ban]
        dp[k][i] %= mod

print(dp[K][0]%mod)
