# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 01:03:56 2021

@author: kazuk
"""

from itertools import permutations
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
relation = [[0] * n for _ in range(n)]
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    relation[x][y] = 1
    relation[y][x] = 1

ans = 10**15
for perm in permutations(range(n)):
    now = perm[0]
    time = A[now][0]
    for i in range(1, n):
        next = perm[i]
        if relation[now][next]:
            break
        time += A[next][i]
        now = next
    else:
        ans = min(ans, time)
if ans == 10**15:
    print(-1)
else:
    print(ans)
    