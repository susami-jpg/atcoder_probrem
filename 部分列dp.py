# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 09:28:40 2021

@author: kazuk
"""

"""
部分文字列の数え上げ

【問題概要】
長さ n の文字列 S が与えられる。
S の部分文字列 (空文字含む) として考えられるものの個数を数え上げよ。ただし答えがとても大きくなることがあるので、個数を 1,000,000,007 で割ったあまりを求めよ。
【制約】

1≤n≤1051≤n≤105
Sに登場する文字は英小文字のみ (26 種類)
"""

#dp[i] := 文字列 S において、i 番目の文字 (index0は空白を入れる) は必ず使うものとして、S のうち 0 番目から i 番目までの部分から得られる部分文字列の個数
#初期化: dp[0] = 1 (" "に対応する、文字列Sの先頭に仮の文字列があるものとみなして、それのみを選ぶことに対応)
#ex "nyanpasu"
#dp[0] = 1
#dp[1] = 1 ("n"に対応する、"n"を選ばないといけないことに注意)
#dp[2] = 2 ("y"と"ny"に対応する)
#答えは　Σdp[i](i = 0~n)
#これはSの部分文字列のうち、最後に選び取るindexで場合分けしている
#計算時間は O(n) (より正確には S に登場する文字の種類数を KK として O(KN)) になります。

#部分列dpの遷移式
#dp[i] が定義されているときに、遷移は「次に選ぶ文字を 'a' 〜 'z' で場合分け」して次のように考えます。
#次に選ぶ文字に応じて最左の index を選ぶことで、「同じ部分文字列を生成するなら辞書順最小な選び方をする」というルールを満たすことを保証しています。
#また、ここでは配る DP で書いています。

#次の文字として 'a' を選ぶとき： S の i 文字目以降で最左の 'a' の index を a として 
#dp[a] += dp[i]
#次の文字として 'b' を選ぶとき： S の i 文字目以降で最左の 'b' の index を b として 
#dp[b] += dp[i]
#次に選ぶ文字の中で最も左にあるものを貪欲に選択することで重複がなくなる
#("nyanpasu"の例ではindex(0,2,6),(0,5,6),(3,5,6)はすべて"nas"となるが数え上げではこれらを区別しない)

#ここで、便利配列として
#next[i][c] := S の i 文字目以降で最初に文字 c が登場する index
#を前処理で求めておきます。これは以下のような関数でO(n) でできます:


#英子文字 <-> 整数0~25で変換
def int_to_str(n):
    return chr(n+97)

def str_to_int(s):
    return ord(s)-97

#sの先頭には空白をつけた状態で渡す
#next[i][c]: next[i][c] := S の i 文字目以降で最初に文字 c が登場する index
def calc_next(s):
    l = len(s)
    next = [[l] * 26 for _ in range(l+1)]
    for i in range(l-1, -1, -1):
        for j in range(26):
            now = s[i]
            if s[i] == int_to_str(j):
                next[i][j] = i
            else:
                next[i][j] = next[i+1][j]
        
    return next

mod = 10**9+7
a = input()
s = " " + a
next = calc_next(s)
n = len(s)

#dp[i] := 文字列 S において、i 番目の文字 (index0は空白を入れる) は必ず使うものとして、S のうち 0 番目から i 番目までの部分から得られる部分文字列の個数
dp = [0] * n
dp[0] = 1
for i in range(n):
    for j in range(26):
        next_index = next[i+1][j]
        if next_index < n:
            dp[next_index] += dp[i]
            dp[next_index] %= mod

ans = 0
for i in range(n):
    ans += dp[i]
    ans %= mod
print(ans)



