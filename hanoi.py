# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:50:24 2021

@author: kazuk
"""
        
#関数moveはk段のハノイの塔をstartからendへ移動させる関数。左から、ハノイの塔の段数、始点の軸、予備の軸、終点の軸を表す引数である。
#ハノイの塔k段ををstartからendへ移動させる操作は3段階に分解できる。
#1:k-1段のハノイの塔をstartからyobiに移動させる。move関数が実装されていると仮定するとこれはmove(k-1, start, end, yobi)で実行することができる。
#2:1番したの段の円盤をstartからendに移動させる。
#3:k-1段のハノイの塔をyobiからendに移動させる。move関数が実装されていると仮定するとこれはmove(k-1, yobi, start, end)で実行することができる。
#以上のプログラムをコードに書き直せば、再帰的にmove関数を定義することができる。
#k = 1の場合は#2の操作しか実行されないので#1と#3の操作をk<2という条件で実行することにする。
def move(k, start, yobi, end):
    #操作1を示すコード
    if k >= 2:
        move(k-1, start, end, yobi)
    #操作2を示すコード
    print(f'{start}軸の円盤を{end}軸へ移動')
    #操作3を示すコード
    if k >= 2:
        move(k-1, yobi, start, end)
        
#move(1, 1, 2, 3)
#move(2, 1, 2, 3)
#move(3, 1, 2, 3)
#move(4, 1, 2, 3)
        
