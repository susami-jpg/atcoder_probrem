# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:07:36 2021

@author: kazuk
"""

from bisect import bisect_right
from sys import exit
x, n = map(int, input().split())
p = list(map(int, input().split()))
p_rec = [i for i in range(102)]
for i in p:
    p_rec.remove(i)

def OrLessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

if n == 0:
    print(x)
    exit()
num, ind = OrLessThan(x, p_rec)
if abs(x-p_rec[ind]) <= abs(x-p_rec[ind+1]):
    print(p_rec[ind])
else:
    print(p_rec[ind+1])
    
    