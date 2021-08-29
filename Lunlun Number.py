# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:34:08 2021

@author: kazuk
"""

K = int(input())

ans = []
from sys import setrecursionlimit
setrecursionlimit(10**7)
def dfs(t, n):
    if len(t) == n:
        ans.append(int("".join(t)))
        return
    
    if len(t) == 0:
        for nxt in range(1, 10):
            dfs(str(nxt), n)
        return
    last = int(t[-1])
    if last-1 >= 0:
        dfs(t+str(last-1), n)
    dfs(t+str(last), n)
    if last+1 < 10:
        dfs(t+str(last+1), n)
    return

k = 1
while len(ans) <= K:
    dfs("", k)
    k += 1

#ans.sort() ソートしなくても昇順になっている
print(ans[K-1])


#BFS-likeな解法
from collections import deque
deq = deque()
for i in range(1, 10):
    deq.append(i)
cnt = 0
while 1:
    now = deq.popleft()
    cnt += 1
    if cnt == K:
        print(now)
        break
    #ある数字の末尾の桁はその数字を10で割ったあまり
    last = now%10
    for c in range(-1, 2):
        if 0 <= last+c <= 9:
            deq.append(now*10+last+c)
            