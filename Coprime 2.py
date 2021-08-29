# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 21:41:25 2021

@author: kazuk
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
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

spf = SPF(10**5 + 2)
cnd = set()
for i in range(n):
    fact = set(primefact(a[i], spf))
    for j in set(fact):
        cnd.add(j)

ans = [1] * (m + 1)
for i in cnd:
    now = i
    while now < m+1:
        ans[now] = 0
        now += i

s = []
cnt = 0
for i, c in enumerate(ans):
    if i == 0:continue
    if c:
        cnt += 1
        s.append(i)

print(cnt)
for i in s:
    print(i)
    
