# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:05:46 2021

@author: kazuk
"""

from collections import deque
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
conf = deque()
now = a.pop()
conf.append(now)
while a:
    now = a.pop()
    ans += conf.pop()
    conf.appendleft(now)
    conf.appendleft(now)

print(ans)

    


