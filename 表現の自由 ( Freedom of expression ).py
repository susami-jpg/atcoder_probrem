# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 12:57:32 2021

@author: kazuk
"""

from sys import exit
n, m = map(int, input().split())
mod = 10**9 + 7

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

#逆元によるnCkの高速計算
def inv(n): # MODを法とした逆元
    MOD = 10**9+7
    return pow(n, MOD-2, MOD)

MOD = 10**9+7
mx = 2*10**5
fact = [1] * (mx+1) # 階乗を格納するリスト
for i in range(mx):
    fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算
        
def comb(n, k):
    return (fact[n] * inv(fact[n-k]) * inv(fact[k])) % MOD # comb(n,k) = n!/((n-k)!k!)
    
flg = 0
if n < 0:
    flg = 1
temp = 1
    
factor = factorization(abs(n))

if abs(n) != 1:
    for _, num in factor:
        temp *= comb(m-1+num, num)
        temp %= mod

ans = 0
for i in range(m):
    if flg:
        cnd = i * 2 + 1
    else:
        cnd = i * 2
    if cnd > m:
        break
    cnd = temp * comb(m, cnd)
    ans += cnd
    ans %= mod


print(ans%mod)

