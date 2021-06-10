# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 03:48:23 2021

@author: kazuk
"""
N = int(input())
S = str(input())
count = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            if S.find(str(i)) != -1: 
                key1 = S.find(str(i))
                if S.find(str(j), key1 + 1) != -1:                    
                    key2 = S.find(str(j), key1 + 1)
                    if S.find(str(k), key2 + 1) != -1:
                        count += 1
                
print(count)

#findメソッドは前から検索する
#引数一つで前から検索
#引数二つで前から検索+開始点を指定
#引数三つで前から検索+開始点を指定+終了位置を指定
#rfindは後ろから検索