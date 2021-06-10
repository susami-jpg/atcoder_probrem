# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:24:59 2021

@author: kazuk
"""

n = int(input())
member = []
for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    member.append((a,b,c,d,e))
    
def is_ok(x):
    # 条件を満たすかどうか？問題ごとに定義
    binset = set()
    for m in member:
        bin = 0
        for i in range(5):
            if m[i] >= x:
                bin |= (1 << i)
        binset.add(bin)
    for i in binset:
        for j in binset:
            for k in binset:
                #計算の優先度は"-" > "<<"であることに注意
                if i | j | k == ((1 << 5) - 1):
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

ok = 0
ng = 10 ** 9 + 1
print(meguru_bisect(ng, ok))

