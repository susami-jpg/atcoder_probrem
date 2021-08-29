# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:09:56 2021

@author: kazuk
"""

def main():
    from sys import setrecursionlimit, stdin
    setrecursionlimit(10**7)
    input = stdin.readline
    n, mod = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)
    
    #dp1[v]: 頂点vを含む部分木の塗り方の総数
    #dp1[v] = Π dp1[c] + 1 (cはvの子ノード、dp1[c]はvを黒く塗る場合の数
    #+1はvを白く塗る場合1通りに決まるため)
    dp1 = [-1] * n
    
    #dfs1は帰りがけ順でdp1の計算を行う
    def dfs1(v, par):
        if dp1[v] != -1:
            return dp1[v]
        
        prod = 1
        for nextv in adj[v]:
            if nextv == par:continue
            dfs1(nextv, v)
            prod *= dp1[nextv]
            prod %= mod
        #prodはvを黒色に塗る場合の数
        dp1[v] = prod + 1 #vを白色に塗る場合の数も足してdpテーブル更新
        return dp1[v]%mod
    
    dfs1(0, -1)
    
    #dp2[v]:　頂点vを含まない親方向の部分木の塗り方の総数(dfs1と逆方向)
    #dp2[v] = Π dp1[c] * dp2[p] + 1 (pはvの親ノード、cはvを除くpの子ノード)
    #...dp2[p]までがpを黒色に塗る場合の数、+1はpを白色に塗る場合の数
    dp2 = [-1] * n
    
    #dfs2は行きかけ順でdp2の計算を行う
    #配るdpで行う(dp2[v]を計算するのではなく、vの子ノードのdp2[c]を計算する)
    #prodはvの親ノードのdp2の値(dp2[p]にあたる)
    
    #親ノードのない根と仮定したノードのdp2は1とする
    dp2[0] = 1
    
    def dfs2(v, par):
        #左右からの子ノードのdp1の値について累積積をとってvの子ノードのdp2の計算を高速化
        L = len(adj[v])
        left = [1] * (L+1)
        right = [1] * (L+1)
        for i in range(1, L+1):
            child_L = adj[v][i-1]
            child_R = adj[v][L-i]
            left[i] = left[i-1]
            #dfs2で見探索ならchildである
            if child_L != par:
                left[i] *= dp1[child_L]
                left[i] %= mod
            right[L-i] = right[L-i+1]
            if child_R != par:
                right[L-i] *= dp1[child_R]
                right[L-i] %= mod
                
        #vの子ノードについてdp2を更新 -> dfs2
        for i, child in enumerate(adj[v]):
            #すでに探索済みならcontinue
            if child == par:continue
            #restはchild以外のvの子ノードのdp1の値の総積
            rest = left[i] * right[i+1]
            #行きかけ順なのでdp2[v]は計算済み
            dp2[child] = rest * dp2[v] + 1
            dp2[child] %= mod
            dfs2(child, v)
        return
    
    dfs2(0, -1)
    
    for v in range(n):
        ans = (dp1[v]-1) * dp2[v]
        ans %= mod
        print(ans)

if __name__ == "__main__":
    main()
    


    
    
        
    
    
    

    