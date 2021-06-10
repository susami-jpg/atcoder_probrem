# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:13:13 2021

@author: kazuk
"""


from collections import defaultdict

#UnionFindのNodeは0indexであることに注意
class UnionFind():
    def __init__(self, n):
        self.n = n
#parents
#各要素の親要素の番号を格納するリスト
#要素が根（ルート）の場合は-(そのグループの要素数)を格納する
        self.parents = [-1] * n
#find(x)
#要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

#union(x, y)
#要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

#size(x)
#要素xが属するグループのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.find(x)]

#same(x, y)
#要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

#members(x)
#要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

#roots()
#すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

#group_count()
#グループの数を返す
    def group_count(self):
        return len(self.roots())
    
#all_group_members
#{ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
#defaultdictは辞書dictのサブクラス
#print(uf.all_group_members())
# {0: [0, 2], 1: [1, 3, 4, 5]}
#print(list(uf.all_group_members().values()))
# [[0, 2], [1, 3, 4, 5]]
    def all_group_size(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        group_members = list(map(len, list(group_members.values())))
        return group_members
    

n, m = map(int, input().split())
edge = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge.append((a, b))

from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

nc2 = combinations_count(n, 2)
uf = UnionFind(n)
ans = []
count = nc2
for _ in range(m):
    ans.append(count)
    a, b = edge.pop()
    if uf.same(a, b):
        continue
    count -= uf.size(a) * uf.size(b)
    uf.union(a, b)
    
for i in ans[::-1]:
    print(i)
    
        
    
    
        
        
    
    