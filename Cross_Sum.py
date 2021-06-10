# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 08:55:07 2021

@author: kazuk
"""

#pypyなら通る
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
hw = []
for _ in range(h):
    hw.append(list(map(int, input().split())))
lowsum = [sum(i) for i in hw]
hw_t = [list(x) for x in zip(*hw)]
colsum = [sum(i) for i in hw_t]

for i in range(h):
    ans = []
    for j in range(w):
        p = lowsum[i] + colsum[j] - hw[i][j]
        ans.append(p)
    print(*ans)

        
    