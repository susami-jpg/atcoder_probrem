# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:18:44 2021

@author: kazuk
"""

#TLE
def main():
    from sys import stdin
    input = stdin.readline
        
    h, w = map(int, input().split())
    rs, cs = map(int, input().split())
    rt, ct = map(int, input().split())
    rs -= 1
    cs -= 1
    rt -= 1
    ct -= 1
    
    maze = [input() for _ in range(h)]
    
    def valid(y, x):
        return 0 <= y <= h-1 and 0 <= x <= w-1
    
    def dim_to_int(y, x, d):
        return y*w*4 + x*4 + d
    
    def dijkstra(sy, sx, gy, gx): # (始点, グラフのリスト)
        from heapq import heappop, heappush
        INF = 10 ** 18
        #dist = [[[INF] * 4 for _ in range(w)] for _ in range(h)] # INF で初期化
        dist = [INF] * (h*w*4)
        #check = [[[False] * 4 for _ in range(w)] for _ in range(h)]
        check = [False] * (h*w*4)
        q = [] # （距離・ノード）
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for d in range(4):
            now = dim_to_int(sy, sx, d)
            dist[now] = 0
            q.append((0, sy, sx, d))
        while q:
            cost, y, x, d = heappop(q) # 今いるノード
            now = dim_to_int(y, x, d)
            if y == gy and x == gx:
                return cost
            if check[now]: continue # すでに行っていたらcontinue
            check[now]= True # 訪問済み
            for nex in range(4): # 先のノード・距離
                nexty = y + dy[nex]
                nextx = x + dx[nex]
                next = dim_to_int(nexty, nextx, nex)
                if not valid(nexty, nextx) or maze[nexty][nextx] == "#":continue
                if check[next] != False: continue
                if d == nex:cost = 0
                else:cost = 1
                if dist[next] <= dist[now] + cost: continue
                dist[next] = dist[now] + cost
                heappush(q, (dist[next], nexty, nextx, nex)) # 必ず[0]が距離になるように（優先度付きキュー）
        goal = dim_to_int(gy, gx, 0)
        return min(dist[goal:goal+4])
    
    print(dijkstra(rs, cs, rt, ct))

if __name__ == "__main__":
    main()

