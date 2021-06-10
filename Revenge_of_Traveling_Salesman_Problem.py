# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:23:05 2021

@author: kazuk
"""
inf = 10 ** 10
n, m = map(int, input().split())
st = [[[inf, inf] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    s, t, d, time = map(int, input().split())
    st[s - 1][t - 1] = [d, time]
    st[t - 1][s - 1] = [d, time]
#dp[S][v]:集合Sに存在する頂点を全て訪問済みで現在頂点vにいるときのそこまでの最短距離と通り数を記録
dp = [[[inf, 0] for _ in range(n)] for _ in range(1 << n)]
#始点での距離は0で方法は一通り
dp[0][0] = [0, 1]
for S in range(1, 1 << n):
    for v in range(n):
        res = inf
        count = 0
        for u in range(n):
            #集合Sに現在地点vが含まれていない場合何もしない
            if (S >> v) & 1 == 0:
                continue
            if (S >> u) & 1 == 1:
                dcnd = dp[S ^ (1 << v)][u][0] + st[u][v][0]
                if dcnd <= st[u][v][1]:
                    if dcnd < res:
                        res = dcnd
                        count = dp[S ^ (1 << v)][u][1]
                    if dcnd == res:
                        count += dp[S ^ (1 << v)][u][1]
        dp[S][v][0] = res
        dp[S][v][1] = count
print(dp)
                    
                
           
                
                
                






#dfsは、訪問済み頂点の集合Sと現在地点vを受け取り、スタート地点までの最短経路と通り数
def dfs(S, v, dp):
    #vにすでに訪れていた場合
    if dp[S][v][0] != -1:
        return dp[S][v]
        #全ての頂点を訪問し、スタート地点に戻ってきたとき
    if S == (1 << n) - 1 and v == 0:
        return 0, 1
    res = inf
    count = 1
    for u in range(n):
        if (S >> u) & 1 == 0:
            cnd = st[v][u][0] + dfs(S|1 << u, u, dp)[0]
            if cnd < res:
                cnd = res
                count = 1
            if cnd == res:
                count += 1
    if res + st[v][u][0] <= st[v][u][1]:
        dp[S][v] = [res, count]
    return res, count

ans, count = dfs(0, 0, dp)
if ans == inf:
    print('IMPOSSIBLE')
else:
    print(ans, count)
    
            
            
            
    
    