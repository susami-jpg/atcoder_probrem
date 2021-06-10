# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:53:55 2021

@author: kazuk
"""

#showはツリーを見やすくするための関数
def show(T):
    if T == None:
        return ''
    L, data, R = T
    return '(' + show(L) + str(data) + show(R) + ')'

#insertはツリーTに数値nを正しい位置に挿入する関数
def insert(T, n):
    if T == None:
        return ((), n, ())
    L, data, R = T
    if n < data:
        return (insert(L, n), data, R) #nが左にある場合は左のツリーをinsertに代入することで再帰的に関数を呼び出す。
    return (L, data, insert(R, n))

#searchはツリーT中に数値nがあるかどうかを判定
def search(T, n):
    if len(T) == 0:
        return False
    L, data, R = T
    if n == data:
        return True
    if n < data:
        return search(L, n) #nが左にある場合は左のツリーをsearchに代入することで再帰的に関数を呼び出す。
    return search(R, n)    

#2本探索木からデータを削除するプログラム
#目的のデータの子が0個であった場合、目的のデータの節点を削除
#子が1個ある場合、目的のデータを削除し、その子を目的のデータの親につける
#子が2個ある場合が複雑である。まず削除対象の節点の右の部分木の最小値mを削除する(削除対象から右に行って、後はずっと左に行った終点の値)。
#mを削除対象の値と置き換える。
#最小値mの子は0か1なので循環論法とはならず、矛盾は生じない。

#removeは数値nをツリーTの中から削除する関数
#remove_min関数はT内の最小値mと残りの2本探索木を返す関数
def remove(T, n):
    if T == None:
        return
    L, data, R = T
    if n == data:
        if L == None:
            return R #削除対象の左部分木がない場合
        if R == None:
            return L #削除対象の右部分木がない場合
        #削除対象が2個の子を持つ場合
        m, X = remove_min(R) #右の部分木の最小値mとmを削除した残りの部分木Xを返す
        return (L, m, X)
    if n < data:
        return (remove(L, n), data, R) #nがdataより小さい場合nは左の部分木に存在するはずなので左の部分木に再帰的にremove関数を適用
    return (L, data, remove(R, n)) #nがdataより大きい場合・・・

#remove_min関数はT内の最小値mと残りの2本探索木を返す関数
def remove_min(T):
    L, data, R = T
    if len(L) == None:
        return (data, R) #左の部分木がない場合
    m, X = remove_min(L) #左の部分木の最小値と残りの木を返す
    return (m, (X, data, R)) #(X, data, R)は左の部分木からmを削除した残りの部分木Xをdata, Rと結合することで全体としてはツリーTから最小値mを削除したツリーを返している。


    
        