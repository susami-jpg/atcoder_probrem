# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:06:53 2021

@author: kazuk
"""

from heapq import heappop, heappush
from sys import exit
def solve():
    n = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(n)]
    #第一要素、第二要素ともに昇順でソート
    schedule.sort(key=lambda x:(x[0],x[1]))
    INF = 10**15
    #番兵を置く
    schedule.append((INF, INF))
    hq = []
    x = 0
    for l, r in schedule:
        #次の区間までの箱に今入れられる候補のボールを入れられるか?
        while x < l:
            #候補のボールがなければ全部入れられている
            if len(hq) == 0:
                #xを次の区間の左まで進める
                x = l
                break
            #今入れられるボールのうち最も締め切りの近いボールを見る
            min_r = heappop(hq)
            #締め切り越えならもうボールは入れられない
            if min_r < x:
                print("No")
                return
            #xを1つ進める(ボールをいれた)
            x += 1
        #xがlまで進んだ状態なので今見ているボールを候補に入れる
        heappush(hq, r)
    print("Yes")
        

T = int(input())
for _ in range(T):
    solve()
    