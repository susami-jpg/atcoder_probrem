# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:13:16 2021

@author: kazuk
"""

def sort(A):
    for i in range(1, len(A)):
        insert(i, A)
        
def insert(i, A):
    temp = A[i]
    for j in range(i - 1, -1, -1):
        if A[j] > temp:
            A[j + 1] = A[j]
        else:
            A[j + 1] = temp
            break
    else:
        A[0] = temp
        
A = [3,4,2,1,3,1,1,6]
sort(A)
print(A)

def sort2(A):
    for i in range(0, len(A)):
        if bubble(i, A) == 0:
            break
        
def bubble(i, A):
    exchange = 0
    for j in range(len(A) - 1, i, -1):
        if A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            exchange += 1
    return exchange
#exchangeは交換された場合に1になる変数。0であればbubbleをbreakする。
            
sort2(A)
print(A)
