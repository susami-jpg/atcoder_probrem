# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 03:08:11 2021

@author: kazuk
"""
#ヒープソートの流れ
#基本的には大きい値を後ろに移動させることでソートする。未配列のリストからその中での最大値を素早く発見するためにヒープを構築する。
#１：与えられた任意の配列に対してヒープの構築を行う。これによって未配列リストの先頭に最大値がくる。
#2:構築されたヒープの先頭要素をリストのヒープの後ろにつける(根の削除）。これによってヒープは崩れるが、ヒープの後ろはソート済みとなる。
#3:2によってヒープが崩れたが根(先頭要素)以外のヒープは保たれている。ヒープを再構築するために節点の交換を行う。
#以降2,3の繰り返し


def sort(A):
    #construct_heap(A, 0)は、リストAで表される完全２分木に対してヒープの構築を行う。
    #ヒープとは、親の値がの子値より大きいという条件を常に満たすものである。
    construct_heap(A, 0);print(A)
    #以下でリストの先頭からlast番目までで表されるヒープ(last番目より後ろはソート済み)に対する「根の削除」と「節点の交換」を繰り返している。すなわち手順２と手順３がforループによって繰り返されている。
    #lastを最後尾から先頭の次(1番目)まで減らしながら繰り返している。減らすことでソート済み配列が一個ずつ増えていく。
    for last in range(len(A) - 1, 0, -1):    
        A[0], A[last] = A[last], A[0];print(A)#手順２。ヒープの構築したあと、先頭要素(根)を最後方に持っていく操作(根の削除)。これによってソート済みとなる。
        #手順3。リストAの先頭からlast-1番目までで表される完全２分木に対して0番目の節点から節点の交換を行う関数。したがって削除されていない(未ソート、準ヒープ)の完全２分木に対する節点の交換を意味する。
        exchange_nodes(A, 0, last - 1);print(A)

#関数left,rightはそれぞれリストにおけるn番目の要素の左の子のインデックスと右の子のインデックスを返す。
def left(n):
    return 2 * n + 1

def right(n):
    return 2 * n + 2

#リストAの先頭からlast番目までで表される完全２分木に対してn番目の節点から節点の交換を行う関数。
def exchange_nodes(A, n, last):
    #前提としてlast番目までの要素で完全２分木を表す
    #上記より、条件last < left(n)はその完全２分木にn番目の節点がないということを意味する。
    if last < left(n):
        return
    child = left(n) #変数childにはAのn番目の節点のうち大きい方のインデックスが代入される。
    #right(n) <= lastはn番目の節点には左の子も右の子もあるということを意味する。
    if right(n) <= last:
        if A[left(n)] < A[right(n)]:
            child = right(n) #右の子と左の子を比較して、大きいほうをchildに代入
    if A[n] < A[child]: 
        A[n], A[child] = A[child], A[n];print(A) #childのほうが親の値(A[n])より大きい場合、要素を交換する。これは節点の交換の操作に当たる。
        exchange_nodes(A, child, last) #Aのchild番目から節点の交換を行うことの再帰的な記述
   
        
#construct_heap(A, n)はリストAで表される完全２分木に対してn番目の節点からヒープの構築を行う関数
#ヒープ構築の手順
#1:Aの根にこがなければ何もせず終了、子があればAの子から始まる部分木(２つあれば２つとも)に対してヒープの構築を行う。
#2:そのあとにAの節点の交換を行う。
#これはヒープの構築の再帰的な定義になっている。

def construct_heap(A, n):
    last = len(A) - 1
    if last < left(n): #n番目の節点に左の子がない、すなわち子が全くない場合
        return
    construct_heap(A, left(n)) #左の子があることは確定したので左の子から始まる部分木についてヒープの構築を行う
    if right(n) <= last:
        construct_heap(A, right(n)) #右の子がある場合は右の子から始まる部分木についてもヒープの構築を行う
    #ここまでのコードによってn番目の節点から始まる部分木は、n番目の節点以外がヒープになった(根の部分以外はconstruct_heap関数の再帰呼び出しによってヒープとなった)
    #あとは根の部分を含めてヒープとするために節点の交換を行う。これでヒープは完成する。
    exchange_nodes(A, n, last)
    
    
    