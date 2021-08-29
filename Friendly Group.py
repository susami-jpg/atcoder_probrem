# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:23:31 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
#dim[i][j] :　身長i以下,体重j以下の人数
dim = [[0] * 5001 for _ in range(5001)]

for _ in range(n):
    a, b = map(int, input().split())
    dim[a][b] += 1

for _ in range(2):
    for i in range(1, 5001):
        for j in range(1, 5001):
            if _ == 0:
                dim[i][j] += dim[i][j-1]
            else:
                dim[i][j] += dim[i-1][j]

ans = 0
for i in range(1, 5001):
    for j in range(1, 5001):
        ceil_i = min(i+k, 5000)
        ceil_j = min(j+k, 5000)
        max_team = dim[ceil_i][ceil_j] - dim[ceil_i][j-1] - dim[i-1][ceil_j] + dim[i-1][j-1]
        ans = max(ans, max_team)

print(ans)

        
    