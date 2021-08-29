# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 00:03:32 2021

@author: kazuk
"""

#MLE
while 1:
        
    from collections import deque
    n, m = map(int, input().split())
    if n == m == 0:
        break
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    na, a = a[0], [0] + a[1:]
    nb, b = b[0], [0] + b[1:]
    nc, c = c[0], [0] + c[1:]
    
    def bins(a):
        res = []
        for i in range(n+1):
            if i in a:
                res.append("1")
            else:
                res.append("0")
        return int("".join(res[::-1]), 2)
    
    def binlen(i):
        return bin(i).count("1")
    
    def top(i):
        if i == 0:
            return 0
        return len(bin(i)[2:])
    
    Sa = bins(a)
    Sb = bins(b)
    Sc = bins(c)
    
    dist = [[[-1] * (1 << (n+1)) for _ in range(1 << (n+1))] for _ in range(1 << (n+1))]
    dist[Sa][Sb][Sc] = 0
    
    deq = deque()
    deq.append((Sa, Sb, Sc))
    while deq:
        x, y, z = deq.popleft()
        lx, ly, lz = binlen(x)-1, binlen(y)-1, binlen(z)-1
        topx, topy, topz = top(x), top(y), top(z)
        #a -> b
        if lx and topx > topy:
            nextx = x^(1<<topx-1)
            nexty = y|(1<<topx-1)
            if dist[nextx][nexty][z] == -1:
                dist[nextx][nexty][z] = dist[x][y][z] + 1
                deq.append((nextx, nexty, z))
        #c -> b
        if lz and topz > topy:
            nextz = z^(1<<topz-1)
            nexty = y|(1<<topz-1)
            if dist[x][nexty][nextz] == -1:
                dist[x][nexty][nextz] = dist[x][y][z] + 1
                deq.append((x, nexty, nextz))
        #b -> a
        if ly and topy > topx:
            nextx = x|(1<<topy-1)
            nexty = y^(1<<topy-1)
            if dist[nextx][nexty][z] == -1:
                dist[nextx][nexty][z] = dist[x][y][z] + 1
                deq.append((nextx, nexty, z))
        #b -> c
        if ly and topy > topz:
            nextz = z|(1<<topy-1)
            nexty = y^(1<<topy-1)
            if dist[x][nexty][nextz] == -1:
                dist[x][nexty][nextz] = dist[x][y][z] + 1
                deq.append((x, nexty, nextz))
    
    ans_a, ans_c = dist[(1 << (n+1))-1][1][1], dist[1][1][(1 << (n+1))-1]
    if ans_a == ans_c == -1:
        print(-1)
    else:
        ans = min(ans_a, ans_c)
        if ans > m:
            print(-1)
        else:
            print(ans)
            

        

