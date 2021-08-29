# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:33:58 2021

@author: kazuk
"""

from collections import deque, defaultdict
n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
S = defaultdict(int)
i = 0
deq = deque()
seed = 0
while i < n:
    now = A[i]
    deq.append(now)
    if S[now] == 0:
        seed += 1
    S[now] += 1
    while seed > k:
        p = deq.popleft()
        S[p] -= 1
        if S[p] == 0:
            seed -= 1
    i += 1
    ans = max(ans, len(deq))
print(ans)
