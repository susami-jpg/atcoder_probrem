# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:36:56 2021

@author: kazuk
"""

def counting(a, b, X = []):
    A = [[-1 for j in range(b + 1)] for i in range(a + 1)] #全要素が-1のb行*a列の表を作製
    for i in range(0, a + 1):
        A[i][0] = 0 #1列目の要素を全て0に変更
    for j in range(0, b + 1):
        A[0][j] = 0 #1行目の要素を全て0に変更    
    for (i, j) in X: #タプルを受け取る。
        A[i][j] = 0 #行き止まりの交差点X(x, y)を0に変更
#0行目、0列目はカウントしないことに注意
    A[1][1] = 1
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if A[i][j] == -1:
                A[i][j] = A[i - 1][j] + A[i][j - 1] #0行目を作っている効果がここでも現れる(1列目に関して例外処理をする必要がない。)
    
    return A[a][b]

print(counting(3, 4,[(1,2),(1,3)]))
                
     