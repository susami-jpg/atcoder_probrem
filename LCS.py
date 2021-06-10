# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:48:22 2021

@author: kazuk
"""
#PyPyで通ってた
import sys
# input処理を高速化する
input = sys.stdin.readline
s = [' '] + list(input())
t = [' '] + list(input())
lens = len(s)
lent = len(t)
dp = [[0] * lent for _ in range(lens)]
for i in range(1, lens):
    for j in range(1, lent):
        if s[i] == t[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

maxlen = dp[-1][-1]
i = lens - 1
j = lent - 1
ans = []
while maxlen:
    if s[i] == t[j]:
        ans.append(s[i])
        i -= 1
        j -= 1
        maxlen -= 1
    else:
        if dp[i - 1][j] == maxlen:
            i -= 1
        else:
            j -= 1
print(''.join(ans[::-1]))


#以下のコードでAC(PyPy)
import sys
# input処理を高速化する
input = sys.stdin.readline
# 入力
S = input()
T = input()
def chmax(a, b):
    if a >= b:
        return a
    else:
        return b
def lcs(s, t):
    dp = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                dp[i+1][j+1] = chmax(dp[i+1][j+1], dp[i][j] + 1)
            dp[i+1][j+1] = chmax(dp[i+1][j+1], dp[i+1][j])
            dp[i+1][j+1] = chmax(dp[i+1][j+1], dp[i][j+1])
    ans = ''
    i = len(S)
    j = len(T)
    while (i>0  and j>0):
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans += s[i-1] 
            i -= 1
            j -= 1
    
    print(ans[::-1])
        
lcs(S, T)
            
            
        



