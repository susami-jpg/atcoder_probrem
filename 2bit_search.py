# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:27:57 2021

@author: kazuk
"""

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

for mnum in m:
    for i in range(2 ** n):
        bini = list('0' * (n - len(bin(i)[2:])) + bin(i)[2:])
        num = 0
        for ind, j in enumerate(bini):
            if j == '1':
                num += A[ind]
        if num == mnum:
            print('yes')
            break
    else:
        print('no')
            
#>>> i = 5
#>>> bin(i)
#'0b101'  # 5 を 2 進数で表記すると 101
#>>> bin(i >> 2)
#'0b1'  # 5 を 2 回右にシフトすると 001
#>>> print((i >> 2) & 1)
#1  # 5 を 2 回右にシフトしたものと 1 の論理積は 1 (=True)    
            
money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(i), end="")
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
    print(bag)
    