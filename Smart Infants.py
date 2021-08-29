# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:23:46 2021

@author: kazuk
"""

#TLE
#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################

#####ide_ele#####
ide_ele = float('inf')
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

from sys import exit, stdin
from bisect import bisect_left, insort_left
input = stdin.readline
class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        insort_left(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1
            ind = bisect_left(self.h, x)
            self.h.pop(ind)

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]
    
    def get_max(self):
        return self.h[-1]
    
    #HeapDictの中身がなければTrue
    def empty(self):
        if len(self.h) == 0:
            return True
        else:
            return False


enji = dict()
n, q = map(int, input().split())
max_b = 2*10**5 + 1
hd = HeapDict()
school = dict()
min_s = [float('inf')] * max_b
seg = SegTree(min_s, segfunc, ide_ele)

for i in range(n):
    a, b = map(int, input().split())
    enji[i+1] = [a, b]
    if not b in school:
        school[b] = HeapDict()
    school[b].insert(a)
    max_rate = school[b].get_max()
    seg.update(b, max_rate)

for _ in range(q):
    c, d = map(int, input().split())
    
    #転校パート
    #園児のrateと現在の学園を得る
    enji_rate, enji_school = enji[c]
    #現在の学園から園児のrateを消す
    school[enji_school].erase(enji_rate)
    #転校後の学園のmax_rateを得る(誰もいなければinfを返す)
    if school[enji_school].empty():
        upd = float('inf')
    else:
        upd = school[enji_school].get_max()
    #seg木のupdate
    seg.update(enji_school, upd)
    #転校先に学校を更新
    enji[c][1] = d
    
    #転校先の学園パート
    if not d in school:
        school[d] = HeapDict()
    school[d].insert(enji_rate)
    upd = school[d].get_max()
    seg.update(d, upd)
    
    print(seg.query(0, max_b+1))
    
    
    
    

