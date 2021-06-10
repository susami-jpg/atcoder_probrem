# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:55:01 2021

@author: kazuk
"""
#pypyだと通らないが、python3で通る
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, q = map(int, input().split())
node = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

counter = [0] * (n + 1)
def dfs(v, par, acc):
    counter[v] += acc
    for nextv in node[v]:
        #循環を防ぐ
        if nextv != par:
            dfs(nextv, v, counter[v])
    return
   
for _ in range(q):
    p, x = map(int, input().split())
    counter[p] += x
dfs(1, 0, 0)
counter = counter[1:]
print(*counter)