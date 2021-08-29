# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 01:03:55 2021

@author: kazuk
"""

from bisect import bisect_left
from itertools import accumulate
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

h.sort()
hpre = []
hnex = []
hrev = h[1:]
for i in range(n//2):
    i *= 2
    hpre.append(abs(h[i+1] - h[i]))
    hnex.append(abs(hrev[i+1] -hrev[i]))

hpre = [0] + list(accumulate(hpre))
hnex = [0] + list(accumulate(hnex))

def LessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_left(A, K)
    return ans, (-1 if ans == 0 else ans - 1)


def is_ok(x):
    for i in range(m):
        W = w[i]
        cnt = 0
        num, W_ind = LessThan(W, h)
        if W_ind == -1:
            cnt += abs(h[0] - W)
            cnt += hnex[-1]
        elif num%2 == 0:
            cnt += abs(h[W_ind+1] - W)
            cnt += hpre[num//2]
            cnt += hnex[-1] - hnex[num//2]
        else:
            cnt += abs(h[W_ind] - W)
            cnt += hpre[num//2]
            cnt += hnex[-1] - hnex[num//2]
        if cnt <= x:
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

ans = meguru_bisect(-1, 10**12)
print(ans)
