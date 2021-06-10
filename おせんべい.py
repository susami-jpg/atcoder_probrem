# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:45:45 2021

@author: kazuk
"""
#間に合わない
import numpy as np

R, C = map(int, input().split())
a = [list(input().split()) for _ in range(R)]
maxc = 0

for i in range(2 ** R):
    A_copy = np.array(a[:])
    count = 0
    for j in range(R):
        if (i >> j) & 1:
            row = int(''.join(A_copy[j]), 2)
            t = list(bin(~row & (2 ** C - 1))[2:])
            nul = C - len(t)
            t = list('0' * nul) + t
            A_copy[j] = t
    collist = np.count_nonzero(A_copy == '0', axis=0)
    for x in collist:
        y = R - x
        count += max(x, y)
    maxc = max(maxc, count)
print(maxc)

#PyPyなら間に合う
from itertools import product
R, C = map(int,input().split())
lines = []
for r in range(R):
    line = list(map(int,input().split()))
    lines.append(line)
lines = list(zip(*lines)) #*listでリストの中身をアンパック、すなわちリストから中身だけを取り出した状態で渡す
#zip(*list)でリストの転置を行う
ans = 0
for p in product((0,1),repeat=R): #productは与えられたリスト(今回は要素)のすべての組み合わせをリストにして返す
    #repeat = R でR回繰り返すことを示す
    #上記は(0, 1)というタプルの中からR回選ぶ操作をしている　表裏を決定する二進数
    sm = 0
    for line in lines: #列を取り出す
        cnt = 0
        for r in range(R):
            if p[r] == line[r]:
                cnt += 1
        sm += max(cnt, R-cnt)
    ans = max(ans, sm)
print (ans)

        
            