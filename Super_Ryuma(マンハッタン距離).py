# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:28:10 2021

@author: kazuk
"""

from sys import exit
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

x1 = r1 + c1
y1 = r1 - c1
x2 = r2 + c2
y2 = r2 - c2


#0手、すなわちスタート地点とゴール地点が同じ
if r1 == r2 and c1 == c2:
    print(0)
    exit()

#一手でいけるか

#移動A(a+b = c+d)
if x1 == x2:
    print(1)
    exit()

#移動B(a-b = c-d)
if y1 == y2:
    print(1)
    exit()

#移動C(|a-c| + |b-c| <= 3)
if max(abs(x1-x2), abs(y1-y2)) <= 3:
    print(1)
    exit()


#二手でいけるか

#移動A + B
#パリティが同じなら移動可能
if x1 % 2 == x2 % 2:
    print(2)
    exit()

#移動A + C
#x, yそれぞれについて、距離の差が3以内なら移動可能
if abs(x1 - x2) <= 3 or abs(y1 - y2) <= 3:
    print(2)
    exit()

#移動C + C
#移動Cの範囲が3->6に変更
if max(abs(x1 - x2), abs(y1 - y2)) <= 6:
    print(2)
    exit()

#3手では確実に行ける
#一手目でパリティ変更し、パリティが同じならどこでも2手以内でいけるため
print(3)

    