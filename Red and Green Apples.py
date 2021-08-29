# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:33:26 2021

@author: kazuk
"""

from heapq import heappop, heappush, heapify
X, Y, a, b, c = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort()

red = A[:X]
green = B[:Y]
heapify(red)
heapify(green)
while C:
    if red[0] < green[0]:
        min_apple = red[0]
        to = 1
    else:
        min_apple = green[0]
        to = 0
    if min_apple >= C[-1]:
        break
    if to:
        heappop(red)
        heappush(red, C.pop())
    else:
        heappop(green)
        heappush(green, C.pop())

ans = sum(red) + sum(green)
print(ans)

    