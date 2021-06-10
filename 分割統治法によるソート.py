# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:12:29 2021

@author: kazuk
"""
#分割統治法(そのままでは解決できない大きな問題を小さな問題に分割し、そのすべてを解決することで最終的に最初の問題全体を解決する方法)
#分割統治法による選択ソート
def sort(A):
    if len(A) < 2:
        return A
    #select_minは受け取ったリストの先頭をリストの最小値と交換する関数    
    head, *B = select_min(A) #headは一つの値を指定（リストの先頭)。*BでリストAの残りの部分を指定。*はリストの残りの部分を指定する。
    return [head] + sort(B)

def select_min(A):
    if len(A) < 2:
        return A
    *B, tail = A #リストAとリストBの違いは最後尾の要素の有無。
    head, *C = select_min(B) #selection_sort関数によってリストBの先頭を最小値に変更。
    if head < tail:
        return [head] + [tail] + C  #全体としてはリストAを示す。headとtailを比較して最小のほうを先頭に持ってくる。
    else:
        return [tail] + [head] + C #Cとtailの順序はどちらでもよい

A = [2,1,3,5,6,5,6,4,8,9,7,6,5,4,6,1,2,3]
print(sort(A))
#selection_rec関数の定義：受け取ったリストの先頭をリストの最小値と交換する関数。
#まず引数にリストAを渡す。リストAの長さが0か1ならそのまま返す。
#リストAを最後尾の要素とそれ以外に分割する。最後尾の要素をtailとし、それ以外の部分、すなわちリストAからtailを消したリストをリストBとする。
#リストBをselection_rec関数引き渡し、先頭要素が最小値となったリストBを得る。
#上記のリストBを先頭要素(head)とそれ以外(リストC)に分割
#headとtailを比較してリストAにおける最小値を決定し、先頭に持ってくる。
#考え方としては最小値が先頭(head)にあるリストBに要素(tail)を追加するとき、tailがheadより小さいかどうかで、できあがるリストAの先頭要素が変化するということ。

#分割統治法によるバブルソート
def sort2(A):
    if len(A) < 2:
        return A
    #select_minは受け取ったリストの先頭をリストの最小値と交換する関数    
    head, *B = modify_order(A) #headは一つの値を指定（リストの先頭)。*BでリストAの残りの部分を指定。*はリストの残りの部分を指定する。
    return [head] + sort2(B)
#modify_order関数は一回回るごとに一番前に最小値が来る。

#modify_order関数はリストの最後尾の要素(tail)とその一つ手前の要素(hip)を比較し、昇順に整序する関数
def modify_order(A):
    if len(A) < 2:
        return A
    *B, hip, tail = A #リストAをhip, tailとそれ以外に分割
    if tail < hip:
        return modify_order(B + [tail]) + [hip]
    else:
        return modify_order(B + [hip]) + [tail]
print(sort2(A))

#分割統治法による挿入ソート
def sort3(A):
    if len(A) < 2:
        return A
    return insert(sort3(A[:-1]), A[-1])

#insert(A, temp)は整列済みリストAの適切な位置にtempを挿入する関数。
def insert(A, temp):
    if len(A) < 1:
        return [temp] #len(A) < 2としてしまうとAにひとつようそがあったときにtempとの並べ方が返せない。
    #return A　としてしまうとtempをAのなかに入れられない。ここでのA、tempと実際にinsert関数で使う変数が異なることに留意。
    *B, tail = A
    if temp < tail:
        return insert(B, temp) + [tail]
    else:
        return A + [temp]

print(sort3(A))

    

