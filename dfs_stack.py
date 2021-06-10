# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:18:24 2021

@author: kazuk
"""

n = int(input())
ukv = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]

stack = []
visited = []
time = 0
d = [0] * (n + 1)
f = [0] * (n + 1)
for i in range(1, n + 1):
    if i not in visited:
        stack.append(i)
        visited.append(i)
        time += 1
        d[i] = time

        while stack:
            s = stack[-1]
            k = ukv[s][1]
            if k == 0:
                stack.pop()
                time += 1
                f[s] = time
            else:
                ukv[s][1] -= 1
                v = ukv[s].pop(2)
                if v not in visited:
                    stack.append(v)
                    visited.append(v)
                    time += 1
                    d[v] = time

for i in range(1, n + 1):
    print(i, d[i], f[i])