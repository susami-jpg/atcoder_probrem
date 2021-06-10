# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:34:29 2021

@author: kazuk
"""

n, m = map(int, input().split())
terms = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    terms.append((a, b))
k = int(input())
person = []
for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    person.append((c, d))

def check(dish):
    cnt = 0
    for a, b in terms:
        if dish[a] and dish[b]:
            cnt += 1
    return cnt

ans = 0
for i in range(1 << k):
    dish = [0] * n
    for j in range(k):
        if (i >> j) & 1:
            dish[person[j][1]] += 1
        else:
            dish[person[j][0]] += 1
    cnt = check(dish)
    ans = max(ans, cnt)
print(ans)
            
    
    