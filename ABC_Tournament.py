# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:14:00 2021

@author: kazuk
"""

n = int(input())
A = [0] + list(map(int, input().split()))
a = A[:]

for i in range(1, n):
    del_list = []
    for j in range(1, pow(2, n-i) + 1):
        if a[2*j-1] < a[2*j]:
            del_list.append(2*j-1)
        else:
            del_list.append(2*j)
    for d in del_list[::-1]:
        ans = d
        a.pop(d)

v = min(a[1], a[2])
print(A.index(v))


            
        