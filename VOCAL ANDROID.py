# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 15:23:37 2021

@author: kazuk
"""
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:00:38 2021

@author: kazuk
"""

"""
使い方

1. なんでもよいので初期化用のリストを用意
    a = [14, 5, 9, 13, 7, 12, 11, 1, 7, 8]
2. 区間に行う操作を決める
   区間の最小値、最大値を求めたい、区間の和を求めたいなど。今回は、最小値を求めるとします。segfuncに関数を書き込んでください。

    def segfunc(x, y):
        return min(x, y)
3. 単位元を定める
   初期化に使います。演算に影響を与えないものです。最小値を求めるなら無限大がこれに当たります。

    ide_ele = float('inf')
4. オブジェクトを作成、引数は上の3つ
    seg = SegTree(a, segfunc, ide_ele)
5. 各操作を行えます
     リストは0-indexで扱ってください。（いつも通りです。）
     行える操作は以下の2つです。
         1. ある1つの要素の更新
             update(k, x) : k番目の要素をxに更新します。
         2. ある区間の操作の結果を取得
             query(l, r) : [l, r)(l以上r未満の区間)から値を取得します。
             # [0, 8)の最小値を表示
             print(seg.query(0, 8)) # 1
             # 5番目を0に変更
             seg.update(5, 0)
             # [0, 8)の最小値を表示
             print(seg.query(0, 8)) # 0
            

その他の操作（最小値以外）
操作	segfunc	単位元
最小値	min(x, y)	float('inf')
最大値	max(x, y)	-float('inf')
区間和	x + y	0
区間積	x * y	1
最大公約数	math.gcd(x, y)	0

"""

#####segfunc#####
def segfunc(x, y):
    return max(x, y)
#################

#####ide_ele#####
ide_ele = -float("inf")
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


from sys import exit
n = int(input())
frase = [(0)] + [tuple(map(int, input().split())) for _ in range(n)]

a = [0] * 394
dp_prev = SegTree(a, segfunc, ide_ele)
dp = SegTree(a, segfunc, ide_ele)

for i in range(1, n+1):
    for j in range(394):
        s, l, p = frase[i]
        #dp[i][j] = max(dp[i][j], dp[i-1][j])の更新
        #フレーズを使わない場合
        dp.update(j, max(dp.query(j, j+1), dp_prev.query(j, j+1)))
        #dp[i][j] = max(max(dp[i][j-l:j-s]) + p, dp[i][j])
        left = max(0, j-l)
        right = j-s
        if j-s >= 0:
            cnd = max(dp.query(left, right+1) + p, dp.query(j, j+1))
            dp.update(j, cnd)
    dp_prev = dp

m = int(input())
ans = []
for _ in range(m):
    w = int(input())
    cnd = dp_prev.query(w, w+1)
    if cnd == 0:
        print(-1)
        exit()
    else:
        ans.append(cnd)

for i in ans:
    print(i)
    
        