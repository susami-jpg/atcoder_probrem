# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 21:36:48 2021

@author: kazuk
"""

h, w, c = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(h)]
ans = 10**15

def rails(i, j):
    return maze[i][j] - c * (i + j)

def rails_plus(i, j):
    return maze[i][j] + c * (i + j)

def mk_acc_min(maze):
    INF = 10**15
    acc_min = [[INF] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if i == j == 0:
                continue
            elif i == 0:
                acc_min[i][j] = min(acc_min[i][j-1], rails(i, j-1))
            elif j == 0:
                acc_min[i][j] = min(acc_min[i-1][j], rails(i-1, j))
            else:
                acc_min[i][j] = min(acc_min[i-1][j], rails(i-1, j),\
                                    acc_min[i][j-1], rails(i, j-1))
                    
    return acc_min

def min_cost(acc):
    min_c = 10**15
    for i in range(h):
        for j in range(w):
            cnd = acc_min[i][j] + rails_plus(i, j)
            min_c = min(min_c, cnd)
    return min_c

acc_min = mk_acc_min(maze)
ans = min(ans, min_cost(acc_min))
maze = [row[::-1] for row in maze]
acc_min = mk_acc_min(maze)
ans = min(ans, min_cost(acc_min))

print(ans)

    
#公式解説の解法
h, w, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
ans = INF = 10**15           
#dp[i][j]  := （青木君が一方の駅をすでに建設して、現在(i, j)にいるとき、それまでにかかった費用として考えられる最小値）
#1マス移動するのにコストがcかかると解釈する(マンハッタン距離でコストが加算されていくため)
#移動は左上から右下に向かっていくとしてよい(真逆の方向は同じ結果、左右反転パターン(右上から左下への移動)はあとで行う必要があるので注意)

def min_cost(a):
    cnd = 10**15
    dp1 = [[INF] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i == j == 0:
                #前の移動がないので駅の建設しかできない
                dp1[i][j] = a[i][j]
            elif i == 0:
                dp1[i][j] = min(dp1[i][j-1] + c, a[i][j])
            elif j == 0:
                dp1[i][j] = min(dp1[i-1][j] + c, a[i][j])
            #場合:駅の建設かすでに駅を建設済みで上から来たか、右から来たか
            else:
                dp1[i][j] = min(dp1[i][j-1] + c, dp1[i-1][j] + c, a[i][j])
    
    dp2 = [[INF] * w for _ in range(h)]
    #以下で、dp1[i][j]の値を用いて問題の答えを求める方法を述べます。 まず 
    #dp2[i][j]を、dp2[i][j]:= （ 2つ目の駅を (i,j)に建てて青木君がどこかへ飛び立ったとき、そこまでにかかった費用として考えられる最小値）と定義します。
    
    for i in range(h):
        for j in range(w):
            if i == j == 0:
                continue
            elif i == 0:
                dp2[i][j] = min(dp1[i][j-1] + c + a[i][j], dp2[i][j])
            elif j == 0:
                dp2[i][j] = min(dp1[i-1][j] + c + a[i][j], dp2[i][j])
            else:
                #上からきて駅建設か右からきて駅建設か
                dp2[i][j] = min(dp2[i][j],\
                                dp1[i-1][j] + c + a[i][j],\
                                    dp1[i][j-1] + c + a[i][j])
            cnd = min(cnd, dp2[i][j])
    return cnd

ans = min(ans, min_cost(a))
a = [row[::-1] for row in a]
ans = min(ans, min_cost(a))
print(ans)

            
