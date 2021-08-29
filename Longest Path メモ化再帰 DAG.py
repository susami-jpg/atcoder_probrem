# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 13:14:33 2021

@author: kazuk
"""

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    def chmax(a, b):
        if a >= b:
            return a
        else:
            return b
        
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
    
    memo = [-1] * n
    
    
    def dp(v):
        if memo[v] != -1:
            return memo[v]
        l = 0
        for nextv in adj[v]:
            l = chmax(l, dp(nextv) + 1)
        memo[v] = l
        return l
    
    ans = 0
    for v in range(n):
        if memo[v] != -1:
            cnd = memo[v]
        else:
            cnd = dp(v)
        ans = chmax(ans, cnd)
    
    print(ans)
    
    
if __name__ == "__main__":
    main()