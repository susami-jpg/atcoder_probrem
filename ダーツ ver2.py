# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:02:22 2021

@author: kazuk
"""

from bisect import bisect_right
N, M = map(int, input().split())
points = [int(input()) for _ in range(N)]
points.append(0)
p2 = []
n2 = len(points)
for i in range(n2):
    for j in range(i, n2):
        p2.append(points[i] + points[j])


def OrLessThan(K: int, A: list) -> int:
    "配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ"
    "-1の時は解が無い時"
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

p2.sort()
n = len(p2)
ans = 0
for p in p2:
    if p > M:
        break
    rest = M - p
    _, ind = OrLessThan(rest, p2)
    if ind == -1:continue
    ans = max(ans, p+p2[ind])
print(ans)
