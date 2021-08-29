# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:15:11 2021

@author: kazuk
"""

from itertools import accumulate

n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
a = list(accumulate(a))
b = list(accumulate(b))


def is_ok(x):
    for i in range(x + 1):
        j = x - i
        if i > n or j > m:
            continue
        if a[i] + b[j] <= k:
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

ans = meguru_bisect(n + m + 1, 0)
print(ans)
