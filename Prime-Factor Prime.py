# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 17:46:37 2021

@author: kazuk
"""

#エラトステネスの篩を用いた高速素因数分解
#区間に使える
from math import sqrt
from collections import defaultdict
def factorization(l, r):
    n = int(sqrt(r)) + 1
    
    #エラトステネスの篩
    #Lは問題によって調節
    L = 10**5+1
    is_prime = [1] * L
    is_prime[0] = is_prime[1] = 0
    for i in range(2, L):
        if is_prime[i]:
            now = i+i
            while now < L:
                is_prime[now] = 0
                now += i
                
    #valはnまでの素因数で割った結果を記録(val[i] != 1ならiは素数)
    val = [i for i in range(l, r+1)]
    #cntはその数を何回割ったかを記録
    cnt = [0] * (r-l+1)
    #区間内の数字についての素因数分解の結果を持つリスト
    #rec = defaultdict(list)
    
    for i in range(n):
        if is_prime[i]:
            t = i
            c = 1
            while t ** c <= r:
                if l%(t**c) == 0:
                    k = l//(t**c)
                else:
                    k = l//(t**c) + 1
                #sはl以降の最初の(t**c)の倍数
                s = k*(t**c)
                while s <= r:
                    #s-lとすることで配列を0indexに戻す
                    cnt[s-l] += 1
                    #tのc条まで、すなわち素因数tでval[i]を割れるだけ割っておく
                    val[s-l] //= t
                    s += t**c
                #c(素因数の乗数)を増やす
                c += 1
    
    ans = 0
    for i in range(l, r+1):
        #val[i-l]が素数の場合
        if val[i-l] != 1:
            cnt[i-l] += 1
        if is_prime[cnt[i-l]]:
            ans += 1
    return ans 

l, r = map(int, input().split())
print(factorization(l, r))

    