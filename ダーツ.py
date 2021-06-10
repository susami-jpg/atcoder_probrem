# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 20:55:50 2021

@author: kazuk
"""
import bisect
n, m = map(int, input().split())
#投げない、すなわち0点のパターンを加える
p = [0]
for _ in range(n):
    p.append(int(input()))
p.sort()
#pは一本のダーツを投げた時の点数の取り方をソートしたリスト
s = []
for i in p:
    for j in p:
        s.append(i + j)
s.sort()
#sは二本のダーツを投げた時の点数の取り方をソートしたリスト
#ここまでオーダーN**2

#二本のダーツを投げた時点で得点Mとの差を考慮して残りの二本のダーツによって獲得できる点数を決める
#その組み合わせによって獲得した点数の中で最大の点数が目的の値
ans = 0
for i in s:
    if m < i:
        break #二本目のダーツまででオーバーしてたらout
    rest = m - i
    index = bisect.bisect(s, rest) 
#二分探索で残りの二本のダーツによって獲得する点数の最適値を決める
    ans = max(ans, i + s[index - 1])

print(ans)
#二分探索をすると、計算量は、O((N^2)log(N^2))となります。（log(N^2)=2logNなので計算量はO((N^2)logN)とも表せます）
        


    

    