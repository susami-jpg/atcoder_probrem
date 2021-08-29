# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 21:38:02 2021

@author: kazuk
"""

def main():
    from sys import setrecursionlimit, stdin
    setrecursionlimit(10**7)
    #input = stdin.readline
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    
    edge = [sorted(e) for e in edge]
    ans = []
    seen = [0] * n
    def dfs(v, par):
        seen[v] = 1
        ans.append(v+1)
        for nextv in edge[v]:
            if seen[nextv]:continue
            dfs(nextv, v)
            ans.append(v+1)
        return
    
    dfs(0, -1)
    print(*ans)

if __name__ == "__main__":
    main()
    