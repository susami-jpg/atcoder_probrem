# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:20:23 2021

@author: kazuk
"""

#01-BFSの高速化
#マスの1次元化：　あまり効果ない？
#goalについたらwhileを強制終了：　効果はありそうだが答えに不安
#今いる場所から行ったほうがcostが小さくなるものだけdeqに追加: かなり効果あり
#costの更新をnowではなくnextで行う: 効果あり

def main():
    from sys import stdin, exit
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
        return 0 <= y <= h-1 and 0 <= x <= w-1 and maze[y][x] == "."
    
    def dim_to_int(y, x, d):
        return y*w*4 + x*4 + d
    
    from collections import deque
    deq = deque()
    INF = 10**15
    dist = [INF] * (h*w*4)
    for d in range(4):
        deq.append((rs, cs, d))
        now = dim_to_int(rs, cs, d)
        dist[now] = 0
        
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while deq:
        y, x, d = deq.popleft()
        now = dim_to_int(y, x, d)
        if y == rt and x == ct:
            print(dist[now])
            exit()
        cost = dist[now]
        for nxt in range(4):
            nexty = y + dy[nxt]
            nextx = x + dx[nxt]
            if not valid(nexty, nextx):continue
            next = dim_to_int(nexty, nextx, nxt)
            #now -> nextに移動した場合にcostが改善されるならdeqに追加
            if d == nxt and cost < dist[next]:
                #costの更新をnowではなくnextで行う
                dist[next] = cost
                deq.appendleft((nexty, nextx, nxt))
            elif cost + 1 < dist[next]:
                dist[next] = cost+1
                deq.append((nexty, nextx, nxt))

if __name__ == "__main__":
    main()