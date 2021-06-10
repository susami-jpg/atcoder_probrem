# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:50:31 2021

@author: kazuk
"""

from math import floor
from sys import stdin
input = stdin.readline

def acc_d(a, h, w):
    for i in range(h):
        for j in range(w):
            if i != 0:
                a[i][j] += a[i-1][j]
    for i in range(h):
        for j in range(w):
            if j != 0:
                a[i][j] += a[i][j-1]
    return a


#累積和を計算したテーブルaにおいて左上の座標を(y1,x1)、右下の座標を(y2,x2)としたときの区画の累積和を返す
#0index
def kukaku(a, y1, x1, y2, x2):
    if y1 == 0 and x1 == 0:
        return a[y2][x2]
    elif y1 == 0:
        return a[y2][x2] - a[y2][x1-1]
    elif x1 == 0:
        return a[y2][x2] - a[y1-1][x2]
    else:
        return a[y2][x2] - a[y2][x1-1] - a[y1-1][x2] + a[y1-1][x1-1]
    
n, k = map(int, input().split())
pond = [list(map(int, input().split())) for _ in range(n)]
lim = floor(k**2/2) + 1


#中央値がx以下かどうかの判定
#k*kの区画内の要素を降順に並べた時にfloor(k**2/2)+1未満個のx以上の数があれば中央値はx以下となる
def is_ok(x):
    binpond = []
    #x以上なら1、x未満なら0としてpondを01に変換
    for row in pond:
        row = [1 if c > x else 0 for c in row]
        binpond.append(row)
    #二次元累積和をとる
    binpond = acc_d(binpond, n, n)
    #k*kの区画内のx以上の数の個数を得て判定
    for i in range(n-k+1):
        for j in range(n-k+1):
            y1 = i
            x1 = j
            y2 = i+k-1
            x2 = j+k-1
            cnd = kukaku(binpond, y1, x1, y2, x2)
            if cnd < lim:
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

print(meguru_bisect(-1, 10**9))
