# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 01:18:48 2021

@author: kazuk
"""

from bisect import bisect_right
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

#x以下の個数がK個以上あるか
def is_ok(x):
    # 条件を満たすかどうか？問題ごとに定義
    cnt = 0
    for a in A:
        cnt += bisect_right(B, x//a)
    if cnt >= K:
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

ans = meguru_bisect(0, 10**19)
print(ans)

