# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:00:38 2021

@author: kazuk
"""

#TLE →　pow(10, n-i, 7)と第三引数を設定することで解決
from sys import stdin
#input = stdin.readline
def main():
    n = int(input())
    s = list(map(int, list(str(input()))))
    x = list(str(input()))
    
    #i番目の文字を決定した時のmod7がjであるときにどちらが勝つか
    dp1 = [[-1] * 7 for _ in range(n+1)]
    
    dp1[-1][0] = 1
    for j in range(1,7):
        dp1[-1][j] = 0
    
    for i in range(n-1, -1, -1):
        if x[i] == "T":
            turn = 1
        else:
            turn = 0
        for j in range(7):
            #0を選択する場合
            cnd1 = dp1[i+1][j]
            #siを選択する場合
            cnd2 = dp1[i+1][(j + s[i] * pow(10, n-i, 7)) % 7]
            #遷移先が自分の勝敗と同じならそれを選択
            if turn == cnd1:
                dp1[i][j] = cnd1
            else:
                dp1[i][j] = cnd2
    
    #最初の何も選んでいない状態ではmod7は0なので初期状態はdp[0][0]
    ans = dp1[0][0]
    
    if ans:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
    
"""
N−1 ラウンド目が終了した時点で高橋君に勝ち目があるかを考えてみましょう。この時点での 
Tを10進法の数とみなし 7で割ったあまりを rとします。また、文字 Snを数と同一視します。

n-1桁目までの余りがrならそれに一桁する操作は*10でありその時の余りは10*rとなる
(ex 127 % 7 = 1 : 1270 % 7 = 10)
これにSiを足さない、つまり0を選択する場合は 10*r%7であり、Siを足す場合は (10*r+Si)%7

Xnが T のとき、10rか 10r+Snのどちらかが7の倍数であれば高橋君の勝ちです。Xnが A のとき、
10r と 10r+Snがともに 7 の倍数であれば高橋君の勝ちです。

このように、後ろから考えることで、次のようなDPができることがわかります。

dp[i]=次の条件を満たす数 rの集合
条件： 
iラウンド目が終了した時点で、Tを 7 で割ったあまりが r であるとき、ここからゲームを続けると
高橋君が勝つ(rは0~6)

初期状態は dp[N] = {0}
XiがTのとき、dp[i-1] = {r|(10r mod 7)∈ dp[i] or (10r + Si mod 7)∈ dp[i]}
XiがAのとき、dp[i-1] = {r|(10r mod 7)∈ dp[i] and (10r + Si mod 7)∈ dp[i]}

最終的に0∈dp[0]なら高橋君の勝ち、それ以外なら青木君の勝ち
"""

n = int(input())
s = list(map(int, list(str(input()))))
x = list(str(input()))

dp = [set() for _ in range(n+1)]
dp[n].add(0)

for i in range(n)[::-1]:
    if x[i] == "T":
        for r in range(7):
            if 10 * r % 7 in dp[i+1] or (10 * r + s[i]) % 7 in dp[i+1]:
                dp[i].add(r)
    else:
        for r in range(7):
            if 10 * r % 7 in dp[i+1] and (10 * r + s[i]) % 7 in dp[i+1]:
                dp[i].add(r)

if 0 in dp[0]:
    print("Takahashi")
else:
    print("Aoki")
    
            
        
        
    

