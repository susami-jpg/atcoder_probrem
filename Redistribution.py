# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 01:51:29 2021

@author: kazuk
"""

s = int(input())
mod = 10 ** 9 + 7
dp = [0] * (s+1)
accdp = [0] * (s+1)
dp[0] = accdp[0] = 1
#dp[v] := 総和が v となるような数列の個数
#このとき、次のように場合分けできる。

#最後の項が 3 のとき、残りの総和を v - 3 にすればよいので dp[ v - 3 ] 通り
#最後の項が 4 のとき、同様に dp[ v - 4 ] 通り
#...
#最後の項が v - 1 のとき、同様に dp[ 1 ] 通り
#最後の項が v のとき、dp[ 0 ] 通り
#よって、

#dp[ v ] = dp[ v - 3 ] + dp[ v - 4 ] + ... + dp[ 0 ]

#となる。あとはこれに従って素直に求めていける。計算量は O(S2) となる (DP 状態量が O(S) で、各遷移が O(S) であるため)。

for i in range(1, s+1):
    if i - 3 < 0:
        accdp[i] = accdp[i-1]%mod
    else:
        dp[i] = accdp[i-3]%mod
        accdp[i] = (accdp[i-1] + dp[i])%mod

print(dp[s])
