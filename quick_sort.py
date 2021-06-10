# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 01:24:42 2021

@author: kazuk
"""
def sort(A):
    if len(A) < 2:
        return A
    p = A[0]
    X, Y = divide(p, A[1:]) #pを基準としてdivide関数によってX,Yに分ける。
    return sort(X) + [p] + sort(Y) #分けた配列を合成。合成するX,Yそれぞれ再帰的にsortに代入されることで同じこと(pを基準として配列Xをさらに分ける。)が繰り返される。
#基準として利用したpは以降sortに引数として渡す必要はない(pはリストのあるべき場所に指定されるから)。    

def divide(p, A):
    if len(A) < 1:
        return ([], [])
    X, Y = divide(p, A[1:]) #関数divideは配列Aをpとの大小関係でXとYに分割する。
    #divideは再帰的に定義しており、Aを分割するのに先頭部分A[0]と残りの部分A[1:]に分けてAの分割を書く。これはフィボナッチ数列の定義式とやっていることは似ている。
    a = A[0]
    if a < p:
        return ([a] + X, Y)
    else:
        return (X, [a] + Y)
    
A = [3,2,1,2,5,6,7,5,4]    
print(sort(A))
#考え方としては、リストAから先頭要素を除いたリストをdivide関数によってpを基準として二つのリストXとYに分割。
#pとリストAの先頭要素aを比較して、リストXとリストYのどちらかに追加する。
        