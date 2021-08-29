# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 00:41:58 2021

@author: kazuk
"""

from heapq import heappop, heappush
n, m, x = map(int, input().split())
tree = [int(input()) for _ in range(n)]
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    adj[a-1].append((b-1, t))
    adj[b-1].append((a-1, t))
    
#dp[i]: 木0から木vに到達するのに要する最短時間
#木 v に到達した時点での最短所要時間が T であったとする
#もし cost[i]>X ならば、木 v の高さ 0 の地点に飛びついたと考えてよい
#逆に cost[i]<=X ならば、木 v の高さ X−T の地点に飛びついたと考えてよい

def dijkstra(s, g, x):
    INF = float("inf")
    dp = [INF] * n
    fix = [False] * n
    hq = []
    heappush(hq, (0, s))
    dp[0] = 0
    while hq:
        _, v = heappop(hq)
        #dp[v]は木vに来るまでの最短時間
        fix[v] = True
        
        #現在位置をdpの値から復元
        #dp[v]>xなら高さ0に飛びついたと考えてよい
        if dp[v] > x:
            h = 0
        #dp[v]<=xなら高さ(x-dp[v])に飛びついたと考えてよい
        else:
            h = x - dp[v]
        for nextv, w in adj[v]:
            if fix[nextv] == False:
                #移動するためのcost計算
                #移動先の高さが木の高さより高いとき→移動先の木の高さまで移動
                #diffは移動するための高さ調節の時間
                if tree[nextv] < h-w:
                    diff = h - w - tree[nextv]
                    cost = dp[v] + diff + w
                #移動先の高さが0以上木の高さ以下のとき→そのまま移動
                elif 0 <= h-w <= tree[nextv]:
                    cost = dp[v] + w
                #移動先の高さが0未満になるとき→移動先の高さが0になるように登って調整
                #(調整できないときはその移動は無理)
                else:
                    if w > tree[v]:continue #今いる木で飛び移るために必要な分上れない場合
                    diff = w-h
                    cost = dp[v] + diff + w
                    
                #dijkstraパート(costの更新、hqにつっこむ)
                dp[nextv] = min(dp[nextv], cost)
                heappush(hq, (dp[nextv], nextv))
                
    #ゴール地点で頂点に上るのにかかる時間の調節
    if dp[g] > x:
        h = 0
    else:
        h = x - dp[g]
    return dp[g] + tree[g] - h

ans = dijkstra(0, n-1, x)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
    



# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 00:41:58 2021

@author: kazuk
"""

from heapq import heappop, heappush
n, m, x = map(int, input().split())
tree = [int(input()) for _ in range(n)]
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    adj[a-1].append((b-1, t))
    adj[b-1].append((a-1, t))
    
#dp[i]: 木0から木vに到達するのに要する最短時間
#木 v に到達した時点での最短所要時間が T であったとする
#もし cost[i]>X ならば、木 v の高さ 0 の地点に飛びついたと考えてよい
#逆に cost[i]<=X ならば、木 v の高さ X−T の地点に飛びついたと考えてよい

def dijkstra(s, g, x):
    INF = float("inf")
    dp = [INF] * n
    fix = [False] * n
    hq = []
    heappush(hq, (0, s))
    while hq:
        time, v = heappop(hq)
        if fix[v]:continue
        #timeは木vに来るまでの最短時間
        fix[v] = True
        dp[v] = time
        
        #現在位置をdpの値から復元
        #dp[v]>xなら高さ0に飛びついたと考えてよい
        if time > x:
            h = 0
        #dp[v]<=xなら高さ(x-dp[v])に飛びついたと考えてよい
        else:
            h = x - time
        for nextv, w in adj[v]:
            #移動するためのcost計算
            #移動先の高さが木の高さより高いとき→移動先の木の高さまで移動
            if tree[nextv] < h-w:
                diff = h - w - tree[nextv]
                cost = time + diff + w
            #移動先の高さが0以上木の高さ以下のとき→そのまま移動
            elif 0 <= h-w <= tree[nextv]:
                cost = time + w
            #移動先の高さが0未満になるとき→移動先の高さが0になるように登って調整
            #(調整できないときはその移動は無理)
            else:
                if w > tree[v]:continue #今いる木で飛び移るために必要な分上れない場合
                diff = w-h
                cost = time + diff + w
                
            #dijkstraパート(costの更新、hqにつっこむ)
            if cost < dp[nextv]:
                dp[nextv] = cost
                heappush(hq, (dp[nextv], nextv))
    if dp[g] > x:
        h = 0
    else:
        h = x - dp[g]
    return dp[g] + tree[g] - h

ans = dijkstra(0, n-1, x)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
    



    
            


    
            
