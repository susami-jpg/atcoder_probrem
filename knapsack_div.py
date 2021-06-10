# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 02:09:05 2021

@author: kazuk
"""
#分割ナップザック問題は貪欲法によって解ける
#関数maxは、与えられた荷物の名前と価値を重量からなるタプルのリストAとナップザックの重量制限nを受け取り、
#貪欲法によって分割ナップザック問題を解いて、合計価値と、荷物ごとの選んだ重量のリストを返す関数
def max(A, n):
    def  f(t): return t[1] / t[2] 
    A.sort(key = f, reverse = True) #sortにkeyとして関数を与えると、リストの各要素をその関数に与えた結果で比較し整列する
    #各要素のkgあたりの価値を降順(reverse = True)に並び替える
    b = 0; items = []
    for (i, p, w) in A:
        if n >= w: #荷物の重さが重量制限を超えないとき
            b = b + p #合計価値を更新
            items = items + [(i, w)] #選ぶ荷物を更新
            n = n - w #重量制限の残り
        else: #荷物の重さが重量制限を超えるとき
            b = b + p * n / w #残量(n)分の価値を更新
            items = items + [(i, n)] #n分だけ荷物'i'を加える
            break
    return (b, items)

A = [('A', 400, 5), ('B', 300, 4), ('C', 200, 2), ('D', 300, 1)]
print(max(A, 5))