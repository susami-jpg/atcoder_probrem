# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:28:09 2021
 
@author: kazuk
"""
 
def main():
    from sys import stdin
    from collections import defaultdict
    from itertools import accumulate
    input = stdin.readline
    group = defaultdict(list)
    n, k = map(int, input().split())
    for _ in range(n):
        c, g = map(int, input().split())
        group[g].append(c)
     
    #dp[i][j]:　iグループ目まででj冊の本を選ぶ時の最大価値
    INF = 10**15
    dp = [[-INF] * (k+1) for _ in range(11)]
    dp[0][0] = 0
        
    for i in range(10):
        G = group[i+1]
        G.sort(reverse=True)
        G = [0] + G
        G = list(accumulate(G))
        for j in range(k+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            for l in range(1, len(G)):
                if j+l > k:break
                dp[i+1][j+l] = max(dp[i+1][j+l], dp[i][j] + G[l] + l*(l-1))
                
        
    print(dp[10][k])

if __name__ == "__main__":
    main()
    