# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:33:20 2021

@author: kazuk
"""

a, b = map(int, input().split())

#2整数の最大公約数を求める
#再帰関数を使う場合
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

#2整数の最小公倍数を求める
def multiple(a, b):
    return a*b // euclid(a, b)

ans = multiple(a, b)
if ans > 10 ** 18:
    print("Large")
else:
    print(ans)