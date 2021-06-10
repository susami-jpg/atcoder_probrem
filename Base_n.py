# -*- coding: utf-8 -*-
"""
Created on Wed May 26 16:47:58 2021

@author: kazuk
"""

from sys import exit
x = str(input())
m = int(input())

if len(x) == 1:
    if int(x) <= m:
        print(1)
    else:
        print(0)
    exit()

d = 0

for i in list(x):
    if d < int(i):
        d = int(i)

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out


def is_ok(n):
    w = Base_n_to_10(x, n)
    if w <= m:
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

if not is_ok(d + 1):
    print(0)
    exit()
    
maxok = meguru_bisect(10**18 + 1, d + 1)
print(maxok - d)


