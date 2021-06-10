# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:36:04 2021

@author: kazuk
"""

#三分探索とは「たかだか一つしか極値のない関数ffにおける極値を探索するアルゴリズム」です。
#三分探索で扱える関数は、「たかだか一つのみ極値が存在するグラフ」になります。
#よって、極値が複数あると出発点によっては最小化などを発見することができません。
#凸性があるかどうかを確認することが大事です。

#目的の関数を設定
def cost(x):
    return 

#範囲設定
left = 0
right = 10**18

for i in range(10**5):
    m1 = (2*left + right) / 3
    m2 = (left + 2*right) / 3
    if cost(m1) < cost(m2):
        right = m2
    else:
        left = m1
print(cost(left))