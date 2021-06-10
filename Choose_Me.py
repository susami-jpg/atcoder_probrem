# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 04:33:54 2021

@author: kazuk
"""

n = int(input())
town = []
for _ in range(n):
    a, b = map(int, input().split())
    town.append((2*a + b, a, b))
town.sort(reverse=True)


def is_ok(x):
    taka = 0
    aoki = 0
    for t, a, b in town[:x]:
        taka += a + b
    for t, a, b in town[x:]:
        aoki += a
    if taka > aoki:
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

ans = meguru_bisect(0, 2*10**5)
print(ans)