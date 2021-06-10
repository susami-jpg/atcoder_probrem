# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:27:43 2021

@author: kazuk
"""
import re
n = 5
A = 'H4 C9 S4 D2 C3'.split()
B = A
C = A
def num(card):
    return int(card[1])

def BubbleSort(len, list):
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if num(A[j]) < num(A[j - 1]):
                A[j], A[j - 1] = A[j - 1], A[j]
    return A
    
def SelectionSort(len, list):
    for i in range(0, n):
        minj = i
        for j in range(i + 1, n):
            if num(B[minj]) > num(B[j]):
                minj = j
        if minj != i:
            B[i], B[minj] = B[minj], B[i]
    return B
    
def IsStable(beforesort, sortlist):
    for i in range(0, num(sortlist[-1]) + 1):
        list1 = re.findall('.{}'.format(i), beforesort)
        list2 = re.findall('.{}'.format(i), sortlist)
        if list1 != list2:
            return print('Not stable')
    return print('Stable')

print(BubbleSort(n, A))
print(IsStable(C, BubbleSort(n, A)))
print(SelectionSort(n, B))
print(IsStable(C, SelectionSort(n, B)))