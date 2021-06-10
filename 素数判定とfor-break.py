# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:41:47 2021

@author: kazuk
"""

def sosu(n):
    for i in range(1, n + 1):
        for j in range(2, i):
            if i <= 2:
                print(i)
                continue
            if i % j == 0:
                break #内側のループを抜け出す。
        else:
            print(i)
#for-else-breakの関係
#forとelseが同インデントにある場合、for文が実行され終了したのちにelseが実行される。
#for文の中身にbreakがあった場合、breakが実行された際にelseは実行されない。    

 
l1 = [1,2,3,4,5,6,7,8]
l2 = [4,5,3,6,2,32,445,23,20]
for i in l1:
    print('Start outer loop')

    for j in l2:
        print('--', i, j)
        if i == 2 and j == 20:
            print('-- BREAK inner loop')
            break
    else:
        print('-- Finish inner loop without BREAK')
        continue

    print('BREAK outer loop')
    break
# Start outer loop
# -- 1 10
# -- 1 20
# -- 1 30
# -- Finish inner loop without BREAK
# Start outer loop
# -- 2 10
# -- 2 20
# -- BREAK inner loop
# BREAK outer loop
#内側のループがbreakではなく正常に終了したときはelse内のcontinueが実行される。continueは外側のループに対するもので、以降の処理（外側のループのbreak）をスキップして次のサイクルに進む。
#内側のループがbreakで終了したときはelse内のcontinueが実行されず処理が続行される。この場合、外側のループのbreakが実行される。
#結果的に内側のループがbreakで終了したときは必ず外側のループのbreakも実行される。
#三重ループは以下のようになる。ネストが深くなっても考え方は同じ。   
