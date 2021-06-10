# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:03:46 2021

@author: kazuk
"""

while True:
    n, w, d = map(int, input().split())
    if n == w == d == 0:
        break
    square = [(w, d)]
    def cut(p, s):
        w, d = square.pop(p - 1)
        s %= (2*w + 2*d)
        if 0 < s < w:
            if s <= w - s:
                s1 = (s, d)
                s2 = (w-s, d)
            else:
                s1 = (w-s, d)
                s2 = (s, d)
        elif w < s < w+d:
            if s-w < w+d-s:
                s1 = (w, s-w)
                s2 = (w, w+d-s)
            else:
                s1 = (w, w+d-s)
                s2 = (w, s-w)
        elif w+d < s < 2*w + d:
            if s-w-d < 2*w + d - s:
                s1 = (s-w-d, d)
                s2 = (2*w + d - s, d)
            else:
                s1 = (2*w + d - s, d)
                s2 = (s-w-d, d)
        elif 2*w + d < s < 2*w + 2*d:
            if s - 2*w - d < 2*w + 2*d - s:
                s1 = (w, s - 2*w - d)
                s2 = (w, 2*w + 2*d - s)
            else:
                s1 = (w, 2*w + 2*d - s)
                s2 = (w, s - 2*w - d)
        square.append(s1)
        square.append(s2)
        
    for _ in range(n):
        p, s = map(int, input().split())
        cut(p, s)
    
    ans = [w*d for (w, d) in square]
    ans.sort()
    print(*ans)
