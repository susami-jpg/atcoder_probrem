# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 01:01:09 2021

@author: kazuk
"""

from sys import stdin
input = stdin.readline
def main():
    R, C, K = map(int, input().split())
    maze = [[0] * C for _ in range(R)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        maze[r-1][c-1] = v
    
    
    #dp[i][j][k]: i行j列にいて、同じ行でk個のアイテムを取った時の得点の最大値
    dp = [[[0] * C for _ in range(R)] for _ in range(4)]
    #アイテムがない場所では価値0のアイテムを取ったと考えてよい
    #アイテムのない場所でアイテムを取らない場合のdpもあるので問題ない
    dp[1][0][0] = maze[0][0]
    
    for i in range(R):
        for j in range(C):
            for k in range(4):
                #下に遷移する場合(アイテムを取らない場合)
                if i + 1 < R:
                    dp[0][i+1][j] = max(dp[0][i+1][j], dp[k][i][j])
                #下に遷移してアイテムを取る場合(下に遷移するなら所持アイテム数は確実に0か1)
                #下への遷移は同じ行でいくつアイテムを持っていてもよい
                    dp[1][i+1][j] = max(dp[1][i+1][j], dp[k][i][j] + maze[i+1][j])
                #横に遷移する場合(アイテムを取らない場合)
                if j + 1 < C:
                    dp[k][i][j+1] = max(dp[k][i][j+1], dp[k][i][j])
                    #横に遷移してアイテムを取る場合
                    if k < 3:
                        dp[k+1][i][j+1] = max(dp[k+1][i][j+1], dp[k][i][j] + maze[i][j+1])
    
    print(max(dp[0][-1][-1], dp[1][-1][-1], dp[2][-1][-1], dp[3][-1][-1]))
                    
    
if __name__ == "__main__":
    main()
            
            
                
    