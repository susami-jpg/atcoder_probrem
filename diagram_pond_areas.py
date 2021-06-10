# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:16:18 2021

@author: kazuk
"""

#\の場所をスタックに保存することで、/を受け取った時にそれと対応する\を見つけることができる
#上記の方法で、対応する\、/を用いて面積を計算すること = 横向きに面積を計算していくということ

#入力が\のときはそのインデックスをスタックに保存する
#入力が/の時はスタックからpopし、現在のインデックスと組み合わせて横向きに面積を計算する
#計算した面積の総和をとって総面積を計算する

#ただ、これだけでは各水たまりの面積を計算できないので、

#/の時にpopしたインデックスと計算した面積のタプルを保存する
#必要に応じて上記のタプルを結合していく(水たまりを結合する操作に相当)
#以上のために2つのスタックを用意します。

#\のインデックスを保存するスタック
#popしたインデックスと計算した面積のタプルを保存するスタック

def diagram_areas(n):
    s1 = []
    s2 = []
    for ind, i in enumerate(n):
        if i == r'\'':
            s1.append(ind)
        if i == '/':
            l = s1.pop
            t = ind - l
            if s2 and s2[-1][0] > l:
                s2[-1] = (l, t + s2[-1][1])
            else:
                s2.append((l, t))
    s = 0
    for i in range(len(s2)):
        s += s2[i][1]
    return s

n = repr('\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/' + '\'')


import sys
import os


s = input().strip()

S1 = []  # sum of pond
S2 = []  # each pond
area = 0

for i, c in enumerate(s):
    if c == '\\': #これで一つ分の'\'
        S1.append(i)
    elif c == '_':
        pass
    elif c == '/' and S1:
        j = S1.pop(-1)
        area += i - j

        # for each pond
        pond_sum = i - j  
        while S2 and S2[-1][0] > j:
            pond_sum += S2[-1][1]
            S2.pop(-1)
        S2.append([j, pond_sum]) #各池の面積の更新

pond_areas = []
for data in S2:
    pond_areas.append(data[1])

# answer
print(area) #総面積
print(len(pond_areas), *pond_areas) #各池の数、各池の面積

            