# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:57:25 2021

@author: kazuk
"""

def main():
    from sys import setrecursionlimit, stdin
    input = stdin.readline
    setrecursionlimit(10**7)
    h, w = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(h)]
    mod = 10**9+7
    
    def valid(y, x):
        return 0 <= y <= h-1 and 0 <= x <= w-1
    
    #dp[i][j]: マス(i, j)にくる通り数
    dp = [[-1] * w for _ in range(h)]
    
    def dfs(y, x):
        if dp[y][x] != -1:
            return dp[y][x]
        
        cnt = 1
        for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nexty, nextx = y+a, x+b
            if valid(nexty, nextx) and maze[y][x] > maze[nexty][nextx]:
                cnt += dfs(nexty, nextx)
                cnt %= mod
        dp[y][x] = cnt
        return cnt
    
    ans = 0
    for y in range(h):
        for x in range(w):
            ans += dfs(y, x)
    
    print(ans%mod)
    
if __name__ == "__main__":
    main()
    
