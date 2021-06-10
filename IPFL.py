# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:51:29 2021

@author: kazuk
"""

#T=1の場合はswapがO(1)で行えるので問題ない(一つの文字の交換)。
#T=2の場合は、普通にやるとO(N)かかるのでこれを何とかしたい。(前半部分と後半部分の交換はO(N)かかる)
n = int(input())
s = list(str(input()))
q = int(input())
turn = False
def turnindex(x):
    if x < n:
        return x + n
    else:
        return x - n
    
for _ in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if turn:
            a = turnindex(a)
            b = turnindex(b)
            s[a], s[b] = s[b], s[a]
        else:
            s[a], s[b] = s[b], s[a]
    else:
        if turn:
            turn = False
        else:
            turn = True
if turn:
    s = s[n:] + s[:n]
print(''.join(s))



        
        