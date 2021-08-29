# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:55:30 2021

@author: kazuk
"""
N, M, K = map(int, input().split())
MOD = 998244353
ans = 0
#逆元によるnCkの高速計算
def inv(n): # MODを法とした逆元
    return pow(n, MOD-2, MOD)

mx = 2*10**5
fact = [1] * (mx+1) # 階乗を格納するリスト
for i in range(mx):
    fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算
        
def comb(n, k):
    return (fact[n] * inv(fact[n-k]) * inv(fact[k])) % MOD # comb(n,k) = n!/((n-k)!k!)


for k in range(K+1):
    cnd = M
    cnd *= comb(N-1, k) * pow(M-1, N-1-k, MOD)
    ans += cnd
    ans %= MOD
print(ans)

    