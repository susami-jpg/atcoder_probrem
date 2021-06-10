# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:14:21 2021

@author: kazuk
"""

from collections import deque
s = list(input())
deq = deque()
#反転してるかどうかのフラグ
R = False
for i in s:
    if i == 'R':
        if R:
            R = False
        else:
            R = True
    else:
        #反転してたら先頭に要素追加
        if R:
            deq.appendleft(i)
        #反転していなければ末尾に要素追加
        else:
            deq.append(i)
deq = list(deq)
if R:
    deq = deq[::-1]
ans = []
#stackの考え方を利用して2連続で並んでいる要素を削除
for i in deq:
    if not ans:
        ans.append(i)
    elif ans[-1] == i:
        ans.pop()
    else:
        ans.append(i)

print(''.join(ans))
