# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:29:45 2021

@author: kazuk
"""

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

#円環は考えにくいので切り出して考えるためにaを二回並べた2n列にする
a = a * 2

#列a[i] ~ a[i + n - 1] の両端を互いに取り合っていくゲームとして考える(残りn個のピース)
#初めに切る場所(i)はn通り
#f(i, j)は両端がiとjの時にjoi君が得られる最大のポイント数を返す関数とする
#つまりf(0, n - 1), f(1, n), f(2, n + 1) ... f(n, 2n - 1)の最大値が答えとなる

#列がiを表し行がjを表すと考える
dp = [[0] * 2 * n for _ in range(2 * n)]

def f(i, j):
    #ピースが残り一つしかないとき、joiくんが先攻なのでとれる
    if i == j:
        dp[i][j] = a[i]
    #ピースが残り二つの時、大きいほうをとる
    elif i + 1 == j:
        dp[i][j] = max(a[i], a[j])
    else:
        c1 = dp[i + 1][j - 1]
        c2 = dp[i + 2][j]
        c3 = dp[i][j - 2]
        if a[i + 1] > a[j]:
            if a[i] > a[j - 1]:
                dp[i][j] = max(c2 + a[i], c1 + a[j])
            else:
                dp[i][j] = max(c2 + a[i], c3 + a[j])            
        else:
            if a[i] > a[j - 1]:
                dp[i][j] = max(c1 + a[i], c1 + a[j])
            else:
                dp[i][j] = max(c1 + a[i], c3 + a[j])
                
#a[i]をとる場合でa[i + 1] < a[j]の時
#a[i]をとる場合でa[i + 1] > a[j]の時
#a[j]を取る場合でa[i] > a[j - 1] 
#a[j]を取る場合でa[i] < a[j - 1]
#elseのdpをfにかえても結果は同じだが、メモ化再帰にすることで高速化
cnd = []
for l in range(2 * n):
    for i in range(2 * n - l):
        j = i + l
        f(i, j)
        if l == n - 1:
            cnd.append(dp[i][j])
        if l == n:
            break
            
print(max(cnd))