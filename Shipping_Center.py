# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:43:39 2021

@author: kazuk
"""
from bisect import bisect
n, m, q = map(int, input().split())
bag = []
for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))
xh = list(map(int, input().split()))
query = []
for _ in range(q):
    l, r = map(int, input().split())
    query.append((l, r))
    
def restx(l, r):
    return sorted(x[:l - 1] + x[r:])
#2次元配列を二番目の要素に注目して降順にソートする
bag = sorted(bag, reverse=True, key=lambda x: x[1])  #[1]に注目してソート
#引数として荷物と箱を受け取り、それらの組み合わせによって得られる最大価値を返す
def value(bag, x):
    val = 0
    while bag and x:
        lug = bag.pop(0)
        w = lug[0]
        index = bisect(x, w)
        if w <= x[-1]:
            if w == x[index - 1]:
                x.pop(index - 1)
            else:
                x.pop(index)
            val += lug[1]
    return val

for (l, r) in query:
    x = xh[:]
    x = restx(l, r)
    bagc = bag[:]
    print(value(bagc, x))

        
        
        