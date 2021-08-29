# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:02:19 2021

@author: kazuk
"""

#SPFによる前処理とクエリの高速素数判定

#SmallestPrimeFactor
#自分の素因数の中で最小の素因数を記録
#前処理O(NloglogN)
#nは調べたい範囲の最大値
def SPF(n):
    spf = [i for i in range(n + 1)]
    check = [False] * (n + 1)
    spf[0] = 0
    spf[1] = 1
    check[0] = check[1] = True
    for i in range(2, int(n**0.5) + 1):
        if check[i]: continue
        for j in range(i, n + 1, i):
            if check[j]:continue
            spf[j] = i
            check[j] = True
    return spf


"""
primefactは素因数分解した結果を返す
ただしsetではない
ex: 9 -> 3, 3を返す
"""
#上のSPFによる前処理を終えた前提(関数内のspfは上の関数を使用した返り値のリストを参照している)
#クエリごとにO(logN)で素因数分解した結果を返す
#素因数分解なのでn=0,1はエラーを吐くので注意
def primefact(n, spf):
    fact = []
    while n != 1:
        fact.append(spf[n])
        n //= spf[n]
    return fact

#関数SPFで前計算済み
#primefactでnの素因数分解の結果を用いてnの約数の個数を得る
def div_count(n, spf):
    from collections import Counter
    fact = primefact(n, spf)
    rec = Counter(fact)
    cnt = 1
    for val in rec.values():
        cnt *= (val+1)
    return cnt

#オイラー関数
#関数SPFで前計算済み
#正の整数 N が与えられる。
#1,2,…,N のうち、N と互いに素であるものの個数
#N=pe11pe22…peKK
#N=p1e1p2e2…pKeK
#と素因数分解できるとき、オイラー関数値は

#φ(N)=N(1−1/p1)(1−1/p2)…(1−1/pK)

def Euler_count(n, spf):
    from collections import Counter
    fact = primefact(n, spf)
    rec = Counter(fact)
    cnt = n
    for key in rec.keys():
        cnt *= (1 - (1/key))
    return int(cnt)

max_n = 1000001
spf = SPF(max_n)
f = [0] * max_n
f[1] = 2
for i in range(2, max_n):
    f[i] = f[i-1] + Euler_count(i, spf)

t = int(input())
for _ in range(t):
    n = int(input())
    print(f[n])
    


    
    
