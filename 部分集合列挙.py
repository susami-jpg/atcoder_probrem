# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 00:01:18 2021

@author: kazuk
"""

# 集合Mの部分集合を列挙
# R が結果
# 1を引く(デクリメントする)という操作は1になっている一番下位のビットを0にして、それより下のビットをすべて1にする、という操作なので（0のときは除く）、結果的にもれなくかぶりなく列挙できます。
M = int(input())
R = []
v = (-1) & M
while v:
    R.append(v)
    v = (v - 1) & M

for r in R:
    print(bin(r))


# サイズKの部分集合を列挙
# T⊆{0,1,...,N−1}, |T|=Kとなる部分集合Tを列挙する。
# R が結果
K = int(input())
N = int(input()) #要素0,1,...n-1の中からＫ個選んで集合とするものを列挙
R = []
v = (1 << K) - 1
while v < (1 << N):
    R.append(v)
    x = v & -v; y = v + x
    v = ((v & ~y) // x >> 1) | y