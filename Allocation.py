# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:02:41 2021

@author: kazuk
"""

n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]


def is_ok(m):
    stack = []
    for wi in w:
        if wi > m:
            return False
        elif stack and stack[-1] + wi <= m:
            stack[-1] += wi
        else:
            stack.append(wi)
    if len(stack) <= k:
        return True
    else:
        return False
            


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(0, 10**12))