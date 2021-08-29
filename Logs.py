# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:57:34 2021

@author: kazuk
"""

from math import ceil, floor
n, k = map(int, input().split())
a = list(map(int, input().split()))

def is_ok(x):
    cnt = 0
    for i in range(n):
        cnt += ceil(a[i]/x) - 1
    if cnt > k:
        return False
    else:
        return True
    

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

ans = meguru_bisect(0, 10**9)
print(ans)
