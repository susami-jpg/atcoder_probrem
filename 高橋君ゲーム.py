# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:54:30 2021

@author: kazuk
"""

from itertools import accumulate
from math import floor
from sys import exit
n, k = map(int, input().split())
a = [0] + [int(input()) for _ in range(n)]
if sum(a) == k:
    print(1)
    exit()
game = list(accumulate(a))
INF = 10 ** 15
dp = [[INF] * (n + 1) for _ in range(n + 1)]
dp[0][0] = dp[1][0] = 0
dp[1][1] = 1
for i in range(2, n + 1):
    for j in range(i+1):
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        if j-1 >= 0:
            x = dp[i-1][j-1] * (game[i] - game[i-1])
            x = floor(x/game[i-1]) + 1
            
            if x <= a[i]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + x)
                
                
for j in range(n, -1, -1):
    if dp[-1][j] <= k:
        print(j)
        break
    
"""
sum = a1 + a2 + ... + an とします。K < sum の時, 「K 回勝った」というのは「K 回以下勝った」と言い換えても同じであることを示します(K = sum のときは「全部勝つ」という選択肢以外ないのでこれは成り立ちません)。

L < K 回勝った場合を考えます。このとき, 残りの K-L 回の勝つ日をうまく選べば機嫌の良い日が同じかそれ以上になることを示せば良いです。そのための勝つ日の選び方を考えるのですが, N 日間を後ろから見ていき, その日(x 日目とする)が全勝でないなら, 残り勝ち数がなくなるか, その日が全勝になるまで勝ち数を増やします。このようにすると,

x 日目以前では機嫌の良い日の日数は変わらない
x+1 日目以降は全勝しているので, 勝率は常に上昇しており, 機嫌が良かったのに悪くなることはない。また, x 日目の勝率は上がるので, x 日目に機嫌が悪かったのが良くなることはあっても良かったのが悪くなることはない。
以上により, 機嫌の良い日は多くなることはあっても少なくなることはありません。以上により, 「K 回勝った」というのは「K 回以下勝った」と言い換えても良いことが分かりました。
b/a < (b+x)/(a+x) (x > 0, 0 < b < a)のは常に成り立つ
"""