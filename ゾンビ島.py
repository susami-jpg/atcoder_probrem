# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:09:46 2021

@author: kazuk
"""

from heapq import heappop, heappush
from collections import deque
inf = 10 ** 10
n, m, k, s = map(int, input().split())
p, q = map(int, input().split())
c = set()
for _ in range(k):
    c.add(int(input()))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

#bfsはスタート地点をうけとって、そこから最短のゾンビ村までの距離のリストを返す関数
def bfs(c):
    que = deque()
    zombi = [inf] * (n + 1)
    for i in list(c):
        que.append(i)
        zombi[i] = 0
    while que:
        now = que.popleft()
        for nextv in adj[now]:
            if zombi[nextv] != inf:
                continue
            zombi[nextv] = zombi[now] + 1
            que.append(nextv)
    return zombi

zombi = bfs(c)
            
def dijkstra(st, g):
    money = [inf] * (n + 1)
    money[st] = 0
    hq = [(0, st)]
    fix = [False] * (n + 1)
    while hq[0][1] != g:
        now = heappop(hq)[1]
        fix[now] = True
        for nextv in adj[now]:
            if fix[nextv] == False and nextv not in c:
                zom = zombi[nextv]
                if nextv == n:
                    stay = 0
                elif zom <= s:
                    stay = q
                else:
                    stay = p
                if money[now] + stay < money[nextv]:
                    money[nextv] = money[now] + stay
                heappush(hq, (money[nextv], nextv))
    
    return hq[0][0]

print(dijkstra(1, n))

    