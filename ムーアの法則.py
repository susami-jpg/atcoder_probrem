# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:43:10 2021

@author: kazuk
"""
p = float(input())
def f(x):
    return x + p * pow(2,-(x/1.5)) #pow(x, a)でxのa条を計算できる

#三分探索
#関数f(x)が最小となるようなxを見つける
def triser(low, high):
    while abs(high - low) > 0.0000000001:
        c1 = (low * 2 + high) / 3
        c2 = (low + high * 2) / 3
        if f(c1) >= f(c2):
            low = c1
        else:
            high = c2
    return low

ans = triser(0, 10 ** 18)
print(f(ans))

#関数f(x)を微分した式が単調増加あるいは単調減少の場合
#関数f(x)は凸型のグラフ
#よって関数f(x)の極小値を求めればよい

#別解
import sympy as sym
#微分
#sym.diff(f(x))
#方程式　= 0
p = float(input())
def f(x):
    return x + p * pow(2,-(x/1.5))
x = sym.Symbol('x')
g = x + p * pow(2,-(x/1.5))
eq = sym.Eq(sym.diff(g), 0)
#方程式を解く
ans2 = sym.solve(eq)
print(f(ans2[0]))


