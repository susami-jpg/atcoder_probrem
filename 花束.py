# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 01:54:22 2021

@author: kazuk
"""

R, B = map(int, input().split())
X, Y = map(int, input().split())

#x個の花束はつくれるか?
def is_ok(k):
    #x個の花束を作るためには、少なくともx本の赤い花とx本の青い花が必要
    restR = R-k
    restB = B-k
    if restR < 0 or restB < 0:return False
    if (restR/(X-1)) + (restB/(Y-1)) >= k:
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

ans = meguru_bisect(10**18, 0)
print(ans)