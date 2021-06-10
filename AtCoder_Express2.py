# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 23:29:35 2021

@author: kazuk
"""

from itertools import accumulate
n, m, q = map(int, input().split())
exp = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int, input().split())
    exp[l][r] += 1

for i in range(n + 1):
    exp[i] = list(accumulate(exp[i]))

exp_t = [list(x) for x in zip(*exp)]
for i in range(n + 1):
    exp_t[i] = list(accumulate(exp_t[i]))

exp = [list(x) for x in zip(*exp_t)]
    
for _ in range(q):
    l, r = map(int, input().split())
    print(exp[r][r] - exp[r][l - 1] - exp[l - 1][r] + exp[l - 1][l - 1])
    


    
    