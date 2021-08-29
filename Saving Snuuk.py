# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:38:53 2021

@author: kazuk
"""

from heapq import heappop, heappush

n, m, s, t = map(int, input().split())
s -= 1
t -= 1
edge_money = [[] for _ in range(n)]
edge_snuke = [[] for _ in range(n)]

for _ in range(m):
    u, v, a, b = map(int, input().split())
    edge_money[u-1].append((v-1, a))
    edge_money[v-1].append((u-1, a))
    edge_snuke[u-1].append((v-1, b))
    edge_snuke[v-1].append((u-1, b))

def dijkstra(s, t, edge):
    INF = 10**18
    dis = [INF] * n
    fix = [False] * n
    dis[s] = 0
    hq = [(0, s)]
    while hq:
        _, v = heappop(hq)
        fix[v] = True
        for nextv, cost in edge[v]:
            if fix[nextv]:continue
            if dis[nextv] > dis[v] + cost:
                dis[nextv] = dis[v] + cost
                heappush(hq, (dis[nextv], nextv))
    return dis

dis_money = dijkstra(s, t, edge_money)
dis_sunuke = dijkstra(t, s, edge_snuke)

ans = []
acc_min = 10**18
for i in range(n-1, -1, -1):
    acc_min = min(acc_min, dis_money[i] + dis_sunuke[i])
    ans.insert(0, 10**15-acc_min)

for i in range(n):
    print(ans[i])
