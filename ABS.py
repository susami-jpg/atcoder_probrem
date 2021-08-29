# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:40:42 2021

@author: kazuk
"""

#TLE dp解法
from sys import setrecursionlimit, stdin
input = stdin.readline
setrecursionlimit(10**7)
n, z, w = map(int, input().split())
a = list(map(int, input().split()))

#f(id,turn,x,y) := 山札からid枚既に引いたときに、turnの番で、Xさんの手持ちがx, Yさんの手持ちがyである時のスコア
dp = dict()

def f(id, turn, x, y):
    if id == n:
        return abs(x-y)
    
    if (id, turn, x, y) in dp:
        return dp[(id, turn, x, y)]
    
    #xの手番
    if turn == 0:
        ma = -1
        for i in range(id, n):
            ma = max(ma, f(i+1, 1-turn, a[i], y))
        dp[(id, turn, x, y)] = ma
        return ma
    
    #yの手番
    else:
        mi = 10**15
        for i in range(id, n):
            mi = min(mi, f(i+1, 1-turn, x, a[i]))
        dp[(id, turn, x, y)] = mi
        return mi

ans = f(0, 0, z, w)
print(ans)

    

#O(1)解法
n, z, w = map(int, input().split())
a = list(map(int, input().split()))
if n >= 2:
    print(max(abs(a[-1]-w), abs(a[-1]-a[-2])))
else:
    print(abs(a[-1] - w))
    
