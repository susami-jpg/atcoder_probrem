# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 23:15:52 2021

@author: kazuk
"""

b = [list(map(int, input().split())) for _ in range(2)] + [[0] * 3]
c = [list(map(int, input().split())) + [0] for _ in range(3)]

A = [["*"] * 3 for _ in range(3)]

#Sはすべての得点の総和
S = 0
for i in range(3):
    for j in range(3):
        S += b[i][j] + c[i][j]
        
#盤面を埋め終わったときの直大の得点を返す関数
def calc(A):
    score = 0
    for i in range(2):
        for j in range(3):
            if A[i][j] == A[i+1][j]:
                score += b[i][j]
    
    for i in range(3):
        for j in range(2):
            if A[i][j] == A[i][j+1]:
                score += c[i][j]
    
    return score


def dfs(A, turn):
    if turn == 9:
        return calc(A)
    
    elif turn%2 == 0:
        max_score = -10*15
        for i in range(3):
            for j in range(3):
                if A[i][j] != "*":continue
                A[i][j] = "o" #丸をかく
                #最大スコアの更新
                max_score = max(max_score, dfs(A, turn + 1))
                A[i][j] = "*" #盤面を元に戻す
        return max_score
    
    else:
        min_score = 10**15
        for i in range(3):
            for j in range(3):
                if A[i][j] != "*":continue
                A[i][j] = "x"
                min_score = min(min_score, dfs(A, turn + 1))
                A[i][j] = "*"
        return min_score
                
chokudai = dfs(A, 0)
chokuko = S - chokudai
print(chokudai)
print(chokuko)


                        