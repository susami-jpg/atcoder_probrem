# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:58:52 2021

@author: kazuk
"""

n, L = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
A = [0] * n
A[0] = a[0]
for i in range(1, n):
    A[i] = a[i] - a[i-1]
A.append(L - a[-1])

def is_ok(x):
    #スコアをxにできるか?
    cnt = 0
    piece = 0
    for i in range(len(A)):
        if piece >= x:
            cnt += 1
            piece = A[i]
        else:
            piece += A[i]
    if piece >= x:
        cnt += 1
    
    if cnt >= k+1:
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

INF = 10**15
ans = meguru_bisect(INF, 0)
print(ans)
