# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:43:21 2021

@author: kazuk
"""

from sys import setrecursionlimit
setrecursionlimit(10**7)
n = int(input())
a = list(map(int, input().split()))

#dp[i][j][k]: 寿司が1個の皿がi枚、2個の皿がj枚、3個の皿がk枚の時の寿司がなくなるまでの操作回数の期待値
#dpテーブルを-1で初期化するとTLE
"""
リスト参照が多いため、Pythonだと制限時間が厳しい。

Pythonでは変数に何でも入れられるため普段あまり意識しないが、データ型の概念はしっかりとある。 変数を扱うたびに「この変数の型はなんぞや」のチェックから入るのが、Pythonが便利な反面、遅い一因となっている（要出典）。

PyPyでは、事前の型推論によりチェックを一部省略することで高速化を図っている部分があるが、処理の中でintもfloatも取り得る変数にしてしまうとその推論が上手く働かない。

今回のように小数が入るとわかっている場合は、初期化する値も小数にしておけば、よりPyPyの恩恵を享受できる、とのこと。

"""

dp = [[[-1.0] * 301 for _ in range(301)] for _ in range(301)]

#全ての皿が0なら操作回数も0
dp[0][0][0] = 0

#dp[i][j][k] = i/n * (dp[i-1][j][k] + 1)   寿司1個の皿をあてた
#            + j/n * (dp[i+1][j-1][k] + 1)　寿司2個の皿をあてた
#            + k/n * (dp[i][j+1][k-1])　　　　寿司3個の皿をあてた
#            + (1 - (i+j+k)/n) * (dp[i][j][k] + 1) 寿司0個の皿をあてた

def dfs(i, j, k):
    if i < 0 or j < 0 or k < 0:
        return 0
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    p = 1 - (i+j+k)/n
    E1 = dfs(i-1, j, k)
    E2 = dfs(i+1, j-1, k)
    E3 = dfs(i, j+1, k-1)
    E = (i/n * (1 + E1) + j/n * (1 + E2) + k/n * (1 + E3) + p) / (1 - p)
    dp[i][j][k] = E
    return E

i = a.count(1)
j = a.count(2)
k = a.count(3)

dfs(i, j, k)
print(dp[i][j][k])

    
    