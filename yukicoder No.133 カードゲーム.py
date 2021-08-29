# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:31:58 2021

@author: kazuk
"""

from itertools import permutations

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
num = 0
for a in permutations(A):
    for b in permutations(B):
        num += 1
        a_win = 0
        b_win = 0
        for i in range(n):
            if a[i] > b[i]:
                a_win += 1
            elif a[i] < b[i]:
                b_win += 1
        if a_win > b_win:
            ans += 1

print(ans/num)


                
                
            

