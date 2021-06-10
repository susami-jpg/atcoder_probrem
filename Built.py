# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:55:14 2021

@author: kazuk
"""

from heapq import heappop, heappush

n = int(input())
xlist = []
ylist = []
for i in range(n):
    x, y = map(int, input().split())
    xlist.append((x, i))
    ylist.append((y, i))
xlist.sort()
ylist.sort()

edge = [[] for _ in range(n)]
for i in range(n - 1):
    nowx = xlist[i][1]
    nowy = ylist[i][1]
    nextx = xlist[i + 1][1]
    nexty = ylist[i + 1][1]
    dx = abs(xlist[i][0] - xlist[i + 1][0])
    dy = abs(ylist[i][0] - ylist[i + 1][0])
    edge[nowx].append((dx, nextx))
    edge[nextx].append((dx, nowx))
    edge[nowy].append((dy, nexty))
    edge[nexty].append((dy, nowy))

hq = []
heappush(hq, (0, 0))
visited = [False] * n
ans = 0
while hq:
    weight, now = heappop(hq)
    if visited[now] == True:
        continue
    ans += weight
    visited[now] = True
    for w, nextv in edge[now]:
        heappush(hq, (w, nextv))

print(ans)
        
    
    
        


        
            
    


    