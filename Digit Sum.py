# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:23:34 2021

@author: kazuk
"""

mod = 10**9+7
k = list("0" + input())
K = list(map(int, k))
d = int(input())

#dp[i][smaller][j]: 、前からi番目の桁まで確定している時に、kと同じならsamller=False
#違うならsamller = True、でmod dがjであるようなk以下の場合の数
dp = [[[0] * d for _ in range(2)] for _ in range(len(K))]
#0index(i=0)があるとみると(ex: "0"12432)
"""
まず、i=0とはどういう状況かを考えます。
上のdp配列の定義に戻ると、dp[0]というのは、

「上から-1桁目までで条件を満たす数の総数」

です。「-1桁目なんてないじゃないか」と思うかもしれません。しかし、こう考えてはどうでしょう。

N=12345とします。この上から0桁目は1です。-1桁目があるとすれば、その左隣です。そこには、0があるとは考えられないでしょうか。

i=-1桁目の数字は常に0である。こう考えると、先程の初期条件にも納得がいきます。
0以下の正整数は、0以外にありません。そして、それはNの-1桁目に一致しているので、smaller=0に属します。
また、-1桁目以前は全て0ですから、3は出てきていません。故に、0はj=0に属します。
こうして、smaller=j=0の場合だけ1、それ以外は0ということになります。
"""
dp[0][0][0] = 1
for i in range(len(K)-1):
    for smaller in range(2):
        for j in range(d):
            conf = dp[i][smaller][j]
            if smaller:
                for k in range(10):
                    dp[i+1][smaller][(j + k)%d] += conf
                    dp[i+1][smaller][(j + k)%d] %= mod
            else:
                max_flg = K[i+1]
                for k in range(max_flg):
                    dp[i+1][1][(j + k)%d] += conf
                    dp[i+1][1][(j + k)%d] %= mod
                dp[i+1][smaller][(j + max_flg)%d]\
                    += conf
                dp[i+1][smaller][(j + max_flg)%d] %= mod

ans = dp[-1][0][0] + dp[-1][1][0] - 1
print(ans%mod)


    

 