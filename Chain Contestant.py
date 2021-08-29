# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:40:14 2021

@author: kazuk
"""

#初期提出コード
#いまいちなんであってるかわからない
mod = 998244353
n = int(input())
s = input()
s = [ord(i) - 65 for i in s]
#dp[i][S][j] := i番目の大会で、集合S種類の大会に参加済み、最後に出た大会がjであるような場合の数
dp = [[[0] * 11 for _ in range(1<<10)] for _ in range(n)]
ans = 0
dp[0][0][10] = 1
dp[0][(1<<s[0])][s[0]] = 1
for i in range(n-1):
    for S in range(1<<10):
        for j in range(11):
            #i+1回目の大会がjである場合
            if s[i+1] == j:
                #すでにs[i+1]種類目の大会に参加済みの場合
                if (S>>s[i+1]) & 1:
                    #参加するor参加しないで2通り
                    dp[i+1][S][j] += dp[i][S][j] * 2
                    dp[i+1][S][j] %= mod
                #まだs[i+1]種類目の大会に参加していない場合
                else:
                    for k in range(11):
                        if k == j:continue
                        dp[i+1][S|(1<<s[i+1])][j] += dp[i][S][k]
                    dp[i+1][S|(1<<s[i+1])][j] %= mod
            #i+1回目の大会がjでない場合
            #i+1回目の大会には参加しない
            else:
                #i+1回目の大会に参加しない場合
                dp[i+1][S][j] += dp[i][S][j]
                dp[i+1][S][j] %= mod

ans = 0
for S in range(1<<10):
    for j in range(11):
        if dp[-1][S][j] >= 1:
            ans += dp[-1][S][j]
            ans %= mod
print(ans-1)



#改善コード
#場合分けがきれい
mod = 998244353
n = int(input())
s = input()
s = [ord(i) - 65 for i in s]
#dp[i][S][j] := i番目の大会で、集合S種類の大会に参加済み、最後に出た大会がjであるような場合の数
dp = [[[0] * 11 for _ in range(1<<10)] for _ in range(n)]
ans = 0
#j=10は今までコンテストに出たことがない場合の値(初期化)
dp[0][0][10] = 1
dp[0][(1<<s[0])][s[0]] = 1
for i in range(n-1):
    for S in range(1<<10):
        for j in range(11):
            #i+1回目の大会がjで、すでにs[i+1]種類目の大会に参加済みの場合
            if s[i+1] == j and (S>>s[i+1]) & 1:
                #参加するor参加しないで2通り
                dp[i+1][S][j] += dp[i][S][j] * 2
                dp[i+1][S][j] %= mod
                #まだs[i+1]種類目の大会に参加していない場合
    
            #i+1回目の大会がjでない場合
            else:
                #i+1回目の大会に参加する場合
                #すでにs[i+1]の大会に参加していたら参加できない
                if (~S>>s[i+1])&1:
                    dp[i+1][S|(1<<s[i+1])][s[i+1]] += dp[i][S][j]
                    dp[i+1][S|(1<<s[i+1])][s[i+1]] %= mod
                #i+1回目の大会に参加しない場合
                dp[i+1][S][j] += dp[i][S][j]
                dp[i+1][S][j] %= mod

ans = 0
for S in range(1<<10):
    #参加したことのない場合の数(j=10)の場合は数えないよう注意
    for j in range(10):
        if dp[-1][S][j] >= 1:
            ans += dp[-1][S][j]
            ans %= mod
print(ans)



                