# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:40:38 2021

@author: kazuk
"""

n = int(input())
A = list(map(int, input().split()))
a_max = 10**6 + 1
counter = [0] * a_max

for a in A:
    if counter[a]:
        counter[a] += 1
    else:
        i = 1
        while 1:
            num = a * i
            if num >= a_max:
                break
            counter[num] += 1
            i += 1

ans = 0
for a in A:
    if counter[a] == 1:
        ans += 1

print(ans)

