# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 09:39:45 2021

@author: kazuk
"""

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]

cnt = 0
for i in range(h-1):
    for j in range(w-1):
        if A[i][j] > B[i][j]:
            point = -1
        else:
            point = 1
        
        if A[i][j] == B[i][j]:
                continue
        k = abs(A[i][j] - B[i][j])
        cnt += k
        for a in range(2):
            for b in range(2):
                A[i+a][j+b] += point * k

for i in range(h):
    for j in range(w):
        if A[i][j] != B[i][j]:
            print("No")
            break
    else:
        continue
    break
else:
    print("Yes")
    print(cnt)
    
