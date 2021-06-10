# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:31:26 2021

@author: kazuk

"""

#n個の整数を含む数列 S と、q 個の異なる整数を含む数列 T を読み込み、T に含まれる整数の中で S に含まれるものの個数 Cを出力するプログラムを作成してください。
S = [6,7,8,9,12]
n = len(S)

T = [12]
q = len(T)

ans = 0
for i in range(q):
    L = 0
    R = n
    while L + 1 < R:
        M = (L + R) // 2
        if S[M] <= T[i]:
            L = M
        else:
            R = M

    find = S[L] == T[i]
    ans = ans + find
print(ans)

x = 0
for i in range(q):
    L = 0
    R = n
    while L + 1 < R:
        M = (L + R) // 2
        if S[M] == T[i]:
            x += 1
            break
        elif S[M] < T[i]:
            L = M
        else:
            R = M

print(x)