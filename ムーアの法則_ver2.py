# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:51:01 2021

@author: kazuk
"""

#atcoderではsympyは使えない
import sympy as sym
p = float(input())
x = sym.Symbol('x')
cost = x + p / pow(2, x / 1.5)
dcost = sym.diff(cost)

def is_ok(a):
    if dcost.subs(x, a) <= 0:
        return True
    else:
        return False
    # 条件を満たすかどうか？問題ごとに定義
    


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 0.000000001):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ok = 0
ng = 10 ** 18 + 1

ax = meguru_bisect(ng, ok)
print(cost.subs(x, ax))
