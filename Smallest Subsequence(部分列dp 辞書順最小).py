# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 16:37:38 2021

@author: kazuk
"""

n, K = map(int, input().split())
s = input()

#dp[i][j]: i文字目まで見た時にi文字目より右にあるjの中で最も左にあるjのindex
dp = [[n] * 26 for _ in range(n+1)]

def str_to_int(s):
    return ord(s) - 97

def int_to_str(n):
    return chr(n + 97)

for i in range(n-1, -1, -1):
    now = str_to_int(s[i])
    for j in range(26):
        if now == j:
            dp[i][j] = i
        else:
            dp[i][j] = dp[i+1][j]

ans = ""
#前から選べる文字の中で最もaに近いものを貪欲に選んでいく

#is_okはi番目のjを選べるかどうかを判定
def is_ok(i, j):
    #あと何文字選ぶ必要があるか
    rest = K - len(ans)
    #i番目のjを選ぶ時にそれ自身を含めてあと何文字選べるか
    cnd = n - dp[i][j]
    return rest <= cnd

#はじめに、[$ K]文字の1文字目を `a` にできるか？を試し、だめであれば1文字目を`b`にできるか？を試します。
#これを1文字目に関して`z`まで行います。
#その中で、「できる」となった最小の文字を採用すればよいです。

#次に、どういうときにOKでどういうときにだめか？を考えます。
#これは、`a`を採用するとなったとき[$ N]文字の文字列の中で、今選ぶことのできる範囲のうち最も左にあるものを選択すべきです。
#そして、その位置を選んだ時、残りの[$ K - k] 文字以上残っているかを調べます。

#iは現在地を示す、初期値は0
i = 0
for k in range(K):
    for j in range(26):
        #i文字目以降で最も左にあるjがつかえるかどうか
        #jは辞書順小さいものから(aから)貪欲に選べるか判定
        if is_ok(i, j):
            #ansの文字列k番目にjが使えるなら
            ans += int_to_str(j)
            #現在地の移動(i文字目の次まで飛ぶ)
            #次からはi以降でつかえる最小のjを貪欲に見つける
            i = dp[i][j] + 1
            break
print(ans)

