# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:19:26 2021

@author: kazuk
"""

k = int(input())

#7, 77, 777, 7777...という数列は
#A(i+1) = A(i) * 10 + 7
#と表せる

def row7(n):
    return n * 10 + 7

#mod kを考える
#数列を順にみていって、mod kが0になったらその項で割り切れる
#ループに入ったら割り切れない

loop = set()
now = 7%k
loop.add(now)
i = 1
while 1:
    if now == 0:
        print(i)
        break
    now = row7(now) % k
    i += 1
    if now in loop:
        print(-1)
        break
    loop.add(now)


