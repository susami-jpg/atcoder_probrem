# -*- coding: utf-8 -*-
"""
Created on Sat May 22 19:47:05 2021

@author: kazuk
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

amod = [0] * 46
bmod = [0] * 46
cmod = [0] * 46

for i in a:
    i %= 46
    amod[i] += 1
for i in b:
    i %= 46
    bmod[i] += 1
for i in c:
    i %= 46
    cmod[i] += 1

ans = 0
for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a + b + c) % 46 == 0:
                ans += (amod[a] * bmod[b] * cmod[c])

print(ans)
    