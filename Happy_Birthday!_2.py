# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:50:53 2021

@author: kazuk
"""

from collections import deque
n = int(input())
a = list(map(int, input().split()))
a = [x%200 for x in a]

def check(a):
    l = len(a)
    mod = [[] for _ in range(200)]
    for i in range(1, 1 << l):
        cnd = deque()
        for j in range(l):
            if (i >> j) & 1:
                cnd.append(j + 1)
        m = 0
        for k in cnd:
            m += a[k - 1]
        m %= 200
        if mod[m]:
            mod[m].append(cnd)
            return mod[m]
        else:
            mod[m].append(cnd)
    else:
        return False

if n >= 8:
    print('Yes')
    b, c = check(a[:8])
    print(len(b), *b)
    print(len(c), *c)
else:
    ans = check(a)
    if ans:
        print('Yes')
        print(len(ans[0]), *ans[0])
        print(len(ans[1]), *ans[1])
    else:
        print('No')
        
                
        