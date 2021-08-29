# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:32:53 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
inf = 10 ** 5 + 1
a_rec = [0] * inf
ans = 0
for i in a:
    a_rec[i] += 1
    ans += i

q = int(input())
for _ in range(q):
    b, c = map(int, input().split())
    move = a_rec[b]
    a_rec[c] += move
    a_rec[b] = 0
    ans += move * c
    ans -= move * b
    print(ans)




