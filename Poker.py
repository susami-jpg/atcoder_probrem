# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:33:33 2021

@author: kazuk
"""

k = int(input())
s = list(map(int, list(str(input()))[:4]))
t = list(map(int, list(str(input()))[:4]))

card = [k] * 10
taka = [0] * 10
aoki = [0] * 10

for i in s:
    card[i] -= 1
    taka[i] += 1
for i in t:
    card[i] -= 1
    aoki[i] += 1

def score(card):
    s = 0
    for i in range(1, 10):
        s += i * pow(10, card[i])
    return s

per = 0
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            cnd = card[i] * (card[i] - 1)
        else:
            cnd = card[i] * card[j]
        if cnd <= 0:
            continue
        taka[i] += 1
        aoki[j] += 1
        if score(taka) > score(aoki):
            ans += cnd
        per += cnd
        taka[i] -= 1
        aoki[j] -= 1
print(ans / per)
            
            
            

        