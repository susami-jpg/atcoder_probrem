# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:04:00 2021

@author: kazuk
"""

from sys import exit
n = int(input())
s = list(input())
if len(set(s)) == 1:
    print(0)
    exit()

now = 1
prev = 0
cnt = 1
ans = 0
while 1:
    if now >= n:
        break
    if s[prev] != s[now]:
        ans += cnt * (n - now)
        cnt = 1
        prev = now
    else:
        cnt += 1
    now += 1

print(ans)
