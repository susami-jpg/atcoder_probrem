# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 12:49:12 2021

@author: kazuk
"""

n = int(input())
k = int(input())
#1~nのn種類の数字から重複を許してk個選ぶ場合の数
#k個の玉を用意する
#n-1個の仕切りを用意する
#仕切りで区切られた区間が1~nのどれかに対応し、その区間内にある数がその区間に対応する数字の数となる
#n-1+k C n-1 = n-1+k C k

# nCk.pyよりも高速かな？（powを外に出した）
def combination(n, k):
    nCk = under = top = 1
    mod = 10 ** 9 + 7

    # 分母
    for i in range(2, k + 1):
        under *= i
        under %= mod

    # 分子
    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

print(combination(n-1+k, k))