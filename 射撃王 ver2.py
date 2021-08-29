# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:17:13 2021

@author: kazuk
"""

N = int(input())
#全ての風船を割った時の累積時間(t=0で1個、t=1で2個、...t=N-1でN個の風船が割れた状態になる)
max_T = (N-1)*N//2
balloon = [tuple(map(int, input().split())) for _ in range(N)]

#x以下の高度ですべての風船を割り切れるか?
def is_ok(x):
    #各風船を割るときの上限の時間のリスト
    lim_time = []
    #各風船についてx以下で割るために使える時間の上限をだす(この時間までには割らなければならない)
    for H, S in balloon:
        lim_time.append((x-H)//S)
    #lim_timeが早い風船から割っていく
    lim_time.sort()
    for t, lim in enumerate(lim_time):
        #現在時刻で上限を超えている風船があればx以下で割り切るのは不可能
        if t > lim:
            return False
    return True
        
def meguru_bisect(ng, ok):
    while abs(ng-ok) > 1:
        mid = (ng+ok)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = meguru_bisect(-1, 10**18+1)
print(ans)

