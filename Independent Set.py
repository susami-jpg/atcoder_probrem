# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:41:42 2021

@author: kazuk
"""
def main():
    from sys import setrecursionlimit, stdin
    input = stdin.readline
    setrecursionlimit(10**7)
    mod = 10**9 + 7
    n = int(input())
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)
    
    #dp[i][j]=( 頂点iを(j?黒く:白く)塗ったとき、iを親とする部分木の塗り方の場合の数)
    dp = [[-1] * 2 for _ in range(n)]
    
    flg = [0] * n
    par = [0] * n
    
    def dfs(v):
        if flg[v]:
            return dp[v][0], dp[v][1]
        #自分を白色で塗る場合の部分木の塗り方の場合の数
        cnt_white = 1
        #自分を白色で塗る場合の部分木の塗り方の場合の数
        cnt_black = 1
        par[v] = 1
        for nextv in adj[v]:
            if par[nextv]: continue
            w, b = dfs(nextv)
            cnt_white = (cnt_white * (w + b))%mod
            cnt_black = (cnt_black * w)%mod
        dp[v][0] = cnt_white%mod
        dp[v][1] = cnt_black%mod
        flg[v] = 1
        return cnt_white, cnt_black
    
    #根を0として探索
    dfs(0)
    
    print((dp[0][0] + dp[0][1])%mod)

if __name__ == "__main__":
    main()
    

    

