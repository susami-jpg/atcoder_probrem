# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 01:14:00 2021

@author: kazuk
"""

#基本的には，すべての平行移動の仕方を一つずつ試して，一致する個所を見つけたら出力すればよい．ただし，「すべての平行移動の仕方」は無限にあるので文字通りにすべてを試すのは不可能である．探すべき星座の中の任意の1点を選んで特別扱いし，この点が写真の中の n 個の星の一つに一致するように平行移動する方法をすべて考えれば，平行移動の仕方として高々 n 通り試せばよいことがわかる．

#n 通りの平行移動の仕方を一つずつ試すと決まれば，実際に必要なことは，平行移動後の星座のすべての点が写真に含まれるかどうかを調べることである．含まれていれば平行移動した量を出力して終了し，含まれていなければ次の平行移動の仕方を試せばよい．

#素朴に写真の星の座標を与えられたまま長さ n の配列で記憶した場合，ある点が写真に含まれるかどうかを調べるのに O(n) 時間かかるので，星座全体が含まれるかどうかを調べるには O(mn) 時間かかる．平行移動の仕方は O(n) 通りあるので，全部で O(mn2) 時間かかることになる．この方法で，各入力に対し高々10秒程度プログラムを実行すれば解ける．

m = int(input())
sign = []
star = []
for _ in range(m):
    x, y = map(int, input().split())
    sign.append((x, y))
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    star.append((x, y))

sign_copy = sign[:]

base = sign.pop()
for i in range(n):
    (x, y) = (star[i][0] - base[0], star[i][1] - base[1])
    slide = []
    for j in range(n):
        slide.append((star[j][0] - x, star[j][1] - y))
    for s in slide:
        if s in sign:
            sign.remove(s)
    if len(sign):
        sign = sign_copy
    else:
        print(x, y)
        break
    
    
    
    
