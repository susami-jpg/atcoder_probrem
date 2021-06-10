# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 02:03:12 2021

@author: kazuk
"""

#想定解法だがTLE
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    inf = 10 ** 15
    #自己循環路を候補として記録
    cnd = [inf] * n
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a-1].append((c, b-1))
        if a == b:
            cnd[a-1] = c
    
    def chmin(a, b):
        if a > b:
            return b
        else:
            return a

    def chmax(a, b):
        if a > b:
            return a
        else:
            return b
    
    def dijkstra(v):
        hq = []
        dist = [inf] * n
        fix = [False] * n
        #s'として本来のスタート地点から一手先に進んだ頂点をスタート地点とする。
        #こうすることでスタート地点への帰り道を探すことができる。
        for c, nextv in adj[v]:
            dist[nextv] = chmin(dist[nextv], c)
            heappush(hq, (c, nextv))
        while hq:
            now = heappop(hq)[1]
            fix[now] = True
            for c, nextv in adj[now]:
                if not fix[nextv]:
                    dist[nextv] = chmin(dist[nextv], dist[now] + c)
                    heappush(hq, (dist[nextv], nextv))
        return dist[v]
    
    for v in range(n):
        ans = chmin(cnd[v], dijkstra(v))
        if ans < inf:
            print(ans)
        else:
            print(-1)

if __name__ == "__main__":
    main()

