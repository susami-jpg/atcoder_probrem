# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:53:42 2021

@author: kazuk
"""

def InsertationSort(shufflelist):
    n = len(shufflelist)
    for i in range(1, n):
        v = shufflelist[i]
        j = i - 1
        while v < shufflelist[j] and j >= 0:
            shufflelist[j + 1] = shufflelist[j]
            shufflelist[j] = v
            j -= 1    
        print(shufflelist)
    return shufflelist

def BubbleSort(shufflelist):
    n = len(shufflelist)
    for i in range(0, n):
        for j in range (n-1, i, -1):
            if shufflelist[j-1] > shufflelist[j]:
                shufflelist[j-1], shufflelist[j] = shufflelist[j], shufflelist[j-1]
                print(shufflelist)
    return shufflelist


def SelectionSort(shufflelist):
    n = len(shufflelist)
    for i in range(0, n):
        minj = i
        for j in range(i + 1, n):
            if shufflelist[minj] > shufflelist[j]:
                minj = j
        if minj != i:
            shufflelist[i], shufflelist[minj] = shufflelist[minj], shufflelist[i]
            print(shufflelist)
    return shufflelist



num = int(input())
B = [int(i) for i in input().split()]


def InsertationSort2(n, A, g):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            global cnt 
            cnt += 1
        A[j + g] = v
        
G = [i for i in range(num-1, 0, -1)]
m = len(G)
cnt = 0

def ShellSort(n, A):
    for i in range(0, m):
        InsertationSort2(n, A, G[i])
    

ShellSort(num, B)
print(m)
print(*G)
print(cnt)
for i in B:
    print(i)


