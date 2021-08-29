# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:13:55 2021

@author: kazuk
"""

n = int(input())
robot = []
for _ in range(n):
    x, l = map(int, input().split())
    robot.append((x+l, x-l))

robot.sort()
ans = 1
r = robot[0][0]
for i in range(1, n):
    if r <= robot[i][1]:
        r = robot[i][0]
        ans += 1

print(ans)
