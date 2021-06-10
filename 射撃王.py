# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:51:29 2021

@author: kazuk
"""
N = int(input())
HS = []
for _ in range(N):
    H, S = map(int, input().split())
    HS.append((H, S))

def is_ok(V):
    tlist = []
    for (h, s) in HS:
        if V - h < 0:
            return False #設定した高さをすでに超えている風船があればダメ
        t = (V - h) // s #風船を割るまでに残された時間
        tlist.append(t)
    tlist.sort()
    for i, t in enumerate(tlist): #期限が早いものから割っていく
        if i > t:
            return False #時間切れ
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

print(meguru_bisect(-1, int(1e14)))