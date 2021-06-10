# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:17:37 2021

@author: kazuk
"""

#解法としては微妙
"""
from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
box = [0] * (10 ** 7)
deq = deque()

for i in a[:m]:
    box[i] += 1
    deq.append(i)

for i in range(10 ** 7):
    if box[i] == 0:
        mex = i
        break
ans = mex
for i in range(n - m):
    now = deq.popleft()
    next = a[m + i]
    deq.append(a[m + i])
    box[now] -= 1
    box[next] += 1
    if now < mex:
        if box[now] == 0:
            mex = now
        else:
            while True:
                if box[mex] == 0:
                    break
                mex += 1
    else:
        while True:
            if box[mex] == 0:
                break
            mex += 1
    ans = min(mex, ans)
print(ans)
"""
            
#公式解説の解法
n, m = map(int, input().split())
a = list(map(int, input().split()))
indexlist = [[] for _ in range(n + 1)]
for i, x in enumerate(a):
    indexlist[x].append(i)
end = len(a) - 1
for mex in range(10 ** 7):
    cnd = indexlist[mex]
    if len(cnd) == 0:
        print(mex)
        break
    prev = -1
    cnd.append(n)
    for c in cnd:
        diff = c - prev - 1
        if diff >= m:
            print(mex)
            break
        prev = c
    else:
        continue
    break

        
        
