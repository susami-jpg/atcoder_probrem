# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:55:49 2021

@author: kazuk
"""

n = int(input())
red = []
blue = []



red = [tuple(map(int, input().split())) for _ in range(n)]
blue = [tuple(map(int, input().split())) for _ in range(n)]
blue.sort()

ans = 0
for c, d in blue:
    now = 0
    max_point = -1
    min_diff = 10000000
    while now < len(red):
        a, b = red[now]
        if a < c and b < d:
            cnd = d-b
            if cnd < min_diff:
                min_diff = cnd
                max_point = now
        now += 1
    if max_point != -1:
        red.pop(max_point)
        ans += 1
print(ans)