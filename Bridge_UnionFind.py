# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:39:08 2021

@author: kazuk
"""


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

n, m = map(int, input().split())
edge = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge.append((a, b))

from itertools import combinations
ans = 0
for edgecnd in combinations(edge, m - 1):
    uf = UnionFind(n)
    for (a, b) in edgecnd:
        uf.union(a, b)
    if uf.group_count() > 1:
        ans += 1
print(ans)
    