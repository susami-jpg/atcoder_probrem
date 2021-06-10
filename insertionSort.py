# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:56:06 2021

@author: kazuk
"""

def insertionSort(a, n):
    for i in range(n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v
        print(a)
    return

n = int(input())
a = list(map(int, input().split()))
insertionSort(a, n)