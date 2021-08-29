# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 08:59:24 2021

@author: kazuk
"""

s = input()
n = len(s)
#ok[l][r]:　l以上r未満の区間の文字を消せるか(True or False)
#ok[i][i] = True　で初期化
ok = [[False] * (n+1) for _ in range(n+1)]
for i in range(n):
    ok[i][i] = True

for diff in range(1, n+1):
    for l in range(n-diff+1):
        r = l + diff
        #l+1からr-1の間で区切って分割した区間の両方が消せるなら区間[l, r)は消せる
        for mid in range(l+1, r):
            ok[l][r] |= (ok[l][mid] & ok[mid][r])
        #"i" [文字列1] "w" [文字列2] "i"　の場合
        #文字列1,2が消せるかどうかで区間[l, r)が消せるかが決まる
            if s[l] == "i" and s[mid] == "w" and s[r-1] == "i":
                ok[l][r] |= (ok[l+1][mid] & ok[mid+1][r-1])
    

#dp[r]: r番目までの文字列でいくつの文字を消せるか(ここでもrは含まない、0index)
dp = [0] * (n+1)
for r in range(1, n+1):
    dp[r] = max(dp[r], dp[r-1])
    for l in range(r):
        #[l, r)が消せるなら、rまでの区間で消せる文字数はdp[l] + (r-l)になる
        if ok[l][r]:
            dp[r] = max(dp[r], dp[l] + (r-l))

print(dp[n]//3)
