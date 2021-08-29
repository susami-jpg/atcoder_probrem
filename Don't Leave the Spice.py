# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:11:43 2021

@author: kazuk
"""


#####segfunc#####
def segfunc(x, y):
    return max(x, y)
#################

#####ide_ele#####
ide_ele = -float('inf')
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

w, n = map(int, input().split())
dish = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
INF = float('inf')
#dp[i][j]: i番目までのdishを選択して香辛料をj mg消費するときの最大価値
dp_prev = [-INF] * (w+1)
dp = [-INF] * (w+1)
dp_prev[0] = 0
for i in range(1, n+1):
    seg = SegTree(dp_prev, segfunc, ide_ele)
    L, R, v = dish[i]
    for j in range(w+1):
        dp[j] = dp_prev[j]
        l = max(0, j-R)
        r = j-L
        if r < 0:continue
        max_prev = seg.query(l, r+1)
        dp[j] = max(dp[j], max_prev + v)
    dp_prev = dp
    dp = [-INF] * (w+1)

ans = dp_prev[-1]
if ans < 0:
    print(-1)
else:
    print(ans)

    
        
        

