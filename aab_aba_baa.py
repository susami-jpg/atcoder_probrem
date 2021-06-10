# -*- coding: utf-8 -*-
"""
Created on Mon May 24 23:28:10 2021

@author: kazuk
"""

a, b, k = map(int, input().split())
comb = [[0 for _ in range(j)] for j in range(1, 62)]
comb[0][0] = 1
for i in range(1, 61):
    for j in range(i + 1):
        if j == 0:
            comb[i][j] = comb[i - 1][j]
        elif j == i:
            comb[i][j] = comb[i - 1][j - 1]
        else:
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
            
ans = []
num = k
while a > 0 and b > 0:
    #aにした場合にある通り数のなかに辞書順kが存在する場合
    if comb[a + b - 1][a - 1] >= num:
        ans.append("a")
        a -= 1
    #bにした場合
    else:
        ans.append("b")
        #辞書順の更新
        num -= comb[a + b - 1][a - 1]
        b -= 1
    
if a:
    for _ in range(a):
        ans.append("a")
if b:
    for _ in range(b):
        ans.append("b")
print("".join(ans))

    