# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:53:30 2021

@author: kazuk
"""
from itertools import permutations
n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

#関数dictはあたえられた数列を辞書順に並び替えて返す
for i, p in enumerate(permutations(range(1, n + 1))): #permutation関数は辞書順で順列のタプルをかえす
#rangeは範囲内の数字を1 2 3 ..10というような数字の並びを返す
    if p == P:
        a = i
    if p == Q:
        b = i
print(abs(a - b))
    
    
    

    
    
    
    
    