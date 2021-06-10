# -*- coding: utf-8 -*-
"""
Created on Wed May 26 00:55:46 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
cnt = 0

def selectionSort(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
                global cnt
        if i != minj:
            cnt += 1
            a[i], a[minj] = a[minj], a[i]
    return a

print(*selectionSort(a, n))
print(cnt)
                