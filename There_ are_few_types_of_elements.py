# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:29:47 2021

@author: kazuk
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import deque
q=deque()
ans = 0
for c in a:
    q.append(c)  ## dequeの右端に要素を一つ追加する。
    #(追加した要素に応じて何らかの処理を行う)

    while q and len(set(q)) > k: #(満たすべき条件):
        rm=q.popleft() ## 条件を満たさないのでdequeの左端から要素を取り除く
        #(取り除いた要素に応じて何らかの処理を行う)
    ans = max(ans, len(q))
    #(何らかの処理を行う。whileがbreakしたので、dequeに入っている連続部分列は条件を満たしている。特に右端の要素から左に延ばせる最大の長さになっている。
print(ans)

