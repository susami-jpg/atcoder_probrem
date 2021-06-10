# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:03:36 2021

@author: kazuk
"""

from collections import deque
q=deque()
for c in a:
    q.append(c)  ## dequeの右端に要素を一つ追加する。
    #(追加した要素に応じて何らかの処理を行う)

    while not #(満たすべき条件):
        rm=q.popleft() ## 条件を満たさないのでdequeの左端から要素を取り除く
        #(取り除いた要素に応じて何らかの処理を行う)

    #(何らかの処理を行う。whileがbreakしたので、dequeに入っている連続部分列は条件を満たしている。特に右端の要素から左に延ばせる最大の長さになっている。


##ex
## 入力の受け取り
n,k=map(int,input().split())
a=[int(input()) for i in range(n)]

## コーナーケースの処理
if 0 in a:
    print(n)
    exit()

ans=0
q=deque()
p=1  ## 今、見ている区間の要素の積をpで管理する。
for c in a:
    q.append(c)  ## dequeの"右端"に要素を一つ追加する。
    p*=c

    while q and p>k: ## 要素の積がKを超えているか？
        rm=q.popleft() ## 条件を満たさないのでdequeの"左端"から要素を取り除く
        p//=rm ## 取り除いた値に応じて要素の積を更新する

    ans=max(ans,len(q)) ## dequeに入っている要素の積がK以下になるまで区間を縮めた。

print(ans)


#l, rを用いる場合
n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

# 0が含まれる場合
if 0 in s: 
    ans = n
else:
    r, l = 0, 0 # 右端と左端のインデックス
    sum_s = 1 # 右端と左端に含まれる合計値
    ans = 0
    while r < n:
        # 右端を進めたときの積がK以下なら、右端を進める
        if sum_s * s[r] <= k:
            sum_s *= s[r]
            r += 1
            ans = max(ans, r - l)
        # 右端と左端を進める
        elif r == l:
            r += 1
            l += 1
        # 左端を進める
        else:
            sum_s //= s[l] # 左端を進めたときに取り除かれる要素を合計値からも取り除く
            l += 1
        # print('l={}, r={}, size={}, {}'.format(l, r, r - l, s[l:r]))
print(ans)