# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 00:37:30 2021

@author: kazuk
"""

x, y, a, b = map(int, input().split())

def is_ok(t):
    cost = x
    cnt = 0
    while 1:
        if cnt == t:
            break
        if cost * a < b:
            cost *= a
            cnt += 1
        else:
            break
    cost += (t - cnt) * b
    if cost < y:
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

ans = meguru_bisect(y, 0)
print(ans)
